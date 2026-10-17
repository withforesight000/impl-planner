# impl-planner APM package

`impl-planner` is a planning-only skill for software repositories or configuration-management tool repositories.
Use it when you want Codex, Claude Code, or GitHub Copilot to produce an implementation plan, not to implement the change.

日本語版: [README.ja.md](README.ja.md)

## What this package does

- Produces a Plan.md-style implementation plan grounded in repository evidence.
- Organizes the plan around the requested outcome, purpose and background, repository understanding, assumptions, unknowns, and task-sized milestones.
- Gives each milestone an implementation approach, affected files or modules with reasons, scope, acceptance criteria, validation, decision notes, risks, and rollback considerations.
- Traces impact across entrypoints, call sites, configuration, tests, and adjacent documentation, while aligning validation with the repository's existing style.
- Distinguishes facts, inferences, proposals, and unknowns, and respects existing architecture or layering patterns.
- Provides recommended and rejected alternatives when detailed decision support is needed, and checks that acceptance criteria and risk actions are actionable.
- Uses conditional task profiles for APIs, UI, async work, migrations, security, monorepos, dependency upgrades, and configuration management.

## Reading the plan

- Start with `Purpose and Background` for the current problem, intended result, and main exclusions. `Repository Understanding` identifies what was inspected and how consequential missing references affect the plan.
- `Missing Context and Ambiguities` distinguishes decisions only you can make from planner research and implementation-time checks. `Assumptions` explains important planner assumptions and their consequences; your explicit decisions remain decisions.
- Each milestone describes an observable result. Its decision notes explain the source, reason, and main tradeoff of important choices without repeating the overview.
- `Plan status: Final` means there is no planning blocker, not that you approved the plan or that implementation or validation is complete. `Provisional` identifies the remaining blocker and dependent scope. Read the short explanation after the status.
- Validation distinguishes discovered commands from actual execution results. A listed command is not evidence that a check passed. These conventions apply to small plans too, using short prose or bullets rather than mandatory tables.

See the [compact Final example](.apm/skills/impl-planner/references/mini-example.md) and the [Japanese Provisional example](.apm/skills/impl-planner/references/provisional-example.md). The latter illustrates missing external evidence when interaction is unavailable; it does not replace clarification when questions can be asked.

## Notes

- The skill is planning-only.
- It must not instruct the agent to edit files, run mutating commands, or proceed to implementation.
- For extended plans with independent read-only research or critique, the skill delegates at least one task when subagents are available; otherwise it uses a deliberate second pass. Small or strictly sequential plans do not require delegation.
- When the user asks for more detail, the skill should return multiple options, a recommended option, and tradeoffs.
- The skill accepts prompts in both Japanese and English.

## How to install with `apm`

You do not need to clone this repository to install the skill on your PC.
Install it directly from the repository reference:

```bash
apm install withforesight000/impl-planner#3.1.0 --global --target codex
```

If you want to preview the install before applying it, use:

```bash
apm install withforesight000/impl-planner#3.1.0 --dry-run --global --target codex
```

You can also install the same package for other supported targets:

```bash
apm install withforesight000/impl-planner#3.1.0 --global --target claude,copilot
```

If you do have a working copy, you can still pack it first with `apm pack --archive` and install the resulting bundle the same way.

## How to use the skill

**We recommend using this skill in your tool’s Plan mode.**

Use this skill when you need an implementation plan for a new feature, a refactor, an Ansible change, or a design decision.

Minimal prompt:

```text
Use `impl-planner` to create an implementation plan for this task.

- What you want to achieve
  - [who should be able to do what, and in which situation]
- Background
  - [what happens now, who is affected, and how it causes problems]
  - [why you want to address it now]
```

Detailed prompt:

Fill in only what you know, focusing on the goal and task-specific conditions. Omitted fields are handled using applicable instructions and repository conventions; see the detailed input guide below.

