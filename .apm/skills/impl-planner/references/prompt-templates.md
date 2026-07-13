# impl-planner Prompt Templates

Use these when you want reusable prompt examples without reading the full README.

## English

### Minimal Input

```text
Use `impl-planner` to create an implementation plan for this task.

- What you want to achieve
  - [what you want to achieve]
- Background
  - [why it is needed / what problem exists now]
```

### Detailed Input

```text
Use `impl-planner` to create an implementation plan.

- Repository / system
  - [software repository or configuration-management tool repository name]
- Repository understanding
  - [what this repository is meant to achieve]
  - [main implementation approach / primary processing flow]
- What you want to achieve
  - [what you want to implement]
- Background
  - [why it is needed / what problem exists now]
- Domain knowledge AI is likely to miss
  - [business rules]
  - [exception handling]
  - [background of existing specifications]
- In scope
- Out of scope
- Points that need detailed explanation or judgment from AI
- Design rules to keep
  - [architecture constraints]
  - [existing patterns]
  - [implementations to avoid]
- Impact surfaces to inspect
  - [entrypoint / routing / registration]
  - [related test / fixture / docs]
- Constraints
  - [backward compatibility]
  - [performance]
  - [security]
  - [operations]
  - [runtime / library constraints]
- Acceptance criteria
- Validation steps
  - [build / test / lint / typecheck / e2e]
  - [manual verification steps]
- Known pitfalls
- Open questions
```

## 日本語

### 最小入力

```text
impl-planner を使って、このタスクの実装 plan を作ってください。

- やりたいこと
  - [何を実現したいか]
- 背景
  - [なぜ必要か / 何が今の問題か]
```

### 詳細入力

```text
impl-planner を使って実装 plan を作ってください。

- 対象リポジトリ
  - [ソフトウェアまたは構成管理ツールのリポジトリ名]
- リポジトリ全体の理解
  - [このリポジトリが何を達成するものか]
  - [主な実現方法 / 主要な処理の流れ]
- やりたいこと
  - [何を実現したいか]
- 背景
  - [なぜ必要か / 何が今の問題か]
- AIが気づきにくいドメイン知識
  - [業務ルール]
  - [例外処理]
  - [既存仕様の背景]
- 今回やること
- 今回やらないこと
- AIに詳しく解説・判断してほしいポイント
- 守るべき設計・流儀
  - [アーキテクチャ制約]
  - [既存パターン]
  - [避けたい実装]
- 影響範囲として見てほしい箇所
  - [entrypoint / routing / registration]
  - [関連しそうな test / fixture / docs]
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
```
