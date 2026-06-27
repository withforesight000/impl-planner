# impl-planner APM package

`impl-planner` は、ソフトウェアまたは構成管理ツールのリポジトリ向けの「計画専用」Skill です。
Codex、Claude Code、GitHub Copilot に実装 plan を作らせたいときに使います。実装そのものは行いません。

English: [README.md](README.md)

## この package でできること

- Plan.md 形式の実装 plan を作る
- 明示的に求められた場合は、自己完結した HTML レポートも出力できる
- plan の前にリポジトリ理解を要約する
- 先に前提不足や曖昧点を列挙する
- Assumptions を明示する
- タスク規模に応じて plan の構造を調整する
- milestone ごとに次を整理する
  - goal
  - files / modules likely affected
  - acceptance criteria
  - validation commands
  - decision notes to avoid oscillation
  - main risks
  - rollback considerations
- 影響を受けそうなファイルや module には理由も付ける
- エントリポイント、呼び出し元、設定、テスト、隣接するドキュメントまで含めて、影響範囲を広めにたどる
- validation command はリポジトリ既存の検証スタイルに合わせる
- Clean Architecture, MVC, Hexagonal Architecture, DDD, feature-based structure などの既存アーキテクチャやレイヤリング規約がある場合は、それを確認して尊重する
- milestone 間に依存関係がある場合は順序の理由を明示する
- 判断が難しいときは、推奨案、却下した代替案、その理由を出す
- acceptance criteria、validation、risk、mitigation、rollback が実行可能か自己点検する
- 必要に応じて、次回そのまま使える短いプロンプト例を出す

## リポジトリ構成

- `apm.yml`: APM package manifest
- `.apm/skills/impl-planner/SKILL.md`: Skill 本体
- `.apm/skills/impl-planner/references/plan-contract.md`: 中核の出力契約
- `.apm/skills/impl-planner/references/examples.md`: 必要時に読む例と再利用用プロンプトテンプレート
- `.apm/skills/impl-planner/references/detail-request.md`: 必要時に読む判断材料提示の構造
- `.apm/skills/impl-planner/references/html-output.md`: 必要時に読む HTML レポート制約
- `.apm/skills/impl-planner/references/formatting.md`: 必要時に読む formatting 制約

## 使い方

新機能、リファクタ、構成管理ツールの変更、設計判断などで「まず plan が欲しい」ときにこの Skill を使います。
ブラウザで見やすいレビュー用の成果物が欲しい場合だけ、HTML 出力を明示してください。

最小入力の例:

```text
impl-planner を使って、このタスクの実装 plan を作ってください。

- 目的
  - [何を実現したいか]
- 背景
  - [なぜ必要か / 何が今の問題か]
```

詳細入力の例:

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

各項目を入力すると何がよくなるか:

