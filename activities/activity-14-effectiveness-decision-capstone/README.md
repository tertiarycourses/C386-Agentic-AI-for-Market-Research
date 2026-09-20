# Activity 14 — Effectiveness Decision Capstone

LO4 · C386 · v1.0

# Goal

A synthetic cross-channel campaign has spend, leads and revenue. Teams combine Cowork evidence synthesis and Claude Code calculations into a budget recommendation with attribution sensitivity, margin boundaries and a human approval record.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/campaigns.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Reconcile inputs -> compute denominator-aware metrics -> apply margin -> inspect attribution -> challenge confounders -> recommend bounded test -> human approve -> monitor.
Digital Marketing’s strategy evaluation is operationalised as denominator-aware metrics,margin reconciliation and a capped human-approved experiment. Vendor tool lists are capability prompts,not measured evidence of business improvement.

# Worked calculation

Paid CPL=$1200/30=$40; revenue ROAS=2; contribution after spend=$2400×0.5-$1200=$0. ROAS is not profit or causal ROI.

# Step-by-step

1. Inspect campaigns.csv and reconcile leads96,spend2100,revenue6000.
2. Read assets/decision-template.md and margin-boundaries.md.
3. Ask Claude Code Prompt 1 for deterministic calculations; review before running.
4. Verify paid CPL40,ROAS2,contribution0 and total contribution900.
5. Use Cowork to synthesise calculations with evidence from prior activities.
6. Ask Prompt 2 to red-team profitability,attribution and privacy claims.
7. Design a capped experiment with metric,control,window,stop rule and owner.
8. Save report,budget test and approval record showing human approval pending.

# Prompt1

Create an evidence-linked effectiveness report from synthetic campaigns.csv and earlier activity outputs. Calculate CPL, revenue ROAS and contribution after listed spend. Explain attribution and causal limits. Recommend a capped test; keep approval pending and do not change or publish campaigns.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

96 leads; spend $2100; revenue $6000; contribution $900; paid CPL40 and contribution0; human approval pending.

# Failure and recovery

The report calls paid search profitable because ROAS is 2. At a 50% gross margin, contribution after media spend is zero before other costs.
State attribution model, accounting coverage and consent limitations. Cap recommendations to a test budget and require human sign-off before publishing or changing campaigns.

# Submit

effectiveness-report.md,budget-test.csv and approval-record.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
