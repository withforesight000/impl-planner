# impl-planner Core Output Contract

Use this compact contract for every implementation plan. Write prose in the
user's language. Use the extended contract only when its trigger applies.

## Required Structure

Start in this order:

- `# <concise implementation plan title>` / `# <短い実装計画のタイトル>`
- `## Purpose and Background` / `## 目的と背景`
- `## Repository Understanding` / `## リポジトリ理解`
- `## Missing Context and Ambiguities` / `## 前提不足・曖昧点`
- `## Plan.md`
- First line inside `## Plan.md`: one status line from the fixed templates below.

Emit only the matching language and status template verbatim:

English:

```text
Plan status: Final (No planning blockers; does not indicate approval, implementation, or validation completion.)
Plan status: Provisional (Important facts or decisions remain unresolved; resolve them before finalizing the implementation approach.)
```

Japanese:

```text
Plan status: Final (実装方針を確定できる計画。承認・実装・検証の完了は意味しません。)
Plan status: Provisional (重要な未確認・未決定事項が残る暫定計画。実装方針の確定には解消が必要です。)
```

The outcome-specific title is the first non-empty output, without a preamble;
do not use a generic title such as `Plan.md`. In label pairs, `/` separates
alternatives: emit only the user's language.

In `Purpose and Background` / `目的と背景`, state the requested outcome, why it
matters, the current problem or motivation, and known user-provided constraints.
Normally use two to four short bullets to explain the current problem, the
intended result, and the main exclusions so the reader can assess intent before
reading implementation details. This is a density guide, not a fixed quota.
When the user did not provide background, say `Not provided.` / `未提供。` rather
than inventing one.

Within `Missing Context and Ambiguities` / `前提不足・曖昧点`, use:

- `### Blocking now` / `### 今答えないと plan が破綻するもの`
- `### Can proceed with assumptions` / `### 仮定を置けば進められるもの`
- `### Can confirm during implementation` / `### 実装中に確認すればよいもの`

Keep each of these three subsections to at most five items for ordinary plans,
or ten for plans using the extended contract. Choose the contract by scope,
uncertainty, and risk, not changed-line count alone. These are ceilings, not
targets: write `None.` / `なし。` when empty. Order items by planning impact and
group genuinely related matters without hiding distinct blockers. If material
items still exceed the limit, investigate further, resolve questions when
interaction is available, or split the plan into coherent scopes before finalizing.
Never omit a material unknown to meet the cap; if it cannot be resolved or split
in the current interaction, disclose the overflow and its impact explicitly rather
than claiming a complete list or an unblocked plan.

For each material unknown, identify who resolves it and the dependent scope:

- Blockers: unresolved matter, required user decision or planner investigation,
  and impact. Follow the question flow in `SKILL.md`; investigate repository-
  answerable facts and do not leave resolvable blockers merely to issue a plan.
- Assumptions: adopted assumption, basis, and impact if wrong, with IDs such as
  A1 for references instead of repetition. Prefer repository conventions and
  call out architecture, compatibility, data safety, security, or operational
  consequences. Keep them in `Can proceed with assumptions`, never a standalone section.
- Implementation-time checks: what to check, when, and consequences of the result.

Explicit user requirements and selected options remain decisions; record their
origin in requirements or decision notes, not as assumptions.

Use `### Milestone N: <short title>` and `####` milestone fields. Every
milestone includes the following labels once, in this order, in the request
language:

- `goal` / `目的`
- `requirements covered` / `対応する要件`
- `implementation approach` / `実装方針`
- `files / modules likely affected` / `影響がありそうなファイル / モジュール`
- `out of scope` / `対象外`
- `acceptance criteria` / `受け入れ条件`
- `validation commands` / `検証コマンド`
- `decision notes to avoid oscillation` / `判断のぶれを防ぐメモ`
- `main risks` / `主なリスク`
- `rollback considerations` / `ロールバック時の考慮事項`

For a small, low-risk change, use one concise milestone and retain every field.
Write `None.` / `なし。` or `Not applicable.` / `該当なし。` when a required field
has no material content.
Do not cap milestone count for larger work. Split milestones only at an
independently verifiable outcome, dependency boundary, risk or rollback unit, or
ownership boundary; do not split merely by file list.

## Grounding and Unknowns

- Summarize the repository's purpose, relevant boundary, likely impact, and
  discovered validation style without repeating its documentation.
- In `Repository Understanding`, identify the scope actually inspected and any
  consequential uninspected or inaccessible documents or related repositories.
  Explain how missing evidence affects the plan; never imply an unread source
  was verified. Do not list irrelevant gaps.
- Use `Plan status: Final` only when no blocker remains. In a non-interactive
  best-effort response with a remaining blocker, use `Provisional` and follow
  its status line with the blocker and dependent scope. For `Final`, add only
  material plan-specific follow-up, not a repeated definition. Report actual
  implementation or validation progress separately; introduce no routine approval gate.

## Milestone Rules

