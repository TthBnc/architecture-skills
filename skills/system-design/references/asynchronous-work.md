# Asynchronous work and external effects

## Core decisions

Match the mechanism to the job:

| Need | Viable starting point | Extra responsibility |
| --- | --- | --- |
| Short synchronous operation | Direct request with bounded execution | Timeout and uncertain-outcome handling |
| Work can finish after acknowledgment | Durable job record/queue plus workers | Claiming, retry, status, replay, overload |
| Independent consumers need replayable ordered events | Partitioned log/stream | Keys, per-partition order, retention, consumer progress |
| Multi-step work waits, retries, and resumes over long periods | Durable state machine or workflow engine | Versioning, compensation, activity idempotence, operations |

Kafka offsets capture consumer progress, and a crash between an effect and an offset commit can cause reprocessing. Ordering within a partition is not global ordering. For Temporal-style execution, deterministic workflow replay and external activities have distinct roles; external activities can still repeat. If a queue and worker satisfy the requirements, a workflow platform needs a further justification.

## Safe retry contracts

Callers can express operation identity with a request identifier. Reuse with incompatible parameters needs a defined rejection. Recording that identity and applying a local mutation must not leave a gap that permits repeat effects. Define what a late duplicate means and how long the identity is retained. Identical parameters alone do not establish identical intent.

## Application considerations

For each workflow, trace: accept → persist → dispatch → execute → commit result → acknowledge. Insert a crash or lost response between each pair. Identify which states can be retried, replayed, or reconciled, and what prevents the irreversible action from repeating. A queue acknowledgment, an idempotent producer, or a workflow history does not grant exactly-once effects in an unrelated payment/email/storage API.

If a database mutation and event publication must agree, choose and verify a mechanism such as an atomic outbox plus retrying dispatcher; consumers still need duplicate handling. Bound retries with backoff/jitter, deadlines, and classification of retryable errors. Quarantine or surface poison work with a replay policy instead of silently dropping it. Define cancellation and partial-success behavior where relevant.

Do not promise compensation can undo every real-world effect. For uncertain external results, include provider-supported operation identity/status reconciliation or an explicit manual resolution path. Verify the chosen provider's contract before relying on it.