```text
Use `impl-planner` to create an implementation plan.

- Repository / system
  - [repository to change and the target application, feature, or operational system]
- What you want to achieve
  - [who should be able to do what, and in which situation]
- Background
  - [what happens now, who is affected, and how it causes problems]
  - [why you want to address it now]
- Acceptance criteria
  - [the situation or action and the resulting behavior that would demonstrate completion]
  - [behavior or state to preserve during failures or exceptional cases]
- In scope
  - [work and coverage to include in this change to achieve the goal]
- Out of scope
  - [related changes to exclude or defer]
- Business and system context AI is likely to miss
  - [business rules to preserve, exceptional conditions, and reasons behind existing specifications]
  - [paths or URLs of specifications, sequence diagrams, or other documents to prioritize, and the specific parts to inspect]
  - [related repositories that make up the service, their roles, and how they relate to this change]
- Constraints
  - Backward compatibility
    - [operations, APIs, settings, or data formats that must keep working unchanged, and who uses them]
    - [acceptable changes and conditions requiring migration steps or advance notice]
  - Performance
    - [operations that must not slow down, expected data volumes, or concurrent usage]
    - [desired response time, throughput, or memory usage; include numbers or comparison baselines only if available]
  - Security
    - [guidelines or internal policies to follow or consult, and whether they are mandatory or advisory; you may ask AI to select suitable references]
    - [who should be able to view or modify what, and information that must not be stored, displayed, or logged]
  - Operations
    - [environments, operating procedures, periods when downtime is unacceptable, or acceptable downtime]
    - [conditions to preserve during recovery or rollback, and data that must not be lost]
  - Runtime / library constraints
    - [required or unchangeable technologies, versions, or execution environments, and why]
    - [conditions on adding or updating dependencies, licenses, or support periods]
- Known pitfalls
  - [what broke in a similar past change and under which conditions]
- Open questions
  - [unknown: facts about the current system that need investigation]
  - [undecided: choices where options exist but no direction has been selected]
- Points that need detailed explanation or judgment from AI
  - [decisions you are unsure about, options to compare, and points needing a recommendation and rationale]
- Design rules to keep
  - [layer or module responsibilities to preserve and why]
  - [existing patterns or shared functionality to follow]
  - [implementation approaches to avoid and why]
- Repository understanding
  - [whose needs the system serves and what it helps them achieve]
  - [the main flow you know: from input through processing and storage to output]
- Impact surfaces to inspect
  - [likely related screens, entrypoints, callers, or registration code; include paths only if known]
  - [likely related tests, fixtures, or documentation]
- Validation steps
  - [known build, test, lint, typecheck, or e2e commands that check the acceptance criteria]
  - [conditions to reproduce manually, actions to take, and results to inspect]
```

### Detailed input guide

**You do not need to fill in every field.** Focus on your goal, background, and task-specific conditions. You do not need to repeat instructions already documented in `AGENTS.md`, relevant skills, or other repository documentation, or write “follow AGENTS.md” in each field. Name a particular skill or reference if you want to ensure it is considered.

For omitted fields, the planner uses the following approach:

1. Follow applicable `AGENTS.md` and relevant skill instructions.
2. Where those instructions do not cover the issue, inspect existing code, tests, and documentation to identify established behavior and conventions.
3. If uncertainty remains, proceed with reasonable assumptions for low-impact matters and state those assumptions in the plan. Ask about matters that materially affect the goal, scope, compatibility, safety, or other important decisions.

An omitted field does not mean “no constraints” or “out of scope.” Do not guess file paths, commands, behavior, or business rules to fill the template. If you already know something is unclear or undecided, record it under `Open questions`.

The examples below describe one fictional task: improving recovery after an order form fails to save. Its repository name, rules, and constraints are illustrative, not requirements for your task. Keep the copyable prompt above brief and use this guide when a field is hard to fill in.

