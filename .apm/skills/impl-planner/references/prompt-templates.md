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
  - [repository to change and the target application, feature, or operational system]
- Repository understanding
  - [whose needs the system serves and what it helps them achieve]
  - [the main flow you know: from input through processing and storage to output]
- What you want to achieve
  - [who should be able to do what, and in which situation]
- Background
  - [what happens now, who is affected, and how it causes problems]
  - [why you want to address it now]
- Domain knowledge AI is likely to miss
  - [behavior or decisions that seem reasonable in general but are wrong for this business]
  - [conditions where the usual rules do not apply and the expected behavior in those cases]
  - [business reasons behind the existing specifications]
- In scope
  - [work and coverage to include in this change to achieve the goal]
- Out of scope
  - [related changes to exclude or defer]
- Points that need detailed explanation or judgment from AI
  - [decisions you are unsure about, options to compare, and points needing a recommendation and rationale]
- Design rules to keep
  - [layer or module responsibilities to preserve and why]
  - [existing patterns or shared functionality to follow]
  - [implementation approaches to avoid and why]
- Impact surfaces to inspect
  - [likely related screens, entrypoints, callers, or registration code; include paths only if known]
  - [likely related tests, fixtures, or documentation]
- Constraints
  - [existing usage, APIs, or data formats that must remain compatible]
  - [acceptable processing time or load; include numbers only when justified]
  - [information that must not be stored or displayed and permission boundaries to preserve]
  - [operational conditions such as acceptable downtime, execution environments, or recovery requirements]
  - [required runtimes or libraries, or ones that cannot change, and why]
- Acceptance criteria
  - [the situation or action and the resulting behavior that would demonstrate completion]
  - [behavior or state to preserve during failures or exceptional cases]
- Validation steps
  - [known build, test, lint, typecheck, or e2e commands that check the acceptance criteria]
  - [conditions to reproduce manually, actions to take, and results to inspect]
- Known pitfalls
  - [what broke in a similar past change and under which conditions]
- Open questions
  - [unknown: facts about the current system that need investigation]
  - [undecided: choices where options exist but no direction has been selected]
```

### Detailed input guide

Fill in what you know; you do not need to answer every field. Leave unknowns or undecided points under `Open questions` instead of guessing file paths, commands, or behavior. An empty field does not mean there are no constraints.

The examples below describe one fictional task: improving recovery after an order form fails to save. Its repository name, rules, and constraints are illustrative, not requirements for your task. Keep the copyable prompt above brief and use this guide when a field is hard to fill in.

| Field | Why it helps | Questions to consider | Example entry |
| --- | --- | --- | --- |
| `Repository / system` | Identifies the target and its boundaries. | Which repository, application, or operational target should change? | The order-entry web app in the fictional `order-portal` repository. |
| `Repository understanding` | Connects the change to the system's purpose and flow. | What does the system do? What processing flow do you already know? | Staff enter orders in a form; the web app sends them to an API for storage. |
| `What you want to achieve` | Defines the desired outcome. | Who should be able to do what, and in which situation? | Staff can retry a failed save without re-entering the order. |
| `Background` | Explains the problem and its priority. | What happens now, and why is it a problem? | A failed save clears the form, forcing staff to enter the order again. |
| `Domain knowledge AI is likely to miss` | Captures business rules and their context. | What seemingly reasonable behavior would be wrong for this business? | Two identical orders can be intentional. Matching contents alone must not be treated as proof of a duplicate. |
| `In scope` | Identifies the work to include. | What changes must this task cover? | Preserve input after failure, show an error, and support manual retry without duplicating the same submission. |
| `Out of scope` | Prevents unwanted expansion. | What related work should wait? | Automatic retries and restoring input after the page is closed. |
| `Points that need detailed explanation or judgment from AI` | Focuses comparison and explanation. | Which decision needs options and a recommendation? | Compare ways to prevent duplicates when the server saves an order but its response never arrives. |
| `Design rules to keep` | Preserves established implementation conventions. | Which existing patterns must remain, and why? | Keep API calls in the existing shared client so authentication and error handling stay consistent. |
| `Impact surfaces to inspect` | Provides leads for repository investigation. | Which screens, callers, tests, or docs might be affected? | Inspect the order form, shared API client, order-creation API, and save-related tests; exact paths are unknown. |
| `Constraints` | Rules out unacceptable solutions. | What compatibility, performance, security, or operational limits apply? | Existing API clients must keep working. Do not persist order input in browser storage. |
| `Acceptance criteria` | Makes completion observable. | What result would demonstrate success, including failure cases? | Failed saves retain input and display an error. Retrying saves the order once, even if the first response was lost. |
| `Validation steps` | Explains how to check the expected results. | Which known checks or manual steps can demonstrate those results? | Disconnect before saving and check retained input and the error. Also simulate a lost response after a successful save, retry, and verify one stored order. Test commands are unknown. |
| `Known pitfalls` | Highlights past failures. | What went wrong with a similar change, and under what conditions? | A previous retry fix created duplicates when the server had saved successfully but the client timed out. |
| `Open questions` | Keeps uncertainty separate from decisions. | What is unknown, and what has not been decided? | Unknown: whether the API already recognizes repeated submissions. Undecided: whether the UI should offer canceling a pending retry. |

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

```text
impl-planner を使って実装 plan を作ってください。

