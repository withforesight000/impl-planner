# Configuration-Management Task Profile

Use this checklist to investigate changes in Ansible or other declarative configuration-management repositories.

- Trace inventory, groups, host/group variables, role boundaries, variable precedence, templates, handlers, playbooks, and service dependencies.
- State idempotency expectations and validate an unchanged second run where repository tooling permits it.
- If you include syntax checking, check mode, or a targeted dry run, explain the limits of each check. Check mode alone cannot establish the safety of every runtime action.
- Identify where secrets come from. Keep values out of the plan and exclude secret material from proposed commits.
- Describe handler notification behavior, service state changes, partial-apply recovery, inventory rollback, and role/play rollback when relevant.
- Keep generated host-specific state, destructive operations, and non-idempotent shell commands explicit in risks and validation.
