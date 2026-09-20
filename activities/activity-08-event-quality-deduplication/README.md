# Activity 08 — Event Quality and Deduplication

LO4 · C386 · v1.0

# Goal

A synthetic event export contains duplicate purchases and a missing transaction ID. Claude Code should create a reproducible audit without silently removing evidence or treating a CSV as a live GA4 test.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/events.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Parse schema -> isolate purchases -> validate transaction IDs -> group duplicates -> reconcile value -> emit accepted and quarantined rows -> human review.
AI Strategy’s analytics/automation discussion is adapted into a deterministic audit with raw-to-accepted reconciliation; automation must retain excluded rows and reasons.

# Worked calculation

Raw purchase value = 600+600+500+400 = $2100. Valid distinct transaction value = $1100; duplicate $600 and missing-ID $400 are quarantined.

# Step-by-step

1. Inspect all five rows and mark purchase versus lead events.
2. Read assets/audit-rules.md; record identity and currency rules.
3. Launch Claude Code from the working copy and ask for a plan before code changes.
4. Use Prompt 1 to request an audit script reading only mock-data/events.csv.
5. Review the code for transaction_id grouping and missing-ID quarantine.
6. Run the generated script locally or use the supplied validate.py baseline.
7. Verify $2100 raw,$600 duplicate,$400 missing-ID,$1100 accepted.
8. Save script, audit CSV and reconciliation note under outputs.

# Prompt1

Audit synthetic events.csv. Keep raw inputs unchanged. Identify duplicate transaction IDs and missing purchase IDs. Produce row-level reasons and reconcile raw $2100 to valid distinct $1100. Do not deduplicate by value or claim a live GA4 test.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Five raw rows retained in audit; T001 counted once; T002 once; E04 missing-ID; accepted value $1100.

# Failure and recovery

Deduplicating by value removes two different $600 orders. Transaction identity, not price equality, determines duplication.
Keep raw exports immutable, log rejection reasons, validate currency before summing, and make deduplication rules explicit. This dataset does not test actual GA4 deduplication.

# Submit

event-audit.csv and reconciliation.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
