---
name: ml-system-design
description: Design production ML-backed features and their data, evaluation, training, and serving architecture. Use for classifiers, recommenders, retrieval, forecasting, or ML architecture decisions; not ordinary model-API coding, factual ML explanations, or mock interviews.
license: MIT
---

# ML system design

Turn an ML-backed product goal into a proportionate, testable design. Cover the decisions the user needs; a single model-serving decision does not require a full platform blueprint. Design only unless the user requests implementation. Proposed experiments, data collection, deployments, and policy changes do not authorize their execution.

## Ground the decision

- Establish the user-visible action, product objective, error consequences, and constraints that change the design: available data and labels, scale, freshness, latency, budget, privacy, and operating ownership.
- For existing systems, inspect relevant code, schemas, inference contracts, metrics, and deployment constraints before proposing replacements. Distinguish observations from assumptions.
- Ask only consequential unanswered questions. When progress is possible, state provisional assumptions and identify which decision changes if an assumption fails.
- Include a heuristic, existing model, or manual baseline. ML is a means to the product outcome; insufficient data can justify a collection-first or non-ML design.

## Work through the consequential choices

1. Connect the product objective to the prediction or ranking task, observable labels, offline metrics, online outcome, and guardrails. Choose the action threshold separately from the model score. Read [objectives-and-evaluation.md](references/objectives-and-evaluation.md) for metric and experiment design.
2. Trace raw events through labels, example construction, features, training, inference, action, and feedback. Specify when information becomes available. Read [data-and-features.md](references/data-and-features.md) for leakage, sampling, and feature freshness.
3. Compare credible model families against the baseline and constraints. State the learning target, required supervision, representation, and major complexity costs. Hyperparameters are empirical decisions, not facts to invent. Read [models-and-retrieval.md](references/models-and-retrieval.md) when selecting models, embeddings, or ranking stages.
4. Design the training and serving paths together. Trace the critical path, fallbacks, version compatibility, refresh, and recovery. Read [serving-and-operations.md](references/serving-and-operations.md) when a production lifecycle or inference architecture is in scope.
5. Stress the weakest assumptions: delayed or biased labels, new entities, distribution changes, skew, corrupt features, and consequential prediction errors. Prioritize what could change the decision; do not append every possible ML concern.

## Deliver a usable decision

Scale the artifact to the request. For a complete feature, usually include:

- Objective, constraints, unknowns, and a recommendation with its rationale.
- A diagram or clear description covering both training and serving; show where outcomes return as labels.
- Essential data/label contracts, time semantics, model input/output, and policy actions.
- Baseline versus viable alternatives, including what evidence justifies extra complexity.
- Evaluation slices, validation and rollout gates, fallback/recovery behavior, owners, and remaining experiments.

Attach estimates to units and assumptions: eligible events per day, label delay, inference requests and candidates, model/index size, and stage latency or compute where they matter. Distinguish measured values from hypotheses. Explain what would make you revise the recommendation.

## Scope and verification

Read only the relevant bundled references. Verify current primary documentation when a decision depends on vendor capabilities, limits, guarantees, costs, or specialized domain knowledge. If unavailable, label the dependency unverified and give a validation step. This guidance does not prove a design production-ready or establish best practice for every ML domain.
