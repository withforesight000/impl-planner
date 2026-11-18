---
name: impl-planner
description: "Create repository-grounded plans for software or configuration-management changes. Use for implementation plans (実装計画 / 実装 plan), Plan.md, implementation milestones, or comparing implementation approaches before coding. Planning only; does not implement changes."
---

# impl-planner

Write an implementation plan. Leave file edits, migrations, and other
source-changing commands to implementation. Keep delegated work read-only.

## Core Workflow

1. Inspect the repository before asking questions. Read relevant entrypoints,
   callers, configuration, tests, documentation, and existing validation. Use
   non-mutating commands only; do not ask for facts the repository can answer.
   Inspect direct dependents of a central file before fixing the affected surface.
2. Identify what blocks the plan, what can proceed under a safe assumption, and
   what can wait until implementation. After research, ask one to three
   questions per round about issues that would materially change the plan.
   Follow each round with research on the affected area. Ask again only if a
   remaining or newly discovered blocker materially changes the plan.
   Explain recommendations and tradeoffs in Markdown using
   `references/detail-request.md` when it applies. Use the structured-question
   tool for the actual question or selection when available and present the
   selection prompt once. Otherwise, ask a concise question in conversation if
   possible. If a blocker remains and you cannot interact with the user, return
   a clearly marked provisional plan that states the blocker and its impact.
   In that case, record unresolved decisions in the plan itself. Avoid leaving
   a question awaiting an answer or mimicking the selection tool in prose.
3. Before drafting, classify the change. For medium or larger, cross-cutting,
   data-affecting, security-sensitive, deployment-sensitive, or
   configuration-management work, read `references/extended-plan-contract.md`.
   When in doubt, read it.
4. For work using the extended contract, delegate meaningful independent
   read-only research before drafting when subagent tools are available. If
   only independent critique is useful, defer delegation until step 7. Read
   `references/research-and-critique.md` before delegating. Small or strictly
   sequential work needs no delegation. If subagent tools are unavailable,
   have the authoring agent review the completed draft as described in step 7.
5. Read `references/plan-contract.md` and produce its Markdown contract in the
   user's language, including its required structure for small plans.
6. Apply its milestone sizing rules; trace outward to callers, configuration,
   tests, and docs when repository evidence indicates they are affected.
7. For work using the extended contract, read `references/research-and-critique.md`
   and run its critic checklist after drafting. If independent critique is the
   qualifying task from step 4, delegate it now when subagent tools are available.
   Otherwise prefer a reviewer with fresh context when useful and available.
   In other cases, have the authoring agent review the complete draft
   against the checklist. Run this review even if another agent handled research.
8. Apply `references/plan-contract.md` → `Final Check` to every plan before responding.

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
- `references/examples.md`, `references/mini-example.md`, or
  `references/prompt-templates.md`: only when an example would help the user.
- `references/platform-notes.md`: Codex, Claude Code, GitHub Copilot, native Plan modes,
  subagents, or platform-specific operation.