- In `implementation approach`, explain the change mechanism, responsibility
  boundaries, and critical conditions that prevent incorrect implementation.
  Keep necessary ordering and state, failure, compatibility, or safety constraints;
  do not turn the section into a line-by-line coding or testing procedure.
  Put observable completion conditions in `acceptance criteria`, detailed test
  and measurement procedures in `validation commands`, and choice rationale
  and tradeoffs in `decision notes to avoid oscillation`. Refer to their IDs
  instead of repeating their details; retain enough local context to understand
  the approach without chasing references for every sentence.
  For consequential concrete values or prescribed techniques, identify whether
  they come from user requirements, inspected existing behavior, or a planner
  proposal. Give the basis for proposals and distinguish adjustable choices
  from mandatory conditions; do not invent precision where evidence is missing.
  Scale detail to decision needs and implementation risk, not a fixed word or
  bullet count. Shortening must not erase important constraints.
- In `files / modules likely affected`, use a Markdown table with exactly two
  columns: `File / module` and `Reason and planned change` in English, or
  `ファイル / モジュール` and `変更理由・内容` in Japanese. Use one row per file
  or module, combining why it needs attention and what will change in the second
  cell (for example, "To prevent X, update Y"). Identify files by their full
  repository-root-relative paths, not ambiguous basenames. For multiple
  repositories, prefix each path with its repository name and make that convention
  clear. Existing paths must be verified by inspection; mark proposed new paths
  `New file planned` / `新規作成予定`. For modules, name the verified directory
  or relevant file paths. If the location cannot yet be identified, state
  `Path unknown` / `パス未特定` and the known investigation scope rather than
  inventing a path. Grouped entries must still list each path explicitly.
  Connect the reason to the file's responsibility, requirement gap or consequence
  of leaving it unchanged, and requirement ID. An action such as "align wording"
  alone is not a reason. Usually one or two short sentences per cell suffice.
  Group paths only when both the reason and change apply to every listed path.
  For investigation-only or conditional candidates, say why investigation is
  needed, what remains unknown, and the condition for a change; explicitly state
  that modification is not yet confirmed. Do not invent a current defect or imply
  that every listed file must change merely to fill these fields. When there are
  no affected files or modules, use `None.` / `なし。` rather than an empty table.
- Describe the outcome, then the change order that connects current boundaries
  to the target behavior. Do not invent unsupported APIs, schemas, or commands.
- Each milestone's `goal` describes an observable result at its completion, not
  merely an activity. In decision notes, give the source of important choices
  (user instruction, existing specification, or planner proposal), the reason,
  and the main tradeoff where relevant; identify decisions not to reopen.
  Compare alternatives only when needed
  to assess the decision; do not require a table or a label on every sentence.
- Assign stable requirement or constraint IDs such as `R1` and connect them to
  affected surfaces, acceptance criteria, and validation.
- Make acceptance criteria observable. Use existing validation commands when
  discovered; otherwise name the validation class rather than fabricating one.
- Map each criterion to a check that can actually establish it. Package checks
  do not establish semantic agreement between documents; specify a content review
  for such criteria. Do not treat a proposed check as a successful result.
- In `validation commands`, use a Markdown table with exactly three columns:
  `Condition to verify`, `Validation method`, and `Command` in English, or
  `確認する条件`, `検証方法`, and `コマンド` in Japanese. Put the observable
  condition and acceptance IDs in the first cell, the check ID, procedure, and
  expected result in the second, and the verified available command in the third.
  For checks not performed through commands, fill the command cell with a
  parenthesized method label such as `(Document review)` / `(文章レビュー)`
  or `(Manual check)` / `(手動確認)`; do not leave it blank or use a dash.
  If a command is needed but not yet identified, write `Not yet identified` /
  `未特定`; do not invent it or disguise the gap as a manual check.
  Move long commands or multi-step procedures below the table and reference
  them by check ID; use fenced code blocks for commands.
  Keep execution status and results outside the table: use one shared statement
  when all checks are unexecuted, or report individual results by check ID.
  Mark commands `[Observed]`, `[Recommended]`, or `[Unknown]` when provenance
  matters. `[Observed]` means inspected existence or documented use, not a
  successful execution; distinguish actual results from unexecuted checks.
- In `main risks`, use a Markdown table with exactly two columns: `Risk / impact`
  and `Mitigation` in English, or `リスク・影響` and `対応策` in Japanese. Each
  row pairs a concrete failure and its consequence with a prevention, detection,
  or recovery action; reference validation IDs when useful. Do not invent a
  resolved mitigation if an unresolved dependency still blocks the plan.
- All prescribed tables apply to small plans too when entries exist.
  If there is genuinely nothing applicable, use `None.` / `なし。` or
  `Not applicable.` / `該当なし。` instead of an empty table; unknown validation
  commands alone do not make validation inapplicable.

## Final Check

- Structure: required title, headings, order, status template, fields, and table formats.
- Reader decisions: clear outcome/exclusions, decision sources, assumption placement,
  five/ten-item limits and visible overflow; no blocker disguised as an assumption.
- Evidence: inspected scope, missing sources, qualified paths, command provenance,
  actual execution status, and plan status agree.
- Implementation: mechanisms and critical constraints remain clear; values have
  a source/basis, ordering respects architecture, and details are not duplicated.
- Traceability: requirements, file reasons, acceptance, and validation agree;
  checks follow repository style and can establish the claimed conditions.
- Risk and scope: concrete responses, rollback considerations, proportional
  detail, and no implementation or unnecessary approval gates.
