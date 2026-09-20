# Activity 12 — Bounded Demand Forecast

LO3 · C386 · v1.0

# Goal

Six synthetic monthly enquiry counts are used to forecast one month. Claude Code must compare a last-value baseline and three-month moving average, preserving seasonality and short-history uncertainty.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/demand.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Check regular intervals -> reserve test period -> compute naive baseline -> compare moving average -> record error -> state scenario range -> monitor change.
AI Strategy’s demand-analysis examples are adapted into baseline comparison,held-out error and campaign-change monitoring. Short-history model precision is explicitly bounded.

# Worked calculation

September last-value forecast=104; three-month mean=(96+100+104)/3=100. At August, rolling mean of May-July=93.33; absolute error=10.67.

# Step-by-step

1. Inspect demand.csv and identify the June campaign change.
2. Read assets/forecast-protocol.md and reserve August as holdout.
3. Ask Claude Code Prompt 1 to implement baseline and moving average.
4. Review that August is not used in its own predicted value.
5. Run the analysis or supplied validate.py.
6. Verify September 104 and 100; August MA error 10.67.
7. Write an assumption-based low/base/high scenario distinct from a statistical interval.
8. Save forecast CSV,script and assumptions note under outputs.

# Prompt1

Forecast one month from six synthetic observations. Compare last-value and three-month averages. Hold August out for evaluation before forecasting September. Do not fabricate confidence intervals. Report assumptions, errors and a monitoring trigger.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Naive 104; moving-average 100; August moving-average error 10.67; campaign shift and seasonality caveats.

# Failure and recovery

The agent fits an elaborate model to six points and reports a precise probability interval. The data do not support such precision.
Use simple baselines, avoid training on the held-out month, label scenario ranges as assumptions, and discuss campaign shifts plus missing annual seasonality.

# Submit

forecast.csv and forecast-assumptions.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
