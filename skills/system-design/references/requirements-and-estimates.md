# Requirements and estimates

## Core decisions

Describe observable user/client operations first; system qualities should be tied to an operation and, where meaningful, quantified. Name the entities and sketch their contracts, then trace a working end-to-end path before adding optimization. Estimates are most useful when they change an architectural choice. Revise the initial model as the flow exposes missing state or relationships.

## Engineering adaptation

Timeboxes, fixed requirement counts, and an assumed large distributed deployment are not production requirements. A small tool may be adequately served by one application and a database. An embedded, offline, regulated, or latency-critical system has different constraints; discover them rather than assuming a web-service deployment.

Useful questions depend on the decision:

- Which operation must succeed, and what must never happen? What is the authoritative outcome when a client times out?
- What is the workload: active users, requests/events per second, burst duration, read/write mix, payload size, retention, geographic distribution, and skew?
- Which latency percentile and measurement boundary matter? Is the target request acknowledgment, durable acceptance, or finished processing?
- What loss, staleness, outage, and recovery are acceptable? What is the ownership, team capacity, cost envelope, or deployment restriction?

Use these as prompts, not a compulsory questionnaire. Separate current load, forecast, and a stress scenario. State missing parameters and which decisions depend on them.

Examples of decision-oriented estimates, not measured capacity:

- Arrival rate × mean service time approximates average concurrent work under stable conditions. Averages do not establish tail latency or burst capacity; measure the service-time distribution.
- Daily ingest bytes = events/second × mean bytes/event × 86,400. Multiply retention and replication/storage overhead separately. Compression and indexing need measurement.
- If arrival rate exceeds sustainable service rate, a backlog grows. With spare processing capacity, drain time is approximately backlog/(service rate − ongoing arrival rate); a queue does not create processing capacity.

List units and ranges, identify the bottleneck the arithmetic exposes, and choose a benchmark that could invalidate the estimate. Do not infer costs or vendor throughput from these formulas.
