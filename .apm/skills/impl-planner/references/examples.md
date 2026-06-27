# impl-planner Examples

Read this reference only when examples would help the user reuse the skill or when a compact example is needed to calibrate plan density.

## Mini-Example

This example shows the expected density for a small English request. Adapt language and labels to the user's request.

```md
## Repository Understanding

- This package defines a planning-only APM skill and keeps the skill contract, examples, and README usage guidance aligned.
- The implementation is documentation-driven: `SKILL.md` is the entrypoint, `plan-contract.md` defines the output shape, and README files explain user-facing usage.
- Validation is handled through APM audit and dry-run packaging commands.

## Missing Context and Ambiguities

### Blocking now

- None.

### Can proceed with assumptions

- Assume the existing documentation structure should stay intact and only wording or template examples change.

### Can confirm during implementation

- Confirm the updated prompt examples still map cleanly to the skill contract before finalizing docs.

## Assumptions

- The package remains planning-only.
- The plan should prefer explicit context capture over free-form narrative when the user asks for a detailed prompt.

## Plan.md

## Milestone 1: Update prompt examples

### goal

- Document a compact prompt shape for small requests and a template-heavy prompt shape for detailed requests.

### files / modules likely affected

- `README.md`
- `README.ja.md`
- `SKILL.md` and `plan-contract.md` if the prompt contract itself changes

### acceptance criteria

- English and Japanese READMEs both show the list-based minimal prompt and detailed prompt.
- The detailed prompt includes fields for domain knowledge that AI is likely to miss.
- The detailed prompt includes a field for points that need detailed explanation or judgment from AI.
- The detailed prompt asks for broad impact surfaces when that matters, including entrypoints, routing, registration, tests, fixtures, and docs.
- The wording stays planning-only and does not imply implementation work.

### validation commands

- `apm audit --file .apm/skills/impl-planner/SKILL.md`
- `apm pack --dry-run`

### decision notes to avoid oscillation

- Prefer list-based prompt templates over prose-heavy examples for the detailed input section.
- When improving prompt templates, bias toward prompting for likely impact surfaces instead of only the obvious edit target.
```

## Future Usage Prompts

If useful, include a final section named `## Skill Usage Prompt Examples / Skill 利用時のプロンプト例`.

Use this section when it helps the user reuse the skill without repeating the full contract. Omit it when the user asked for a concise plan or when the prompts would add noise.

Include both examples when you include the section:

### 最小入力

```text
impl-planner を使って、このタスクの実装 plan を作ってください。

- 目的
  - [何を実現したいか]
- 背景
  - [なぜ必要か / 何が今の問題か]
```

### 詳細入力

```text
impl-planner を使って実装 plan を作ってください。

- 対象リポジトリ
  - [ソフトウェアまたは構成管理ツールのリポジトリ名]
- やりたいこと
  - [何を実現したいか]
- 今回やること
- 今回やらないこと
- 守るべき設計・流儀
  - [アーキテクチャ制約]
  - [既存パターン]
  - [避けたい実装]
- AIが気づきにくいドメイン知識
  - [業務ルール]
  - [例外処理]
  - [既存仕様の背景]
- 制約
  - [後方互換性]
  - [性能]
  - [セキュリティ]
  - [運用]
  - [ランタイム / ライブラリ制約]
- 受け入れ条件
- 検証方法
  - [build / test / lint / typecheck / e2e]
  - [手動確認手順]
- 既知の地雷
- 未確定事項
- AIに詳しく解説・判断してほしいポイント
```

最小入力は、目的と背景を短く書けば十分です。
詳細入力は、ドメイン知識、制約、検証、判断ポイントまで埋めると plan の精度が上がります。
