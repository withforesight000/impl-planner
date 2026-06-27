---
name: impl-planner
description: Create implementation plans for software repositories or configuration-management tool repositories. Use when the user asks for an implementation plan, 実装 plan, Plan.md, milestones, planning before coding, 実装前の計画, or decision support for a new feature/change. This skill is planning-only: do not implement, edit files, run mutating commands, or instruct another agent to proceed with implementation.
---

# impl-planner

Use this skill to produce an implementation plan for a software repository change or a configuration-management tool repository change. Stay in planning mode. Do not implement code, edit files, apply migrations, run formatters that rewrite files, or issue commands whose purpose is to perform the change.

## Workflow

1. Ground the plan in the environment before asking questions.
   - Read or search relevant files, configs, schemas, types, manifests, docs, and existing patterns.
   - Use non-mutating commands only. Dry-run checks and tests are allowed when they do not edit tracked source.
   - Do not ask the user for facts that can be discovered from the repository.
   - Accept user prompts in Japanese or English.
2. Separate unknowns before planning.
   - List what would break the plan if unanswered now.
   - List what can proceed under explicit assumptions.
   - List what can be confirmed during implementation.
3. State assumptions explicitly.
   - Prefer conservative assumptions that follow repository conventions.
   - If an assumption affects architecture, data safety, compatibility, security, or operations, call it out.
4. Produce the final plan in Plan.md style using the contract in `references/plan-contract.md`.
   - Write explanatory prose and bullet contents in the same language the user used for the request.
   - Use the English or Japanese structural labels from the contract based on the user's request language, unless the user explicitly asks for a different variant.
   - Scale the plan to the task size: small, low-risk changes can use one concise milestone and omit empty optional subsections; risky or cross-cutting changes should use the full structure.
5. Include usage prompts for future users when useful.
   - Prefer a short prompt example section only when it helps reuse the skill.
   - Include both a minimal prompt and a detailed prompt when you include the section.
6. Self-check the plan before returning it.
   - Confirm acceptance criteria are observable.
   - Confirm validation commands are concrete or the validation class is explicit.
   - Confirm risks have matching rollback or mitigation notes when risk exists.
   - Confirm assumptions are explicit and do not hide blocking unknowns.

## Planning Rules

- Prefer existing codebase conventions, frameworks, module boundaries, helper APIs, and validation style.
- Preserve type safety.
- Avoid silent failure. Plans must require visible errors, validation, or explicit fallback behavior where failure is possible.
- For configuration-management tool repositories, account for inventory/group vars, idempotence, handler behavior, check mode, secrets, role boundaries, and rollback implications.
- For software repositories, account for public interfaces, compatibility, migrations, data flow, failure modes, test coverage, and deployment or rollout risk when relevant.
- Do not invent detailed schemas, flags, APIs, or validation rules unless the request or discovered code requires them. Where a choice matters, present the decision and a recommended default.
- Prefer Markdown headings and bullet lists. Tables are allowed only when they make comparisons or file lists easier to scan.
- Close every code block if one is used.

## Detail-Request Mode

When the user asks for more detail, asks for decision support, or cannot choose an implementation direction, respond with Markdown bullets that include:

- A clearly marked recommended option.
- Multiple viable options.
- For each option: merits, drawbacks, tradeoffs, and when it applies.
- Any information still needed to decide, without pretending certainty.

After a choice is made, reflect it in the plan's `Assumptions` or milestone `decision notes to avoid oscillation`.

## Output Contract

Read `references/plan-contract.md` before producing the final plan. Follow that structure exactly unless the user explicitly asks for a different format.
