# impl-planner Detail-Request Response

Read this reference when the user asks for more detail, asks for decision support, asks for multiple options, or cannot choose an implementation direction.

## Response Format

Use this structure before the final plan. Resolve the decision first, then carry the chosen option into the required top-level output. Do not add a competing top-level structure beside a final plan.

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

- List only facts that would change the recommendation.
- Mark each item as a blocker, a safe assumption, or something that can be confirmed during implementation.

## Carry Decisions Into the Plan

- After a choice is made, reflect it in `Assumptions` or milestone `decision notes to avoid oscillation`.
- Do not pretend certainty where a missing fact would change the recommendation.
- Keep rejected alternatives concise unless the user explicitly asks for deeper comparison.
- If a blocker remains and interaction is unavailable, return a `Plan status: Provisional` plan with branches only for the affected milestones.
