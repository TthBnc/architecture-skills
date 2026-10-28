---
name: system-design-review
description: Review a proposed system architecture or consequential design decision against requirements, finding evidenced correctness, reliability, scaling, and operational risks. Use for engineering design reviews, not mock interviews or routine code-style review.
license: MIT
---

# System Design Review

Produce an independent assessment of a supplied design that helps its owner decide what to change, verify, or accept. Review depth follows the decision's consequences and the user's scope.

## Establish the review target

Read the proposed artifact and relevant requirements first. For a repository-backed design, inspect the specific interfaces, persistence paths, tests, and deployment constraints needed to establish claims. Keep implementation evidence distinct from design intent. If no artifact exists, ask for it or offer a narrowly scoped assessment of the stated proposal; do not invent a system to criticize.

Identify essential user behavior, invariants, workload, latency/freshness needs, dependencies, and team or budget constraints. Resolve only consequential ambiguity. Mark assumptions and conditional risks clearly; an unspecified property is not automatically a defect.

Use [review lenses](references/review-lenses.md) for requirement-to-flow checks. Load [failure and contention reasoning](references/failure-and-contention.md) when shared state, retries, reservations, or overload affect correctness. Use [reporting findings](references/findings.md) to report results.

## Trace before judging

Follow the critical requests or events through identity checks, state changes, external effects, responses, and recovery. Identify authoritative state and the operation that enforces each invariant. Walk a concrete counterexample through the supplied design: concurrent requests, duplicate delivery, stale reads, dependency timeout, or resource exhaustion as relevant.

Separate a demonstrated violation from an unresolved detail. A diagram that omits a retry policy is evidence of uncertainty, not proof of infinite retries. Cite artifact sections, file paths and verified lines, or observed behavior. Link source material only for the general reasoning it actually supports.

Examine alternatives proportionately. A simpler mechanism that meets the stated requirements is a useful alternative; a large rearchitecture needs a concrete reason. Respect mandated technologies and organizational constraints. Do not recommend components just because they occur in a familiar worked example.

## Return a decision-ready review

Lead with the most consequential findings. For each material issue give:

- Severity tied to impact and likelihood under stated conditions.
- Artifact evidence and a concrete failure scenario.
- The affected requirement or invariant.
- A bounded correction or viable options, including their cost.
- A test, measurement, or clarification that would establish the claim or fix.

Separate confirmed findings, conditional risks, and open questions. Deduplicate issues with the same root cause. Include concise strengths or accepted tradeoffs when they materially affect the decision. If there are no substantiated findings, say so and state the scope and evidence limits; do not pad with generic concerns.

Review only unless implementation is requested. Never change infrastructure, submit external comments, or treat a design review as deployment authorization.

## Verification limits

Verify current product behavior against primary documentation when a finding depends on it; if unavailable, make the finding conditional and name the missing verification. Do not infer guarantees from a technology name, transaction label, lock TTL, or marketing claim. All working guidance is bundled locally.
