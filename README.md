# impl-planner APM package

`impl-planner` is a planning-only skill for software repositories or configuration-management tool repositories.
Use it when you want Codex, Claude Code, or GitHub Copilot to produce an implementation plan, not to implement the change.

日本語版: [README.ja.md](README.ja.md)

## What this package does

- Produces a Plan.md-style implementation plan
- Can optionally produce a self-contained HTML report when explicitly requested
- Summarizes repository understanding before planning
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
- Requires reasons for likely affected files and modules
- Traces likely impact outward from entrypoints, call sites, configs, tests, and adjacent docs when estimating affected files
- Aligns validation commands with the repository's existing validation style
- Checks for an existing architecture or layering pattern such as Clean Architecture, MVC, Hexagonal Architecture, DDD, or feature-based structure and respects it when present
- Makes milestone ordering explicit when milestones depend on one another
- Supports detailed decision support and rejected-alternative notes when the answer is not obvious
- Self-checks that acceptance criteria, validation, risks, mitigations, and rollback actions are actionable
- Can include concise example prompts the user can reuse next time when helpful

## Repository layout

- `apm.yml`: APM package manifest
- `.apm/skills/impl-planner/SKILL.md`: Skill entrypoint
- `.apm/skills/impl-planner/references/plan-contract.md`: Core output contract
- `.apm/skills/impl-planner/references/examples.md`: Optional examples and reusable prompt templates
- `.apm/skills/impl-planner/references/detail-request.md`: Optional decision-support response structure
- `.apm/skills/impl-planner/references/html-output.md`: Optional HTML report constraints
- `.apm/skills/impl-planner/references/formatting.md`: Optional formatting constraints

## How to use the skill

Use this skill when you need an implementation plan for a new feature, a refactor, an Ansible change, or a design decision.
Ask for HTML output only when you want a browser-readable review artifact or visual report.

Minimal prompt:

```text
Use `impl-planner` to create an implementation plan for this task.

- What you want to achieve
  - [what you want to achieve]
- Background
  - [why it is needed / what problem exists now]
```

Detailed prompt:

```text
Use `impl-planner` to create an implementation plan.

- Repository / system
  - [software repository or configuration-management tool repository name]
- Repository understanding
  - [what this repository is meant to achieve]
  - [main implementation approach / primary processing flow]
- What you want to achieve
  - [what you want to implement]
- Background
  - [why it is needed / what problem exists now]
- Domain knowledge AI is likely to miss
  - [business rules]
  - [exception handling]
  - [background of existing specifications]
- In scope
- Out of scope
- Points that need detailed explanation or judgment from AI
- Design rules to keep
  - [architecture constraints]
  - [existing patterns]
  - [implementations to avoid]
- Impact surfaces to inspect
  - [entrypoint / routing / registration]
  - [related test / fixture / docs]
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
```

Why each detailed field helps:

| Field | Why it helps |
| --- | --- |
| `Repository / system` | Anchors the plan to the correct codebase, runtime, and repository type. This is especially useful when the workspace has multiple packages, services, roles, or configuration-management targets. |
| `Repository understanding` | Helps the planner reason from the system's purpose and main flow before drilling into files. It also reduces plans that are locally plausible but misaligned with how the repository actually delivers value. |
| `What you want to achieve` | Defines the target outcome so milestones stay outcome-oriented. Without this, the plan can drift into a list of edits instead of describing the behavior or state that should exist after implementation. |
| `Background` | Explains why the change matters and which current problem the plan should solve. This helps the planner choose tradeoffs that fit the motivation instead of optimizing for an unrelated interpretation of the request. |
| `Domain knowledge AI is likely to miss` | Captures business rules, exceptions, and historical context that are hard to infer from code alone. Supplying this up front prevents the plan from flattening important edge cases into generic implementation steps. |
| `In scope` | Prevents the plan from becoming too narrow or leaving intended work implicit. It gives the planner permission to include all work that should be considered part of the change. |
| `Out of scope` | Prevents implementation drift and avoids planning work that should not happen now. This is useful when adjacent refactors, migrations, or cleanup tasks are tempting but would make the plan too broad. |
| `Points that need detailed explanation or judgment from AI` | Directs extra reasoning toward the decisions where AI help is most valuable. Use this for areas where you want tradeoffs, alternatives, or deeper explanation rather than a terse milestone list. |
| `Design rules to keep` | Preserves architecture, existing patterns, and implementation constraints. It helps the planner respect layer boundaries, module ownership, naming conventions, and approaches the repository already uses. |
| `Impact surfaces to inspect` | Reduces missed files by pointing to entrypoints, registration, tests, fixtures, and docs that may move together. This is one of the strongest fields for improving the `files / modules likely affected` section. |
| `Constraints` | Keeps compatibility, performance, security, operations, and runtime limits visible in the plan. Constraints make the plan more realistic by ruling out solutions that would be technically possible but unacceptable for this repository. |
| `Acceptance criteria` | Makes completion observable and reviewable. Clear criteria help the implementer and reviewer agree on when the change is actually done. |
| `Validation steps` | Aligns the plan with the checks the implementer should run. Providing known commands or manual checks helps the plan follow the repository's existing validation style instead of guessing. |
| `Known pitfalls` | Surfaces failure modes that may not be obvious from a normal code search. This helps the plan include mitigations, rollback notes, or focused validation for areas that have caused issues before. |
| `Open questions` | Separates blockers, assumptions, and items that can be confirmed during implementation. This prevents uncertainty from being hidden inside the plan as if it were already decided. |

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
