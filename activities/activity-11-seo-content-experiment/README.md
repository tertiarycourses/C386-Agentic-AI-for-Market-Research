# Activity 11 — SEO Content Experiment

LO2 · C386 · v1.0

# Goal

A synthetic search-content export tracks impressions, clicks and enquiries. Cowork should cluster intent and propose an experiment, using observed rate information without claiming an invented search ranking or guaranteed AI visibility.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/search-content.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Normalise query -> classify intent -> map page/claim -> calculate CTR and enquiry rates -> isolate one content change -> define control/window -> assess uncertainty.
Digital Marketing’s SEO/SEM concepts and Coupler’s intent-to-content workflow are adapted into commercial-intent hypotheses and a controlled content brief. No ranking or AI-visibility guarantee is taught.

# Worked calculation

CTR = clicks/impressions. Training query: 48/800=6%; enquiry/click = 6/48=12.5%. High impression volume alone does not establish useful demand.

# Step-by-step

1. Inspect search-content.csv and distinguish impressions,clicks,enquiries.
2. Read assets/content-brief.md and approved-claims.csv.
3. Ask Cowork Prompt 1 for an intent and rate table.
4. Verify four CTRs and the training query’s 12.5% enquiry/click rate.
5. Choose one landing-page claim or CTA change tied to commercial intent.
6. Define baseline,control,outcome,window and stop rule.
7. Ask Prompt 2 to list seasonality and traffic-composition confounders.
8. Save intent map and experiment brief; label as a proposed test.

# Prompt1

Analyse the synthetic search export, calculate CTR and enquiry-per-click, cluster intent, and propose one controlled content experiment. Use approved claims only. State confounders and avoid promising rankings or AI visibility.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

CTRs 4%,3%,6%,3%; training enquiry/click 12.5%; one isolated change and explicit confounder.

# Failure and recovery

A content plan targets the highest-impression query and ignores enquiry quality. Optimise against the decision metric rather than raw reach.
Avoid keyword stuffing and unsupported claims. Record source date, search geography and device where available. Seasonal and ranking changes can confound before/after comparisons.

# Submit

intent-map.csv and experiment-brief.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