- 対象リポジトリ: 対象のコードベース、実行環境、リポジトリ種別を plan の前提にできます。workspace 内に複数 package、service、role、構成管理対象がある場合に特に効きます。
- リポジトリ全体の理解: 個別ファイルを見る前に、全体の目的と主要な処理の流れから考えられます。局所的には正しそうでも、リポジトリ全体の価値提供とずれた plan になるのを防ぎやすくなります。
- やりたいこと: milestone が作業内容ではなく、達成したい結果に寄りやすくなります。ここが曖昧だと、plan が変更作業の列挙に寄ってしまい、実装後にどうなっているべきかが弱くなります。
- 背景: なぜ必要か、今どの問題を解くべきかが plan に反映されます。背景があると、AI が別の意図で最適化してしまうのを避け、判断の優先順位を合わせやすくなります。
- AIが気づきにくいドメイン知識: コードから推測しにくい業務ルール、例外、仕様の背景を補えます。先に渡しておくと、重要な edge case を一般的な実装手順として薄めてしまうリスクが下がります。
- 今回やること: plan が狭くなりすぎたり、意図した作業が暗黙になったりするのを防げます。今回の変更に含めるべき作業を、AI が遠慮して落とす可能性も減らせます。
- 今回やらないこと: 実装範囲のブレや、今回やるべきでない作業の混入を防げます。隣接するリファクタ、migration、cleanup が魅力的でも、今回の plan を広げすぎないために有効です。
- AIに詳しく解説・判断してほしいポイント: AI の推論を厚く使いたい判断箇所に集中できます。単なる milestone の列挙ではなく、tradeoff、代替案、理由づけがほしい部分を明示できます。
- 守るべき設計・流儀: アーキテクチャ、既存パターン、避けたい実装を崩しにくくなります。layer 境界、module ownership、命名規則、既存 helper の使い方を尊重した plan になりやすくなります。
- 影響範囲として見てほしい箇所: entrypoint、登録処理、テスト、fixture、docs などの変更漏れを減らせます。`files / modules likely affected` の精度を上げるうえで、特に効果が大きい項目です。
- 制約: 後方互換性、性能、セキュリティ、運用、ランタイム制約を plan に織り込めます。技術的には可能でも、このリポジトリでは採れない案を早めに除外しやすくなります。
- 受け入れ条件: 完了判定が観測可能になり、レビューしやすくなります。実装者と reviewer が、何をもって完了とするかを揃えやすくなります。
- 検証方法: 実装者が実行すべき確認を、リポジトリの検証スタイルに寄せやすくなります。既知の command や手動確認を渡すと、AI が雑に一般的な test だけを提案する可能性が下がります。
- 既知の地雷: 通常のコード探索だけでは見えにくい失敗パターンを先に避けられます。過去に問題になった箇所を渡すことで、mitigation、rollback、重点的な検証を plan に入れやすくなります。
- 未確定事項: blocking、assumptions、実装中に確認するものを分けやすくなります。不確実なことを、決定済みの前提のように plan に混ぜ込むリスクを下げられます。

より詳しく渡す場合は、スコープ、制約、受け入れ条件、検証方法、既知の地雷、未確定事項、AIが気づきにくいドメイン知識、リポジトリ全体の理解、影響範囲として見てほしい箇所、AIに詳しく解説・判断してほしいポイントまで書くと plan の精度が上がります。
影響範囲を広めに見てほしい場合は、エントリポイント、ルーティング、登録処理、設定、テスト、fixture、ドキュメントも明示すると plan が漏れにくくなります。
リポジトリに既存のアーキテクチャやレイヤリングの規約があるなら、それを明示すると境界を崩さない plan になりやすくなります。

## 検証方法

リポジトリルートで次を実行します。

```bash
apm audit --file .apm/skills/impl-planner/SKILL.md
apm pack --dry-run
apm pack --archive --dry-run -v
```

これで Skill のメタデータが正しく、パッケージ内容が想定どおりか確認できます。

## 配布方法

- `apm pack` で配布用 bundle を作る
- 生成された artifact を downstream のインストールやリリース自動化に使う
- `apm.yml` と `.apm/skills/impl-planner/` を source of truth として保つ

## `apm` でインストールする方法

この repository を clone しなくても、PC に Skill をインストールできます。
リポジトリ参照を直接指定して install します。

```bash
apm install withforesight000/impl-planner --global --target codex
```

事前に内容を確認したい場合は、`--dry-run` を付けます。

```bash
apm install withforesight000/impl-planner --dry-run --global --target codex
```

他の対応先にも同じ package を入れられます。

```bash
apm install withforesight000/impl-planner --global --target claude,copilot
```

working copy を持っている場合は、`apm pack --archive` で bundle を作ってから同じ手順で install できます。

## 補足

- この Skill は計画専用です。
- ファイル編集、破壊的コマンド、実装開始を促してはいけません。
- 詳細説明を求められたら、複数案、推奨案、メリット・デメリット・トレードオフを返します。
