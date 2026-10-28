# Interview flow

## A flexible progression

Establish important functional behavior and quality constraints, identify core entities and the interface, build a complete high-level flow, then investigate the constraints that most challenge it. Estimates earn their place when they affect a design decision. A processing-heavy system may benefit from an explicit input-to-output flow before its component diagram.

Suggested approximate pacing: requirements 5 minutes, entities 2, interface 5, optional data flow 5, high-level design 10–15, deep dives 10. These are interview aids, not universal rules or evidence of time elapsed in a chat. An exercise with no long data pipeline need not add one. A candidate can revise entities and interfaces while discovering the design.

In a 40-minute-equivalent text exercise, use those proportions as stage emphasis. State stage transitions when useful, not fabricated countdowns. Keep a running note of the agreed requirements, candidate choices, untested assumptions, hints, and open probes. If the user requests a real-time simulation, use available time evidence and the agreed stop rule.

## Probing without giving the solution

A useful sequence is:

1. “What does the user need to accomplish?”
2. After a candidate proposes a flow: “Where does this request change authoritative state?”
3. After the baseline works: probe the particular quality goal or failure case that matters most.

Ask only the next question in the conversation. Do not send this entire sequence as a questionnaire.

For a reservation design, a gentle hint could ask what occurs when two users select the same resource. A stronger hint supplies a specific concurrent interleaving. A final hint may name a conditional update, while still leaving the candidate to explain its effect. Select hints based on the actual gap; a candidate already enforcing exclusivity should receive a different probe.

The interviewer may offer facts about the scenario when asked. Label chosen numbers as exercise assumptions. Do not reveal an answer by embedding every desired technology in the prompt. Accept alternative approaches that satisfy the agreed constraints.
