# Activity 01 — Evidence Registry

LO1 · C386 · v1.0

# Goal

A Singapore learning provider must decide whether to launch an evening AI marketing programme. A search summary is insufficient: each demand claim needs a source, date, population and permission record.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/sources.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Classify primary/secondary and qualitative/quantitative sources; record first-party origin, time window and consent; separate direct observations from interpretations.
Digital Marketing’s research/strategy framing is adapted here into a decision-population-source contract: customer,competitor,market and performance evidence remain separate. Agent synthesis is checked against original source rows.

# Worked calculation

Evening preference = 72 / 120 = 60%; denominator is surveyed existing learners, not the Singapore market.

# Step-by-step

1. Open mock-data/sources.csv and count four records excluding the header.
2. Read assets/decision-brief.md and write the decision, population and time horizon in your working note.
3. Create a new Cowork task using only a copied activity folder; inspect the proposed read/write scope before approving.
4. Paste Prompt 1 from prompts.pdf; request the register in outputs/evidence-register.csv.
5. Check that S01-S04 all appear exactly once and that no invented source is present.
6. Calculate 72/120 and 36/80 independently in a spreadsheet; label both denominators.
7. Ask Prompt 2 to challenge the strongest demand claim and identify missing evidence.
8. Save outputs/research-brief.md with a recommendation to collect target-population evidence.

# Prompt1

Create an evidence register from sources.csv. Preserve every source_id. Separate observation, inference and recommendation. State each denominator and date. Do not generalise these synthetic observations to the Singapore market.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Four uniquely identified sources; each claim states population, period, confidence and an explicit limitation.

# Failure and recovery

A global report is used to claim Singapore buying intent. Its population and date do not match the decision, so the claim must be downgraded.
Retain provenance, access permission and citation per claim. Use anonymised exports; never include emails, phone numbers or credentials in the research workspace.

# Submit

evidence-register.csv and research-brief.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
