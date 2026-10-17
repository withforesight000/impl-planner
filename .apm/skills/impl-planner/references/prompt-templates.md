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

Fill in only what you know, focusing on the goal and task-specific conditions. Omitted fields are handled using applicable instructions and repository conventions; see the detailed input guide below. You do not need to repeat “follow AGENTS.md” in each field.

```text
Use `impl-planner` to create an implementation plan.

- Repository / system
  - [repository to change and the target application, feature, or operational system]
- What you want to achieve
  - [who should be able to do what, and in which situation]
- Background
  - [what happens now, who is affected, and how it causes problems]
  - [why you want to address it now]
- Acceptance criteria
  - [the situation or action and the resulting behavior that would demonstrate completion]
  - [behavior or state to preserve during failures or exceptional cases]
- In scope
  - [work and coverage to include in this change to achieve the goal]
- Out of scope
  - [related changes to exclude or defer]
- Constraints
  - Backward compatibility
    - [operations, APIs, settings, or data formats that must keep working unchanged, and who uses them]
    - [acceptable changes and conditions requiring migration steps or advance notice]
  - Performance
    - [operations that must not slow down, expected data volumes, or concurrent usage]
    - [desired response time, throughput, or memory usage; include numbers or comparison baselines only if available]
  - Security
    - [guidelines or internal policies to follow or consult, and whether they are mandatory or advisory; you may ask AI to select suitable references]
    - [who should be able to view or modify what, and information that must not be stored, displayed, or logged]
  - Operations
    - [environments, operating procedures, periods when downtime is unacceptable, or acceptable downtime]
    - [conditions to preserve during recovery or rollback, and data that must not be lost]
  - Runtime / library constraints
    - [required or unchangeable technologies, versions, or execution environments, and why]
    - [conditions on adding or updating dependencies, licenses, or support periods]
- Domain knowledge AI is likely to miss
  - [behavior or decisions that seem reasonable in general but are wrong for this business]
  - [conditions where the usual rules do not apply and the expected behavior in those cases]
  - [business reasons behind the existing specifications]
- Known pitfalls
  - [what broke in a similar past change and under which conditions]
- Open questions
  - [unknown: facts about the current system that need investigation]
  - [undecided: choices where options exist but no direction has been selected]
- Points that need detailed explanation or judgment from AI
  - [decisions you are unsure about, options to compare, and points needing a recommendation and rationale]
- Design rules to keep
  - [layer or module responsibilities to preserve and why]
  - [existing patterns or shared functionality to follow]
  - [implementation approaches to avoid and why]
- Repository understanding
  - [whose needs the system serves and what it helps them achieve]
  - [the main flow you know: from input through processing and storage to output]
- Impact surfaces to inspect
  - [likely related screens, entrypoints, callers, or registration code; include paths only if known]
  - [likely related tests, fixtures, or documentation]
- Validation steps
  - [known build, test, lint, typecheck, or e2e commands that check the acceptance criteria]
  - [conditions to reproduce manually, actions to take, and results to inspect]
```

### Detailed input guide

**You do not need to fill in every field.** Focus on your goal, background, and task-specific conditions. You do not need to repeat instructions already documented in `AGENTS.md`, relevant skills, or other repository documentation, or write “follow AGENTS.md” in each field. Name a particular skill or reference if you want to ensure it is considered.

For omitted fields, the planner uses the following approach:

1. Follow applicable `AGENTS.md` and relevant skill instructions.
2. Where those instructions do not cover the issue, inspect existing code, tests, and documentation to identify established behavior and conventions.
3. If uncertainty remains, proceed with reasonable assumptions for low-impact matters and state those assumptions in the plan. Ask about matters that materially affect the goal, scope, compatibility, safety, or other important decisions.

An omitted field does not mean “no constraints” or “out of scope.” Do not guess file paths, commands, behavior, or business rules to fill the template. If you already know something is unclear or undecided, record it under `Open questions`.

