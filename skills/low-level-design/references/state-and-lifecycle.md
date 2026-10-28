# State and lifecycle

## Design guidance

- Replace unrelated booleans representing exclusive states with a representation of the allowed states. The game example's playing/won/draw alternatives avoid contradictions such as “draw and still running.” An enum alone does not ensure that related fields agree; enforce transitions too.
- Walk operations in the order that preserves rules. The game flow validates the actor and lifecycle, places a valid move, checks win before draw, and changes turn only while play continues. This ordering is specific to those rules; derive it again for a different domain.
- Distinguish independently changing facts. A locker's access code can expire while a package remains inside. Releasing capacity merely because a credential expired violates physical occupancy.
- Use a state diagram or transition table when operation validity varies by lifecycle. A small enum and explicit transition function can be enough; a state machine does not require one class per state.

## Application considerations

For a consequential transition, record:

| Before | Command and guard | Authoritative change | Effect | Failure outcome |
| --- | --- | --- | --- | --- |
| Current state | Required actor/input/version | Next state and invariant | Dependency call/event | Unchanged, retryable, or recovery state |

Specify terminal states, expiry boundary semantics, cancellation, restart behavior, and who owns cleanup only when those concerns apply. Use an injectable clock for time-dependent validation where it makes testing practical. Do not treat an expired permission as proof that the underlying work or physical action has stopped.

If more than one execution can change the same invariant, identify the conflicting operations and required indivisible change. Choose synchronization or transactional behavior based on the actual process, persistence layer, and runtime. A language-level lock cannot protect independent processes; a database transaction does not automatically coordinate an external device. Verify the relevant primitives rather than promising safety from a diagram.

Separate “requested,” “acknowledged,” and “completed” when an external effect can fail or be uncertain. Decide whether retries require deduplication or reconciliation. These concerns need task-specific validation.

For resources such as handles, subscriptions, workers, or connections, name who creates them, who closes them, and what happens on setup failure or repeated shutdown. Do not introduce a resource manager when ordinary lexical scope or the project's existing lifecycle mechanism suffices.
