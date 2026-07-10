# impl-planner Extended Planning Contract

Read this only for medium or larger, cross-cutting, data-affecting,
security-sensitive, deployment-sensitive, or configuration-management work.
It extends `plan-contract.md`; do not repeat its general rules.

## Evidence and Blockers

- Label direct repository facts `[Observed]`, evidence-based conclusions
  `[Inferred]`, intended changes `[Proposed]`, and unresolved facts `[Unknown]`.
  Anchor observed claims to a path, symbol, config key, command, or equivalent.
- In an interactive environment, ask at most three questions only when the
  answer changes architecture, compatibility, data safety, security, operations,
  or scope. Safe assumptions remain visible and do not stop the plan.
- For a provisional plan, branch only the milestones changed by the unresolved
  decision and do not describe the result as ready for implementation.

## Extended Milestone Fields

In addition to the core fields, include these labels when they add information:

- `requirements covered` / `対応する要件`: assign stable IDs such as `R1`.
- `out of scope` / `対象外`: prevent adjacent work from expanding the change.
- `decision notes to avoid oscillation` / `判断のぶれを防ぐメモ`: record a
  selected default and rejected alternatives that should not be reopened.
- `main risks` / `主なリスク`: connect material risk to mitigation or validation.
- `rollback considerations` / `ロールバック時の考慮事項`: state disablement,
  reversal, or explicitly irreversible data and service consequences.

Trace every meaningful requirement or constraint through the milestone,
affected surface, observable acceptance criterion, and validation item.

## Extended Final Check

- Current behavior, proposed behavior, public interfaces, data flow, state, and
  error handling are covered where the change affects them.
- Migration, compatibility, rollout, security, idempotence, and dependency risks
  have an explicit mitigation, validation, or rollback path when relevant.
- No unsupported path, symbol, command, or repository behavior is labeled as an
  observed fact.
