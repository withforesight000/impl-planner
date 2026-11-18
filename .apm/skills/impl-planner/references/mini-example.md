# impl-planner Mini Example

This English example shows how much detail to include in a small plan. The
inspection notes describe a hypothetical scenario. Follow the contract's
labels for the user's language.

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

- `R1`: Both prompt versions ask for the desired outcome and background. The detailed version also asks for relevant repository context.
- `R2`: Preserve the package's planning-only behavior and valid bundle.

#### implementation approach

- Planner proposal: edit the bundled minimal and detailed templates directly, then mirror the corresponding language in each README, following A1. Preserve the planning-only boundary in R2; completion conditions and comparison procedures are defined in AC1–AC3 and V1–V2.

#### files / modules likely affected

Paths are relative to this repository's root.

| File / module | Reason and planned change |
| --- | --- |
| `README.md` and `README.ja.md` | To give readers equivalent copyable prompts in both languages (R1), align the minimal and detailed wording with the corresponding language in the bundled reference. |
| `.apm/skills/impl-planner/references/prompt-templates.md` | Updating only the READMEs would leave installed skill users with inconsistent prompts (R1), so update the distributed templates with the same terminology. |

#### out of scope

- Reworking packaging, output headings, or adding implementation-time automation.

#### acceptance criteria

- `AC1 [R1]` The minimal prompt asks for the desired outcome and background. The detailed prompt also asks for relevant repository context. Each README matches its bundled copy, and the English and Japanese prompts have equivalent meaning.
- `AC2 [R2]` Prompts request planning only, without instructions to implement.
- `AC3 [R2]` Required package checks pass and the dry-run bundle includes the prompt reference.

#### validation commands

All checks below are unexecuted. `[Observed]` identifies documented commands only.

| Condition to verify | Validation method | Command |
| --- | --- | --- |
| AC1, AC2: Each prompt asks for the intended information, agrees across copies and languages, and requests planning only. | V1: Compare each README with the bundled reference and compare the two languages. Check that both prompts ask for the outcome and background, the detailed prompt also asks for repository context, and both request planning only. | (Document review) |
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

- The direct-edit approach follows the inspected duplication and avoids adding tooling for this wording change. It preserves some duplication, checked by V1. This is a planner choice under A1, not an additional user requirement.

#### main risks

| Risk / impact | Mitigation |
| --- | --- |
| A terminology change can leave English and Japanese examples out of sync, giving readers different planning instructions. | Review both READMEs and the bundled templates together using V1. |

#### rollback considerations

- Revert the terminology change as one documentation-only commit if it causes confusion.
````
