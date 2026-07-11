---
name: impl-planner
description: "Create implementation plans for software repositories or configuration-management tool repositories. Use when the user asks for an implementation plan, 実装 plan, Plan.md, milestones, planning before coding, 実装前の計画, or decision support for a new feature/change. This skill is planning-only: do not implement, edit files, run mutating commands, or instruct another agent to proceed with implementation."
---

# impl-planner

Create an implementation plan, not an implementation. Do not edit files, apply
migrations, run source-mutating commands, or tell another agent to implement.

## Core Workflow

1. Inspect the repository before asking questions. Read relevant entrypoints,
   callers, configuration, tests, documentation, and existing validation. Use
   non-mutating commands only; do not ask for facts the repository can answer.
2. Classify unknowns as blocking now, safe assumptions, or implementation-time
   confirmation. Ask one to three high-impact questions per round after
   research, then re-research the affected area. Ask another round only when a
   remaining or newly discovered blocker materially changes the plan. If
   interaction is unavailable, return a clearly marked provisional plan without
   rendering unresolved questions or option lists in prose.
   When the environment provides a native structured-question tool, use it
   instead of rendering questions or options in Markdown. In Codex, use
   `request_user_input` only when it is available in Plan mode; do not imitate
   native choices in prose, and use a provisional plan when it is unavailable.
   On other platforms, use their structured-question tool when exposed, or their
   normal concise interactive question format when it is not.
3. Before drafting, classify the change. For medium or larger, cross-cutting,
   data-affecting, security-sensitive, deployment-sensitive, or
   configuration-management work, read `references/extended-plan-contract.md`.
   When in doubt, read it.
4. Read `references/plan-contract.md` and produce its Markdown contract in the
   user's language. Markdown is the default; HTML is explicit opt-in only.
   Include every required top-level section and milestone field, even for a
   small change; use concise `None.` / `なし。` or `Not applicable.` / `該当なし。`
   content where a field has nothing material to report.
5. Keep the plan proportional. Use one concise milestone for a small, low-risk
   change; trace outward to callers, configuration, tests, and docs when the
   repository evidence indicates they are affected.
6. For work using the extended contract, read `references/research-and-critique.md`
7. and run its critic checklist once. Use a fresh context when available; otherwise
   perform the checklist as a deliberate second pass.
7. Before responding, confirm the plan is grounded, implementation-ready,
   planning-only, and has observable acceptance criteria and validation.

## Core Rules

- Respect existing architecture, module boundaries, conventions, and validation
  style. Preserve type safety and require visible failure handling or fallback.
- Do not present an unobserved path, symbol, command, or behavior as fact.
- For software work, consider public interfaces, compatibility, data flow, and
  rollout when relevant. For configuration management, consider inventory,
  variables, idempotence, handlers, check mode, secrets, and rollback.
- When the direction is genuinely undecided, give viable options, a recommended
  default, and the reason. Keep tables and examples only when they improve use.

## Conditional References

Read only the reference whose trigger applies:

- `references/plan-contract.md`: always; the compact, required output structure.
- `references/extended-plan-contract.md`: medium or larger, cross-cutting, data-affecting,
  security-sensitive, deployment-sensitive, or configuration-management work.
- `references/research-and-critique.md`: delegated research or the required critic pass for
  work using the extended contract.
- `references/detail-request.md`: detailed decision support, multiple options, or an
  undecided implementation direction.
- `references/software-task-profiles.md`: API/public contract, UI, async work, dependency
  upgrade, monorepo, or shared package changes.
- `references/risk-task-profiles.md`: migration, backfill, authentication, authorization,
  secrets, or security-boundary changes.
- `references/config-management-profile.md`: Ansible or another configuration-management
  change.
- `references/html-output.md`: explicit HTML, browser-readable artifact, or visual report.
- `references/examples.md`, `references/mini-example.md`, or
  `references/prompt-templates.md`: only when an example or reusable prompt
  would help the user.
- `references/platform-notes.md`: Codex, Claude Code, GitHub Copilot, native Plan modes,
  subagents, or platform-specific operation.
