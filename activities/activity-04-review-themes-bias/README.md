# Activity 04 — Review Themes and Bias

LO2 · C386 · v1.0

# Goal

Eight fictional course reviews mention timing, relevance and support. An agent must code textual evidence without inventing customer identities or treating volunteered reviews as a representative survey.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/reviews.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Define codebook -> quote evidence -> assign theme -> review disagreement -> count -> qualify interpretation. Keep negation and mixed sentiment visible.
Columbia research cautions that generated respondents may compress response variation and exhibit prompt sensitivity. These real-text synthetic training rows test coding mechanics; synthetic personas cannot replace a target-population sample.

# Worked calculation

Timing mentions = 3/8 = 37.5%; relevance = 3/8; support = 2/8. These are coded mentions, not sentiment scores or market prevalence.

# Step-by-step

1. Read reviews.csv and assets/codebook.md without inspecting theme_reference as an answer shortcut.
2. Copy the text and IDs to a working CSV; keep theme_reference only for later verification.
3. Ask Cowork Prompt 1 for evidence-linked coding.
4. Review R06 negation and R08 mixed wording manually.
5. Calculate theme counts from the coded rows and confirm total equals eight.
6. Compare results with the reference categories; document disagreements.
7. Use Prompt 2 to explain volunteer-review selection bias.
8. Save coded data and a bounded theme memo in outputs.

# Prompt1

Code the eight synthetic reviews using the supplied codebook. Preserve review_id, include a short evidence quote, theme and mixed-sentiment flag. Explain selection bias. Do not infer demographics or invent additional reviews.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Eight review IDs retained; 3 timing,3 relevance,2 support; R08 mixed qualifier; selection-bias limitation.

# Failure and recovery

R08 is flattened into positive sentiment although it says the exercises were rushed. Mixed sentiment needs a separate qualifier.
Use short de-identified extracts; maintain row-level auditability; have a human review ambiguous assignments; do not infer protected characteristics.

# Submit

coded-reviews.csv and theme-memo.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
