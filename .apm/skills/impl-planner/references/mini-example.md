# impl-planner Mini Example

This illustrative example shows the expected density for a small English request.
Inspection statements describe the assumed example scenario, not checks performed
by reading this file. Adapt language and labels to the user's request.

````md
# Align planning prompt terminology

## Purpose and Background

- Current prompt terminology differs between usage examples; after this change, readers can copy equivalent English and Japanese prompts from the READMEs and bundled reference.
- User requirement: preserve bilingual guidance and the planning-only behavior. Packaging behavior and output headings remain unchanged.

## Repository Understanding

- Inspected: both READMEs, `references/prompt-templates.md`, `SKILL.md`, and `references/plan-contract.md` under `.apm/skills/impl-planner/`, plus `apm.yml` and `AGENTS.md`.
- The package distributes planning instructions; its existing validation uses APM audit and dry-run packaging. No consequential external references remain unread in this scenario.

## Missing Context and Ambiguities

### Blocking now

- None.

### Can proceed with assumptions

- A1: The inspected prompt duplication can be maintained directly without a generator. If more copies are discovered, include them in the consistency review before reconsidering tooling; no user decision is needed to proceed.

### Can confirm during implementation

- Implementer: compare the edited examples with the contract and run the package checks below; mismatches require correcting the affected wording or bundle.

## Plan.md

Plan status: Final (No planning blockers; does not indicate approval, implementation, or validation completion.)

The changes and checks below have not been performed.

### Milestone 1: Update prompt examples

#### goal

- Readers can copy equivalent minimal and detailed prompts from either README or the bundled reference.

#### requirements covered

- `R1`: Prompt templates consistently capture the desired outcome and relevant repository context.
- `R2`: Preserve the package's planning-only behavior and valid bundle.

#### implementation approach

- Planner proposal: align terminology in the bundled minimal and detailed templates, then mirror the corresponding language in each README. Apply A1 to any additional copies found.

#### files / modules likely affected

Paths are relative to this repository's root.

| File / module | Reason and planned change |
| --- | --- |
| `README.md` and `README.ja.md` | To give readers equivalent copyable prompts in both languages (R1), align the minimal and detailed wording with the corresponding language in the bundled reference. |
| `.apm/skills/impl-planner/references/prompt-templates.md` | Updating only the READMEs would leave installed skill users with inconsistent prompts (R1), so update the distributed templates with the same terminology. |

#### out of scope

- Reworking packaging, output headings, or adding implementation-time automation.

#### acceptance criteria

- `AC1 [R1]` Minimal and detailed prompts agree across README and bundled copies in each language, with equivalent meaning between languages.
- `AC2 [R2]` Prompts request planning only, without instructions to implement.
- `AC3 [R2]` Required package checks pass and the dry-run bundle includes the prompt reference.

#### validation commands

All checks below are unexecuted. `[Observed]` identifies documented commands only.

| Condition to verify | Validation method | Command |
| --- | --- | --- |
| AC1, AC2: Prompts agree across languages and copies and remain planning-only. | V1: Compare the minimal and detailed prompts in both READMEs and the bundled reference, including meaning, fields, and planning-only wording against the Skill contract. | (Document review) |
| AC3: Required package checks pass and the prompt reference is bundled. | V2: Run the documented package checks; require successful exits and confirm the prompt reference appears in the bundle file list. | [Observed] See the V2 command block below, from `AGENTS.md`. |

V2 commands:

```bash
apm audit --file .apm/skills/impl-planner/SKILL.md
apm audit --file apm.yml
apm pack --dry-run
apm pack --archive --dry-run -v
apm install --dry-run --target codex
apm install --dry-run --target claude
apm install --dry-run --target copilot
```

#### decision notes to avoid oscillation

- User decision: retain bilingual, planning-only guidance. Planner proposal: reuse the existing list structure to keep prompts easy to copy; this preserves some duplication, checked by V1.

#### main risks

| Risk / impact | Mitigation |
| --- | --- |
| A terminology change can leave English and Japanese examples out of sync, giving readers different planning instructions. | Review both READMEs and the bundled templates together using V1. |

#### rollback considerations

- Revert the terminology change as one documentation-only commit if it causes confusion.
````
