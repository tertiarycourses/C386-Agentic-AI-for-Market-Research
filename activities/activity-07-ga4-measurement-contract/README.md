# Activity 07 — GA4 Measurement Contract

LO4 · C386 · v1.0

# Goal

A marketing team needs GA4-compatible event definitions for course discovery, lead submission and purchase. Cowork can draft the measurement contract, but event collection and consent remain implementation responsibilities.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/measurement-plan.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Business question -> event trigger -> recommended event -> parameter schema -> consent -> validation evidence -> key-event designation. Avoid treating button clicks as successful submissions.
The legacy GA4 deck supplies the event-driven measurement coverage floor. Current Google event semantics govern names,parameters,key events and implementation evidence.

# Worked calculation

Contract completeness = 4 defined triggers / 4 events = 100%; it does not establish live tracking coverage.

# Step-by-step

1. Read measurement-plan.csv and assets/event-contract-template.md.
2. Open the official GA4 recommended-events reference linked in sources.md.
3. Compare generate_lead and purchase semantics with the proposed triggers.
4. Ask Cowork Prompt 1 to draft the contract.
5. Add transaction_id,currency,value and items to purchase requirements.
6. Check every event parameter for personal information; remove direct identifiers.
7. Write what evidence would prove an event arrived in a permitted test property.
8. Save the contract and consent notes; label implementation not executed.

# Prompt1

Review the synthetic measurement plan against GA4 recommended event semantics. Produce a business-question-to-event contract. Distinguish a successful lead from a button click. Include consent and no-PII controls; do not claim live implementation.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Four events with unambiguous success triggers; purchase transaction_id,currency,value,items; no personal-data parameters.

# Failure and recovery

generate_lead fires when a form button is pressed even if validation fails. The event trigger must be confirmed successful submission.
Use recommended event semantics and current official documentation. Never send names, emails or phone numbers as analytics parameters. Collection is gated by the organisation’s consent policy.

# Submit

measurement-contract.csv and consent-notes.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
