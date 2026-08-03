# Lab 8 — Diagnose Performance and Propose One Bounded Scaling Experiment

**Course:** Agentic AI for Linkedin Marketing (C386)  
**Version:** v1.0 (3 August 2026)  
**Topic 4:** Automating and Scaling LinkedIn with AI Agents  
**Maps to:** LO6: Validate synthetic LinkedIn results, calculate defined metrics, diagnose the decision chain, and produce a human-reviewed improvement with guardrails and rollback.  
**Tools:** Spreadsheet application, approved AI assistant, supplied synthetic performance CSV and Labs 1-7 outputs  
**Duration:** 55 minutes

---

## Goal

LO6: Validate synthetic LinkedIn results, calculate defined metrics, diagnose the decision chain, and produce a human-reviewed improvement with guardrails and rollback.

## What You Will Do

You analyse a supplied synthetic performance export without assuming that reach equals business value. You define each metric, check the data, compare like with like, identify the most plausible bottleneck, and recommend one controlled change that remains inside the governed workflow.

## What You Will Build

C386-linkedin-pack/08-performance-diagnosis-and-improvement.md plus C386-linkedin-pack/08-cleaned-performance-metrics.csv containing definitions, quality log, calculations, funnel diagnosis, alternative explanations, experiment card, approval decision, cooldown, rollback, and course-pack manifest.

## Prerequisites

- Retain the Lab 1 decision chain and guardrails, the Lab 4 content metrics, and the Lab 7 canonical states, approval packet, and trace schema.
- Open labs/resources/northstar-linkedin-performance.csv.
- Use only the synthetic values; do not export or upload real member, message, or account data.

> **Data note.** Use only the supplied synthetic case files and an approved AI assistant. Do not scrape LinkedIn, use unauthorised bots or browser extensions, mass-send invitations or messages, publish automatically, or paste credentials or real personal data into prompts.

## Steps

**1. Create the analysis file and cleaned metric table. Use the exact CSV schema below so duplicate instances, comparison dimensions, dispositions, counts, rates, and caveats remain reviewable.**

```text
Files: C386-linkedin-pack/08-performance-diagnosis-and-improvement.md and C386-linkedin-pack/08-cleaned-performance-metrics.csv
CSV columns: row_instance_id,source_record_id,date,content_type,pillar,audience_stage,disposition,issue,impressions,members_reached,interactions,engagement_rate_pct,profile_view_rate_pct,follower_rate_pct,messages_sent,replies,reply_rate_pct,qualified_conversations,qualified_conversation_rate_pct,owned_outcomes,outcome_rate_pct,caveat
row_instance_id must be unique even when source_record_id repeats; use distinct IDs such as ROW-010A and ROW-010B for the duplicate R-010 records.
Markdown sections: Decision Question | Metric Dictionary | Data Quality | Calculations | Funnel | Diagnosis | Alternatives | Experiment Card | Decision Log | Pack Manifest
```

**2. Write the decision question and metric hierarchy. Separate discovery, engagement, profile activity, conversation, and business outcome. Name the primary outcome and at least two guardrails from Lab 1.**

```text
Question: Which single controllable change is most likely to improve <OUTCOME> for <AUDIENCE> while protecting <GUARDRAILS>?
```

**3. Define every metric before calculating it: source field, numerator, denominator, filters, time period, scope, unit, limitation, and missing-denominator treatment. Treat LinkedIn analytics as estimates and do not mix member-post and Page definitions silently.**

```text
Minimum: impressions | members_reached | interactions | engagement_rate | profile_view_rate | follower_rate | reply_rate | qualified_conversation_rate | outcome_rate. A blank or zero denominator returns N/A, never 0%.
```

**4. Inspect the CSV. Check row count, unique IDs, dates, missing values, negative values, impossible relationships, duplicates, content type, audience stage, and whether comparison periods and denominators are compatible.**

```text
Quality disposition: USE | USE WITH CAVEAT | EXCLUDE | OWNER TO VERIFY.
```

