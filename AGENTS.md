# Repository Guide

This repository contains the `impl-planner` APM package. The source of truth is:

- `apm.yml`
- `.apm/skills/impl-planner/SKILL.md`
- `.apm/skills/impl-planner/references/plan-contract.md`
- `.apm/skills/impl-planner/references/examples.md`
- `.apm/skills/impl-planner/references/detail-request.md`
- `.apm/skills/impl-planner/references/html-output.md`
- `.apm/skills/impl-planner/references/formatting.md`
- `README.md`
- `README.ja.md`

## Working Rules

- Keep the project planning-only. Do not add implementation code, migrations, or other behavior changes unless the user explicitly asks for them.
- Prefer `apply_patch` for file edits.
- Prefer `rg` / `rg --files` for searches and file discovery.
- Do not use destructive git commands such as `git reset --hard` or `git checkout --` unless the user explicitly asks for them.
- Keep `README.md` in English except for the Japanese README link near the top.
- Keep `README.ja.md` in Japanese.
- Keep `impl-planner` skill prompts and documentation consistent across README files and the Skill contract.
- The skill accepts prompts in both Japanese and English.

## Validation

When changing the package or the skill, verify with the local APM CLI:

```bash
apm audit --file .apm/skills/impl-planner/SKILL.md
apm audit --file apm.yml
apm pack --dry-run
apm pack --archive --dry-run -v
apm install --dry-run --target codex
apm install --dry-run --target claude
apm install --dry-run --target copilot
```

Use these checks to confirm that the package metadata, skill contract, and bundle contents still match the intended layout.

## Documentation Conventions

- When adding user-facing usage examples, include both a minimal prompt and a detailed prompt.
- When the user asks for more detail, present multiple options, a recommended option, and tradeoffs.
- Keep milestone plans in the same heading structure defined by the Skill contract.
