# Data and Security Task Profiles

Read only the relevant profile sections. Escalate unresolved choices that change data safety, security, compatibility, or operational behavior to a blocker.

## Database Migration and Backfill

- Identify schema change, migration ordering, forward/backward compatibility, old/new application coexistence, backfill source and batching, integrity checks, and observability.
- Distinguish reversible operations from irreversible data changes. State rollback limits honestly; restoring application code alone may not restore data.
- Include rollout and validation phases when a migration changes live data or service compatibility.

## Authentication, Authorization, Secrets, and Security Boundaries

- Identify the trust boundary, principal, permission decision point, protected resource, secure default, error exposure, audit trail, and secret handling.
- Require a blocker when the intended permission matrix or default access policy is not established by the request or repository evidence.
- Never replace an unresolved security decision with a permissive assumption. Include targeted negative-path validation and rollback or disablement behavior.
