---
name: low-level-design
description: Design or assess component internals, responsibilities, interfaces, state ownership, and lifecycle rules in real software. Use for module or object design and bounded design reviews; not mock interviews or whole-system infrastructure planning.
license: MIT
---

# Low-level design

Produce an implementable component design whose state changes and contracts satisfy the user's requirements. Adapt to the project's language and conventions: functions, modules, data types, and objects are all valid. A class hierarchy is not the default output.

## Ground the decision

- Establish the component boundary, callers, required operations, observable outcomes, and important invalid actions. Ask only for consequential missing facts; otherwise state assumptions.
- For existing software, inspect the relevant public interfaces, state writes, dependency lifecycle, and tests before proposing changes. Identify compatibility constraints and cite paths when available.
- Respect the requested mode: design, bounded review, or implementation. A design request alone does not call for code changes, installation, or deployment.

## Build the smallest useful model

1. Trace required behavior to state, its owner, and the rule that owner enforces. Distinguish data from entities with identity or lifecycle. An extra noun does not automatically require an extra type.
2. Specify contracts before filling in internals: inputs, results, errors, preconditions, mutation, and postconditions. Explain which parts callers may rely on.
3. Walk a representative operation through the owners in execution order. Show a meaningful rejection or failure path. Identify what changes and what remains unchanged.
4. Select data structures and abstractions for the actual workload and expected change. Compare a simpler alternative when adding indirection. Prefer a direct branch or function until interchangeable behavior, lifecycle, or coupling justifies more.
5. Where relevant, define resource creation/disposal, cancellation, reentrancy, concurrency boundaries, and persistence failure behavior.
6. Validate the consequential rules with concrete cases and identify any guarantee that still needs implementation or runtime evidence.

For a small decision, answer it directly. For a component blueprint, include responsibilities and ownership, essential contracts, a core flow or state transition, the choice and rejected alternative, and targeted validation. Use a diagram or table only when it makes the design clearer. Produce code or a saved design document when the user requests it or repository conventions call for it.

## Load references only as needed

- For modeling responsibilities or an unclear boundary, read [ownership-and-contracts.md](references/ownership-and-contracts.md).
- For lifecycle rules, redundant state, or operation ordering, read [state-and-lifecycle.md](references/state-and-lifecycle.md).
- When choosing an abstraction or reviewing a proposed pattern, read [abstraction-decisions.md](references/abstraction-decisions.md).
- For an existing-design assessment or verification plan, read [review-and-validation.md](references/review-and-validation.md).

## Review mode

Review against stated behavior and actual code or design evidence. Rank findings by consequences, explaining the failing operation, violated contract or invariant, and smallest useful correction. Separate demonstrated defects from risks and unanswered questions. Do not manufacture findings to fill a template or grade the design by pattern counts.

## Verification limits

For language/runtime guarantees, specialized safety constraints, or current library behavior that affects the design, inspect the implementation or consult primary documentation when needed. State what remains unverified. A good design argument is not proof that concurrency, security, or recovery is correct.
