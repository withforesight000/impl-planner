# impl-planner Detail-Request Response

Use this reference when the user asks for more detail, wants to compare options, or needs help choosing a direction.

## Response Format

Use this structure before the final plan. Resolve the decision first, then carry the chosen option into the required top-level output. Do not add a competing top-level structure beside a final plan.

Use the format below to explain the options. If a decision is needed, follow
the question and fallback rules in `SKILL.md`. A request for explanation alone
requires no choice or approval.

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

- Apply `plan-contract.md` for decision sources, assumption placement, and status.
- Do not pretend certainty where a missing fact would change the recommendation.
- Keep rejected alternatives concise unless the user explicitly asks for deeper comparison.
- In a provisional plan, branch only the milestones affected by the blocker.
