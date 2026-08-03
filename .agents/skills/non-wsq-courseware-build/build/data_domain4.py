"""Topic 4 - governed operations, analytics, and responsible scale."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Design the Governed Content and Engagement Operations Workflow",
        objective="LO5: Design a traceable draft-first workflow for content, comments, and follow-ups with explicit states, approvals, exceptions, and authorised external-action boundaries.",
        desc=(
            "You connect the earlier content calendar, prospect rules, and outreach drafts into one operations workflow. "
            "The agent prepares and checks internal artefacts; human owners retain profile identity, publishing, invitations, messages, relationship judgement, and incident correction."
        ),
        build="C386-linkedin-pack/07-governed-operations-workflow.md containing the workflow map, state machine, role and permission matrix, approval packets, engagement router, exception paths, trace schema, and simulation results.",
        services="Approved AI assistant, text editor or diagram tool, Labs 1-6 outputs and supplied engagement scenarios",
        duration="45 minutes",
        prerequisites=[
            "Complete Labs 1-6 and retain the latest approved foundation, prompt contract, calendar, prospect queue, and outreach rules.",
            "Open labs/resources/northstar-engagement-scenarios.csv.",
            "Use a diagram or Markdown table; no live account, credential, bot, extension, or external integration is required.",
        ],
        steps=[
            ("Create 07-governed-operations-workflow.md with sections for Scope, Workflow Map, States, Roles and Permissions, Approval Packets, Engagement Router, Exceptions, Trace Record, and Simulation.", "File: C386-linkedin-pack/07-governed-operations-workflow.md"),
            ("State the workflow boundary. In scope: approved-source intake, validation, internal drafting, quality checks, prioritisation, review packets, recommendations, and learning records. Out of scope: scraping, unauthorised access, automated engagement, automatic invitations or messages, credential handling, and unreviewed publication.", "External-action rule: use only current LinkedIn features or organisation-approved integrations after a named human decision."),
            ("Draw the canonical state flow: INTAKE, VALIDATE, DRAFT, CHECK, READY FOR HUMAN REVIEW, READY FOR HUMAN ACTION, HUMAN ACTION, OBSERVE, LEARNING CAPTURED. Add RETURN FOR REVISION, HOLD, and STOP branches; record ESCALATE TO <OWNER> as an action attached to a safe state, not as a competing state.", "No transition may move from DRAFT or CHECK directly to READY FOR HUMAN ACTION or HUMAN ACTION. Only a named human decision can set READY FOR HUMAN ACTION."),
            ("Create the role and permission matrix for Requester, Agent, Brand Owner, Fact Owner, Publisher, Relationship Owner, Privacy Owner, Commercial Owner, Legal Owner, and Operations Owner. Record read, draft, decide, act, correct, and audit rights.", "Separation: the agent cannot approve its own output; the Publisher cannot invent missing proof; the Relationship Owner handles recipient context; Commercial and Legal Owners decide within their named remit."),
            ("Define one approval packet schema shared by profile, content, and outreach work. Include goal, audience or recipient, exact draft, source map, model or prompt version, checks, unknowns, risk, proposed action, owner, decision, timestamp, and correction path.", "A reviewer should decide without reconstructing hidden chat context."),
            ("Build the engagement router for the supplied synthetic comments and messages. Classify praise, question, correction, complaint, commercial interest, privacy request, abuse, sensitive issue, and unknown; assign DRAFT RESPONSE, WAIT, or STOP as the safe state and record any ESCALATE TO <OWNER> action separately.", "The router drafts nothing for a row with insufficient context until the owner supplies it. Privacy and sensitive cases enter STOP before escalation."),
            ("Add operational exceptions: source unavailable, stale evidence, model output malformed, voice failure, policy concern, confidential detail, duplicate item, missed date, wrong recipient, negative response, and current interface change.", "Exception row: trigger | safe state | preserved evidence | owner | correction or rollback | restart condition."),
            ("Define the trace record for every run: run_id, artefact_id, input sources and versions, prompt version, model or tool, checks, reviewer, decision, action owner, external action if any, timestamp, outcome, exception, and next step.", "Keep secrets and message content out of the trace when a reference ID is sufficient."),
            ("Simulate the six fixed scenarios end to end: ready content, stale claim, voice mismatch, privacy request, interested reply, and request to auto-send. Record every state transition, final safe state, separate escalation action, and a before/after evidence row for each correction.", "Expected: ready content -> READY FOR HUMAN ACTION; stale claim -> HOLD; voice mismatch -> RETURN FOR REVISION; privacy request -> STOP + ESCALATE TO PRIVACY OWNER; interested reply -> READY FOR HUMAN ACTION; auto-send request -> STOP. No external action occurs.\n| Scenario | Before | After | Source or reason | Reviewer | Timestamp |"),
        ],
        slide_steps=[
            ("Separate internal preparation from external action with explicit states, role permissions, a complete review packet, and no path that bypasses human approval.", "INTAKE -> DRAFT -> CHECK -> HUMAN REVIEW -> HUMAN ACTION"),
            ("Route engagement and operational exceptions to a safe state, preserve evidence, name the owner, and log every decision for learning and correction.", "RESPOND / WAIT / REVISE / STOP / ESCALATE"),
        ],
        test=(
            "Open 07-governed-operations-workflow.md. Every main and exception state must have an entry rule, owner, allowed next states, and trace fields; no path may bypass human review. "
            "All six fixed simulations must finish in their stated expected safe state with a complete record and change-evidence row. READY FOR HUMAN ACTION must appear only after a named human decision; the request to auto-send must finish STOP without executing or simulating an external LinkedIn action."
        ),
        checkpoint="Keep the workflow and trace schema. Lab 8 uses them to validate performance data, diagnose the system, and log one bounded improvement recommendation.",
        troubleshooting=[
            ("The workflow diagram has arrows but no decisions", "Add entry criteria, owner, evidence, decision options, and failure path to every state transition."),
            ("The approval packet contains only the draft", "Add goal, audience, sources, versions, checks, unknowns, risk, proposed action, owner, and correction path."),
            ("The engagement router drafts a reply to every row", "Use DRAFT RESPONSE, WAIT, or STOP as the safe state; record any ESCALATE TO <OWNER> action separately. Require sufficient context and separate relationship, privacy, complaint, and sensitive cases."),
        ],
        challenge="Add a two-person review path for a high-reputation-risk post and show how disagreement, expiry, and correction are recorded.",
        reflection="Which workflow record would be most valuable after a public correction, and what must it contain to support accountability?",
    ),
    dict(
        num=8,
        topic=4,
        title="Diagnose Performance and Propose One Bounded Scaling Experiment",
        objective="LO6: Validate synthetic LinkedIn results, calculate defined metrics, diagnose the decision chain, and produce a human-reviewed improvement with guardrails and rollback.",
        desc=(
            "You analyse a supplied synthetic performance export without assuming that reach equals business value. "
            "You define each metric, check the data, compare like with like, identify the most plausible bottleneck, and recommend one controlled change that remains inside the governed workflow."
        ),
        build="C386-linkedin-pack/08-performance-diagnosis-and-improvement.md plus C386-linkedin-pack/08-cleaned-performance-metrics.csv containing definitions, quality log, calculations, funnel diagnosis, alternative explanations, experiment card, approval decision, cooldown, rollback, and course-pack manifest.",
        services="Spreadsheet application, approved AI assistant, supplied synthetic performance CSV and Labs 1-7 outputs",
        duration="55 minutes",
        prerequisites=[
            "Retain the Lab 1 decision chain and guardrails, the Lab 4 content metrics, and the Lab 7 canonical states, approval packet, and trace schema.",
            "Open labs/resources/northstar-linkedin-performance.csv.",
            "Use only the synthetic values; do not export or upload real member, message, or account data.",
        ],
        steps=[
            ("Create the analysis file and cleaned metric table. Use the exact CSV schema below so duplicate instances, comparison dimensions, dispositions, counts, rates, and caveats remain reviewable.", "Files: C386-linkedin-pack/08-performance-diagnosis-and-improvement.md and C386-linkedin-pack/08-cleaned-performance-metrics.csv\nCSV columns: row_instance_id,source_record_id,date,content_type,pillar,audience_stage,disposition,issue,impressions,members_reached,interactions,engagement_rate_pct,profile_view_rate_pct,follower_rate_pct,messages_sent,replies,reply_rate_pct,qualified_conversations,qualified_conversation_rate_pct,owned_outcomes,outcome_rate_pct,caveat\nrow_instance_id must be unique even when source_record_id repeats; use distinct IDs such as ROW-010A and ROW-010B for the duplicate R-010 records.\nMarkdown sections: Decision Question | Metric Dictionary | Data Quality | Calculations | Funnel | Diagnosis | Alternatives | Experiment Card | Decision Log | Pack Manifest"),
            ("Write the decision question and metric hierarchy. Separate discovery, engagement, profile activity, conversation, and business outcome. Name the primary outcome and at least two guardrails from Lab 1.", "Question: Which single controllable change is most likely to improve <OUTCOME> for <AUDIENCE> while protecting <GUARDRAILS>?"),
            ("Define every metric before calculating it: source field, numerator, denominator, filters, time period, scope, unit, limitation, and missing-denominator treatment. Treat LinkedIn analytics as estimates and do not mix member-post and Page definitions silently.", "Minimum: impressions | members_reached | interactions | engagement_rate | profile_view_rate | follower_rate | reply_rate | qualified_conversation_rate | outcome_rate. A blank or zero denominator returns N/A, never 0%."),
            ("Inspect the CSV. Check row count, unique IDs, dates, missing values, negative values, impossible relationships, duplicates, content type, audience stage, and whether comparison periods and denominators are compatible.", "Quality disposition: USE | USE WITH CAVEAT | EXCLUDE | OWNER TO VERIFY."),
            ("Calculate counts and rates in the spreadsheet. Show formulas, keep counts beside rates, and return N/A for a blank or zero denominator. Verify the three fixed seed results before continuing.", "interactions = reactions + comments + reposts + saves + sends + link_visits\nengagement_rate_pct = interactions / impressions * 100\nprofile_view_rate_pct = profile_viewers_from_post / impressions * 100\nfollower_rate_pct = followers_gained / impressions * 100\nreply_rate_pct = replies / messages_sent * 100\nqualified_conversation_rate_pct = qualified_conversations / messages_sent * 100\noutcome_rate_pct = owned_outcomes / qualified_conversations * 100\nSeed checks: R-001 engagement_rate_pct = 3.83%; R-002 engagement_rate_pct = 5.24%; R-009 reply_rate_pct = 33.33%."),
            ("Build the funnel view from impressions to members reached, meaningful interactions, profile viewers, replies, qualified conversations, and the synthetic owned outcome. State where direct attribution is unavailable.", "Do not treat an impression, reaction, profile view, or reply as a completed business outcome."),
            ("Ask the AI to diagnose the largest constrained drop using the quality log and metric definitions. Require three possible explanations, evidence for and against each, missing evidence, and one proposed controllable variable.", "The AI may recommend; it may not change frequency, content, messaging, targeting, permissions, or account behaviour."),
            ("Challenge the diagnosis. Compare like content types and audience stages, inspect outliers, consider timing and source freshness, and reject any causal claim not supported by the synthetic design.", "Diagnosis status: SUPPORTED | PLAUSIBLE | WEAK | NOT TESTABLE WITH CURRENT DATA."),
            ("Complete one bounded experiment card: hypothesis, single variable, baseline and direction, primary metric, guardrails, segment, owner, approval packet, observation window and sample, cooldown, stop threshold, and rollback. Finish the decision log, outputs 01-08 manifest, and before/after correction table.", "Decision: HOLD | HUMAN-RUN PILOT | REVISE | STOP; no live change.\n| Item | Before | After | Reason | Reviewer | Timestamp |"),
        ],
        slide_steps=[
            ("Define metrics, validate the synthetic export, calculate transparent counts and rates, and separate discovery, engagement, profile, conversation, and business outcomes.", "DEFINE -> VALIDATE -> CALCULATE -> INTERPRET"),
            ("Diagnose alternatives, then propose one controlled variable with an owner, guardrails, observation window, cooldown, stop threshold, and rollback.", "HYPOTHESIS -> HUMAN DECISION -> OBSERVE -> HOLD / ADAPT / ROLLBACK"),
        ],
        test=(
            "Open 08-performance-diagnosis-and-improvement.md and 08-cleaned-performance-metrics.csv. Verify R-001 engagement 3.83%, R-002 engagement 5.24%, and R-009 reply rate 33.33%; the two R-010 instances must have distinct row_instance_id values and explicit duplicate dispositions, while R-011 impossible reach and R-012 missing denominator must carry explicit dispositions, and blank or zero denominators must return N/A. "
            "The diagnosis must state alternatives and limitations, and the experiment must change exactly one variable with an owner, primary metric, two guardrails, observation window, cooldown, stop threshold, and rollback. The course-pack manifest must list outputs 01 through 08."
        ),
        checkpoint="The connected C386-linkedin-pack is complete. Re-run the manifest and three random evidence traces before adapting any part of the system to authorised workplace data.",
        troubleshooting=[
            ("Rates look impressive but counts are tiny", "Report numerator and denominator beside every rate, widen the observation window, and avoid a decision until the minimum useful sample is met."),
            ("The AI claims a post caused revenue", "Return to the funnel and label missing attribution; distinguish correlation, contribution, and verified owned outcomes."),
            ("The experiment changes content, timing, and audience together", "Choose the single highest-priority controllable variable and hold all other planned conditions stable."),
        ],
        challenge="Create a pre-mortem with three ways the proposed experiment could harm trust, data quality, or workflow capacity, then add one early-warning indicator for each.",
        reflection="What evidence would make you reverse the experiment even if the primary metric improved?",
    ),
]