The examples below describe one fictional task: improving recovery after an order form fails to save. Its repository name, rules, and constraints are illustrative, not requirements for your task. Keep the copyable prompt above brief and use this guide when a field is hard to fill in.

| Field | Why it helps | Questions to consider | Example entry |
| --- | --- | --- | --- |
| `Repository / system` | Identifies the target and its boundaries. | Which repository, application, or operational target should change? | The order-entry web app in the fictional `order-portal` repository. |
| `What you want to achieve` | Defines the desired outcome. | Who should be able to do what, and in which situation? | Staff can retry a failed save without re-entering the order. |
| `Background` | Explains the problem and its priority. | What happens now, and why is it a problem? | A failed save clears the form, forcing staff to enter the order again. |
| `Acceptance criteria` | Makes completion observable. | What result would demonstrate success, including failure cases? | Failed saves retain input and display an error. Retrying saves the order once, even if the first response was lost. |
| `In scope` | Identifies the work to include. | What changes must this task cover? | Preserve input after failure, show an error, and support manual retry without duplicating the same submission. |
| `Out of scope` | Prevents unwanted expansion. | What related work should wait? | Automatic retries and restoring input after the page is closed. |
| `Constraints` | Rules out unacceptable solutions. | What compatibility, performance, security, or operational limits apply? | Existing API clients must keep working. Do not persist order input in browser storage. |
| `Domain knowledge AI is likely to miss` | Captures business rules and their context. | What seemingly reasonable behavior would be wrong for this business? | Two identical orders can be intentional. Matching contents alone must not be treated as proof of a duplicate. |
| `Known pitfalls` | Highlights past failures. | What went wrong with a similar change, and under what conditions? | A previous retry fix created duplicates when the server had saved successfully but the client timed out. |
| `Open questions` | Keeps uncertainty separate from decisions. | What is unknown, and what has not been decided? | Unknown: whether the API already recognizes repeated submissions. Undecided: whether the UI should offer canceling a pending retry. |
| `Points that need detailed explanation or judgment from AI` | Focuses comparison and explanation. | Which decision needs options and a recommendation? | Compare ways to prevent duplicates when the server saves an order but its response never arrives. |
| `Design rules to keep` | Preserves established implementation conventions. | Which existing patterns must remain, and why? | Keep API calls in the existing shared client so authentication and error handling stay consistent. |
| `Repository understanding` | Connects the change to the system's purpose and flow. | What does the system do? What processing flow do you already know? | Staff enter orders in a form; the web app sends them to an API for storage. |
| `Impact surfaces to inspect` | Provides leads for repository investigation. | Which screens, callers, tests, or docs might be affected? | Inspect the order form, shared API client, order-creation API, and save-related tests; exact paths are unknown. |
| `Validation steps` | Explains how to check the expected results. | Which known checks or manual steps can demonstrate those results? | Disconnect before saving and check retained input and the error. Also simulate a lost response after a successful save, retry, and verify one stored order. Test commands are unknown. |

`What you want to achieve` describes the outcome; `In scope` describes the work included. `Acceptance criteria` describes success; `Validation steps` describes how to check it. Business rules belong under domain knowledge, implementation conventions under design rules, and limits on acceptable solutions under constraints.

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

今回の目的や固有の条件を中心に、分かる範囲で記入してください。未記入の項目は適用される指示やリポジトリの慣例で補います。詳しくは下の記入ガイドを参照してください。各項目に「AGENTS.md に従う」と繰り返す必要はありません。

