#!/usr/bin/env python3
"""Check this repository's documentation inventories without modifying files."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import re
import sys


PACKAGE = ".apm/skills/impl-planner"
MAINTENANCE = ".agents/skills/maintain-impl-planner"
REFERENCES = f"{PACKAGE}/references"
BULLET_PATHS = re.compile(
    r"^\s*[-+*]\s+(`[^`]+`(?:\s*,\s*(?:and\s+)?`[^`]+`)*)"
)


@dataclass(frozen=True, order=True)
class Issue:
    file: str
    line: int
    reason: str

    def __str__(self) -> str:
        return f"{self.file}:{self.line}: {self.reason}"


def visible_lines(text: str):
    """Yield numbered Markdown lines outside backtick and tilde fences."""
    fence_char = ""
    fence_size = 0
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if fence_char:
            if re.fullmatch(re.escape(fence_char) + rf"{{{fence_size},}}\s*", stripped):
                fence_char = ""
            continue
        fence = re.match(r"(`{3,}|~{3,})", stripped)
        if fence:
            fence_char = fence.group()[0]
            fence_size = len(fence.group())
            continue
        yield number, line


class Checker:
    def __init__(self, root: Path):
        self.root = root
        self.issues: list[Issue] = []

    def issue(self, file: str, line: int, reason: str) -> None:
        self.issues.append(Issue(file, line, reason))

    def inventory(
        self, file: str, heading: str | None, base: str = ""
    ) -> tuple[set[str], int]:
        """Read only leading code-span paths in the selected section's bullets."""
        try:
            text = (self.root / file).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.issue(file, 1, f"cannot read inventory: {exc}")
            return set(), 1

        active = heading is None
        found = heading is None
        anchor = 1
        entries: dict[str, list[int]] = defaultdict(list)
        for number, line in visible_lines(text):
            if line.startswith("## "):
                if active:
                    break
                if line.strip() == f"## {heading}":
                    active = found = True
                    anchor = number
                continue
            if not active:
                continue
            match = BULLET_PATHS.match(line)
            if not match:
                continue
            for path in re.findall(r"`([^`]+)`", match.group(1)):
                if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", path):
                    continue
                relative = PurePosixPath(path)
                if relative.is_absolute() or ".." in relative.parts:
                    self.issue(file, number, f"expected repository-relative path: {path}")
                    continue
                pattern = str(PurePosixPath(base) / relative)
                if any(char in pattern for char in "*?["):
                    matches = sorted(
                        p.relative_to(self.root).as_posix()
                        for p in self.root.glob(pattern)
                        if p.is_file()
                    )
                    if not matches:
                        self.issue(file, number, f"wildcard matches no files: {path}")
                else:
                    matches = [pattern]
                    if not (self.root / pattern).exists():
                        self.issue(file, number, f"listed path does not exist: {path}")
                for matched in matches:
                    entries[matched].append(number)

        if not found:
            self.issue(file, 1, f"missing section: {heading}")
        elif not entries:
            self.issue(file, anchor, "inventory has no local path entries")
        for path, lines in entries.items():
            for number in lines[1:]:
                self.issue(
                    file, number, f"duplicate coverage: {path} (first at line {lines[0]})"
                )
        return set(entries), anchor

    def require(
        self, file: str, anchor: int, entries: set[str], expected: set[str]
    ) -> None:
        for path in sorted(expected - entries):
            self.issue(file, anchor, f"missing inventory entry: {path}")

    def check_link(self, name: str, target: str) -> None:
        path = self.root / name
        if not path.is_symlink():
            self.issue(name, 1, f"expected relative symlink to {target}")
            return
        try:
            if path.readlink().as_posix() != target:
                self.issue(name, 1, f"expected relative symlink to {target}")
            if not path.exists():
                self.issue(name, 1, f"symlink target is not reachable: {target}")
        except OSError as exc:
            self.issue(name, 1, f"cannot inspect symlink: {exc}")

    def run(self) -> list[Issue]:
        references = self.root / REFERENCES
        if not references.is_dir():
            self.issue(REFERENCES, 1, "references directory is missing")
        expected = {
            "apm.yml",
            f"{PACKAGE}/SKILL.md",
            f"{MAINTENANCE}/SKILL.md",
            *(p.relative_to(self.root).as_posix() for p in references.rglob("*.md")),
        }
        inventories = [
            ("AGENTS.md", None, expected | {"README.md", "README.ja.md"}),
            ("README.md", "Repository layout", expected),
            ("README.ja.md", "リポジトリ構成", expected),
        ]
        expanded = {}
        for file, heading, required in inventories:
            entries, anchor = self.inventory(file, heading)
            self.require(file, anchor, entries, required)
            expanded[file] = entries
        english, japanese = expanded["README.md"], expanded["README.ja.md"]
        for file, missing in (
            ("README.md", japanese - english),
            ("README.ja.md", english - japanese),
        ):
            for path in sorted(missing):
                self.issue(file, 1, f"README layout differs: missing {path}")

        index = f"{REFERENCES}/examples.md"
        entries, anchor = self.inventory(index, "Available Files", REFERENCES)
        examples = {
            p.relative_to(self.root).as_posix()
            for p in references.rglob("*-example.md")
        }
        self.require(index, anchor, entries, examples)
        if not (self.root / ".agents").is_dir() or (self.root / ".agents").is_symlink():
            self.issue(".agents", 1, "expected a real directory")
        self.check_link("CLAUDE.md", "AGENTS.md")
        self.check_link(".claude", ".agents")
        return sorted(self.issues)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[4],
        help="repository root (default: root containing this script)",
    )
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error(f"root must be an existing directory: {args.root}")
    root = args.root.resolve()
    issues = Checker(root).run()
    for issue in issues:
        print(issue)
    if issues:
        print(f"Consistency check failed: {len(issues)} issue(s).")
        return 1
    print("Consistency check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