- 対象リポジトリ
  - [変更するリポジトリ名と、対象のアプリ・機能・運用対象]
- リポジトリ全体の理解
  - [誰のどんな目的を達成するシステムか]
  - [分かっている主な処理の流れ：入力から処理・保存・出力まで]
- やりたいこと
  - [誰が、どの状況で、何をできるようにしたいか]
- 背景
  - [現在何が起きていて、誰がどのように困っているか]
  - [なぜ今回対応したいか]
- AIが気づきにくいドメイン知識
  - [一般的には妥当に見えても、この業務では困る動作や判断]
  - [通常のルールが当てはまらない条件と、その場合に期待する動作]
  - [既存の仕様が今の形になった業務上の理由]
- 今回やること
  - [目的を達成するために、今回の変更に含める作業や対応範囲]
- 今回やらないこと
  - [関連していても、今回は含めない変更や後回しにする作業]
- AIに詳しく解説・判断してほしいポイント
  - [迷っている判断、比較してほしい選択肢、推奨案と理由を知りたい点]
- 守るべき設計・流儀
  - [維持すべきレイヤーやモジュールの役割分担と、その理由]
  - [合わせるべき既存パターンや共通処理]
  - [避けたい実装方法と、それを避ける理由]
- 影響範囲として見てほしい箇所
  - [関連しそうな画面・処理の入口・呼び出し元・登録処理。パスは分かる範囲で]
  - [関連しそうなテスト・テストデータ・ドキュメント]
- 制約
  - [維持すべき既存の使い方・API・データ形式などの互換性]
  - [許容できる処理時間や負荷。数値は根拠がある場合だけ]
  - [保存・表示してはいけない情報や、守るべき権限の境界]
  - [許容できる停止時間、実行環境、復旧などの運用上の条件]
  - [利用必須または変更できないランタイム・ライブラリと、その理由]
- 受け入れ条件
  - [どの状況・操作で、どんな結果になれば完了と判断できるか]
  - [失敗時や例外時にも守るべき動作・状態]
- 検証方法
  - [受け入れ条件を確認できる既知の build・test・lint・typecheck・e2e コマンド]
  - [手動で再現する状況、操作手順、確認する結果]
- 既知の地雷
  - [過去の似た変更で、どんな条件のときに何が壊れたか]
- 未確定事項
  - [不明：現状が分からず、調査してほしいこと]
  - [未決定：選択肢はあるが、まだ方針を決めていないこと]
