# Data and Security Task Profiles

Read only the sections that apply. Treat an unresolved choice as a blocker if
it changes data safety, security, compatibility, or operational behavior.

## Database Migration and Backfill

- Identify schema change, migration ordering, forward/backward compatibility, old/new application coexistence, backfill source and batching, integrity checks, and observability.
- Identify which operations can be reversed and which data changes are permanent.
  Explain what rollback can recover and where recovery stops. Reverting application
  code may leave data changed.
- Include rollout and validation phases when a migration changes live data or service compatibility.

## Authentication, Authorization, Secrets, and Security Boundaries

- Identify the trust boundary, principal, permission decision point, protected resource, secure default, error exposure, audit trail, and secret handling.
- Require a blocker when the intended permission matrix or default access policy is not established by the request or repository evidence.
- Never replace an unresolved security decision with a permissive assumption. Include targeted negative-path validation and rollback or disablement behavior.
