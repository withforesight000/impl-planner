# impl-planner Output Contract

This reference defines the required output shape for implementation planning. Use it for software repository changes or configuration-management tool repository changes.

## Required Top-Level Output

Start with these sections in this order:

- Write explanatory prose and bullet contents in the same language the user used for the request.
- Keep the structural section labels defined below unless the user explicitly asks for a localized variant.

## 前提不足・曖昧点

### 今答えないと plan が破綻するもの

- List ambiguities that materially prevent a correct plan.
- If none, say `なし。`

### 仮定を置けば進められるもの

- List uncertainties that can proceed under explicit assumptions.
- Keep assumptions concrete and implementation-relevant.

### 実装中に確認すればよいもの

- List items that can be verified while implementing without changing the overall plan.

## Assumptions

- State all assumptions used by the plan.
- Include assumptions about scope, compatibility, migration, test strategy, deployment, runtime, data safety, and operational constraints when relevant.
- If the user asked for detail and an option was selected or recommended, record that decision here or in milestone decision notes.

## Plan.md

Use `## Milestone N: <short title>` for each milestone. Every milestone must use the same heading structure below.

### goal

- Describe the milestone outcome, not just an activity.

### files / modules likely affected

- List likely files, modules, roles, playbooks, services, APIs, schemas, or docs.
- Use paths when they are known from exploration.
- If exact paths are unknown, name the module or subsystem and explain what will be discovered.

### acceptance criteria

- Define observable completion criteria.
- Include behavior, compatibility, error handling, and non-regression criteria where relevant.

### validation commands

- List concrete commands when known.
- If commands are unknown, list the expected class of validation, such as typecheck, unit test, integration test, configuration-management syntax-check, configuration-management check mode, or targeted smoke test.
- Do not include commands that mutate source as a validation step unless the user explicitly wants implementation execution.

### decision notes to avoid oscillation

- Record decisions that should not be reopened during implementation unless new facts invalidate them.
- Include recommended defaults and rejected alternatives when they are likely to cause rework.

### main risks

- List the highest-risk technical or operational failure modes.
- Include data safety, compatibility, rollout, security, idempotence, and dependency risks where relevant.

### rollback considerations

- Explain how to revert or disable the change.
- For configuration-management tool repositories, include configuration rollback, inventory rollback, role/play rollback, and service state concerns when applicable.

## Future Usage Prompts

If useful, include a final section named `## Skill 利用時のプロンプト例`.

Use this section when it helps the user reuse the skill without repeating the full contract. Omit it when the user asked for a concise plan or when the prompts would add noise.

Include both examples when you include the section:

### 最小入力

```text
impl-planner を使って、このタスクの実装 plan を作ってください。

目的:
背景:
制約:
```

### 詳細入力

```text
impl-planner を使って実装 plan を作ってください。

対象リポジトリ:
やりたいこと:
今回やること:
今回やらないこと:
守るべき設計・流儀:
制約:
受け入れ条件:
検証方法:
既知の地雷:
未確定事項:
詳細説明が必要な判断ポイント:
```

## Detail-Request Response Format

When the user asks for detailed decision support, use this structure before or alongside the plan:

## Decision Support / 判断材料

### Recommended Option / 推奨案

- State the recommended option and why it fits the current constraints.

### Option 1 / 案 1: <name>

- Merits / メリット:
- Drawbacks / デメリット:
- Tradeoffs / トレードオフ:
- Applies when / 適用条件:

### Option 2 / 案 2: <name>

- Merits / メリット:
- Drawbacks / デメリット:
- Tradeoffs / トレードオフ:
- Applies when / 適用条件:

### Additional Information Needed / 追加で必要な情報

- List missing facts that would change the recommendation.

## Formatting Constraints

- Do not use tables.
- Use Markdown headings and bullet lists.
- Keep every milestone's heading structure identical.
- Close all code blocks.
- Prefer concise, implementation-ready bullets over long prose.
- Do not tell the implementer to start coding or proceed with execution.
