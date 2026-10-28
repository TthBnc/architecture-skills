# Abstraction decisions

## Design guidance

Start with the direct solution. Similar-looking code is not automatically the same concept; premature deduplication can couple unrelated rules. A type's responsibilities should change together. Split concerns when independent change or testing becomes difficult, not to reach a preferred number of classes.

Use an abstraction to hide meaningful variability or dependency complexity. Composition is often easier to change than a hierarchy combining several independent dimensions. Inheritance requires a substitutable contract: a derived type must honor what callers are allowed to expect from the base type.

| Need | Candidate | Simpler alternative and caution |
| --- | --- | --- |
| Exchangeable behavior with one contract | Strategy | Function/callback or direct branch; avoid one interface per trivial method |
| Construction logic callers should not repeat | Factory | Constructor or named function; centralize actual selection/validation |
| Several independent consumers of a change | Observer | Direct calls if relationships are few and stable |
| Optional, composable behavior layers | Decorator | Explicit function pipeline; ordering can change semantics |
| Complicated allowed transitions | State machine | Enum plus transition function before per-state types |
| A coherent entry point over messy collaborators | Facade | Ordinary coordinating function/module |
| Many construction options with validation | Builder | Language-native defaults or named arguments may suffice |
| A shared resource | Explicit lifetime and injection | A global singleton hides dependency and complicates isolation |

Patterns describe solutions; naming one does not justify the complexity. Popularity and numerical pattern limits are not production design rules.

## Application considerations

When adding indirection, identify the concrete requirement it protects and show the next likely change it makes easier. Account for its cost: tracing control flow, extension compatibility, testing, lifecycle, or failure handling. If the only benefit is an imagined future feature, keep the direct design and state what evidence would justify refactoring.

Match the language. An algebraic data type, closure, module, trait, protocol, or plain structure may express the contract better than an object hierarchy. Keep dependency boundaries focused on what the consuming domain needs rather than exposing an entire vendor SDK.

For event subscriptions, define whether notification is synchronous, what an observer failure does, and who unsubscribes. For layered behaviors, determine which order preserves the contract.
