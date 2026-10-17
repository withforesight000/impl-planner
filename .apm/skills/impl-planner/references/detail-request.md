# impl-planner Detail-Request Response

Read this reference when the user asks for more detail, asks for decision support, asks for multiple options, or cannot choose an implementation direction.

## Response Format

Use this structure before the final plan. Resolve the decision first, then carry the chosen option into the required top-level output. Do not add a competing top-level structure beside a final plan.

This structure explains the comparison; it is not the mechanism for collecting
a decision. Explain the recommendation and tradeoffs in Markdown when useful,
then use the available structured-question tool for the actual selection. Do not
repeat its selection prompt in prose. If no structured tool is available, use a
concise conversational question when ordinary interaction is possible. If neither
is possible and a blocker remains, follow the provisional-plan fallback below;
do not end with an unanswered selection prompt. A request for explanation alone
does not require asking the user to choose or approve anything.

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

- Record user-selected options as decisions in the relevant requirements or milestone `decision notes to avoid oscillation`, with their source, reason, and material tradeoff. Do not weaken explicit user decisions into assumptions.
- Put planner assumptions in `Assumptions`, with their basis and the impact if wrong; refer to them from affected milestones.
- Do not pretend certainty where a missing fact would change the recommendation.
- Keep rejected alternatives concise unless the user explicitly asks for deeper comparison.
- If a blocker remains and interaction is unavailable, return a `Plan status: Provisional` plan with branches only for the affected milestones.
