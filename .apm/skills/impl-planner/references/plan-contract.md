# impl-planner Core Output Contract

Use this compact contract for every implementation plan. Write prose in the
user's language. Use the extended contract only when its trigger applies.

## Required Structure

Start in this order:

- `# <concise implementation plan title>` / `# <短い実装計画のタイトル>`
- `## Purpose and Background` / `## 目的と背景`
- `## Repository Understanding` / `## リポジトリ理解`
- `## Missing Context and Ambiguities` / `## 前提不足・曖昧点`
- `## Assumptions`
- `## Plan.md`
- First line inside `## Plan.md`: one status line from the fixed templates below.

Use the matching language and status template verbatim, including its parenthetical
explanation. Keep `Plan status`, `Final`, and `Provisional` in English; do not emit
the bare status or invent a new explanation for each plan.

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

Each pair shows alternatives; emit only the applicable line.

The title is the first non-empty output. Derive it from the requested outcome; do not use a generic title such as `Plan.md` or put explanatory prose before it.
In this document, `/` separates alternative labels; in the actual plan output, emit only the variant that matches the request language.
`## Assumptions` stays `## Assumptions` for both English and Japanese requests.

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
- State what blocks a correct plan, what can proceed under an assumption, and
  what can be confirmed during implementation. Say `None.` / `なし。` when no
  blocker remains.
- For material unknowns in those existing subsections, distinguish a user
  decision from planner research or implementation-time confirmation, and state
  which part of the plan depends on it. Investigate repository-answerable facts
  rather than asking the user. Preserve the Skill's interactive question flow;
  do not leave a resolvable blocker unanswered merely to issue a provisional plan.
- Prefer conservative assumptions that follow repository conventions. Call out
  assumptions affecting architecture, compatibility, data safety, security, or
  operations.
- In `Assumptions`, explain the basis of important planner assumptions and what
  changes if they are wrong. Explicit user requirements and selected options
  are decisions, not assumptions; record their origin in the relevant requirement
  or decision note. Reference assumptions from other sections instead of repeating
  them. If none are needed, say so.
- Use `Plan status: Final` only when no blocker remains. In a non-interactive
  best-effort response, use `Provisional` and identify the unresolved decision.
- Use the fixed status-line explanation from Required Structure. For `Provisional`,
  follow it with a brief plan-specific statement identifying the remaining blocker
  and dependent scope. For `Final`, add a follow-up only if it conveys material
  plan-specific information; do not repeat the fixed definition. Report actual
  implementation or validation progress separately where relevant. The templates
  do not change status-selection rules or introduce a routine approval gate.
- Describe each affected file or module using the fixed entry format below.
  Mark a command as `[Observed]`, `[Recommended]`, or `[Unknown]` when its
  provenance matters.
- In `validation commands`, separate command discovery from execution results.
  `[Observed]` on a command means its existence or documented use was inspected,
  not that it ran successfully. If all checks are unexecuted, one shared statement
  suffices; if some ran, report their actual results and distinguish the rest.

## Milestone Rules

- In `files / modules likely affected`, use a path/module bullet followed by
  exactly two labeled child bullets, in this order:
  - English: `Why change:` then `Planned change:`.
  - Japanese: `変更が必要な理由：` then `変更内容：`.
  The reason must connect the file's responsibility and the current gap or
  consequence of leaving it unchanged to a requirement (use its ID when defined).
  The planned change states what will be modified. An action such as "align
  wording" alone is not a reason. Apply this format to small plans too; usually
  one sentence per child bullet is enough. Group paths only when both the reason
  and planned change genuinely apply to every path; otherwise use separate entries.
  For investigation-only or conditional candidates, say why investigation is
  needed, what remains unknown, and the condition for a change; explicitly state
  that modification is not yet confirmed. Do not invent a current defect or imply
  that every listed file must change merely to fill these fields.
- Describe the outcome, then the change order that connects current boundaries
  to the target behavior. Do not invent unsupported APIs, schemas, or commands.
- Each milestone's `goal` describes an observable result at its completion, not
  merely an activity. In decision notes, give the source of important choices
  (user instruction, existing specification, or planner proposal), the reason,
  and the main tradeoff where relevant. Compare alternatives only when needed
  to assess the decision; do not require a table or a label on every sentence.
- Assign stable requirement or constraint IDs such as `R1` and connect them to
  affected surfaces, acceptance criteria, and validation.
- Make acceptance criteria observable. Use existing validation commands when
  discovered; otherwise name the validation class rather than fabricating one.
- Map each criterion to a check that can actually establish it. Package checks
  do not establish semantic agreement between documents; specify a content review
  for such criteria. Do not treat a proposed check as a successful result.
- State scope exclusions, decisions that should not be reopened, risks, and
  rollback considerations in every milestone; keep a no-op field concise. Use
  the extended contract when evidence, traceability, or risk treatment needs
  detailed handling.

## Final Check

- The plan follows repository evidence and does not hide a blocker as an
  assumption.
- Affected surfaces, acceptance criteria, and validation agree with each other.
- Every milestone contains each required field and every plan contains the
  purpose-and-background section.
- The opening explains the intended change and main exclusions. Important
  decisions, assumptions, and user-owned questions are distinguishable, and
  the status explanation agrees with the evidence and unresolved blockers.
- Each affected file or module has a reason, validation follows the discovered
  repository style, and milestone ordering respects existing architecture.
  Each file entry follows the two-label format and explains why that location
  needs a change or investigation, not just what action is proposed.
- Risks have a mitigation, validation, or rollback action where relevant.
- The plan remains concise enough for the change and never begins implementation.
  Apply these rules to small plans too, using short prose or bullets within the
  existing headings. Keep shared context in one place and specialize it in
  milestones instead of duplicating it.
