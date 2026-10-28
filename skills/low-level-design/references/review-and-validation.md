# Review and validation

## Design guidance

Verify behavior by tracing a concrete initial state, each operation, each state change, and the outcome. Exercise rejections as well as the successful path. In the game, an invalid move must not advance the turn; a winning final move must not be labeled a draw. In the locker, a used or expired code must not grant access, and expired credentials do not release occupied compartments.

Choose data structures in relation to the workload. Scanning a small compartment set can be simpler than maintaining an availability index. An index speeds lookup at the cost of update consistency. Extra state needs a workload-specific justification.

## Application considerations

For an existing design, first establish the intended contract and the actual execution path. A useful finding contains:

- Trigger: a realistic operation and initial state.
- Evidence: code location or design statement supporting the behavior.
- Consequence: violated rule and user-visible effect.
- Correction: the smallest change that restores the contract, with a relevant verification case.

Rank by consequence and likelihood in the stated context. Distinguish a demonstrated bug, a plausible risk requiring evidence, and an optional improvement. Missing information is a question or explicit assumption, not automatically a defect. Avoid broad rewrites when a local correction suffices.

Select validation from the actual risks:

| Risk | Useful validation |
| --- | --- |
| Illegal state or inconsistent derived fields | Invariant checks across representative command sequences |
| Boundary or time rule | Exact boundary, just-before/after, and clock control |
| Rejected command changes state | Snapshot or observable state check before/after rejection |
| Shared mutable reference escapes | Caller mutation attempt followed by invariant check |
| Conflicting operations | Controlled interleaving or transactional integration test |
| Dependency failure or cancellation | Inject failure at the consequential point; check cleanup and retry behavior |
| Compatibility change | Existing caller/contract tests and migration rehearsal where needed |

Use a small executable test when implementation exists and the behavior matters; for a design-only task, give concrete acceptance scenarios and identify what cannot yet be proven. Do not claim to have run a test or validated a guarantee merely because a case is listed.

Concurrency, credential generation, physical actuation, recovery, and specialized safety need task-specific validation when material to the user's system.
