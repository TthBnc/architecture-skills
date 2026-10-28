# Data and interfaces

## Core decisions

Derive resources/entities and access patterns from operations. For each important query, identify filters, ordering, expected cardinality, and an index or access path. Normalize when it helps protect shared facts; introduce duplicated/materialized views when a demonstrated read requirement justifies maintaining and reconciling them. Database selection should follow access patterns and needed guarantees, not the label SQL/NoSQL.

An interface must communicate request/response state and errors. Choose resource operations, action-oriented RPC, or client-shaped queries based on actual consumers and constraints. Cursor pagination can avoid some instability/cost of deep offsets, but needs defined sort order and cursor semantics. Bind authorization to verified identity and check access to the specific resource; user-provided identifiers do not establish permission.

## Correctness boundaries

Specify the lifecycle and invariants that the schema must enforce: uniqueness, valid state transitions, tenant ownership, and atomic multi-record changes. Identify the transaction boundary and the actual isolation/conditional-write behavior needed. A diagram containing a database or lock does not itself establish correctness.

Define read semantics by operation: an approximate dashboard count can lag, while allocating a scarce item may require a single authoritative conditional update. CAP is a statement about behavior under partition, not a blanket instruction to choose consistency or availability for every operation. Confirm actual guarantees in the chosen implementation.

When retrying a mutation, define the logical operation identifier and its tenant/caller scope, request-parameter compatibility, retention, concurrent duplicate handling, and result semantics. Where an external effect exists, local transactionality alone cannot prove that the effect happens once. See [asynchronous work](asynchronous-work.md).

Partitioning/sharding decisions need both distribution and locality analysis: a high-cardinality hash key does not eliminate one extremely active key. Cross-partition queries, rebalancing, global uniqueness, and transactions add work and failure cases. Distributed transactions may be supported by the chosen database; do not assume that sharding makes atomicity impossible. A compensating workflow is not an atomic rollback and may expose intermediate states.

Avoid shortcuts: REST is not mandatory, optional schema details cannot be omitted if they affect correctness, and security or data retention cannot be dismissed because a worked example scoped them out.
