# Delegation and Critique Contract

Read this only when delegating research or running a critic pass.

## Delegation Handoff

Give the worker the user's goal, success criteria, scope and exclusions, and
the read-only constraint. Include the evidence already known, the questions to
answer, where to look, how to report evidence, and when to stop. Supply relevant
conversation context, repository instructions, skill guidance, and file paths
the worker may need.
For delegated critique, also provide the draft plan and the applicable output
contract, or accessible paths the critic must read.
The main planner must verify delegated repository paths and claims before using
them as evidence. Do not claim delegation occurred when no subagent was used.

## Critic Pass

Use a fresh-context critic when available; otherwise the authoring agent reviews
the complete draft against the following checklist after writing it.
Check requirement gaps, unsupported claims, dependency direction, missing
interfaces or data/error flows, weak validation, risks, rollback, scope creep,
and planning-only violations. Re-research only the smallest affected area, once,
unless a new blocker appears.
Review the draft even if another agent researched it. A delegated critic can
perform the review.

Apply `plan-contract.md` → `Final Check` to the draft as well. That contract
defines reader-facing structure, evidence, decision sources, field placement,
and table rules; review against those definitions rather than a second copy.
