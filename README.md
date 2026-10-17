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
  - [what you want to achieve]
- Background
  - [why it is needed / what problem exists now]
```

Detailed prompt:

```text
Use `impl-planner` to create an implementation plan.

- Repository / system
  - [software repository or configuration-management tool repository name]
- Repository understanding
  - [what this repository is meant to achieve]
  - [main implementation approach / primary processing flow]
- What you want to achieve
  - [what you want to implement]
- Background
  - [why it is needed / what problem exists now]
- Domain knowledge AI is likely to miss
  - [business rules]
  - [exception handling]
  - [background of existing specifications]
- In scope
- Out of scope
- Points that need detailed explanation or judgment from AI
- Design rules to keep
  - [architecture constraints]
  - [existing patterns]
  - [implementations to avoid]
- Impact surfaces to inspect
  - [entrypoint / routing / registration]
  - [related test / fixture / docs]
- Constraints
  - [backward compatibility]
  - [performance]
  - [security]
  - [operations]
  - [runtime / library constraints]
- Acceptance criteria
- Validation steps
  - [build / test / lint / typecheck / e2e]
  - [manual verification steps]
- Known pitfalls
- Open questions
```

### Detailed input guide

Fill in what you know; you do not need to answer every field. Leave unknowns or undecided points under `Open questions` instead of guessing file paths, commands, or behavior. An empty field does not mean there are no constraints.

The examples below describe one fictional task: improving recovery after an order form fails to save. Its repository name, rules, and constraints are illustrative, not requirements for your task. Keep the copyable prompt above brief and use this guide when a field is hard to fill in.

| Field | Why it helps | Questions to consider | Example entry |
| --- | --- | --- | --- |
| `Repository / system` | Identifies the target and its boundaries. | Which repository, application, or operational target should change? | The order-entry web app in the fictional `order-portal` repository. |
| `Repository understanding` | Connects the change to the system's purpose and flow. | What does the system do? What processing flow do you already know? | Staff enter orders in a form; the web app sends them to an API for storage. |
| `What you want to achieve` | Defines the desired outcome. | Who should be able to do what, and in which situation? | Staff can retry a failed save without re-entering the order. |
| `Background` | Explains the problem and its priority. | What happens now, and why is it a problem? | A failed save clears the form, forcing staff to enter the order again. |
| `Domain knowledge AI is likely to miss` | Captures business rules and their context. | What seemingly reasonable behavior would be wrong for this business? | Two identical orders can be intentional. Matching contents alone must not be treated as proof of a duplicate. |
| `In scope` | Identifies the work to include. | What changes must this task cover? | Preserve input after failure, show an error, and support manual retry without duplicating the same submission. |
| `Out of scope` | Prevents unwanted expansion. | What related work should wait? | Automatic retries and restoring input after the page is closed. |
| `Points that need detailed explanation or judgment from AI` | Focuses comparison and explanation. | Which decision needs options and a recommendation? | Compare ways to prevent duplicates when the server saves an order but its response never arrives. |
| `Design rules to keep` | Preserves established implementation conventions. | Which existing patterns must remain, and why? | Keep API calls in the existing shared client so authentication and error handling stay consistent. |
| `Impact surfaces to inspect` | Provides leads for repository investigation. | Which screens, callers, tests, or docs might be affected? | Inspect the order form, shared API client, order-creation API, and save-related tests; exact paths are unknown. |
| `Constraints` | Rules out unacceptable solutions. | What compatibility, performance, security, or operational limits apply? | Existing API clients must keep working. Do not persist order input in browser storage. |
| `Acceptance criteria` | Makes completion observable. | What result would demonstrate success, including failure cases? | Failed saves retain input and display an error. Retrying saves the order once, even if the first response was lost. |
| `Validation steps` | Explains how to check the expected results. | Which known checks or manual steps can demonstrate those results? | Disconnect before saving and check retained input and the error. Also simulate a lost response after a successful save, retry, and verify one stored order. Test commands are unknown. |
| `Known pitfalls` | Highlights past failures. | What went wrong with a similar change, and under what conditions? | A previous retry fix created duplicates when the server had saved successfully but the client timed out. |
| `Open questions` | Keeps uncertainty separate from decisions. | What is unknown, and what has not been decided? | Unknown: whether the API already recognizes repeated submissions. Undecided: whether the UI should offer canceling a pending retry. |

`What you want to achieve` describes the outcome; `In scope` describes the work included. `Acceptance criteria` describes success; `Validation steps` describes how to check it. Business rules belong under domain knowledge, implementation conventions under design rules, and limits on acceptable solutions under constraints.

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
