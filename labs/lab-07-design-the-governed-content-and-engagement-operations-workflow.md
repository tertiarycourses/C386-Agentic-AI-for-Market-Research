# Lab 7 — Design the Governed Content and Engagement Operations Workflow

**Course:** Agentic AI for Linkedin Marketing (C386)  
**Version:** v1.0 (3 August 2026)  
**Topic 4:** Automating and Scaling LinkedIn with AI Agents  
**Maps to:** LO5: Design a traceable draft-first workflow for content, comments, and follow-ups with explicit states, approvals, exceptions, and authorised external-action boundaries.  
**Tools:** Approved AI assistant, text editor or diagram tool, Labs 1-6 outputs and supplied engagement scenarios  
**Duration:** 45 minutes

---

## Goal

LO5: Design a traceable draft-first workflow for content, comments, and follow-ups with explicit states, approvals, exceptions, and authorised external-action boundaries.

## What You Will Do

You connect the earlier content calendar, prospect rules, and outreach drafts into one operations workflow. The agent prepares and checks internal artefacts; human owners retain profile identity, publishing, invitations, messages, relationship judgement, and incident correction.

## What You Will Build

C386-linkedin-pack/07-governed-operations-workflow.md containing the workflow map, state machine, role and permission matrix, approval packets, engagement router, exception paths, trace schema, and simulation results.

## Prerequisites

- Complete Labs 1-6 and retain the latest approved foundation, prompt contract, calendar, prospect queue, and outreach rules.
- Open labs/resources/northstar-engagement-scenarios.csv.
- Use a diagram or Markdown table; no live account, credential, bot, extension, or external integration is required.

> **Data note.** Use only the supplied synthetic case files and an approved AI assistant. Do not scrape LinkedIn, use unauthorised bots or browser extensions, mass-send invitations or messages, publish automatically, or paste credentials or real personal data into prompts.

## Steps

**1. Create 07-governed-operations-workflow.md with sections for Scope, Workflow Map, States, Roles and Permissions, Approval Packets, Engagement Router, Exceptions, Trace Record, and Simulation.**

```text
File: C386-linkedin-pack/07-governed-operations-workflow.md
```

**2. State the workflow boundary. In scope: approved-source intake, validation, internal drafting, quality checks, prioritisation, review packets, recommendations, and learning records. Out of scope: scraping, unauthorised access, automated engagement, automatic invitations or messages, credential handling, and unreviewed publication.**

```text
External-action rule: use only current LinkedIn features or organisation-approved integrations after a named human decision.
```

**3. Draw the canonical state flow: INTAKE, VALIDATE, DRAFT, CHECK, READY FOR HUMAN REVIEW, READY FOR HUMAN ACTION, HUMAN ACTION, OBSERVE, LEARNING CAPTURED. Add RETURN FOR REVISION, HOLD, and STOP branches; record ESCALATE TO <OWNER> as an action attached to a safe state, not as a competing state.**

```text
No transition may move from DRAFT or CHECK directly to READY FOR HUMAN ACTION or HUMAN ACTION. Only a named human decision can set READY FOR HUMAN ACTION.
```

**4. Create the role and permission matrix for Requester, Agent, Brand Owner, Fact Owner, Publisher, Relationship Owner, Privacy Owner, Commercial Owner, Legal Owner, and Operations Owner. Record read, draft, decide, act, correct, and audit rights.**

```text
Separation: the agent cannot approve its own output; the Publisher cannot invent missing proof; the Relationship Owner handles recipient context; Commercial and Legal Owners decide within their named remit.
```

**5. Define one approval packet schema shared by profile, content, and outreach work. Include goal, audience or recipient, exact draft, source map, model or prompt version, checks, unknowns, risk, proposed action, owner, decision, timestamp, and correction path.**

```text
A reviewer should decide without reconstructing hidden chat context.
```

**6. Build the engagement router for the supplied synthetic comments and messages. Classify praise, question, correction, complaint, commercial interest, privacy request, abuse, sensitive issue, and unknown; assign DRAFT RESPONSE, WAIT, or STOP as the safe state and record any ESCALATE TO <OWNER> action separately.**

```text
The router drafts nothing for a row with insufficient context until the owner supplies it. Privacy and sensitive cases enter STOP before escalation.
```

**7. Add operational exceptions: source unavailable, stale evidence, model output malformed, voice failure, policy concern, confidential detail, duplicate item, missed date, wrong recipient, negative response, and current interface change.**

```text
Exception row: trigger | safe state | preserved evidence | owner | correction or rollback | restart condition.
```

**8. Define the trace record for every run: run_id, artefact_id, input sources and versions, prompt version, model or tool, checks, reviewer, decision, action owner, external action if any, timestamp, outcome, exception, and next step.**

```text
Keep secrets and message content out of the trace when a reference ID is sufficient.
```

**9. Simulate the six fixed scenarios end to end: ready content, stale claim, voice mismatch, privacy request, interested reply, and request to auto-send. Record every state transition, final safe state, separate escalation action, and a before/after evidence row for each correction.**

```text
Expected: ready content -> READY FOR HUMAN ACTION; stale claim -> HOLD; voice mismatch -> RETURN FOR REVISION; privacy request -> STOP + ESCALATE TO PRIVACY OWNER; interested reply -> READY FOR HUMAN ACTION; auto-send request -> STOP. No external action occurs.
| Scenario | Before | After | Source or reason | Reviewer | Timestamp |
```

## Test It

Open 07-governed-operations-workflow.md. Every main and exception state must have an entry rule, owner, allowed next states, and trace fields; no path may bypass human review. All six fixed simulations must finish in their stated expected safe state with a complete record and change-evidence row. READY FOR HUMAN ACTION must appear only after a named human decision; the request to auto-send must finish STOP without executing or simulating an external LinkedIn action.

## Checkpoint for the Next Lab

Keep the workflow and trace schema. Lab 8 uses them to validate performance data, diagnose the system, and log one bounded improvement recommendation.

## Troubleshooting

- **The workflow diagram has arrows but no decisions:** Add entry criteria, owner, evidence, decision options, and failure path to every state transition.
- **The approval packet contains only the draft:** Add goal, audience, sources, versions, checks, unknowns, risk, proposed action, owner, and correction path.
- **The engagement router drafts a reply to every row:** Introduce WAIT, STOP, and ESCALATE; require sufficient context and separate relationship, privacy, complaint, and sensitive cases.

## Optional Challenge (+10 minutes, outside core duration)

Add a two-person review path for a high-reputation-risk post and show how disagreement, expiry, and correction are recorded. Save the result in the numbered lab output.

## Reflection

Which workflow record would be most valuable after a public correction, and what must it contain to support accountability? Record your answer in the numbered lab output.

---

[← Lab 6](lab-06-draft-the-personalised-connection-and-nurture-sequence.md) · [Lab 8 →](lab-08-diagnose-performance-and-propose-one-bounded-scaling-experiment.md)
