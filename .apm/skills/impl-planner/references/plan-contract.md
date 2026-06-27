# impl-planner Output Contract

This reference defines the required output shape for implementation planning. Use it for software repository changes or configuration-management tool repository changes.

## Required Top-Level Output

Use the instructions below to choose the right level of detail and labels.
The final plan output must start with the missing-context section, followed by `Assumptions`, then `Plan.md`.

- Write explanatory prose and bullet contents in the same language the user used for the request.
- Use the English structural labels for English requests and the Japanese structural labels for Japanese requests unless the user explicitly asks for a different variant.
- Scale the amount of structure to the task size without losing implementation readiness.

## Scale Guidance

- For small, low-risk changes, use one milestone and keep bullets concise.
- For small changes, optional milestone subsections with no meaningful content may be omitted instead of filled with boilerplate.
- Always keep `goal`, `files / modules likely affected`, `acceptance criteria`, and `validation commands` for each milestone.
- Use the full milestone structure for cross-cutting, risky, data-affecting, security-sensitive, deployment-sensitive, or configuration-management changes.
- If the user asks for a concise plan, prefer fewer milestones and shorter bullets while preserving assumptions, observable acceptance criteria, and validation.

## Structural Labels

Use this label set for English requests:

- `## Missing Context and Ambiguities`
- `### Blocking now`
- `### Can proceed with assumptions`
- `### Can confirm during implementation`
- `## Assumptions`
- `## Plan.md`
- `## Milestone N: <short title>`
- `### goal`
- `### files / modules likely affected`
- `### acceptance criteria`
- `### validation commands`
- `### decision notes to avoid oscillation`
- `### main risks`
- `### rollback considerations`

Use this label set for Japanese requests:

- `## 前提不足・曖昧点`
- `### 今答えないと plan が破綻するもの`
- `### 仮定を置けば進められるもの`
- `### 実装中に確認すればよいもの`
- `## Assumptions`
- `## Plan.md`
- `## Milestone N: <short title>`
- `### goal`
- `### files / modules likely affected`
- `### acceptance criteria`
- `### validation commands`
- `### decision notes to avoid oscillation`
- `### main risks`
- `### rollback considerations`

## Missing Context and Ambiguities / 前提不足・曖昧点

### Blocking now / 今答えないと plan が破綻するもの

- List ambiguities that materially prevent a correct plan.
- If none, say `None.` for English or `なし。` for Japanese.

### Can proceed with assumptions / 仮定を置けば進められるもの

- List uncertainties that can proceed under explicit assumptions.
- Keep assumptions concrete and implementation-relevant.

### Can confirm during implementation / 実装中に確認すればよいもの

- List items that can be verified while implementing without changing the overall plan.

## Assumptions

- State all assumptions used by the plan.
- Include assumptions about scope, compatibility, migration, test strategy, deployment, runtime, data safety, and operational constraints when relevant.
- If the user asked for detail and an option was selected or recommended, record that decision here or in milestone decision notes.

## Plan.md

Use `## Milestone N: <short title>` for each milestone. Keep the milestone heading structure consistent within the plan.

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

## Self-Check Gate

Before returning the plan, verify these points and revise the plan if any check fails:

- Each acceptance criterion is observable by a reviewer, test, command, or runtime behavior.
- Each validation command is concrete, or the validation class is explicit when the exact command is unknown.
- Each meaningful risk has a corresponding rollback, mitigation, or decision note.
- Blocking unknowns are not silently converted into assumptions.
- The plan size matches the task size and avoids filler sections.

## Mini-Example

This example shows the expected density for a small English request. Adapt language and labels to the user's request.

```md
## Missing Context and Ambiguities

### Blocking now

- None.

### Can proceed with assumptions

- Assume the existing README structure should stay intact and only installation wording changes.

### Can confirm during implementation

- Confirm `apm install owner/repo --dry-run --global --target codex` succeeds before finalizing docs.

## Assumptions

- The package remains planning-only.
- The install path should prefer repository references over requiring users to clone the repository.

## Plan.md

## Milestone 1: Update installation docs

### goal

- Document clone-free installation using the `owner/repo` APM reference.

### files / modules likely affected

- `README.md`
- `README.ja.md`

### acceptance criteria

- English and Japanese READMEs both show the repository-reference install command.
- The docs include a dry-run command.
- No wording implies users must clone the repository.

### validation commands

- `apm install withforesight000/impl-planner --dry-run --global --target codex`

### decision notes to avoid oscillation

- Prefer `owner/repo` examples over archive examples for the primary install path.
```

## Future Usage Prompts

If useful, include a final section named `## Skill Usage Prompt Examples / Skill 利用時のプロンプト例`.

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

- Use Markdown headings and bullet lists.
- Tables are allowed when they make comparisons, option tradeoffs, or file lists easier to scan.
- Keep milestone heading structure consistent within a plan, except for intentionally concise small-change plans.
- Close all code blocks.
- Prefer concise, implementation-ready bullets over long prose.
- Do not tell the implementer to start coding or proceed with execution.
