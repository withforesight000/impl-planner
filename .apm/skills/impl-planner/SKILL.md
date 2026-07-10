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
   confirmation. Ask at most three high-impact questions after research. If
   interaction is unavailable, return a clearly marked provisional plan.
3. Read `references/plan-contract.md` and produce its Markdown contract in the
   user's language. Markdown is the default; HTML is explicit opt-in only.
4. Keep the plan proportional. Use one concise milestone for a small, low-risk
   change; trace outward to callers, configuration, tests, and docs when the
   repository evidence indicates they are affected.
5. Before responding, confirm the plan is grounded, implementation-ready,
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

- `plan-contract.md`: always; the compact, required output structure.
- `extended-plan-contract.md`: medium or larger, cross-cutting, data-affecting,
  security-sensitive, deployment-sensitive, or configuration-management work.
- `research-and-critique.md`: delegated research or a fresh-context critic pass.
- `detail-request.md`: detailed decision support, multiple options, or an
  undecided implementation direction.
- `software-task-profiles.md`: API/public contract, UI, async work, dependency
  upgrade, monorepo, or shared package changes.
- `risk-task-profiles.md`: migration, backfill, authentication, authorization,
  secrets, or security-boundary changes.
- `config-management-profile.md`: Ansible or another configuration-management
  change.
- `html-output.md`: explicit HTML, browser-readable artifact, or visual report.
- `examples.md`, `mini-example.md`, or `prompt-templates.md`: only when an
  example or reusable prompt would help the user.
- `platform-notes.md`: Codex, Claude Code, GitHub Copilot, native Plan modes,
  subagents, or platform-specific operation.
