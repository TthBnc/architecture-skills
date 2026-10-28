# Production validation and evolution

## Scope

Select production checks in proportion to the decision. Current product facts and specialized guarantees still need verification.

Select checks that affect the actual decision:

- **Trust and data:** identify callers, services, tenant/resource authorization, untrusted inputs, secrets, sensitive data paths, retention/deletion, and backup exposure. State domain-specific review needs; do not declare compliance from an architecture sketch.
- **Failure and recovery:** define what survives a process, dependency, or region failure as relevant. Specify accepted loss and recovery targets, ownership of authoritative state, restore/replay paths, and how to test them.
- **Operation:** choose user-visible success/error/latency signals and diagnostic state such as backlog age or failed transitions. Assign operational ownership proportionate to the team's capacity. Do not equate more dashboards with observability.
- **Delivery:** identify compatibility, schema/data migration, backfill and reconciliation, rollout, and rollback/roll-forward when changing an existing system. A code rollback does not undo an incompatible data rewrite.
- **Cost:** identify dominant cost drivers and an estimate range; distinguish known prices from unverified placeholders. Account for idle capacity, data transfer, retention, and operating burden where material.

## Safe retry contracts: overload

Request rate alone can misrepresent capacity: request resource costs vary. Use measurements of constrained resources and realistic workload mixes. When overloaded, consider cheaper degraded responses or admission limits. Retried work consumes capacity too, so bound retry amplification and shed work where necessary to protect recovery.

## Validation contract

For each material uncertainty, name an experiment and a decision it can change. Examples: benchmark the hot access pattern at peak concurrency; crash a worker after a side effect but before acknowledgment; restore from backup into an isolated environment; introduce delayed or duplicated events; run a migration on representative data. Describe the observation needed, not just "load test" or "add monitoring".

Separate required-before-launch validation from later optimization. Give a simple evolution path with triggers: measured saturation, unacceptable tail latency, recovery limits, cost, or changed guarantees. Do not report design hypotheses as successful test results.
