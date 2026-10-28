# Objectives and evaluation

## Design guidance

Keep four concepts separate: the outcome the product needs, the behavior measured in the product, the ML prediction objective, and the policy action taken from that prediction. For abuse detection, counting detections can reward overblocking; measure impact on legitimate users with error guardrails. For recommendations, clicks can rise while satisfaction falls; pair short-term signals with an appropriate longer-term outcome.

Offline evaluation supports rapid iteration. Online evaluation asks whether the product outcome improves. Neither implies the other. Establish a baseline and inspect relevant slices: new versus established entities, languages, traffic sources, rare classes, and delayed outcomes. Choose slices because failures matter, not to fill a dashboard.

For scarce positives, raw accuracy is inadequate. Evaluate precision/recall at a threshold appropriate to error costs and review capacity; inspect rare-class performance. Preserve the distinction between investigator labels, noisy reports, proxy outcomes, and model-generated labels. Observed outcomes reflect which actions the previous system allowed.

## Evaluation details

Use precise metric definitions and evaluation assumptions:

- **Precision = TP/(TP+FP); recall = TP/(TP+FN).** State the population and time window. A stratified or enriched evaluation set helps inspect rare cases, but production prevalence and sampling weights matter for population metrics, especially precision. Keep an appropriately representative estimate as well.
- **Recall@K** is the share of relevant items retrieved; **Hit@K** asks whether at least one relevant item is retrieved. They coincide only in a single-relevant-item setup. Ranking quality cannot recover relevant candidates already discarded by retrieval.
- Choose splits that simulate the intended use: chronological cutoffs for future predictions, entity or group separation where sharing would leak, and label-maturity windows. Fit preprocessing and tune thresholds on training/validation data; preserve the final test set.
- A shadow system can test latency, operational behavior, and predictions on observed inputs. It cannot reveal how users would have clicked on a different displayed ranking. Causal product claims require a suitable controlled experiment or a justified counterfactual method with logged propensities, support, and assumptions.
- Specify assignment unit, baseline, primary metric, guardrails, observation horizon, and stopping rule before an experiment. Account for repeated users, interference, delayed labels, and uncertainty where material. Offline lift is evidence for a trial, not guaranteed online improvement.
- Choose thresholds on validation data using error costs, capacity, and calibrated scores where probabilities drive action. Reassess under a changed base rate. Human review requires queue capacity, escalation behavior, and feedback quality; it is not an unlimited fallback.

A practical design should state what result would reject the proposed model or policy, and how that result can be measured without leaking future information.
