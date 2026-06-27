# impl-planner APM package

`impl-planner` is a planning-only skill for software repositories or configuration-management tool repositories.
Use it when you want Codex, Claude Code, or GitHub Copilot to produce an implementation plan, not to implement the change.

日本語版: [README.ja.md](README.ja.md)

## What this package does

- Produces a Plan.md-style implementation plan
- Can optionally produce a self-contained HTML report when explicitly requested
- Lists ambiguities before planning
- Records assumptions explicitly
- Scales the amount of structure to the task size
- Breaks the plan into milestones with:
  - goal
  - files / modules likely affected
  - acceptance criteria
  - validation commands
  - decision notes to avoid oscillation
  - main risks
  - rollback considerations
- Supports detailed decision support when the answer is not obvious
- Self-checks that acceptance criteria, validation, risks, and rollback notes are actionable
- Can include concise example prompts the user can reuse next time when helpful

## Repository layout

- `apm.yml`: APM package manifest
- `.apm/skills/impl-planner/SKILL.md`: Skill entrypoint
- `.apm/skills/impl-planner/references/plan-contract.md`: Output contract and prompt examples

## How to use the skill

Use this skill when you need an implementation plan for a new feature, a refactor, an Ansible change, or a design decision.
Ask for HTML output only when you want a browser-readable review artifact or visual report.

Minimal prompt:

```text
Use `impl-planner` to create an implementation plan for this task.

Purpose:
Background:
Constraints:
```

Detailed prompt:

```text
Use `impl-planner` to create an implementation plan.

- Repository / system
  - [software repository or configuration-management tool repository name]
- What you want to achieve
  - [what you want to implement]
- In scope
- Out of scope
- Design rules to keep
  - [architecture constraints]
  - [existing patterns]
  - [implementations to avoid]
- Domain knowledge AI is likely to miss
  - [business rules]
  - [exception handling]
  - [background of existing specifications]
- Constraints
  - [backward compatibility]
  - [performance]
  - [security]
  - [operations]
  - [runtime / library constraints]
- Acceptance criteria
- Validation steps
  - [build / test / lint / typecheck / e2e]
  - [manual verification steps]
- Known pitfalls
- Open questions
- Points that need detailed explanation or judgment from AI
```

For better plans, provide the scope, constraints, acceptance criteria, validation steps, known risks, unresolved questions, domain knowledge that AI is likely to miss, and any points that need detailed explanation or judgment from AI up front.

## How to verify the package

From the repository root:

```bash
apm audit --file .apm/skills/impl-planner/SKILL.md
apm pack --dry-run
apm pack --archive --dry-run -v
```

These checks confirm that the skill metadata is valid and that the package resolves to the expected bundle contents.

## How to distribute

- Use `apm pack` to create a distributable bundle.
- Use the packed artifact for downstream installation or release automation.
- Keep `apm.yml` and `.apm/skills/impl-planner/` as the package source of truth.

## How to install with `apm`

You do not need to clone this repository to install the skill on your PC.
Install it directly from the repository reference:

```bash
apm install withforesight000/impl-planner --global --target codex
```

If you want to preview the install before applying it, use:

```bash
apm install withforesight000/impl-planner --dry-run --global --target codex
```

You can also install the same package for other supported targets:

```bash
apm install withforesight000/impl-planner --global --target claude,copilot
```

If you do have a working copy, you can still pack it first with `apm pack --archive` and install the resulting bundle the same way.

## Notes

- The skill is planning-only.
- It must not instruct the agent to edit files, run mutating commands, or proceed to implementation.
- When the user asks for more detail, the skill should return multiple options, a recommended option, and tradeoffs.
- The skill accepts prompts in both Japanese and English.
