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
- First line inside `## Plan.md`: `Plan status: Final | Provisional`

The title is the first non-empty output. Derive it from the requested outcome; do not use a generic title such as `Plan.md` or put explanatory prose before it.
In this document, `/` separates alternative labels; in the actual plan output, emit only the variant that matches the request language.
`## Assumptions` stays `## Assumptions` for both English and Japanese requests.

In `Purpose and Background` / `目的と背景`, state the requested outcome, why it
matters, the current problem or motivation, and known user-provided constraints.
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
has no material content. Preserve the same information and ordering for explicit
HTML output.
Do not cap milestone count for larger work. Split milestones only at an
independently verifiable outcome, dependency boundary, risk or rollback unit, or
ownership boundary; do not split merely by file list.

## Grounding and Unknowns

- Summarize the repository's purpose, relevant boundary, likely impact, and
  discovered validation style without repeating its documentation.
- State what blocks a correct plan, what can proceed under an assumption, and
  what can be confirmed during implementation. Say `None.` / `なし。` when no
  blocker remains.
- Prefer conservative assumptions that follow repository conventions. Call out
  assumptions affecting architecture, compatibility, data safety, security, or
  operations.
- Use `Plan status: Final` only when no blocker remains. In a non-interactive
  best-effort response, use `Provisional` and identify the unresolved decision.
- Give a reason for each affected file or module. Mark a command as
  `[Observed]`, `[Recommended]`, or `[Unknown]` when its provenance matters.

## Milestone Rules

- Describe the outcome, then the change order that connects current boundaries
  to the target behavior. Do not invent unsupported APIs, schemas, or commands.
- Assign stable requirement or constraint IDs such as `R1` and connect them to
  affected surfaces, acceptance criteria, and validation.
- Make acceptance criteria observable. Use existing validation commands when
  discovered; otherwise name the validation class rather than fabricating one.
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
- Each affected file or module has a reason, validation follows the discovered
  repository style, and milestone ordering respects existing architecture.
- Risks have a mitigation, validation, or rollback action where relevant.
- The plan remains concise enough for the change and never begins implementation.

## Optional Reuse Prompts

When reusable prompts would help and the user did not ask for a concise plan,
append `## Future Usage Prompts` / `## Skill 利用時のプロンプト例` after `Plan.md`.
Include both a minimal and a detailed prompt example in the request language.
Omit this section when it would add noise.
