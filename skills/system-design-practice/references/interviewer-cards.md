# Example interviewer cards

Read the relevant card only after selecting its exercise. Exercise numbers are illustrative assumptions. Keep intended solution concerns private until the candidate reaches them or requests feedback.

## Ticket reservations

Opening prompt: “Design a service where users discover live events and buy tickets.”

If asked, assume assigned seats, a five-minute checkout hold, spiky sales, 100,000 simultaneous customers at a major launch, and the requirement that one seat cannot be sold to two buyers. Search can show slightly stale availability. Narrow the exercise to discovery and booking; there is no need to design every business feature.

Follow the candidate's proposal. Useful probes include the seat state transition, a buyer returning after a hold expires, a crash around payment confirmation, or load on one popular event. Ask one at a time and only after the candidate's relevant explanation. A short database transaction plus authoritative reservation checks is a valid starting point; Redis, microservices, a waiting room, or a separate search engine are not mandatory answers. A hold mechanism alone does not demonstrate payment correctness.

During feedback, distinguish a cache serving stale seat views from the authoritative operation preventing overselling. If the candidate never reaches payments, mark ambiguous external effects unassessed rather than inventing their response.

## API rate limiter

Opening prompt: “Design rate limiting for a public API used by many customers.”

If asked, assume authenticated API keys, separate quotas per customer, burst tolerance, a one-region initial launch, and a budget allowing a shared state service. Let the candidate ask about strict versus approximate limits. Choose one agreed requirement and keep it consistent. Introduce 100,000 requests per second only when scaling becomes the selected deep dive; state it explicitly as new exercise information, and allow revision rather than penalizing the original design retroactively.

Useful probes follow the design: simultaneous checks for one customer, the state store becoming unavailable, one hot customer, or a changed rule reaching different gateways. Token bucket is one viable algorithm, not the required answer. A local-only limiter may be valid for an agreed per-instance approximation. For a strict shared quota, ask the candidate to trace the atomic read-decide-update boundary. Fail-open and fail-closed are judged against the agreed consequence of admission versus rejection, not a memorized label.

Do not use illustrative throughput figures or cloud costs as verified product guarantees. Treat algorithm analysis and deployment benchmarks separately.
