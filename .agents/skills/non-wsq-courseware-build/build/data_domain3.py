"""Topic 3 - prospecting, segmentation, outreach, and nurture."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Build the Evidence-Based Prospect Segmentation Queue",
        objective="LO4: Apply transparent fit, evidence, relationship, timing, and risk rules to authorised synthetic prospect records without scraping or sensitive inference.",
        desc=(
            "You define what a relevant prospect looks like, inspect the supplied synthetic records, and build an explainable decision table. "
            "The agent may summarise and apply the rule, but it must preserve provenance, label uncertainty, avoid sensitive inference, and never access LinkedIn or enrich a record automatically."
        ),
        build="C386-linkedin-pack/05-prospect-segmentation-queue.md with ideal-customer criteria, data dictionary, evidence register, scoring rule, segmented queue, quality checks, exclusions, and human-review log.",
        services="Approved AI assistant, spreadsheet or text editor, supplied synthetic prospect CSV and earlier foundation",
        duration="50 minutes",
        prerequisites=[
            "Complete Labs 1-4 and retain the audience definition, business result, value proposition, voice, and approval status rules.",
            "Open labs/resources/northstar-prospect-scenarios.csv; it contains synthetic records only.",
            "Do not search for the fictional names online or substitute real LinkedIn profile information.",
        ],
        steps=[
            ("Create 05-prospect-segmentation-queue.md with sections for Ideal-Customer Criteria, Data Dictionary, Evidence Register, Decision Rule, Queue, Exclusions, Quality Checks, and Human Review.", "File: C386-linkedin-pack/05-prospect-segmentation-queue.md"),
            ("Define five inclusion criteria from the foundation: organisation context, role relevance, evidence of a matching operational need, relationship path, and timing. Define disqualifiers and fields that must never be inferred.", "Never infer: age, ethnicity, religion, health, political opinion, family status, or any other sensitive characteristic."),
            ("Create the data dictionary for prospect_id, organisation_type, role_context, stated_need, relationship_context, source_id, source_date, consent_or_contact_basis, confidence, risk_flag, and owner_note.", "For each field record: definition | allowed source | valid values | missing-value treatment | owner."),
            ("Inspect the CSV without AI. Confirm row count, unique prospect IDs, required fields, valid source IDs, dates, and explicit do-not-contact or privacy flags. Record missing, duplicate, contradictory, and stale values.", "Quality results: COMPLETE / MISSING / DUPLICATE / CONTRADICTORY / STALE / OWNER TO VERIFY."),
            ("Design an explainable rule that produces PRIORITISE, NURTURE, HOLD, or DO NOT CONTACT. High fit cannot override a do-not-contact flag, unacceptable risk, missing contact basis, or weak evidence.", "Decision order: hard stop -> evidence quality -> fit -> relationship context -> timing -> owner review.\nDO NOT CONTACT = explicit stop.\nHOLD = missing or stale basis/evidence, contradiction, sensitive context, or channel mismatch needs owner resolution.\nPRIORITISE = all five inclusion criteria supported and no disqualifier.\nNURTURE = legitimate basis exists, no hard stop exists, but fit or timing is incomplete; only non-outreach learning or an owner-approved future draft may follow."),
            ("Ask the AI to apply the rule to the pasted synthetic rows. Require a row-by-row rationale that cites the input fields and forbids enrichment, sensitive inference, invented events, and invented familiarity. For every row, return an allowed next step; a reason to engage is permitted only for PRIORITISE or NURTURE.", "Return columns: prospect_id | decision | evidence used | confidence | missing information | risk | allowed next step | reason-to-engage draft | required human decision. For HOLD or DO NOT CONTACT, set reason-to-engage draft to NOT PERMITTED and preserve the safe state. Use only the pasted rows."),
            ("Compare the AI result with the rule manually. Correct any row where the rationale does not match the inputs, uncertainty is hidden, or a hard stop was overridden.", "Record: expected decision | observed decision | mismatch cause | correction | contract change."),
            ("Write one factual reason-to-engage for each PRIORITISE or NURTURE row. It must name a relevant professional context and potential value without pretending a relationship or promising an outcome.", "Pattern: Based on <VERIFIED CONTEXT>, a useful conversation could explore <RELEVANT QUESTION OR VALUE>; <UNKNOWN> remains to be confirmed."),
            ("Add the Human Review queue. The owner confirms identity, current context, contact basis, relevance, and do-not-contact state before deciding whether any future outreach draft is appropriate.", "Statuses: READY FOR MESSAGE DRAFT | HOLD - VERIFY | DO NOT CONTACT. This lab sends nothing."),
        ],
        slide_steps=[
            ("Define ideal-customer criteria, authorised fields, hard stops, and an explainable decision order before asking AI to segment anything.", "HARD STOP -> EVIDENCE -> FIT -> CONTEXT -> TIMING"),
            ("Apply the rule to synthetic records, validate every decision, and hand only relevant, verified rows to a human-reviewed message-drafting queue.", "PRIORITISE / NURTURE / HOLD / DO NOT CONTACT"),
        ],
        test=(
            "Open 05-prospect-segmentation-queue.md. It must define all eleven fields, contain a quality result for every synthetic record, preserve all hard stops, and give every decision a field-level rationale. "
            "Apply the written rule manually to the fixed fixtures P-001 (PRIORITISE), P-004 (NURTURE), P-003 (HOLD), and P-007 (DO NOT CONTACT); the same inputs must produce those decisions. HOLD and DO NOT CONTACT must show reason-to-engage as NOT PERMITTED, and no row may contain scraped, enriched, real, or sensitive information."
        ),
        checkpoint="Keep the reviewed queue. Lab 6 uses only rows marked READY FOR MESSAGE DRAFT and preserves HOLD and DO NOT CONTACT without generating communication for them.",
        troubleshooting=[
            ("The agent prioritises every senior role", "Remove seniority as a shortcut and require relevant need, evidence quality, contact basis, relationship context, timing, and hard-stop checks."),
            ("The rationale adds details not in the CSV", "Delete the detail, mark the field UNKNOWN, and strengthen the instruction that only pasted rows may be used."),
            ("A do-not-contact row appears in the draft queue", "Move hard stops to the first decision stage and re-run all rows; record the control failure in the review log."),
        ],
        challenge="Perform a sensitivity check: change one non-sensitive evidence field on two synthetic rows and show whether the decision changes in the expected and explainable way.",
        reflection="Which missing field most affects the fairness and relevance of the segmentation decision, and why should the workflow hold rather than infer it?",
    ),
    dict(
        num=6,
        topic=3,
        title="Draft the Personalised Connection and Nurture Sequence",
        objective="LO4, LO5: Create concise, relevant, evidence-linked outreach drafts with etiquette rules, stop conditions, privacy protection, and human sending authority.",
        desc=(
            "You turn approved synthetic queue records into a bounded communication sequence. "
            "Each draft uses verified context, adds distinct value, avoids false familiarity and pressure, and stops on no response, decline, uncertainty, privacy concern, or relationship risk."
        ),
        build="C386-linkedin-pack/06-outreach-and-nurture-sequence.md with invitation, welcome, value, and handoff drafts for approved synthetic segments; an evidence map; message checks; stop conditions; and a send-decision log.",
        services="Approved AI assistant, text editor, Lab 5 queue and supplied synthetic message scenarios",
        duration="55 minutes",
        prerequisites=[
            "Complete Lab 5 and use only rows marked READY FOR MESSAGE DRAFT.",
            "Open labs/resources/northstar-message-scenarios.csv.",
            "No connection request or message will be sent; the exercise ends with a human decision record.",
        ],
        steps=[
            ("Create 06-outreach-and-nurture-sequence.md with sections for Sequence Rules, Segment Message Map, Drafts, Evidence Map, Etiquette Checks, Stop Conditions, Escalation, and Send-Decision Log.", "File: C386-linkedin-pack/06-outreach-and-nurture-sequence.md"),
            ("Write the sequence purpose and non-goals. The purpose is to begin a relevant professional conversation; non-goals include maximising volume, evading platform limits, creating urgency, disguising commercial intent, or sending without owner review.", "Operating principle: relevance and recipient agency are guardrails, not variables to optimise away."),
            ("Define the relevance ladder: correct identity, verified context, professional reason, useful value, low-friction next step. State the evidence required at each rung and the fallback when it is missing.", "Fallback: omit the detail, ask a neutral question, hold the draft, or stop - never invent."),
            ("For two READY rows, ask the AI to draft a concise connection invitation. Require a plain-language reason to connect, no fabricated praise, no unsupported claim, no hard pitch, and an output count for characters so the owner can check the current product limit.", "Exact limits can change. The owner verifies the current LinkedIn interface before use; the draft must remain concise regardless of the maximum."),
            ("Draft a welcome message for use only after a connection is genuinely accepted. It should acknowledge the context, offer one useful idea or question, and avoid immediately asking for a meeting.", "Status: DRAFT FOR USE ONLY AFTER VERIFIED ACCEPTANCE."),
            ("Draft one value-adding follow-up and one optional conversation handoff. Each must contribute new value, preserve the evidence map, and make no assumption that the recipient read or agreed with an earlier message.", "No response is not consent or interest. Do not send repeated variants to overcome silence."),
            ("Apply the sequence to the seven fixed supplied scenarios. Record a safe state separately from any escalation action so a privacy, dispute, or sensitive request cannot remain active while waiting for an owner.", "Return columns: scenario_id | safe state DRAFT RESPONSE / WAIT / STOP | escalation action NONE / ESCALATE TO <OWNER> | reason | owner | evidence preserved. MS-05 must be STOP plus ESCALATE TO PRIVACY OWNER; no further use of that record is permitted."),
            ("Run the etiquette and privacy checks: recognisable sender, verified context, truthful intent, proportionate ask, no sensitive inference, no confidential data, no manipulation, easy decline, limited sequence, and named escalation.", "Any failed check sets the message to STOP or RETURN FOR REVISION."),
            ("Complete the Send-Decision Log for each draft. The human owner records recipient verification, context freshness, wording edits, current platform guidance check, decision, and reason. End the lab without sending.", "| Draft ID | Recipient verified | Context current | Current guidance checked | Owner edit | Decision | Reason |"),
        ],
        slide_steps=[
            ("Build each draft up the relevance ladder using only verified identity and context, a professional reason, useful value, and a low-friction next step.", "IDENTITY -> CONTEXT -> REASON -> VALUE -> NEXT STEP"),
            ("Route every scenario through etiquette, privacy, stop, and escalation rules; a human verifies the recipient and decides whether a draft is ever sent.", "DRAFT RESPONSE / WAIT / STOP / ESCALATE"),
        ],
        test=(
            "Open 06-outreach-and-nurture-sequence.md. Each approved segment must have an invitation, post-acceptance welcome, value follow-up, and optional handoff with a complete evidence map. "
            "All seven fixed scenarios MS-01 through MS-07 must have a safe state plus a separate escalation action, reason, and owner. MS-05 must be STOP plus ESCALATE TO PRIVACY OWNER; declined, deletion, disputed, sensitive, and silent cases must not continue automatically. The Send-Decision Log must show no message was sent in the lab."
        ),
        checkpoint="Keep the approved drafts, routing rules, and decision log. Lab 7 combines the content and engagement artefacts into one draft-first operations workflow with a consistent approval packet.",
        troubleshooting=[
            ("The invitation invents a shared interest", "Remove the statement, return to the evidence map, and use a modest verified context or hold the draft."),
            ("Every follow-up repeats the same request", "Give each touch a distinct audience value or question and stop the sequence when no new value exists."),
            ("A privacy request receives a marketing reply", "Set STOP, preserve the original request, avoid further use of the record, and escalate to the named privacy owner."),
        ],
        challenge="Write two versions of the value follow-up for different readiness states and explain why the next action changes while the evidence and etiquette rules do not.",
        reflection="What is the earliest signal that a relevant sequence has become unwanted pressure, and how should the workflow respond?",
    ),
]
