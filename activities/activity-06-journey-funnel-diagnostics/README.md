# Activity 06 — Journey and Funnel Diagnostics

LO3 · C386 · v1.0

# Goal

A synthetic monthly journey moves from landing sessions to enquiry, qualified lead and enrolment. The decision is where to investigate friction, using stage counts with consistent cohort and window definitions.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/funnel.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Use journey-events.csv to validate session-level ordered events in one synthetic cohort and30-day window;derive the aggregate stage counts,then compute conditional and overall rates. Raw aggregate counts alone do not establish a funnel.
Digital Marketing’s customer-experience framework is operationalised through journey stages,conditional rates and friction hypotheses rather than broad journey benefits.

# Worked calculation

Session->enquiry = 96/2400 = 4%; enquiry->qualified = 50%; qualified->enrolment = 25%; full funnel = 0.5%.

# Step-by-step

1. Read funnel.csv and mock-data/journey-events.csv. Confirm each event has a session_id,event_name,timestamp and cohort.
2. Write cohort, entity and window before calculating a rate.
3. Use Cowork Prompt 1 to create a rate table.
4. Verify all three conditional rates plus the overall 0.5%.
5. Run python3 validate.py to verify each later stage is a subset of the preceding stage and timestamp order is valid. Raw aggregate ratios alone are insufficient.
6. Ask Prompt 2 for tracking and customer-intent alternatives.
7. Define one follow-up event or interview question per hypothesis.
8. Save funnel analysis and hypothesis note under outputs.

# Prompt1

Analyse the synthetic funnel. Calculate conditional and overall rates with named denominators. Check cohort and time-window consistency. Propose two testable friction hypotheses, including a tracking explanation; do not assert causation.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Row-level journey-events.csv confirms2400 unique sessions,96 enquiries,48 qualified and12 enrolments;ordered stages share the same session IDs;rates 4%,50%,25%,0.5%;two alternate friction explanations.

# Failure and recovery

A month-end enrolment count is divided by a different month’s enquiries. Time-window mismatch invalidates the conversion rate.
State entity, cohort, order and window. Investigate consent and event completeness before changing creative. Distinguish correlation from causal diagnosis.

# Submit

funnel-analysis.csv and friction-hypotheses.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
