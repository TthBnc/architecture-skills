# Data, labels, and features

## Design guidance

Organize useful signals by source before selecting individual features: item/content, actor/user, behavior, relationships, and request context. Use only the groups that have a predictive hypothesis for this task. For each influential signal, explain representation and availability: immutable content at ingestion, batch aggregates, streaming updates, or request-time context. Fresher computation incurs a cost; establish the quality loss from staleness before adding a streaming pipeline.

Separate trusted human labels from weak supervision and model-generated pseudo-labels. In adversarial applications, yesterday's labels may represent yesterday's attacks; an apparently improving sample can merely reflect the old system filtering easy cases. Preserve label provenance and evaluate on independently judged examples.

A feature is invalid for historical training if it uses knowledge unavailable at the corresponding decision time. Future clicks, post-decision moderation labels, and full-history aggregates can leak. Fit transforms on the training set and apply them consistently at inference. New entities need explicit missing-data behavior and representative training examples; mean imputation alone can hide the absence of history.

Representation follows both data and model: embeddings for suitable sparse categories or learned content, aggregates for cheap behavioral summaries, sequences when order adds measurable value, and appropriate transforms for numeric distributions. Sophisticated representations are options, not an obligation.

## Application considerations

For the few datasets and features that determine the design, record a compact contract:

| Field | Decision it supports |
| --- | --- |
| Entity/event key and deduplication rule | Whether repeated observations alter labels or aggregates |
| Event time, ingestion time, and availability time | Point-in-time joins and delayed/late events |
| Label meaning, provenance, maturity delay, and missingness | Whether a negative means “not yet observed” or “did not occur” |
| Population, sampling rule, and exposure information | Whether observed examples represent deployment traffic |
| Transformation/version and refresh budget | Training/serving compatibility and staleness behavior |
| Owner, access, retention, and deletion handling | Whether the signal can actually be used and maintained |

A shared feature store is one way to reduce skew, not proof that it is absent. Compare historical training examples with the features actually served for matching requests, using privacy-appropriate samples. Include schema, units, null rates, range, freshness, and transformation parity.

For feedback loops, identify exactly how a prediction changes future exposure and labels. Consider audited samples, safe exploration, or debiasing where appropriate; do not introduce random harmful actions merely to obtain unbiased data. Model scores are not independent ground truth.

Review sensitive features, proxies, permissions, and disparate error impact when relevant. Minimize collection to justified signals. No feature's mere predictiveness establishes that its use is permitted or desirable.
