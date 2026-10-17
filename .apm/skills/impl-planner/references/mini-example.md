# impl-planner Mini Example

This illustrative example shows the expected density for a small English request.
Inspection statements describe the assumed example scenario, not checks performed
by reading this file. Adapt language and labels to the user's request.

```md
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

- Planner assumption A1 below keeps the change local; no user decision is needed to proceed.

### Can confirm during implementation

- Implementer: compare the edited examples with the contract and run the package checks below; mismatches require correcting the affected wording or bundle.

## Assumptions

- A1: The inspected prompt duplication can be maintained directly without a generator. If more copies are discovered, include them in the consistency review before reconsidering tooling.

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

- `README.md` and `README.ja.md`: align the user-facing prompt wording in both languages.
- `.apm/skills/impl-planner/references/prompt-templates.md`: distribute the same wording with the skill.

#### out of scope

- Reworking packaging, output headings, or adding implementation-time automation.

#### acceptance criteria

- `AC1 [R1]` Minimal and detailed prompts agree across README and bundled copies in each language, with equivalent meaning between languages.
- `AC2 [R2]` Prompts request planning only, without instructions to implement.
- `AC3 [R2]` Required package checks pass and the dry-run bundle includes the prompt reference.

#### validation commands

All checks below are unexecuted. `[Observed]` identifies documented commands only.

- `V1 [AC1, AC2]` Compare the minimal and detailed prompts in both READMEs and the bundled reference, including meaning, fields, and planning-only wording against the Skill contract.
- `V2 [AC3][Observed]` Run the package's complete validation list from `AGENTS.md`: both `apm audit --file` checks, both `apm pack` dry runs, and all three target-specific `apm install --dry-run` checks. Inspect the file list for the bundled prompt reference.

#### decision notes to avoid oscillation

- User decision: retain bilingual, planning-only guidance. Planner proposal: reuse the existing list structure to keep prompts easy to copy; this preserves some duplication, checked by V1.

#### main risks

- A terminology change can leave English and Japanese examples out of sync.
- Mitigation: review both README files and prompt templates together.

#### rollback considerations

- Revert the terminology change as one documentation-only commit if it causes confusion.
```
