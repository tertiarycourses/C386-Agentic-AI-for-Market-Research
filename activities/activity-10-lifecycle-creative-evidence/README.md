# Activity 10 — Lifecycle Creative from Evidence

LO3 · C386 · v1.0

# Goal

A fictional email campaign targets enquiry and enrolled segments. Cowork must adapt evidence-backed messages to a brand brief while preserving consent rules, avoiding fabricated urgency and producing drafts for human review.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/lifecycle.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

Evidence brief -> segment need -> approved claim -> channel/consent constraint -> draft variant -> human brand review -> measurement hypothesis.
Digital Marketing’s email and relationship concepts plus Customer.io’s marketer examples are adapted into segment-specific claims,consent-aware drafts and a human-review status. The course does not adopt older vendor FAQs as current connector mechanics.

# Worked calculation

Click rate uses sent: 16/80=20%,12/40=30%,18/90=20%. Enrolment per sent: 5%,15%,10%; no claim of incremental email impact.

# Step-by-step

1. Read lifecycle.csv,assets/brand-guide.md and assets/approved-claims.csv.
2. Confirm eligible and sent represent different denominators.
3. Ask Cowork Prompt 1 for three evidence-linked drafts.
4. Calculate click and enrolment-per-sent rates.
5. Check each draft against approved CL01-CL03 claims.
6. Remove unsupported scarcity, promises and invented testimonials.
7. Use Prompt 2 to critique tone, consent and opt-out requirements.
8. Save drafts and review checklist; do not connect a sending account.

# Prompt1

Create lifecycle email drafts for three synthetic segments using approved brand and claim assets. Include claim_ids, rationale, CTA and human-review status. Do not send or invent scarcity. Calculate rates using sent, with non-causal interpretation.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Three segment drafts; claim IDs and CTA; no invented scarcity; send_authorised false; rates use sent.

# Failure and recovery

A draft says only two seats remain without inventory evidence. The urgency claim must be removed or verified by an authorised source.
Draft only; no send authorisation. Use approved factual claims, consented audiences, clear opt-out and reviewer sign-off. Avoid interpreting synthetic clicks as causal lift.

# Submit

message-variants.md and review-checklist.csv
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
