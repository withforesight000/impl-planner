# impl-planner Output Contract

This reference defines the required output shape for implementation planning. Use it for software repository changes or configuration-management tool repository changes.

## Required Top-Level Output

Use the instructions below to choose the right level of detail and labels.
The final plan output must start with the repository-understanding section, followed by the missing-context section, `Assumptions`, then `Plan.md`.
When the user explicitly asks for HTML, use the same content contract in a self-contained HTML report instead of Markdown while preserving the same information and ordering.

- Write explanatory prose and bullet contents in the same language the user used for the request.
- Use the English structural labels for English requests and the Japanese structural labels for Japanese requests unless the user explicitly asks for a different variant.
- Scale the amount of structure to the task size without losing implementation readiness.

## Scale Guidance

- For small, low-risk changes, use one milestone and keep bullets concise.
- For small changes, optional milestone subsections with no meaningful content may be omitted instead of filled with boilerplate.
- Always keep `goal`, `files / modules likely affected`, `acceptance criteria`, and `validation commands` for each milestone.
- Use the full milestone structure for cross-cutting, risky, data-affecting, security-sensitive, deployment-sensitive, or configuration-management changes.
- If the user asks for a concise plan, prefer fewer milestones and shorter bullets while preserving assumptions, observable acceptance criteria, and validation.
- When identifying likely affected files, include the direct edit targets plus the surrounding surfaces that the repository evidence points to: entrypoints, callers, routing or registration, config, tests, fixtures, docs, and generated artifacts when applicable.
- If the repository shows an established architecture or layering pattern, keep the plan aligned with that structure and avoid suggesting changes that would cross or collapse the existing boundaries without justification.

## Structural Labels

Use this label set for English requests:

- `## Repository Understanding`
- `## Missing Context and Ambiguities`
- `### Blocking now`
- `### Can proceed with assumptions`
- `### Can confirm during implementation`
- `## Assumptions`
- `## Plan.md`
- `## Milestone N: <short title>`
- `### goal`
- `### files / modules likely affected`
- `### out of scope`
- `### acceptance criteria`
- `### validation commands`
- `### decision notes to avoid oscillation`
- `### main risks`
- `### rollback considerations`

Use this label set for Japanese requests:

- `## リポジトリ理解`
- `## 前提不足・曖昧点`
- `### 今答えないと plan が破綻するもの`
- `### 仮定を置けば進められるもの`
- `### 実装中に確認すればよいもの`
- `## Assumptions`
- `## Plan.md`
- `## Milestone N: <short title>`
- `### goal`
- `### files / modules likely affected`
- `### out of scope`
- `### acceptance criteria`
- `### validation commands`
- `### decision notes to avoid oscillation`
- `### main risks`
- `### rollback considerations`

## Repository Understanding / リポジトリ理解

- Summarize what the repository appears to achieve and how it achieves it.
- Include detected architecture or layering, relevant entrypoints, likely impact surface, and existing validation style when discoverable.
- Keep this section concise; use it to ground the plan rather than to repeat repository documentation.

## Missing Context and Ambiguities / 前提不足・曖昧点

### Blocking now / 今答えないと plan が破綻するもの

- List ambiguities that materially prevent a correct plan.
- If none, say `None.` for English or `なし。` for Japanese.

### Can proceed with assumptions / 仮定を置けば進められるもの

- List uncertainties that can proceed under explicit assumptions.
- Keep assumptions concrete and implementation-relevant.

### Can confirm during implementation / 実装中に確認すればよいもの

- List items that can be verified while implementing without changing the overall plan.

## Assumptions

- State all assumptions used by the plan.
- Include assumptions about scope, compatibility, migration, test strategy, deployment, runtime, data safety, and operational constraints when relevant.
- If the user asked for detail and an option was selected or recommended, record that decision here or in milestone decision notes.

## Plan.md

Use `## Milestone N: <short title>` for each milestone. Keep the milestone heading structure consistent within the plan.

### goal

- Describe the milestone outcome, not just an activity.

### files / modules likely affected

- List likely files, modules, roles, playbooks, services, APIs, schemas, or docs.
- For each likely affected file or module, include why it is likely affected.
- Use paths when they are known from exploration.
- If exact paths are unknown, name the module or subsystem and explain what will be discovered.
- Prefer a complete impact surface over a minimal edit list. If discovery shows a likely dependency chain, include the upstream entrypoint and downstream tests or adjacent modules rather than only the file that the user named.

### out of scope

- State notable excluded areas when naming them prevents implementation drift.
- Omit this subsection for small changes when there is no meaningful exclusion to record.

### acceptance criteria

- Define observable completion criteria.
- Include behavior, compatibility, error handling, and non-regression criteria where relevant.

### validation commands

- List concrete commands when known.
- Prefer commands and validation classes that match the repository's existing validation style.
- If commands are unknown, list the expected class of validation, such as typecheck, unit test, integration test, configuration-management syntax-check, configuration-management check mode, or targeted smoke test.
- Do not include commands that mutate source as a validation step unless the user explicitly wants implementation execution.

### decision notes to avoid oscillation

- Record decisions that should not be reopened during implementation unless new facts invalidate them.
- Include recommended defaults and rejected alternatives when they are likely to cause rework.

### main risks

- List the highest-risk technical or operational failure modes.
- Include data safety, compatibility, rollout, security, idempotence, and dependency risks where relevant.

### rollback considerations

- Explain how to revert or disable the change.
- For configuration-management tool repositories, include configuration rollback, inventory rollback, role/play rollback, and service state concerns when applicable.

## Self-Check Gate

Before returning the plan, verify these points and revise the plan if any check fails:

- Each acceptance criterion is observable by a reviewer, test, command, or runtime behavior.
- Each validation command is concrete, or the validation class is explicit when the exact command is unknown.
- Validation commands reflect the repository's existing validation style when it is discoverable.
- Each meaningful risk has a corresponding rollback, mitigation, or decision note.
- Blocking unknowns are not silently converted into assumptions.
- The affected-file list reflects the discovered impact surface, not only the obvious edit target, when repository structure indicates additional touched areas.
- Each likely affected file or module has a short reason tied to repository evidence or an explicit assumption.
- The plan does not ignore an established architecture or layering pattern if repository evidence shows one is in use.
- The plan size matches the task size and avoids filler sections.

## Optional References

Read these files only when their trigger applies:

- `examples.md`: read when adding a mini-example or future usage prompt examples would help the user reuse the skill.
- `detail-request.md`: read when the user asks for detailed decision support, multiple options, tradeoffs, or cannot choose an implementation direction.
- `html-output.md`: read when the user explicitly asks for HTML, a browser-readable artifact, or a visual report.
- `formatting.md`: read when formatting constraints are unclear or the output needs tables, code blocks, or unusually compact structure.