```

### 詳細入力の記入ガイド

分かる範囲で記入し、すべての項目に回答する必要はありません。不明なことや未決定のことは、ファイルパス・コマンド・動作を推測で埋めず、`未確定事項` に残してください。空欄は「制約なし」を意味しません。

以下は「注文フォームの保存失敗後の復帰を改善する」という架空のタスクの記入例です。リポジトリ名・業務ルール・制約は説明用であり、実際のタスクの必須要件ではありません。上のコピー用テンプレートは簡潔に保ち、書きにくい項目があるときにこのガイドを参照してください。

| 項目 | 入力すると何がよくなるか | 考えるための問い | 記入例 |
| --- | --- | --- | --- |
| `対象リポジトリ` | 対象とその境界を特定できます。 | どのリポジトリ・アプリ・運用対象を変更しますか？ | 架空の `order-portal` リポジトリにある注文入力用の Web アプリ。 |
| `リポジトリ全体の理解` | システムの目的や処理の流れと変更を結び付けられます。 | 何をするシステムですか？ 分かっている処理の流れは何ですか？ | 担当者がフォームに注文を入力し、Web アプリが API に送って保存する。 |
| `やりたいこと` | 達成したい結果が明確になります。 | 誰が、どの状況で、何をできるようにしたいですか？ | 担当者が、保存に失敗しても注文を入力し直さずに再試行できるようにしたい。 |
| `背景` | 問題と対応の優先度を伝えられます。 | 現在何が起きていて、なぜ困っていますか？ | 保存に失敗するとフォームが消去され、担当者が注文を再入力している。 |
| `AIが気づきにくいドメイン知識` | 業務ルールとその背景を補えます。 | 一般的には妥当に見えても、この業務では困る動作はありますか？ | 同じ内容の注文を意図的に2件作ることがある。内容の一致だけで重複と判断してはいけない。 |
| `今回やること` | 含める作業を明確にできます。 | 今回、どの変更まで含める必要がありますか？ | 失敗時の入力保持、エラー表示、同じ送信を重複登録しない手動再試行。 |
| `今回やらないこと` | 意図しない範囲拡大を防げます。 | 関連していても、今回は後回しにすることは何ですか？ | 自動再試行と、画面を閉じた後の入力復元。 |
| `AIに詳しく解説・判断してほしいポイント` | 比較や説明が必要な判断に集中できます。 | どの判断について、選択肢と推奨案が欲しいですか？ | サーバーでは保存できたが応答が届かなかった場合に、二重登録を防ぐ方法を比較してほしい。 |
| `守るべき設計・流儀` | 既存の実装規約を維持しやすくなります。 | 維持すべき既存パターンと、その理由は何ですか？ | 認証とエラー処理を統一するため、API 呼び出しは既存の共通クライアントに集約する。 |
| `影響範囲として見てほしい箇所` | リポジトリ調査の手掛かりになります。 | 関連しそうな画面・呼び出し元・テスト・ドキュメントはありますか？ | 注文フォーム、共通 API クライアント、注文作成 API、保存関連のテスト。正確なパスは不明。 |
| `制約` | 採用できない解決策を除外できます。 | 互換性・性能・セキュリティ・運用上、守るべき限界は何ですか？ | 既存の API 利用クライアントを壊さない。注文の入力内容をブラウザーのストレージに永続化しない。 |
| `受け入れ条件` | 完了を観測可能にできます。 | 失敗時も含め、どんな結果を確認できれば成功ですか？ | 保存失敗時に入力が残り、エラーが表示される。初回の応答が失われても、再試行による保存は1件だけになる。 |
| `検証方法` | 期待する結果の確かめ方を伝えられます。 | 既知のチェックや手動操作で、どう結果を確認できますか？ | 通信を切って保存し、入力保持とエラーを確認する。保存成功後の応答喪失も再現し、再試行後の登録が1件であることを確認する。テストコマンドは不明。 |
| `既知の地雷` | 過去の失敗を重点的に確認できます。 | 似た変更で、どんな条件のときに何が壊れましたか？ | 過去の再試行対応では、サーバーの保存成功後にクライアントがタイムアウトすると二重登録になった。 |
| `未確定事項` | 不確実なことを決定事項と区別できます。 | 分かっていないことと、まだ決めていないことは何ですか？ | 不明：API が同じ送信の再試行を識別できるか。未決定：再試行待ちを取り消す操作を画面に設けるか。 |

`やりたいこと` は達成したい結果、`今回やること` は含める作業です。`受け入れ条件` は成功した状態、`検証方法` はその確かめ方です。業務ルールはドメイン知識、実装規約は設計・流儀、採用できる解決策の限界は制約に記入します。
