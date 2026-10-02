# Platform Notes

This reference is intentionally separate from the portable output contract. Verify vendor behavior again before relying on it. Codex sources were checked on 2026-09-24; Claude Code and GitHub Copilot sources were checked on 2026-07-10.

## Shared Rule

Native Plan modes provide a write boundary and approval flow. `impl-planner` supplies the portable research, evidence, output, blocker, and critique contract. Do not assume a native plan mode alone guarantees grounded output.

## Codex

- Give the planner the repository goal, constraints, and expected validation, then let it inspect local entrypoints and module boundaries before drafting.
- Keep repository instructions and Skill requirements concise and non-duplicative so critical constraints remain visible in the shared context.
- Current local Codex clients can delegate when applicable `AGENTS.md` or Skill
  instructions request it. Follow the shared delegation rule in `SKILL.md`;
  use its second-pass fallback when subagent tools are unavailable.
- When a plan needs user input, run in Plan mode and use `request_user_input` to
  present native structured choices. If the tool is unavailable, do not imitate
  that UI by listing options in Markdown; return a provisional plan instead.
- Official context: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) and [GPT-6 model guidance](https://developers.openai.com/api/docs/guides/latest-model).

## Claude Code

- Plan mode is read-only until approval. Built-in Explore and Plan subagents use isolated contexts and skip `CLAUDE.md` and parent git status; repeat required constraints in the handoff prompt.
- Use a fresh critic or a deliberate second pass after drafting rather than relying on the draft author's self-assessment.
- Use `AskUserQuestion` when the runtime exposes it. Otherwise, use Claude
  Code's normal concise interactive question flow; do not require Codex's
  `request_user_input` behavior.
- Official context: [permission modes](https://code.claude.com/docs/en/permission-modes) and [subagents](https://code.claude.com/docs/en/sub-agents).

## GitHub Copilot

- The VS Code Plan agent performs discovery, alignment, design, and refinement. Ask it to preserve the final plan outside ephemeral session memory when it must be reviewed or handed off.
- Subagents are independent workers; provide the same scope, evidence, and stopping conditions that the main plan requires.
- Use the Plan agent's alignment questions or another exposed structured-question
  capability. Do not require Codex's `request_user_input` behavior.
- Official context: [planning with agents](https://code.visualstudio.com/docs/agents/planning) and [subagents in VS Code](https://code.visualstudio.com/docs/agents/subagents).

## No-Tool or No-Subagent Fallback

Use the same evidence labels, blocker policy, and critic checklist locally. A platform without subagents must still perform the second-pass checklist and must not claim unseen repository facts.
