---
name: maintain-impl-planner
description: Maintain or review this impl-planner repository's contracts, references, bilingual documentation, package metadata, and maintenance tooling. Use when changing these sources or preparing a requested release; not for producing implementation plans for other repositories.
---

# Maintain impl-planner

Keep changes consistent with their affected contracts, examples, documentation,
and package contents. Respect the user's requested scope and read-only or
planning mode. This skill does not authorize publishing, merging, tagging, or
implementing work when only review or planning was requested.

## Establish the change

1. Read the root `AGENTS.md` and inspect the current branch, working-tree changes,
   and relevant diff. Preserve unrelated work and use the intended checkout.
2. Identify the source being changed and follow its references and dependents.
   The distributed planning skill lives in `.apm/skills/impl-planner/`; this
   maintenance skill lives in `.agents/skills/maintain-impl-planner/`.
   `.claude` links to `.agents`, and `CLAUDE.md` links to `AGENTS.md`.
   Edit each underlying file once.
3. Select the affected surfaces below. Determine whether the change alters the
   meaning or references each document exposes before updating it.

| Change | Surfaces to inspect |
|---|---|
| Add, remove, or rename a reference | Root source-of-truth list, both README layout sections, callers and links, and the `Available Files` section of `references/examples.md` when an example is involved |
| Change the planning contract | Skill entrypoint, core and extended contracts, related references, examples, and explanations and prompts in both READMEs |
| Change an explanation or usage prompt | The underlying contract and its English/Japanese counterparts; include minimal and detailed prompts when adding usage examples |
| Change package metadata or maintenance tooling | `apm.yml`, documented verification commands, scripts and tests, workflow callers, and planned bundle contents |
| Prepare a release explicitly requested by the user | The root `AGENTS.md` release checklist, including manifest/install-example synchronization and publication verification within the authorized scope |

## Check structure and meaning

Run these commands from the repository root after changes, or during a read-only
review. They require Python 3.11 or later and only the standard library:

```bash
python3 -B -m unittest discover -s .agents/skills/maintain-impl-planner/tests -v
python3 -B .agents/skills/maintain-impl-planner/scripts/check_consistency.py
git -c core.fsmonitor=false diff --check
```

The checker defaults to the root containing its resolved script location.
Use `--root PATH` to check a different checkout. It prints all discovered
structural inconsistencies and exits with `0` for success, `1` for inconsistent
contents, or `2` for invalid arguments or an invalid root.

It checks only the root source-of-truth list, README layout inventories,
the example index, and the two shared-instruction links. Wildcards are expanded;
missing entries, stale paths, duplicate coverage, and missing sections fail the
check. Fenced examples and prose are excluded. It is not a general Markdown
link checker.

Separately review the affected prose for agreement between the contract,
examples, and both languages. For contract changes, check that existing examples
still demonstrate the required outcomes and that optional guidance has not
become a contradictory requirement. Passing structural checks does not establish
semantic agreement or generated-plan quality.

## Verify packaging and report evidence

Run the seven APM commands in the root `AGENTS.md` validation section. Inspect
both pack dry runs: the distributed skill and its references must be present;
repository maintenance skills, tests, and CI must not enter the package.
Keep the package's planning-only boundary.

Before a requested commit or PR update, inspect the final diff and working-tree
status and stage only intended files. Report:

- The change and related surfaces checked.
- Actual check results, including warnings and unexecuted checks.
- Content-review results separately from command results.
- Native skill discovery separately from file/link reachability.

For example, APM policy-fetch warnings are not proof that policy checks passed,
and an accessible `.claude/skills` path is not proof that Claude loaded the skill.
When publishing was requested, verify the resulting remote state using the root
release checklist; otherwise do not initiate release actions.
