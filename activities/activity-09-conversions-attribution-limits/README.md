# Activity 09 — Conversions and Attribution Limits

LO4 · C386 · v1.0

# Goal

Four synthetic conversion journeys include paid search, organic search, email and direct visits. Comparing first and last touch illustrates attribution sensitivity without pretending to reproduce GA4 data-driven attribution.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/touchpoints.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Define eligible channels and lookback -> order touches -> choose allocation model -> reconcile totals -> compare sensitivity -> distinguish attribution from lift.
Current Google attribution documentation supports separating allocated credit from incrementality. First/last-touch examples are authored external models,not a reproduction of GA4’s data-driven model.

# Worked calculation

First-touch paid search revenue = $1200; last-touch = $0. Email receives $700 first-touch and $1300 last-touch. Model choice changes assigned credit.

# Step-by-step

1. Inspect touchpoints.csv and confirm four journey IDs.
2. Read assets/model-boundaries.md and define first/last touch.
3. Use Cowork Prompt 1 for channel allocations.
4. Verify each model sums to $2400.
5. Compare paid and email allocation changes.
6. Ask Prompt 2 to challenge a recommendation to cut paid search.
7. Describe one feasible lift experiment and its outcome metric.
8. Save comparison and limitations under outputs.

# Prompt1

Compare first-touch and last-touch attribution for four synthetic journeys. Reconcile each model to $2400. Explain why this does not implement GA4 data-driven attribution or estimate incremental lift. Propose a safer budget decision.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Both models reconcile to $2400; paid first-touch $1200; email last-touch $1300; no causal ROI claim.

# Failure and recovery

The agent cuts paid search because last-touch credit is zero. Assisted demand and incremental impact require separate investigation.
Use attribution for descriptive allocation; use controlled experiments or credible causal designs for incremental effects. Explicitly state identity, consent and lookback limitations.

# Submit

attribution-comparison.csv and model-limitations.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
