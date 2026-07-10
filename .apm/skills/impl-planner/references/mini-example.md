# impl-planner Mini Example

This example shows the expected density for a small English request. Adapt language and labels to the user's request.

```md
## Repository Understanding

- This package defines a planning-only APM skill and keeps the skill contract, examples, and README usage guidance aligned.
- The implementation is documentation-driven: `SKILL.md` is the entrypoint, `plan-contract.md` defines the output shape, and README files explain user-facing usage.
- Validation is handled through APM audit and dry-run packaging commands.
- `[Observed]` evidence refers to files and commands actually inspected; proposed changes are labeled separately.

## Missing Context and Ambiguities

### Blocking now

- None.

### Can proceed with assumptions

- Assume the existing documentation structure should stay intact and only wording or template examples change.

### Can confirm during implementation

- Confirm the updated prompt examples still map cleanly to the skill contract before finalizing docs.

## Assumptions

- The package remains planning-only.
- The plan should prefer explicit context capture over free-form narrative when the user asks for a detailed prompt.

## Plan.md

Plan status: Final

## Milestone 1: Update prompt examples

### goal

- Document a compact prompt shape for small requests and a template-heavy prompt shape for detailed requests.

### requirements covered

- `R1`: Prompt templates consistently capture the desired outcome and relevant repository context.

### implementation approach

- `[Observed]` Align the existing English and Japanese templates with the contract's input terminology.
- `[Proposed]` Update the minimal template first, then apply the same wording to the detailed template and README references.

### files / modules likely affected

- `README.md`: `[Observed]` English user-facing usage guidance must match the prompt contract.
- `README.ja.md`: `[Observed]` Japanese usage guidance must stay aligned with the English README.
- `SKILL.md` and `plan-contract.md`: `[Proposed]` change only if the prompt contract itself changes.

### out of scope

- Reworking APM packaging behavior or adding implementation-time automation.

### acceptance criteria

- `AC1 [R1]` English and Japanese READMEs both show the list-based minimal prompt and detailed prompt.
- The detailed prompt includes fields for domain knowledge that AI is likely to miss.
- The detailed prompt includes a field for points that need detailed explanation or judgment from AI.
- The detailed prompt asks for broad impact surfaces when that matters, including entrypoints, routing, registration, tests, fixtures, and docs.
- The wording stays planning-only and does not imply implementation work.

### validation commands

- `V1 [AC1][Observed]` `apm audit --file .apm/skills/impl-planner/SKILL.md`
- `V2 [AC1][Observed]` `apm pack --dry-run`

### decision notes to avoid oscillation

- Prefer list-based prompt templates over prose-heavy examples for the detailed input section.
- When improving prompt templates, bias toward prompting for likely impact surfaces instead of only the obvious edit target.
```
