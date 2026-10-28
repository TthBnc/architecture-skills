# Findings

Report demonstrated consequences and actionable decisions.

A useful finding is a supported decision, not a checklist item:

> **High — timed-out payment retries can duplicate charges.** Design §4 retries payment initiation with a fresh request ID after a timeout. If the provider accepted the first request but its response was lost, the second ID permits another effect, violating the stated one-charge-per-order invariant. Reuse a stable operation key and define reconciliation for ambiguous outcomes, subject to the provider's verified contract. Validate by injecting a timeout after acceptance and retrying the same order.

The severity here follows the explicit financial invariant and the described retry path. If the artifact simply says “payment integration,” phrase this as a question about ambiguous outcomes rather than alleging duplicate charges.

Use severity in the user's scheme if supplied. Otherwise reserve high severity for plausible violations of critical correctness, confidentiality, availability, or recovery requirements. Medium covers material but bounded risks; low covers smaller consequences. State preconditions instead of creating numeric probabilities without data. Do not let a preferred technology become a severity argument.

Citations should point to evidence: design section, supplied diagram edge, verified code line, a relevant test, or measured behavior. Distinguish what was read from what was executed. A source link supports a principle, not proof that this system has a defect. Current guarantees, limits, pricing, and deployment behavior need current primary evidence when the decision depends on them.

Keep recommendations bounded: minimal safe mechanism, relevant alternative, and a concrete acceptance test or evidence request. Indicate migration or operational costs when they could reverse the recommendation. Merge consequences with the same root cause rather than inflating finding counts.

Finish with only consequential open questions, evidence limits, and the next decision. For a narrow design choice, a short review can be sufficient. For an incomplete design, explain what cannot yet be assessed. A clean review is an acceptable result.
