# Failure and contention reasoning

## Concurrent reservations and purchases

A browsing view may tolerate staleness while booking needs stronger correctness. A database lock held through a human checkout ties up resources for an unbounded interaction. Reservation state plus expiration can separate the checkout interval from a short state transition. Any claim that a lock prevents double booking must identify what the protected commit actually checks.

Trace two buyers racing for the same seat, an expired holder returning, duplicate payment callbacks, and a timeout after an external payment succeeded. Identify the authoritative conditional transition and ownership/version checked at confirmation. A distributed lease expiring does not stop its previous holder from continuing work. Where external effects cannot share the local transaction, review idempotency, reconciliation, and compensation according to the product's promises. A TTL or a payment provider name alone supplies none of these guarantees.

## Rate limiting and overload

Shared limits require a coherent state scope and atomic updates. Partitioning by client spreads independent clients but does not divide a single hot client. Fail-open admits traffic when protection is unavailable; fail-closed sacrifices access to preserve protection. Neither policy is universally correct. Configuration push reduces delay at the cost of delivery and reconnection complexity; polling can suffice when bounded delay is acceptable.

Distinguish a strict global quota from an approximate regional or per-instance allowance. Count the actual operations and benchmark the target deployment rather than treating an illustrative throughput number as a guarantee. Verify the complete read-decide-update operation: grouping writes in a transaction does not by itself prove a prior read is protected against races. If local token allocation or regional independence is used, quantify allowed overshoot and failure behavior. Check retries and queue growth against the bottleneck's capacity.

## Work queues and repeated effects

At-least-once delivery requires reasoning about each effect, not only deduplicating a message ID at ingestion. Examine the crash window between executing an effect and recording completion, deduplication scope and retention, acknowledgement timing, bounded retries, poison work, and a recovery owner. A dead-letter queue stores unresolved work; it does not resolve it. “Exactly once” needs a stated boundary and mechanism.

Use the shortest counterexample that demonstrates a required property is violated. Describe an unresolved risk conditionally when the artifact lacks enough detail.
