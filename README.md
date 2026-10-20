# impl-planner APM package

`impl-planner` is a planning-only skill for software repositories or configuration-management tool repositories.
Use it when you want Codex, Claude Code, or GitHub Copilot to produce an implementation plan, not to implement the change.

日本語版: [README.ja.md](README.ja.md)

## Contents

- [What this package does](#what-this-package-does)
- [Reading the plan](#reading-the-plan)
  - [Purpose and unresolved matters](#purpose-and-unresolved-matters)
  - [Milestone contents](#milestone-contents)
  - [Plan status and validation results](#plan-status-and-validation-results)
- [Planning scope and review](#planning-scope-and-review)
- [How to install with apm](#how-to-install-with-apm)
- [How to use the skill](#how-to-use-the-skill)
  - [Detailed input guide](#detailed-input-guide)
  - [When the AI agent's pre-planning questions are hard to answer](#when-the-ai-agents-pre-planning-questions-are-hard-to-answer)
- [Repository layout](#repository-layout)
- [How to verify the package](#how-to-verify-the-package)
- [How to distribute](#how-to-distribute)

## What this package does

The skill inspects repository code, configuration, tests, and documentation to create an evidence-based implementation plan. It traces affected entrypoints and callers, then aligns the proposed change with existing architecture and validation practices.

The plan is divided into milestones with verifiable outcomes. Each describes the implementation approach, affected files and reasons, exclusions, acceptance criteria, validation, decisions, risks, and rollback.

The skill distinguishes facts, inferences, proposals, and unknowns, and compares options with a recommendation when a decision is needed. Additional checks apply to APIs, UI, asynchronous work, migrations, security, monorepos, dependency upgrades, and configuration management.

## Reading the plan

### Purpose and unresolved matters

`Purpose and Background` explains the current problem, intended result, and main exclusions. `Repository Understanding` identifies the inspected scope and the impact of consequential references that could not be checked.

`Missing Context and Ambiguities` separates blockers, matters that can proceed under assumptions, and implementation-time checks. Assumptions include their basis and consequences if wrong. Explicit user decisions remain decisions; there is no separate assumptions chapter.

Medium or larger changes, changes spanning features or modules, and changes involving data, security, deployment, or configuration management receive more detailed examination of evidence and decision rationale. The level of detail depends on scope, uncertainty, and risk, not changed-line count alone.

Each subsection has at most five items in ordinary plans or ten in plans requiring this closer examination. These are ceilings, not targets. Material overflow is handled through investigation or questions, splitting the plan, or explicit disclosure of the excess and its impact; it is not omitted.

### Milestone contents

Each milestone's goal states an observable completion result. The implementation approach focuses on the change mechanism, responsibility boundaries, and conditions that prevent incorrect implementation. Acceptance criteria hold completion conditions; validation holds detailed tests and measurements. Decision notes explain the source, reason, and main tradeoff of choices without repeating the same explanation.

Consequential values and techniques distinguish user requirements, existing behavior, and planner proposals. Proposals include their basis. Detail follows decision needs and risk; shortening must not remove important constraints.

Affected files use a two-column table: `File / module` and `Reason and planned change`. File paths are verified and relative to the repository root, with repository prefixes for multi-repository work. Proposed paths are marked `New file planned`; unidentified locations are marked `Path unknown` with their investigation scope. Investigation-only entries explicitly state that modification is unconfirmed.

### Plan status and validation results

The plan includes one of these fixed status lines:

- `Plan status: Final (No planning blockers; does not indicate approval, implementation, or validation completion.)`
- `Plan status: Provisional (Important facts or decisions remain unresolved; resolve them before finalizing the implementation approach.)`

A provisional plan identifies its unresolved matters and dependent scope immediately below the status. When interaction is available, the planner seeks clarification rather than using a provisional plan to bypass questions.

Validation uses three columns: `Condition to verify`, `Validation method`, and `Command`. Non-command checks use labels such as `(Document review)` or `(Manual check)`; needed but unidentified commands are marked `Not yet identified`. Long commands appear in referenced code blocks below the table.

Execution status and results appear outside the table, by check ID when needed. A listed command is not evidence that a check passed. Risks use the two columns `Risk / impact` and `Mitigation`. Small plans retain the prescribed file, validation, and risk tables, with short prose or bullets elsewhere.

See the [compact Final example](.apm/skills/impl-planner/references/mini-example.md) and the [Japanese Provisional example](.apm/skills/impl-planner/references/provisional-example.md). The latter illustrates unavailable external evidence and no opportunity for user interaction.

## Planning scope and review

The skill accepts Japanese and English requests. It does not edit files, run state-changing commands, or instruct an agent to begin implementation. Requests for more detail receive multiple options, a recommendation, and their benefits and drawbacks.

For [changes requiring closer examination](#purpose-and-unresolved-matters) with independent read-only research or review, the planner delegates at least one task when subagents are available. Small plans and work that must proceed strictly in sequence do not require delegation.

Plans for these changes also receive a review after drafting. When a separate agent does not perform that review, the authoring agent reviews the complete draft against a checklist after writing it. This review checks missing requirements, unsupported claims, affected scope, validation, risks, and rollback. Delegating research does not remove the requirement to review the draft.

## How to install with `apm`

You do not need to clone this repository to install the skill on your PC.
Install it directly from the repository reference:

```bash
apm install withforesight000/impl-planner#4.0.0 --global --target codex
```

If you want to preview the install before applying it, use:

```bash
apm install withforesight000/impl-planner#4.0.0 --dry-run --global --target codex
```

You can also install the same package for other supported targets:

```bash
apm install withforesight000/impl-planner#4.0.0 --global --target claude,copilot
```

For a local working copy, run `apm pack --archive`, then pass the generated archive path to `apm install`.

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

**You do not need to fill in every field.** Fill in what you know, focusing on your goal, background, and task-specific conditions. Omitted fields are handled using applicable instructions and repository conventions; see the detailed input guide below.

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

You do not need to repeat instructions already documented in `AGENTS.md`, relevant skills, or other repository documentation, or write “follow AGENTS.md” in each field. Name a particular skill or reference if you want to ensure it is considered.

For omitted fields, the planner uses the following approach:

1. Follow applicable `AGENTS.md` and relevant skill instructions.
2. Where those instructions do not cover the issue, inspect existing code, tests, and documentation to identify established behavior and conventions.
3. If uncertainty remains, proceed with reasonable assumptions for low-impact matters and state those assumptions in the plan. Ask about matters that materially affect the goal, scope, compatibility, safety, or other important decisions.

An omitted field does not mean “no constraints” or “out of scope.” Do not guess file paths, commands, behavior, or business rules to fill the template. If you already know something is unclear or undecided, record it under `Open questions`.

The examples below describe one fictional task: improving recovery after an order form fails to save. Its repository name, rules, and constraints are illustrative, not requirements for your task. Keep the copyable prompt above brief and use this guide when a field is hard to fill in.

| Field | Why it helps | Questions to consider | Example entry |
| --- | --- | --- | --- |
| `Repository / system` | Identifies the target and its boundaries. | Which repository, application, or operational target should change? | The order-entry web app in the `order-portal` repository. |
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

### When the AI agent's pre-planning questions are hard to answer

You do not need to choose immediately if an option's meaning or impact is unclear. You can reply by requesting an explanation or further investigation. Use these responses as written, adding any context you know.

| What is difficult | Example reply |
| --- | --- |
| The options are unclear | “Explain with concrete examples how each option changes the user's actions or behavior, using less jargon.” |
| You understand the differences but cannot decide | “Recommend an option for this goal and existing architecture. Explain why, its main drawbacks, and how easily we could change it later. Identify any information still needed to decide.” |
| You do not know the current behavior | “I don't know. Investigate what you can from the repository and related documents, then ask only about what remains unknown.” |
| None of the options fits | “None matches what I want. I want to achieve X and avoid Y. Suggest another option under those conditions.” |
| You want to delegate technical details | “Prioritize X and keep Y unchanged. Use your recommended technical choices within those boundaries in the plan. Ask before changing the goal or scope.” |

It is fine to say either “I don't know the current behavior” or “I haven't decided the direction yet.” Asking for an explanation of a recommendation does not select it. When choosing, make that explicit, for example: “Plan using option A.”

## Repository layout

- `apm.yml`: APM package manifest
- `.apm/skills/impl-planner/SKILL.md`: Skill entrypoint
- `.apm/skills/impl-planner/references/plan-contract.md`: Core output contract
- `.apm/skills/impl-planner/references/extended-plan-contract.md`: Conditional contract for complex or risky changes
- `.apm/skills/impl-planner/references/examples.md`: Index of optional example files
- `.apm/skills/impl-planner/references/mini-example.md`: Compact plan-density example
- `.apm/skills/impl-planner/references/provisional-example.md`: Complete Japanese example of a provisional plan when required evidence and interaction are unavailable
- `.apm/skills/impl-planner/references/prompt-templates.md`: Reusable prompt templates
- `.apm/skills/impl-planner/references/detail-request.md`: Optional decision-support response structure
- `.apm/skills/impl-planner/references/formatting.md`: Optional formatting constraints
- `.apm/skills/impl-planner/references/research-and-critique.md`: Research delegation and post-draft review procedure
- `.apm/skills/impl-planner/references/*-task-profiles.md`: Conditional task checklists
- `.apm/skills/impl-planner/references/config-management-profile.md`: Conditional configuration-management checklist
- `.apm/skills/impl-planner/references/platform-notes.md`: Platform-specific operational notes
- `.agents/skills/maintain-impl-planner/SKILL.md`: Repository maintenance skill
- `.agents/skills/maintain-impl-planner/scripts/check_consistency.py`: Read-only inventory and symlink checker
- `.agents/skills/maintain-impl-planner/tests/test_consistency.py`: Checker regression tests
- `.claude`: Relative symlink to `.agents` for shared maintenance skills

## How to verify the package

Repository maintainers can use `maintain-impl-planner` to identify related
documentation and validation before changing contracts, references, or packaging.
The maintenance skill is stored in `.agents/skills`; `.claude` points to `.agents`.
These maintenance files are outside the distributed APM skill.

Minimal prompt:

```text
Use maintain-impl-planner to check this repository change for missing documentation updates.
```

Detailed prompt:

```text
Use maintain-impl-planner to review the added, removed, and renamed references in this branch.
Check the source-of-truth list, example index, and both README layouts, then review contract and bilingual meaning.
Run the structural checks and APM dry runs and report warnings and unverified items. Do not modify files.
```

Run the local structural checks with Python 3.11 or later:

```bash
python3 -B -m unittest discover -s .agents/skills/maintain-impl-planner/tests -v
python3 -B .agents/skills/maintain-impl-planner/scripts/check_consistency.py
```

The checker detects missing, stale, or duplicate inventory entries and incorrect
shared-instruction links. Use `--root PATH` to check another checkout. Exit codes
are `0` for success, `1` for inconsistent contents, and `2` for invalid arguments
or an invalid root. It does not check general Markdown links or native skill
discovery in an agent client.

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

These commands check skill and package definitions, planned installation for each target, and bundle contents. Bilingual meaning and generated-plan quality require separate review.

## How to distribute

Use `apm pack` to create a bundle for installation or release automation. Maintain the original sources in `apm.yml` and `.apm/skills/impl-planner/`.
