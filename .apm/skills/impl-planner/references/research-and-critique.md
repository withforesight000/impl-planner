# Delegation and Critique Contract

Read this only when delegating research or running a critic pass.

## Delegation Handoff

Repeat the user goal, success criteria, in-scope and out-of-scope boundaries,
read-only constraint, known evidence, questions to answer, expected evidence
format, impact surfaces to inspect, and stopping condition. Do not assume the
worker inherits conversation history, repository instructions, loaded skills, or
files already read.
For delegated critique, also provide the draft plan and the applicable output
contract, or accessible paths the critic must read.
The main planner must verify delegated repository paths and claims before using
them as evidence. Do not claim delegation occurred when no subagent was used.

## Critic Pass

Use a fresh-context critic when available; otherwise use a deliberate second
pass. Check requirement gaps, unsupported claims, dependency direction, missing
interfaces or data/error flows, weak validation, risks, rollback, scope creep,
and planning-only violations. Re-research only the smallest affected area, once,
unless a new blocker appears.
Delegated research does not replace this critic pass; a delegated critic can
fulfill it.

Also apply the core contract's reader-facing checks: can the reader identify the
intended result and exclusions, distinguish user decisions from planner assumptions,
and see who must resolve material unknowns? Check that inspected scope and evidence
gaps agree with the status explanation, that command discovery is not reported as
execution, and that each check can establish its linked acceptance criterion.
Preserve required headings while removing duplicated explanations. Do not introduce
approval gates for decisions that do not require user input.
For each affected file or module, verify the core contract's two-column table:
the reason explains its responsibility and the requirement gap or investigation
need, together with the planned change in the explanation cell. Reject action-only reasons and invented
defects; conditional entries must not imply confirmed modifications.
Check repository-relative file paths, repository prefixes where needed, and
explicit new-file or unknown-path markers. Confirm that assumptions are integrated
into the ambiguity subsections and that five/ten-item caps do not hide blockers;
unresolved overflow must remain visible.
Verify that validation uses three columns and risks use two-column
tables: every condition has an appropriate method, every risk has a concrete
response, and planned validation is not presented as an executed result.
Check that non-command validation has a parenthesized method label in the command
cell, needed but unidentified commands remain explicit, and execution results
are reported outside the table by check ID.
