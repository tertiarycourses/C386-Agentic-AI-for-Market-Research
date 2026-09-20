# Activity 05 — Segments and Customer Value

LO3 · C386 · v1.0

# Goal

A fictional programme has working professionals and career switchers. Behavioural segments should guide research questions and consented messaging, with customer value calculated using explicit margin and retention assumptions.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/segments.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Choose observable non-sensitive variables, compute group sizes and values, validate distinct needs with evidence, avoid assigning personas beyond available data.
Digital Marketing’s consumer-behaviour and relationship framework is adapted into observed segment value plus testable needs. Generated personas are hypotheses only; no demographic identity is inferred from behaviour.

# Worked calculation

Working margin/customer = (24000-12000)/40 = $300. Simple one-period retained margin estimate = $300 × 0.7 = $210; not lifetime value.

# Step-by-step

1. Inspect segment sizes and reconcile total to 80 customers.
2. Read assets/persona-template.md and identify observation versus hypothesis fields.
3. Ask Cowork Prompt 1 for a segment-value table.
4. Calculate contribution margin independently for each row.
5. Confirm $300,$200,$500 unit margins and distinguish total value from unit value.
6. Draft two validation questions per segment; avoid leading questions.
7. Apply Prompt 2 to remove unsupported demographic assumptions.
8. Save the table and persona hypotheses under outputs.

# Prompt1

Analyse synthetic segments.csv. Calculate customers and contribution margin per customer. Create evidence-constrained persona hypotheses using only observed fields. Do not invent age, gender or income. Label retention assumptions and propose validation questions.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Margins/customer 300,200,500; total customers 80; no invented demographic traits; retained-margin assumptions explicit.

# Failure and recovery

The agent invents an age range and income for each segment. Neither field exists; the persona must remain evidence-constrained.
Use behavioural attributes and minimum group size for reporting; label retention as an assumption; suppress identifying small-group combinations.

# Submit

segment-value.csv and persona-hypotheses.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
