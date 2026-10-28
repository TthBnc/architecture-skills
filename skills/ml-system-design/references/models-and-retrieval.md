# Models and retrieval

## Design guidance

Start with a measurable baseline appropriate to the task: rules/manual workflow, a simple statistical model, or an existing model. Compare alternatives on the requirement that motivates a change: quality, label/data budget, inference latency, cost, interpretability, or freshness. Avoid assuming that a transformer, GNN, vector database, or model trained from scratch is necessary.

Higher capacity increases the need for suitable supervision and validation. With little labeled data, consider a simpler model, pretrained representations, or limited fine-tuning. Diagnose with training/validation behavior; changing architecture is not a substitute for detecting leakage or a broken data pipeline. Hyperparameters and representation dimension need experiments against a baseline.

Embeddings express the training objective's similarity, which can be behavioral rather than semantic. A two-tower system jointly learns compatible query/user and candidate/item representations so candidate vectors can be precomputed and retrieved. Define positive pairs and negatives; difficult negatives can improve discrimination, but apparent negatives may contain unlabeled positives.

A large ranking workload can justify retrieval, cheap filtering/ranking, expensive ranking, and final policy/slate ordering. Each added stage spends compute and can discard good items. Measure retrieval recall separately from final ranking quality. Reuse precomputed content where possible; session context may require fresher work. A small catalog may need no retrieval funnel at all.

Cold entities need content/attribute-based or nonpersonalized candidates before interaction-based representations become useful. Existing upstream embeddings are dependencies to verify, not assets to assume exist.

## Application considerations

For retrieval, compare a lexical, structured, or exact-search baseline with learned/approximate retrieval where applicable. Define relevance and evaluate the actual downstream task; attractive nearest-neighbor examples alone do not validate a system. RAG quality also depends on corpus coverage, access control, chunking, filtering, retrieval, and generation; embeddings alone cannot establish answer quality.

Version the encoder, preprocessing, vector dimension, similarity metric, and candidate index together. A new encoder can invalidate all stored vectors even if the dimension is unchanged. Define backfill/build time, new-item updates, deletion propagation, atomic compatibility switching, and rollback. Include filtering and tenant boundaries in recall and latency tests.

Separate model evaluation from search approximation error: compare ANN results with exact retrieval on an appropriate sample. Estimate vector storage as item count × dimension × bytes per value, then add measured index overhead, replicas, metadata, and update headroom. Size and latency examples from a lesson are not vendor guarantees.

For a proposed staged ranker, show candidate counts and the compute/latency budget at each stage. Add a stage only when profiling and quality measurements support it. Do not copy the billion-item example's architecture into a thousand-item application.
