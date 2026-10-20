"""Behavioral tests using disposable repository fixtures and the public CLI."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SKILL = ".agents/skills/maintain-impl-planner"
REFS = ".apm/skills/impl-planner/references"
SCRIPT = f"{SKILL}/scripts/check_consistency.py"
SOURCE = Path(__file__).resolve().parents[1] / "scripts/check_consistency.py"


class ConsistencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.paths = [
            "apm.yml",
            ".apm/skills/impl-planner/SKILL.md",
            f"{SKILL}/SKILL.md",
            f"{REFS}/examples.md",
            f"{REFS}/mini-example.md",
            f"{REFS}/provisional-example.md",
            f"{REFS}/software-task-profiles.md",
            f"{REFS}/risk-task-profiles.md",
            f"{REFS}/config-management-profile.md",
        ]
        for path in self.paths:
            self.write(path, "Fixture\n")
        self.write(
            "AGENTS.md",
            "# Repository Guide\n\nThe source of truth is:\n\n"
            + "".join(f"- `{path}`\n" for path in self.paths)
            + "- `README.md`\n- `README.ja.md`\n"
            + "\n## Working Rules\n\n- Read the guides.\n",
        )
        layout = [
            path for path in self.paths
            if not path.endswith(("software-task-profiles.md", "risk-task-profiles.md"))
        ]
        layout.append(f"{REFS}/*-task-profiles.md")
        for file, heading in (
            ("README.md", "Repository layout"),
            ("README.ja.md", "リポジトリ構成"),
        ):
            self.write(
                file, f"# Guide\n\n## {heading}\n\n"
                + "".join(f"- `{path}`: Description\n" for path in layout)
                + "\n## Other\n",
            )
        self.write(
            f"{REFS}/examples.md",
            "# Examples\n\n## Available Files\n\n"
            "- `mini-example.md`: A small example.\n"
            "- `provisional-example.md`: An incomplete plan.\n"
            "- `software-task-profiles.md`, `risk-task-profiles.md`, "
            "and `config-management-profile.md`: Task guidance.\n\n"
            "## Usage\n",
        )
        (self.root / "CLAUDE.md").symlink_to("AGENTS.md")
        (self.root / ".claude").symlink_to(".agents")
        (self.root / SCRIPT).parent.mkdir(parents=True)
        shutil.copyfile(SOURCE, self.root / SCRIPT)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def replace(self, name, old, new):
        path = self.root / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8")

    def run_check(self, *args, script=SCRIPT, cwd=None):
        return subprocess.run(
            [sys.executable, "-B", str(self.root / script), *map(str, args)],
            cwd=cwd or self.root, text=True, capture_output=True, check=False,
        )

    def assert_failure(self, *messages):
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for message in messages:
            self.assertIn(message, result.stdout)
        self.assertNotIn("Traceback", result.stderr)
        return result

    def test_valid_repository_and_wildcard(self):
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_readmes_are_required_in_root_inventory_only(self):
        original = (self.root / "AGENTS.md").read_text()
        for removed in (("README.md",), ("README.ja.md",), ("README.md", "README.ja.md")):
            with self.subTest(removed=removed):
                content = original
                for name in removed:
                    content = content.replace(f"- `{name}`\n", "")
                self.write("AGENTS.md", content)
                result = self.assert_failure(
                    *(f"AGENTS.md:1: missing inventory entry: {name}" for name in removed)
                )
                self.assertEqual(len(result.stdout.splitlines()), len(removed) + 1)
        self.write("AGENTS.md", original)
        # README layout sections intentionally do not inventory the READMEs themselves.
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_added_reference_is_reported_by_every_inventory(self):
        self.write(f"{REFS}/new-reference.md", "# New\n")
        result = self.assert_failure(f"missing inventory entry: {REFS}/new-reference.md")
        for file in ("AGENTS.md", "README.md", "README.ja.md"):
            self.assertIn(file + ":", result.stdout)

    def test_provisional_example_omission(self):
        for file in ("AGENTS.md", "README.md", "README.ja.md"):
            text = (self.root / file).read_text()
            self.write(file, "".join(
                line for line in text.splitlines(keepends=True)
                if "provisional-example.md" not in line
            ))
        self.assert_failure(f"missing inventory entry: {REFS}/provisional-example.md")

    def test_deleted_reference_and_stale_html_entry(self):
        (self.root / REFS / "mini-example.md").unlink()
        self.replace("AGENTS.md", "## Working Rules",
                     f"- `{REFS}/html-output.md`\n\n## Working Rules")
        self.assert_failure("listed path does not exist: mini-example.md",
                            f"listed path does not exist: {REFS}/html-output.md")

    def test_renamed_reference(self):
        (self.root / REFS / "mini-example.md").rename(self.root / REFS / "small-example.md")
        self.assert_failure("listed path does not exist: mini-example.md",
                            f"missing inventory entry: {REFS}/small-example.md")

    def test_duplicate_and_overlapping_wildcard(self):
        self.replace("AGENTS.md", "- `apm.yml`", "- `apm.yml`\n- `apm.yml`")
        self.replace("README.md", "## Other",
                     f"- `{REFS}/risk-task-profiles.md`\n\n## Other")
        self.assert_failure("duplicate coverage: apm.yml",
                            f"duplicate coverage: {REFS}/risk-task-profiles.md")

    def test_unmatched_wildcard(self):
        self.replace("README.md", "*-task-profiles.md", "*-unknown.md")
        self.assert_failure("wildcard matches no files:",
                            f"missing inventory entry: {REFS}/risk-task-profiles.md")

    def test_missing_sections(self):
        for file, heading in (
            ("README.md", "Repository layout"),
            ("README.ja.md", "リポジトリ構成"),
            (f"{REFS}/examples.md", "Available Files"),
        ):
            with self.subTest(file=file):
                original = (self.root / file).read_text()
                self.replace(file, f"## {heading}", "## Renamed")
                self.assert_failure(f"missing section: {heading}")
                self.write(file, original)

    def test_missing_intro_inventory(self):
        self.write("AGENTS.md", "# Guide\n\n## Working Rules\n")
        self.assert_failure("inventory has no local path entries",
                            "missing inventory entry: apm.yml")

    def test_second_and_third_paths_in_bullet_are_checked(self):
        for name in ("risk-task-profiles.md", "config-management-profile.md"):
            with self.subTest(name=name):
                file = f"{REFS}/examples.md"
                original = (self.root / file).read_text()
                self.replace(file, f"`{name}`", "`absent.md`")
                self.assert_failure("listed path does not exist: absent.md")
                self.write(file, original)

    def test_example_must_be_in_index(self):
        self.replace(f"{REFS}/examples.md",
                     "- `provisional-example.md`: An incomplete plan.\n", "")
        self.assert_failure(f"missing inventory entry: {REFS}/provisional-example.md")

    def test_readme_set_mismatch_for_existing_extra_path(self):
        self.write("notes.txt", "Existing optional path\n")
        self.replace("README.md", "## Other", "- `notes.txt`: Notes\n\n## Other")
        self.assert_failure("README layout differs: missing notes.txt")

    def test_prose_fences_urls_and_other_sections_are_ignored(self):
        ignored = (
            "Prose mentions `absent.md`.\n"
            "- `https://example.org/absent.md`: External reference.\n"
            "````md\n## Fake heading\n- `absent.md`\n```\n````\n"
            "~~~md\n- `absent.md`\n~~~\n"
        )
        self.replace("AGENTS.md", "## Working Rules", ignored + "## Working Rules")
        for file in ("README.md", "README.ja.md"):
            self.replace(file, ": Description", ": Description mentioning `absent.md`")
            self.replace(file, "## Other", ignored + "## Other\n- `absent.md`\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_symlinks_must_have_exact_relative_targets(self):
        for name, target in (("CLAUDE.md", "AGENTS.md"), (".claude", ".agents")):
            with self.subTest(name=name):
                link = self.root / name
                link.unlink()
                link.symlink_to(self.root / target)
                self.assert_failure(f"expected relative symlink to {target}")
                link.unlink()
                link.symlink_to("missing")
                self.assert_failure("symlink target is not reachable")
                link.unlink()
                link.symlink_to(target)

    def test_copied_instruction_file_is_not_a_symlink(self):
        (self.root / "CLAUDE.md").unlink()
        shutil.copyfile(self.root / "AGENTS.md", self.root / "CLAUDE.md")
        self.assert_failure("expected relative symlink to AGENTS.md")

    def test_agents_must_be_a_real_directory(self):
        (self.root / ".agents").rename(self.root / "shared")
        (self.root / ".agents").symlink_to("shared")
        # Explicit root avoids deriving a root from the deliberately moved script.
        result = self.run_check("--root", self.root)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(".agents:1: expected a real directory", result.stdout)

    def test_invalid_root_and_arguments(self):
        for args in (
            ("--root", self.root / "absent"),
            ("--root", self.root / "apm.yml"),
            ("--unknown",),
        ):
            with self.subTest(args=args):
                result = self.run_check(*args)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn("error:", result.stderr)

    def test_existing_empty_root_is_inconsistent_not_invalid(self):
        empty = self.root / "empty"
        empty.mkdir()
        result = self.run_check("--root", empty)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("cannot read inventory", result.stdout)

    def test_subdirectory_symlink_alias_and_explicit_root(self):
        for script in (SCRIPT, SCRIPT.replace(".agents/", ".claude/", 1)):
            for args in ((), ("--root", self.root)):
                with self.subTest(script=script, args=args):
                    result = self.run_check(*args, script=script, cwd=self.root / REFS)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_diagnostics_are_sorted_and_all_issues_are_reported(self):
        self.write(f"{REFS}/z.md", "# Z\n")
        self.write(f"{REFS}/a.md", "# A\n")
        result = self.assert_failure(f"missing inventory entry: {REFS}/a.md",
                                    f"missing inventory entry: {REFS}/z.md")
        lines = result.stdout.splitlines()[:-1]
        self.assertEqual(lines, sorted(lines))
        self.assertEqual(result.stdout, self.run_check().stdout)

    def test_read_only_including_no_python_cache(self):
        def snapshot():
            return {
                p.relative_to(self.root).as_posix():
                ("link", str(p.readlink())) if p.is_symlink()
                else ("file", p.read_bytes()) if p.is_file() else ("directory",)
                for p in self.root.rglob("*")
            }
        before = snapshot()
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(before, snapshot())


if __name__ == "__main__":
    unittest.main()