```text
impl-planner を使って実装 plan を作ってください。

- 対象リポジトリ
  - [変更するリポジトリ名と、対象のアプリ・機能・運用対象]
- やりたいこと
  - [誰が、どの状況で、何をできるようにしたいか]
- 背景
  - [現在何が起きていて、誰がどのように困っているか]
  - [なぜ今回対応したいか]
- 受け入れ条件
  - [どの状況・操作で、どんな結果になれば完了と判断できるか]
  - [失敗時や例外時にも守るべき動作・状態]
- 今回やること
  - [目的を達成するために、今回の変更に含める作業や対応範囲]
- 今回やらないこと
  - [関連していても、今回は含めない変更や後回しにする作業]
- 制約
  - 後方互換性
    - [変更後もそのまま使える必要がある操作・API・設定・データ形式と、その利用者]
    - [変更を許容できる範囲や、移行手順・事前告知が必要になる条件]
  - 性能
    - [遅くなると困る操作や、想定するデータ量・同時利用数]
    - [満たしたい応答時間・処理量・メモリ使用量など。数値や比較対象がある場合だけ]
  - セキュリティ
    - [準拠・参照したいガイドラインや社内規程と、必須要件か参考か。選定をAIに任せてもよい]
    - [誰が何を閲覧・操作できるべきか、保存・表示・ログ出力してはいけない情報など]
  - 運用
    - [利用する環境・運用手順や、停止できない時間帯・許容できる停止時間]
    - [障害時の復旧・切り戻しで守りたい条件や、失ってはいけないデータ]
  - ランタイム / ライブラリ制約
    - [利用必須または変更できない技術・バージョン・実行環境と、その理由]
    - [依存関係の追加・更新や、ライセンス・サポート期間についての条件]
- AIが気づきにくいドメイン知識
  - [一般的には妥当に見えても、この業務では困る動作や判断]
  - [通常のルールが当てはまらない条件と、その場合に期待する動作]
  - [既存の仕様が今の形になった業務上の理由]
- 既知の地雷
  - [過去の似た変更で、どんな条件のときに何が壊れたか]
- 未確定事項
  - [不明：現状が分からず、調査してほしいこと]
  - [未決定：選択肢はあるが、まだ方針を決めていないこと]
- AIに詳しく解説・判断してほしいポイント
  - [迷っている判断、比較してほしい選択肢、推奨案と理由を知りたい点]
- 守るべき設計・流儀
  - [維持すべきレイヤーやモジュールの役割分担と、その理由]
  - [合わせるべき既存パターンや共通処理]
  - [避けたい実装方法と、それを避ける理由]
- リポジトリ全体の理解
  - [誰のどんな目的を達成するシステムか]
  - [分かっている主な処理の流れ：入力から処理・保存・出力まで]
- 影響範囲として見てほしい箇所
  - [関連しそうな画面・処理の入口・呼び出し元・登録処理。パスは分かる範囲で]
  - [関連しそうなテスト・テストデータ・ドキュメント]
- 検証方法
  - [受け入れ条件を確認できる既知の build・test・lint・typecheck・e2e コマンド]
  - [手動で再現する状況、操作手順、確認する結果]
```

### 詳細入力の記入ガイド

**すべての項目を埋める必要はありません。** 今回の目的・背景・固有の条件を中心に記入してください。`AGENTS.md`・関連スキル・リポジトリのドキュメントに記載済みの指示を転記したり、各項目に「AGENTS.md に従ってください」と繰り返したりする必要はありません。特に参照してほしいスキルや資料がある場合は、その名前や参照先を明示してください。

未記入の項目は、次の方針で補います。

1. 適用される `AGENTS.md` と関連スキルの指示に従います。
2. 指示で扱われていない事項は、既存コード・テスト・ドキュメントを調査し、既存の動作や慣例に基づいて判断します。
3. それでも不明な場合、影響が小さい事項は妥当な仮定を置いて進め、計画に明記します。目的・範囲・互換性・安全性などの重要な判断を左右する事項は確認します。

未記入は「制約なし」「対象外」を意味しません。入力のためにファイルパス・コマンド・動作・業務ルールを推測で埋める必要はありません。分からないことや未決定のことを既に把握している場合は、`未確定事項` に記入してください。

以下は「注文フォームの保存失敗後の復帰を改善する」という架空のタスクの記入例です。リポジトリ名・業務ルール・制約は説明用であり、実際のタスクの必須要件ではありません。上のコピー用テンプレートは簡潔に保ち、書きにくい項目があるときにこのガイドを参照してください。

