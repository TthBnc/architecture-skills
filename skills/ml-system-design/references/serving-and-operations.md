# Serving and the operating lifecycle

## Design guidance

Choose batch, request-time, or mixed inference from the freshness/latency need. Cached or precomputed predictions can avoid per-request model execution. Embeddings and features age independently of model weights; define what changes trigger each refresh. Drift can affect inputs, prevalence, or the relationship to outcomes. Monitor features, predictions, and quality when labels arrive, rather than assuming a periodically trained model remains useful.

## Operational baseline

Start with a simple first model, infrastructure tests separate from predictive quality, explicit freshness requirements, checks before model export, and detection of stale or missing features. Assign maintained features an owner. A design plan does not authorize a deployment.

## Operating lifecycle

Map both paths, proportionately:

```text
Historical inputs + matured outcomes → example construction → training/validation
    → versioned model + preprocessing → quality/compatibility gate
Live input → feature retrieval → inference → policy/action → outcome logging
                                  ↑                    ↓
                        fallback/version choice ← monitored behavior
```

- **Serving contract:** inputs, outputs, timeout, critical dependencies, freshness, and version IDs. Budget end-to-end tail latency, including network, feature fan-out, queueing, and retries. Benchmark on representative traffic; adding isolated component medians does not establish an end-to-end tail-latency target.
- **Failure policy:** distinguish unavailable model, corrupt/stale feature, missing history, low confidence, and overload. Choose a baseline, abstention, cached result, or human queue according to error consequences. State the limits of each fallback and how recovery occurs.
- **Reproducibility:** record model, preprocessing, feature/data snapshot, code, configuration, and evaluation versions sufficient to reproduce important decisions within retention/privacy constraints. Make a previous compatible release recoverable.
- **Release proposal:** use offline checks and, when appropriate, shadowing followed by a bounded trial. Identify quality, latency, resource, and policy guardrails and the condition for reverting. A deployment plan remains a proposal unless execution is requested.
- **Monitoring:** distinguish service health, schema/feature coverage and freshness, prediction shifts, and delayed outcome quality by relevant slice. An input-distribution alert is a diagnostic signal, not proof of quality loss; stable inputs also do not prove quality is stable.
- **Retraining:** establish a freshness hypothesis and compare a candidate on appropriately recent, matured evaluation data. Investigate pipeline faults, selection bias, and label changes before retraining. Automatic retraining must not automatically promote a worse model. Online learning adds feedback/poisoning and recovery complexity; use it only for a demonstrated adaptation requirement.
- **Ownership and cost:** identify who responds to a degraded feature, model, and downstream policy. Include labeling and review effort, training/inference compute, data retention, and operational load in the comparison.

This is a design framework, not a complete MLOps, security, or regulated-domain standard. Domain-specific safeguards and current platform behavior require appropriate evidence when they affect a real decision.
