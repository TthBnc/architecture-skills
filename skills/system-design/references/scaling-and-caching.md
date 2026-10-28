# Scaling and caching

## Core decisions

Caching can lower repeated-read cost but introduces freshness, invalidation, stampede, and hot-key behavior. Choose the layer from the reuse pattern: client/CDN, application memory, or shared cache. Specify the authoritative source, key scope, invalidation/expiry, miss behavior, and acceptable stale response. TTL bounds an entry's nominal lifetime; it is not proof of correctness for a protected decision or a guarantee that every observer sees fresh data.

Cache-aside reads fill from the source; write-through or write-behind changes when acknowledgment and authoritative persistence occur. Write-behind requires explicit loss/failure analysis. Coalescing requests and staggering expiry can reduce stampedes. Cache loss can shift traffic to a database that lacks spare capacity: test that path rather than assuming fallback is harmless.

Before sharding, identify whether the bottleneck is query shape, index design, read load, write contention, storage, or a hot key. Consider tuning or simpler scaling options. When partitioning is justified, compare range, hash, and directory routing against locality, skew, movement, and ownership needs. Plan resharding and cross-shard work; do not infer uniform traffic from uniform key distribution.

## Correctness examples

Approximate global rate limiting does not meet a requirement for a strict global quota. State the allowed overshoot and partition behavior; choose coordination or quotas with a proven bound when strictness matters. Fail-open and fail-closed are business/security choices, not universal availability defaults.

A ticket-booking design can separate a heavily cached browse/search path from authoritative scarce-inventory allocation. A cache or time-limited lock alone does not prove no double booking: the authoritative store needs a valid ownership/state transition under races and retries. Expiring a hold must not free an already completed booking. Payment completion may need reconciliation independently of a hold's lifetime.

Test representative skew and bursts, not only aggregate QPS. Design degradation/fairness for scarce capacity, specify what users see during delays, and avoid adding caches, search clusters, streams, and multiple databases unless their roles solve the stated problem.
