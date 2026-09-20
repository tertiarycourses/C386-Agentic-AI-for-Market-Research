# Activity 03 — Competitor Triangulation

LO2 · C386 · v1.0

# Goal

The provider compares three fictional competitors. Advertised prices, course hours and learner-review counts must be normalised before Cowork can recommend a positioning gap.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/competitors.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Match comparable features, units and retrieval dates; distinguish vendor claim from independent evidence; triangulate one claim with two source types before promoting it.
Digital Marketing’s competitive positioning approach is operationalised as matched-offer normalisation and source triangulation; third-party AI-research vendor claims are not validation evidence.

# Worked calculation

Price per hour: 480/8 = $60; 720/16 = $45; 600/12 = $50. The cheapest total price is not the cheapest hourly offer.

# Step-by-step

1. Inspect competitors.csv and identify SGD, hours and review count units.
2. Read assets/offer-boundaries.md and list features excluded from price comparison.
3. Use Cowork on the copied folder and paste Prompt 1.
4. Request a competitor matrix with a calculated sgd_per_hour column.
5. Verify $60, $45 and $50 by hand or spreadsheet.
6. Ask Prompt 2 to challenge rating-based rankings using review volume.
7. Write one positioning hypothesis and the primary evidence needed to test it.
8. Save the matrix and positioning note under outputs.

# Prompt1

Compare these fictional competitors. Calculate SGD per hour, preserve claim_id and review_n, separate advertised facts from inferred positioning, and recommend one hypothesis to test rather than asserting market leadership.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Hourly prices 60,45,50; all three claim IDs cited; at least two uncertainty statements; no unsupported leadership claim.

# Failure and recovery

Cowork labels Harbour the market leader from a 4.8 rating based on eight reviews. Rating and evidence volume must be evaluated separately.
Record comparable offer boundaries and source date. Never claim fictional competitors exist. Preserve unknowns instead of filling gaps with plausible text.

# Submit

competitor-matrix.csv and positioning-note.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
