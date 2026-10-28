# Ownership and contracts

## Design guidance

- Identify operations and invalid actions before choosing types. Derive each stored field and exposed operation from a requirement rather than modeling every noun.
- Put data-specific rules with the owner of that data. Use a coordinator for rules spanning a workflow. A caller should request a valid operation instead of reading internals, deciding externally, and setting several fields itself.
- Distinguish an entity's condition from a relationship managed by a coordinator. Either ownership choice can work if it is explicit and avoids competing authorities. The locker example separates physical package presence from code validity: an expired code does not mean an empty compartment.
- Protect mutable state from accidental writes through returned collections or object references. Copying a collection is insufficient if its elements still expose protected mutable state; select the boundary that the contract requires.
- A concept deserves a separate type when it owns meaningful rules, identity, or lifecycle. In the locker example, package size is an input; an access credential with expiry and compartment association has behavior worth modeling. Different requirements can change that choice.

## Application considerations

Use a small mapping when ownership is ambiguous:

| Concern | Design question |
| --- | --- |
| Authoritative state | Who alone may commit a change, and through which operation? |
| Derived state | Can it be computed? If cached, what invalidates it? |
| Identity | Does equality mean equal value or the same lifecycle entity? |
| Public contract | What must a caller know, and which implementation detail can remain private? |
| Effects | Which calls mutate memory, persist data, or contact an external dependency? |

For important operations, describe input validity, result/error semantics, state changes, and postconditions. State whether a failed operation leaves state unchanged, partially applied, or pending reconciliation. Do not use `bool` when callers must distinguish actionable failures; do not invent an elaborate error hierarchy when a simple result suffices.

In a brownfield design, identify every existing writer to the state being protected. A new wrapper cannot enforce an invariant if old callers still bypass it. Plan a compatible transition if public fields, return types, or ownership must change.
