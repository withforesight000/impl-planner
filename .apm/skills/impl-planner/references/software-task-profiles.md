# Software Task Profiles

Read only the relevant profile sections. These are investigation checklists, not mandatory output sections; omit items that do not apply.

## API and Public Contract Changes

- Trace entrypoints, request/response schemas, exported types, callers, generated clients, and user-facing documentation.
- State compatibility expectations, versioning or deprecation behavior, error mapping, and authentication/authorization boundaries when relevant.
- Validate both direct consumers and integration boundaries; do not list a public API change without identifying its callers or marking them `[Unknown]`.

## UI Changes

- Identify loading, empty, success, and error states; state transitions; accessibility; responsive behavior; and the data boundary used by the view.
- Include visual or manual validation only when the repository has a relevant UI validation convention; otherwise label it `[Recommended]`.
- Trace user-visible copy, telemetry, feature flags, and API error presentation when they are affected.

## Asynchronous Work and Jobs

- Identify producer, consumer, queue/topic, retry policy, ordering assumptions, deduplication, idempotency key, timeout, dead-letter handling, and observability.
- State behavior for duplicate delivery, partial failure, replay, and rollback. Do not assume exactly-once delivery unless repository evidence establishes it.

## Dependency Upgrades

- Inspect the current version, lockfile or generated artifacts, upstream migration notes, direct API usage, runtime compatibility, and existing update convention.
- Separate required compatibility changes from optional cleanup. Include a revert path and validation that exercises changed dependency behavior.

## Monorepos and Shared Packages

- Identify package ownership, exported contracts, downstream consumers, build/test graph, versioning or release boundaries, and generated artifacts.
- Include all observed consumers or mark the consumer inventory `[Unknown]`; do not treat one package-local test as complete validation for a shared contract.
