# Repository Guide

This repository contains the `impl-planner` APM package. The source of truth is:

- `apm.yml`
- `.apm/skills/impl-planner/SKILL.md`
- `.apm/skills/impl-planner/references/plan-contract.md`
- `.apm/skills/impl-planner/references/examples.md`
- `.apm/skills/impl-planner/references/detail-request.md`
- `.apm/skills/impl-planner/references/html-output.md`
- `.apm/skills/impl-planner/references/formatting.md`
- `.apm/skills/impl-planner/references/mini-example.md`
- `.apm/skills/impl-planner/references/prompt-templates.md`
- `.apm/skills/impl-planner/references/research-and-critique.md`
- `.apm/skills/impl-planner/references/software-task-profiles.md`
- `.apm/skills/impl-planner/references/risk-task-profiles.md`
- `.apm/skills/impl-planner/references/config-management-profile.md`
- `.apm/skills/impl-planner/references/platform-notes.md`
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


## Version Release Checklist

When preparing a version release, keep the release state easy to audit:

- Update `apm.yml` to the target version.
- Update install examples in both `README.md` and `README.ja.md` to use the explicit Git tag reference with the target version, such as `withforesight000/impl-planner#1.0.0`.
- Do not use `withforesight000/impl-planner@1.0.0` in APM install examples. APM treats `@...` as alias shorthand and rejects it for this repository reference; use `#<tag>` for Git tags.
- Keep the version bump and install-guide updates in the same release commit when practical, so the released version and documented install command cannot drift.
- Keep unrelated documentation or contract changes in separate commits before the release commit unless the user explicitly asks to combine them.
- Run the full local APM validation listed above before tagging or publishing a release.
- If a release tag already exists and the user asks to retag it, verify the current remote ref first, then update the tag so `refs/tags/<version>^{}` points at the intended HEAD.
- After pushing, verify that `origin/main`, the release tag, and the GitHub Release all point to the intended commit.
- Write GitHub Release notes that summarize the package version, install command changes, user-facing contract or README changes, and the validation commands that were run.

## Documentation Conventions

- When adding user-facing usage examples, include both a minimal prompt and a detailed prompt.
- When the user asks for more detail, present multiple options, a recommended option, and tradeoffs.
- Keep milestone plans in the same heading structure defined by the Skill contract.