| Field | Why it helps | Questions to consider | Example entry |
| --- | --- | --- | --- |
| `Repository / system` | Identifies the target and its boundaries. | Which repository, application, or operational target should change? | The order-entry web app in the fictional `order-portal` repository. |
| `What you want to achieve` | Defines the desired outcome. | Who should be able to do what, and in which situation? | Staff can retry a failed save without re-entering the order. |
| `Background` | Explains the problem and its priority. | What happens now, and why is it a problem? | A failed save clears the form, forcing staff to enter the order again. |
| `Acceptance criteria` | Makes completion observable. | What result would demonstrate success, including failure cases? | Failed saves retain input and display an error. Retrying saves the order once, even if the first response was lost. |
| `In scope` | Identifies the work to include. | What changes must this task cover? | Preserve input after failure, show an error, and support manual retry without duplicating the same submission. |
| `Out of scope` | Prevents unwanted expansion. | What related work should wait? | Automatic retries and restoring input after the page is closed. |
| `Business and system context AI is likely to miss` | Captures business rules and system relationships not visible in the target repository alone. | Which business assumptions must hold? What should be checked in which documents? What do related repositories handle? | Two identical orders can be intentional. Check retry submission identity in docs/order-sequence.md in the order-specs repository. The order-api repository is responsible for order storage and retry deduplication; its current retry-identification behavior needs investigation. |
| `Constraints: Backward compatibility` | Defines the impact on existing users and migration boundaries. | What must keep working unchanged, and for whom? Which changes are acceptable, and when are migration or notice required? | Existing API clients must work without modification. Optional fields may be added, but new required fields need migration and advance notice. |
| `Constraints: Performance` | Identifies operations to protect and comparison baselines. | Which operations or usage volumes matter? Are there target values or comparison baselines? | Avoid slowing down order saves. Usage volumes and targets are unknown; use the current save operation as the comparison baseline. |
| `Constraints: Security` | Separates reference standards from task-specific protections. | Which guidelines are mandatory or advisory? Who may act, and what information needs protection? | Use relevant OWASP guidelines as design references; ask AI to select suitable documents. Do not persist order input in browser storage or write it to logs. |
| `Constraints: Operations` | Clarifies conditions to preserve during changes and failures. | What environment, procedure, or downtime conditions apply? What must recovery or rollback preserve? | Order intake must remain available during business hours. Rollback must not lose orders already saved. |
| `Constraints: Runtime / library constraints` | Bounds technology choices and dependency changes. | Which technologies, versions, or environments must remain, and why? What conditions apply to dependencies, licenses, or support periods? | Keep the existing runtime so deployment needs no operational environment changes. Add dependencies only if existing functionality is insufficient, and check their licenses and support status. |
| `Known pitfalls` | Highlights past failures. | What went wrong with a similar change, and under what conditions? | A previous retry fix created duplicates when the server had saved successfully but the client timed out. |
| `Open questions` | Keeps uncertainty separate from decisions. | What is unknown, and what has not been decided? | Unknown: whether the API already recognizes repeated submissions. Undecided: whether the UI should offer canceling a pending retry. |
| `Points that need detailed explanation or judgment from AI` | Focuses comparison and explanation. | Which decision needs options and a recommendation? | Compare ways to prevent duplicates when the server saves an order but its response never arrives. |
| `Design rules to keep` | Preserves established implementation conventions. | Which existing patterns must remain, and why? | Keep API calls in the existing shared client so authentication and error handling stay consistent. |
| `Repository understanding` | Connects the change to the system's purpose and flow. | What does the system do? What processing flow do you already know? | Staff enter orders in a form; the web app sends them to an API for storage. |
| `Impact surfaces to inspect` | Provides leads for repository investigation. | Which screens, callers, tests, or docs might be affected? | Inspect the order form, shared API client, order-creation API, and save-related tests; exact paths are unknown. |
| `Validation steps` | Explains how to check the expected results. | Which known checks or manual steps can demonstrate those results? | Disconnect before saving and check retained input and the error. Also simulate a lost response after a successful save, retry, and verify one stored order. Test commands are unknown. |

`What you want to achieve` describes the outcome; `In scope` describes the work included. `Acceptance criteria` describes success; `Validation steps` describes how to check it. Business rules, reference documents, and related repositories belong under business and system context, implementation conventions under design rules, and limits on acceptable solutions under constraints.

## Repository layout

- `apm.yml`: APM package manifest
- `.apm/skills/impl-planner/SKILL.md`: Skill entrypoint
- `.apm/skills/impl-planner/references/plan-contract.md`: Core output contract
- `.apm/skills/impl-planner/references/extended-plan-contract.md`: Conditional contract for complex or risky changes
- `.apm/skills/impl-planner/references/examples.md`: Index of optional example files
- `.apm/skills/impl-planner/references/mini-example.md`: Compact plan-density example
- `.apm/skills/impl-planner/references/prompt-templates.md`: Reusable prompt templates
- `.apm/skills/impl-planner/references/detail-request.md`: Optional decision-support response structure
- `.apm/skills/impl-planner/references/formatting.md`: Optional formatting constraints
- `.apm/skills/impl-planner/references/research-and-critique.md`: Conditional delegation and critic-pass contract
- `.apm/skills/impl-planner/references/*-task-profiles.md`: Conditional task checklists
- `.apm/skills/impl-planner/references/config-management-profile.md`: Conditional configuration-management checklist
- `.apm/skills/impl-planner/references/platform-notes.md`: Platform-specific operational notes

## How to verify the package

From the repository root:

```bash
apm audit --file .apm/skills/impl-planner/SKILL.md
apm audit --file apm.yml
apm pack --dry-run
apm pack --archive --dry-run -v
apm install --dry-run --target codex
apm install --dry-run --target claude
apm install --dry-run --target copilot
```

These checks confirm that the skill metadata is valid, that all supported installation targets resolve, and that the package resolves to the expected bundle contents.

## How to distribute

- Use `apm pack` to create a distributable bundle.
- Use the packed artifact for downstream installation or release automation.
- Keep `apm.yml` and `.apm/skills/impl-planner/` as the package source of truth.