**5. Calculate counts and rates in the spreadsheet. Show formulas, keep counts beside rates, and return N/A for a blank or zero denominator. Verify the three fixed seed results before continuing.**

```text
interactions = reactions + comments + reposts + saves + sends + link_visits
engagement_rate_pct = interactions / impressions * 100
profile_view_rate_pct = profile_viewers_from_post / impressions * 100
follower_rate_pct = followers_gained / impressions * 100
reply_rate_pct = replies / messages_sent * 100
qualified_conversation_rate_pct = qualified_conversations / messages_sent * 100
outcome_rate_pct = owned_outcomes / qualified_conversations * 100
Seed checks: R-001 engagement_rate_pct = 3.83%; R-002 engagement_rate_pct = 5.24%; R-009 reply_rate_pct = 33.33%.
```

**6. Build the funnel view from impressions to members reached, meaningful interactions, profile viewers, replies, qualified conversations, and the synthetic owned outcome. State where direct attribution is unavailable.**

```text
Do not treat an impression, reaction, profile view, or reply as a completed business outcome.
```

**7. Ask the AI to diagnose the largest constrained drop using the quality log and metric definitions. Require three possible explanations, evidence for and against each, missing evidence, and one proposed controllable variable.**

```text
The AI may recommend; it may not change frequency, content, messaging, targeting, permissions, or account behaviour.
```

**8. Challenge the diagnosis. Compare like content types and audience stages, inspect outliers, consider timing and source freshness, and reject any causal claim not supported by the synthetic design.**

```text
Diagnosis status: SUPPORTED | PLAUSIBLE | WEAK | NOT TESTABLE WITH CURRENT DATA.
```

**9. Write one bounded experiment card with hypothesis, one variable, baseline, predicted direction, primary metric, guardrails, segment, owner, approval packet, observation window, minimum useful sample, cooldown, stop threshold, and rollback. Complete the decision log, list every final course-pack file, and log each correction in a before/after evidence table.**

```text
Decision: HOLD | APPROVE FOR SMALL HUMAN-RUN PILOT | REVISE | STOP. The lab does not change any live activity.
| Item | Before | After | Source or reason | Reviewer | Timestamp |
```

## Test It

Open 08-performance-diagnosis-and-improvement.md and 08-cleaned-performance-metrics.csv. Verify R-001 engagement 3.83%, R-002 engagement 5.24%, and R-009 reply rate 33.33%; the two R-010 instances must have distinct row_instance_id values and explicit duplicate dispositions, while R-011 impossible reach and R-012 missing denominator must carry explicit dispositions, and blank or zero denominators must return N/A. The diagnosis must state alternatives and limitations, and the experiment must change exactly one variable with an owner, primary metric, two guardrails, observation window, cooldown, stop threshold, and rollback. The course-pack manifest must list outputs 01 through 08.

## Checkpoint for the Next Lab

The connected C386-linkedin-pack is complete. Re-run the manifest and three random evidence traces before adapting any part of the system to authorised workplace data.

## Troubleshooting

- **Rates look impressive but counts are tiny:** Report numerator and denominator beside every rate, widen the observation window, and avoid a decision until the minimum useful sample is met.
- **The AI claims a post caused revenue:** Return to the funnel and label missing attribution; distinguish correlation, contribution, and verified owned outcomes.
- **The experiment changes content, timing, and audience together:** Choose the single highest-priority controllable variable and hold all other planned conditions stable.

## Optional Challenge (+10 minutes, outside core duration)

Create a pre-mortem with three ways the proposed experiment could harm trust, data quality, or workflow capacity, then add one early-warning indicator for each. Save the result in the numbered lab output.

## Reflection

What evidence would make you reverse the experiment even if the primary metric improved? Record your answer in the numbered lab output.

---

[← Lab 7](lab-07-design-the-governed-content-and-engagement-operations-workflow.md) · [Labs index →](README.md)
