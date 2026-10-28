---
name: system-design
description: Design software system architectures or make architectural decisions from requirements, workload, and existing-system constraints. Use for designing services, data flows, storage, asynchronous workflows, or architecture changes; not mock interviews or a standalone review of an existing proposal.
license: MIT
---

# System Design

Produce an architecture or decision that the user can evaluate and implement. Scale the depth to the decision: one storage choice does not require a whole-system blueprint. This skill supplies design reasoning, not permission to implement, deploy, or change external systems.

## Ground the decision

Establish the user-visible behavior, actors, critical data, and correctness invariants. Identify workload shape, burstiness, latency/freshness targets, durability, budget, team capacity, and existing technology where these change the design. Distinguish provided facts, assumptions, estimates, and unresolved questions. Ask a small number of consequential questions; proceed with stated reversible assumptions when useful. Do not invent a workload to justify a familiar architecture.

For an existing system, inspect the relevant interfaces, persistence, request/event flows, and deployment constraints before redesigning it. Honor the requested stack and existing decisions unless the evidence warrants a proposed change. Read [requirements and estimates](references/requirements-and-estimates.md) when framing scope or capacity.

## Develop and challenge the design

1. Start with a viable, simple baseline. Trace a representative operation from input through state changes to response, and identify where authoritative state lives. Add components to address a concrete unmet requirement.
2. For consequential uncertain choices, compare structurally viable alternatives against the same constraints, including operational cost and reversibility. Explain why the chosen design fits and what would change the choice. Parallel independent candidates are optional when the task warrants them and delegation is authorized; no particular model or tool is required.
3. Specify the interfaces, data model, access patterns, and ownership needed to make the design coherent. Read [data and interfaces](references/data-and-interfaces.md) for storage, consistency, APIs, or partitioning decisions.
4. Trace relevant failure paths, not just successful requests. Read [asynchronous work](references/asynchronous-work.md) for retries, jobs, streams, or multi-step operations; [scaling and caching](references/scaling-and-caching.md) for read/write load or partition pressure.
5. Check applicable trust boundaries, tenant isolation, data lifecycle, overload, recovery, observability, and delivery/migration risk. Read [production validation](references/production-validation.md) when the decision affects those concerns. Prioritize material issues; do not turn a small design into an infrastructure checklist.

Use estimates with units and explicit assumptions to settle a decision. Avoid both ritual arithmetic and unmeasured claims that a component will meet a target. Verify current primary documentation when a recommendation depends on a vendor's limits, pricing, protocol, or transactional guarantees. If that verification is unavailable, identify the dependency and leave the claim conditional.

## Deliver a reviewable result

Choose a useful format for the user's request. A substantial design commonly includes requirements and assumptions, a component/data-flow diagram, key interface/data contracts, a brief alternatives rationale, failure/recovery behavior, and validation/evolution steps. A bounded decision may need only a short decision memo. Show which components serve which requirements, who owns state, and where guarantees end.

Identify the next experiment or measurement for unresolved design risks and the signals that justify scaling or revisiting the choice. Do not imply that a design has been deployed, load-tested, or independently verified when it has not.

## Scope

Read only the references relevant to the task. The guidance is bundled locally and needs no companion skill or server. For an unfamiliar specialized domain, identify missing knowledge and verify the guarantees that matter instead of assuming complete coverage.