| 項目 | 入力すると何がよくなるか | 考えるための問い | 記入例 |
| --- | --- | --- | --- |
| `対象リポジトリ` | 対象とその境界を特定できます。 | どのリポジトリ・アプリ・運用対象を変更しますか？ | 架空の `order-portal` リポジトリにある注文入力用の Web アプリ。 |
| `やりたいこと` | 達成したい結果が明確になります。 | 誰が、どの状況で、何をできるようにしたいですか？ | 担当者が、保存に失敗しても注文を入力し直さずに再試行できるようにしたい。 |
| `背景` | 問題と対応の優先度を伝えられます。 | 現在何が起きていて、なぜ困っていますか？ | 保存に失敗するとフォームが消去され、担当者が注文を再入力している。 |
| `受け入れ条件` | 完了を観測可能にできます。 | 失敗時も含め、どんな結果を確認できれば成功ですか？ | 保存失敗時に入力が残り、エラーが表示される。初回の応答が失われても、再試行による保存は1件だけになる。 |
| `今回やること` | 含める作業を明確にできます。 | 今回、どの変更まで含める必要がありますか？ | 失敗時の入力保持、エラー表示、同じ送信を重複登録しない手動再試行。 |
| `今回やらないこと` | 意図しない範囲拡大を防げます。 | 関連していても、今回は後回しにすることは何ですか？ | 自動再試行と、画面を閉じた後の入力復元。 |
| `制約` | 採用できない解決策を除外できます。 | 互換性・性能・セキュリティ・運用上、守るべき限界は何ですか？ | 既存の API 利用クライアントを壊さない。注文の入力内容をブラウザーのストレージに永続化しない。 |
| `AIが気づきにくいドメイン知識` | 業務ルールとその背景を補えます。 | 一般的には妥当に見えても、この業務では困る動作はありますか？ | 同じ内容の注文を意図的に2件作ることがある。内容の一致だけで重複と判断してはいけない。 |
| `既知の地雷` | 過去の失敗を重点的に確認できます。 | 似た変更で、どんな条件のときに何が壊れましたか？ | 過去の再試行対応では、サーバーの保存成功後にクライアントがタイムアウトすると二重登録になった。 |
| `未確定事項` | 不確実なことを決定事項と区別できます。 | 分かっていないことと、まだ決めていないことは何ですか？ | 不明：API が同じ送信の再試行を識別できるか。未決定：再試行待ちを取り消す操作を画面に設けるか。 |
| `AIに詳しく解説・判断してほしいポイント` | 比較や説明が必要な判断に集中できます。 | どの判断について、選択肢と推奨案が欲しいですか？ | サーバーでは保存できたが応答が届かなかった場合に、二重登録を防ぐ方法を比較してほしい。 |
| `守るべき設計・流儀` | 既存の実装規約を維持しやすくなります。 | 維持すべき既存パターンと、その理由は何ですか？ | 認証とエラー処理を統一するため、API 呼び出しは既存の共通クライアントに集約する。 |
| `リポジトリ全体の理解` | システムの目的や処理の流れと変更を結び付けられます。 | 何をするシステムですか？ 分かっている処理の流れは何ですか？ | 担当者がフォームに注文を入力し、Web アプリが API に送って保存する。 |
| `影響範囲として見てほしい箇所` | リポジトリ調査の手掛かりになります。 | 関連しそうな画面・呼び出し元・テスト・ドキュメントはありますか？ | 注文フォーム、共通 API クライアント、注文作成 API、保存関連のテスト。正確なパスは不明。 |
| `検証方法` | 期待する結果の確かめ方を伝えられます。 | 既知のチェックや手動操作で、どう結果を確認できますか？ | 通信を切って保存し、入力保持とエラーを確認する。保存成功後の応答喪失も再現し、再試行後の登録が1件であることを確認する。テストコマンドは不明。 |

`やりたいこと` は達成したい結果、`今回やること` は含める作業です。`受け入れ条件` は成功した状態、`検証方法` はその確かめ方です。業務ルールはドメイン知識、実装規約は設計・流儀、採用できる解決策の限界は制約に記入します。
