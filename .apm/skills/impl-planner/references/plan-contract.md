# impl-planner Core Output Contract

Use this compact contract for every implementation plan. Write prose in the
user's language. Use the extended contract only when its trigger applies.

## Required Structure

Start in this order:

- `## Repository Understanding` / `## リポジトリ理解`
- `## Missing Context and Ambiguities` / `## 前提不足・曖昧点`
- `## Assumptions`
- `## Plan.md`
- `Plan status: Final | Provisional`

Within `Missing Context and Ambiguities` / `前提不足・曖昧点`, use:

- `### Blocking now` / `### 今答えないと plan が破綻するもの`
- `### Can proceed with assumptions` / `### 仮定を置けば進められるもの`
- `### Can confirm during implementation` / `### 実装中に確認すればよいもの`

Use `### Milestone N: <short title>` and `####` milestone fields. Every
milestone includes the following labels in the request language:

- `goal` / `目的`
- `implementation approach` / `実装方針`
- `files / modules likely affected` / `影響がありそうなファイル / モジュール`
- `acceptance criteria` / `受け入れ条件`
- `validation commands` / `検証コマンド`

For a small, low-risk change, use one concise milestone and omit empty optional
fields. Preserve the same information and ordering for explicit HTML output.

## Grounding and Unknowns

- Summarize the repository's purpose, relevant boundary, likely impact, and
  discovered validation style without repeating its documentation.
- State what blocks a correct plan, what can proceed under an assumption, and
  what can be confirmed during implementation. Say `None.` / `なし。` when no
  blocker remains.
- Use `Plan status: Final` only when no blocker remains. In a non-interactive
  best-effort response, use `Provisional` and identify the unresolved decision.
- Give a reason for each affected file or module. Mark a command as
  `[Observed]`, `[Recommended]`, or `[Unknown]` when its provenance matters.

## Milestone Rules

- Describe the outcome, then the change order that connects current boundaries
  to the target behavior. Do not invent unsupported APIs, schemas, or commands.
- Make acceptance criteria observable. Use existing validation commands when
  discovered; otherwise name the validation class rather than fabricating one.
- State notable scope exclusions, risks, decision notes, and rollback only when
  they prevent likely implementation drift. Use the extended contract when any
  of these need detailed treatment.

## Final Check

- The plan follows repository evidence and does not hide a blocker as an
  assumption.
- Affected surfaces, acceptance criteria, and validation agree with each other.
- Risks have a mitigation, validation, or rollback action where relevant.
- The plan remains concise enough for the change and never begins implementation.
