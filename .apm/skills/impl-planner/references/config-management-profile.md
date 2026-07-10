# Configuration-Management Task Profile

Use this profile for Ansible or another declarative configuration-management repository. Treat these as investigation points, not boilerplate.

- Trace inventory, groups, host/group variables, role boundaries, variable precedence, templates, handlers, playbooks, and service dependencies.
- State idempotency expectations and validate an unchanged second run where repository tooling permits it.
- Include syntax checking, check mode, or targeted dry-run only when their limitations are stated; check mode does not prove every runtime action is safe.
- Identify secrets sources and ensure plans do not expose values or propose committing secret material.
- Describe handler notification behavior, service state changes, partial-apply recovery, inventory rollback, and role/play rollback when relevant.
- Keep generated host-specific state, destructive operations, and non-idempotent shell commands explicit in risks and validation.
