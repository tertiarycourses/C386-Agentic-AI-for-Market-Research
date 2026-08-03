# Lab 5 — Build the Evidence-Based Prospect Segmentation Queue

**Course:** Agentic AI for Linkedin Marketing (C386)  
**Version:** v1.0 (3 August 2026)  
**Topic 3:** Lead Generation and Outreach with AI Agents  
**Maps to:** LO4: Apply transparent fit, evidence, relationship, timing, and risk rules to authorised synthetic prospect records without scraping or sensitive inference.  
**Tools:** Approved AI assistant, spreadsheet or text editor, supplied synthetic prospect CSV and earlier foundation  
**Duration:** 50 minutes

---

## Goal

LO4: Apply transparent fit, evidence, relationship, timing, and risk rules to authorised synthetic prospect records without scraping or sensitive inference.

## What You Will Do

You define what a relevant prospect looks like, inspect the supplied synthetic records, and build an explainable decision table. The agent may summarise and apply the rule, but it must preserve provenance, label uncertainty, avoid sensitive inference, and never access LinkedIn or enrich a record automatically.

## What You Will Build

C386-linkedin-pack/05-prospect-segmentation-queue.md with ideal-customer criteria, data dictionary, evidence register, scoring rule, segmented queue, quality checks, exclusions, and human-review log.

## Prerequisites

- Complete Labs 1-4 and retain the audience definition, business result, value proposition, voice, and approval status rules.
- Open labs/resources/northstar-prospect-scenarios.csv; it contains synthetic records only.
- Do not search for the fictional names online or substitute real LinkedIn profile information.

> **Data note.** Use only the supplied synthetic case files and an approved AI assistant. Do not scrape LinkedIn, use unauthorised bots or browser extensions, mass-send invitations or messages, publish automatically, or paste credentials or real personal data into prompts.

## Steps

**1. Create 05-prospect-segmentation-queue.md with sections for Ideal-Customer Criteria, Data Dictionary, Evidence Register, Decision Rule, Queue, Exclusions, Quality Checks, and Human Review.**

```text
File: C386-linkedin-pack/05-prospect-segmentation-queue.md
```

**2. Define five inclusion criteria from the foundation: organisation context, role relevance, evidence of a matching operational need, relationship path, and timing. Define disqualifiers and fields that must never be inferred.**

```text
Never infer: age, ethnicity, religion, health, political opinion, family status, or any other sensitive characteristic.
```

**3. Create the data dictionary for prospect_id, organisation_type, role_context, stated_need, relationship_context, source_id, source_date, consent_or_contact_basis, confidence, risk_flag, and owner_note.**

```text
For each field record: definition | allowed source | valid values | missing-value treatment | owner.
```

**4. Inspect the CSV without AI. Confirm row count, unique prospect IDs, required fields, valid source IDs, dates, and explicit do-not-contact or privacy flags. Record missing, duplicate, contradictory, and stale values.**

```text
Quality results: COMPLETE / MISSING / DUPLICATE / CONTRADICTORY / STALE / OWNER TO VERIFY.
```

**5. Design an explainable rule that produces PRIORITISE, NURTURE, HOLD, or DO NOT CONTACT. High fit cannot override a do-not-contact flag, unacceptable risk, missing contact basis, or weak evidence.**

```text
Decision order: hard stop -> evidence quality -> fit -> relationship context -> timing -> owner review.
DO NOT CONTACT = explicit stop.
HOLD = missing or stale basis/evidence, contradiction, sensitive context, or channel mismatch needs owner resolution.
PRIORITISE = all five inclusion criteria supported and no disqualifier.
NURTURE = legitimate basis exists, no hard stop exists, but fit or timing is incomplete; only non-outreach learning or an owner-approved future draft may follow.
```

**6. Ask the AI to apply the rule to the pasted synthetic rows. Require a row-by-row rationale that cites the input fields and forbids enrichment, sensitive inference, invented events, and invented familiarity. For every row, return an allowed next step; a reason to engage is permitted only for PRIORITISE or NURTURE.**

```text
Return columns: prospect_id | decision | evidence used | confidence | missing information | risk | allowed next step | reason-to-engage draft | required human decision. For HOLD or DO NOT CONTACT, set reason-to-engage draft to NOT PERMITTED and preserve the safe state. Use only the pasted rows.
```

**7. Compare the AI result with the rule manually. Correct any row where the rationale does not match the inputs, uncertainty is hidden, or a hard stop was overridden.**

```text
Record: expected decision | observed decision | mismatch cause | correction | contract change.
```

**8. Write one factual reason-to-engage for each PRIORITISE or NURTURE row. It must name a relevant professional context and potential value without pretending a relationship or promising an outcome.**

```text
Pattern: Based on <VERIFIED CONTEXT>, a useful conversation could explore <RELEVANT QUESTION OR VALUE>; <UNKNOWN> remains to be confirmed.
```

**9. Add the Human Review queue. The owner confirms identity, current context, contact basis, relevance, and do-not-contact state before deciding whether any future outreach draft is appropriate.**

```text
Statuses: READY FOR MESSAGE DRAFT | HOLD - VERIFY | DO NOT CONTACT. This lab sends nothing.
```

## Test It

Open 05-prospect-segmentation-queue.md. It must define all eleven fields, contain a quality result for every synthetic record, preserve all hard stops, and give every decision a field-level rationale. Apply the written rule manually to the fixed fixtures P-001 (PRIORITISE), P-004 (NURTURE), P-003 (HOLD), and P-007 (DO NOT CONTACT); the same inputs must produce those decisions. HOLD and DO NOT CONTACT must show reason-to-engage as NOT PERMITTED, and no row may contain scraped, enriched, real, or sensitive information.

## Checkpoint for the Next Lab

Keep the reviewed queue. Lab 6 uses only rows marked READY FOR MESSAGE DRAFT and preserves HOLD and DO NOT CONTACT without generating communication for them.

## Troubleshooting

- **The agent prioritises every senior role:** Remove seniority as a shortcut and require relevant need, evidence quality, contact basis, relationship context, timing, and hard-stop checks.
- **The rationale adds details not in the CSV:** Delete the detail, mark the field UNKNOWN, and strengthen the instruction that only pasted rows may be used.
- **A do-not-contact row appears in the draft queue:** Move hard stops to the first decision stage and re-run all rows; record the control failure in the review log.

## Optional Challenge (+10 minutes, outside core duration)

Perform a sensitivity check: change one non-sensitive evidence field on two synthetic rows and show whether the decision changes in the expected and explainable way. Save the result in the numbered lab output.

## Reflection

Which missing field most affects the fairness and relevance of the segmentation decision, and why should the workflow hold rather than infer it? Record your answer in the numbered lab output.

---

[← Lab 4](lab-04-build-the-fourteen-day-content-calendar-and-draft-first-workflow.md) · [Lab 6 →](lab-06-draft-the-personalised-connection-and-nurture-sequence.md)
