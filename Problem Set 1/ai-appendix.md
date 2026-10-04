# AI Appendix

## Prompt sent to AI

[Prep] Act as a partner reviewing an analytics deliverable before it
goes to a client board. You are looking for the objection that would
embarrass us in the room.

[Request] I audited a retailer's "average basket value" metric. I found
the naive mean was inflated by a right-skewed B2B tail and by a change
in what was logged between years. I recommend the dashboard show a
trimmed mean with an explicit B2B exclusion rule. Give me the three
strongest objections to that recommendation, ordered by how likely the
client is to raise them, and for each one tell me what evidence would
settle it.

[Iterate] Be specific to this metric. Do not give me generic data
quality advice.

[Mechanism Check] For each objection, say whether it is a question
about the data, about the statistic, or about the business definition
of the metric — these need different kinds of answer.

[Evaluate] Which single additional analysis would most reduce our
exposure?


## Raw AI reply

The three strongest objections are:

1. **“Why is the B2B exclusion rule valid?”**  
   **Type:** Business definition.  
   The client may question whether large orders should automatically be treated as B2B. A high-value consumer purchase could be excluded, or a smaller B2B purchase could remain.  
   **Evidence that would settle it:** Compare the rule with known order type or customer type. Check how many true consumer orders are excluded and how many B2B orders remain after the cutoff.

2. **“Why use a trimmed mean instead of the normal mean?”**  
   **Type:** Statistic.  
   A trimmed mean changes the meaning of “average basket value” because it intentionally removes part of the distribution. If large consumer baskets are real purchases, trimming them may understate actual consumer spending.  
   **Evidence that would settle it:** Compare the ordinary mean, median, trimmed mean, and mean after B2B exclusion on consumer-only data. If the ordinary mean after correctly removing B2B orders is stable, trimming may not be necessary.

3. **“Does this actually fix the change in what was logged between the two years?”**  
   **Type:** Data.  
   Removing B2B orders does not automatically correct a logging change. For example, if cancelled orders appear in Year 2 but not Year 1, they can still affect the metric even after B2B orders are removed.  
   **Evidence that would settle it:** Recalculate the Year 2 metric after separately removing the transactions caused by the logging change, then compare it with the proposed corrected metric.

**Single additional analysis that would most reduce our exposure:**  
Run a sensitivity analysis that separates the two problems: first remove only B2B orders, then remove only the transactions caused by the logging change, and finally remove both. Compare each result with the clean consumer-only average. This would show whether the proposed correction actually recovers the number the dashboard is supposed to measure.


## Changes I made

- I tested the first objection by checking whether any consumer orders were above $500 and whether any B2B orders were at or below $500.
- I also checked how many cancelled orders remained below $500.
- I kept my Phase 2 recommendation, but noted that the $500 rule does not completely fix the logging problem.
