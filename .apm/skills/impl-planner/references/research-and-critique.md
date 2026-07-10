# Research, Delegation, and Critique Contract

Read this reference for medium or larger changes, risky changes, delegated research, or a critic pass.

## Evidence Contract

Use these labels consistently:

- `[Observed]`: directly read in the repository, command output, or user-provided material; include a path, symbol, config key, command, or equivalent anchor when available.
- `[Inferred]`: conclusion drawn from observed evidence; name the evidence it follows from.
- `[Proposed]`: intended new behavior, file, interface, or validation.
- `[Unknown]`: cannot be established from available evidence and may require a question or implementation-time confirmation.

Never label an unverified path, symbol, command, or behavior as observed. Prefer an explicit unknown over a plausible invention.

## Exploration Stop Conditions

Before drafting, establish the relevant repository boundary, direct dependents, and available validation style. Stop broad exploration when those are known. Re-open only the smallest affected area after a critic identifies a concrete gap; make at most one such pass unless a new blocker appears.

## Delegation Handoff

When delegating research, repeat all of the following in the worker prompt:

1. User goal and success criteria.
2. In-scope and out-of-scope boundaries.
3. Read-only boundary; do not implement or edit files.
4. Known evidence with paths and symbols already inspected.
5. Questions the worker must answer and the required `[Observed]`, `[Inferred]`, `[Unknown]` response format.
6. Expected impact surfaces and validation style to inspect.
7. Stop condition: return once the requested evidence is gathered; do not broaden the task.

Do not assume the worker inherited conversation history, repository instructions, loaded skills, or files already read.

## Critic Pass

Use a fresh-context critic when available. Ask it to check only:

- requirement or constraint omissions;
- unsupported paths, symbols, APIs, commands, or repository claims;
- dependency direction, public interface, data flow, state, and error-handling gaps;
- missing validation, rollout, risk, or rollback coverage;
- scope creep and planning-only violations.

If no independent critic is available, run the same list as a deliberate second pass. Incorporate only findings supported by evidence or explicitly label them as unknown/proposed.
