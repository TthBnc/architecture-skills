# Review lenses

Read the lenses relevant to the proposed decision; this is not a requirement to raise every category.

## Requirements to observable behavior

Pair each required behavior with the flow that implements it. Quality goals should identify an operation and a measurable target where the brief supplies one. Estimates are useful when they change a choice, not as ritual arithmetic. Track whether the design actually completes an end-to-end flow before optimizing its parts.

Record the distinction between required properties, owner-approved tradeoffs, and reviewer assumptions. “Fast” may require clarification; it does not authorize inventing a 50 ms SLA. A small internal workflow may need one database and worker, while a global high-traffic brief may justify isolation and partitioning. Evaluate current demand and plausible growth separately.

## Interfaces and ownership

Review pagination for bounded reads, error behavior for recoverability, and repeated requests for duplicate effects. Authentication identifies the caller; authorization checks whether that caller can act on the specific resource. Client-supplied identity does not establish ownership.

Inspect actual trust boundaries and authentication integration when supplied. Neither “JWT” nor “API gateway” proves authorization. Tie any finding to the proposed path and resource. Treat protocol choice as a contextual contract decision rather than a universal REST default.

## Persistence and query paths

Access patterns, volume, and consistency needs shape schemas. Explain which query an index serves. Denormalized copies trade read efficiency for update and reconciliation work. Stable identifiers and database constraints can protect relationships and uniqueness.

A transaction needs the appropriate statements, isolation, and conflict handling to enforce a cross-request invariant. Ask where authoritative state resides, what replication lag affects, and how one entity's hot traffic is bounded. A database-per-service convention is not evidence that a shared database is wrong.

## Operational fit

If consequential to the brief, consider recovery from a worker crash, backup restoration, schema changes, credential and tenant boundaries, and the team's ability to operate the design. Connect each concern to a concrete dependency or requirement. Avoid turning missing compliance context into a claimed legal violation. Make restore drills, latency tests, or migration checks proposed validations until actually performed.
