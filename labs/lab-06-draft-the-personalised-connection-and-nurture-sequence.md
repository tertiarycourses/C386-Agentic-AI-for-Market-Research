# Lab 6 — Draft the Personalised Connection and Nurture Sequence

**Course:** Agentic AI for Linkedin Marketing (C386)  
**Version:** v1.0 (3 August 2026)  
**Topic 3:** Lead Generation and Outreach with AI Agents  
**Maps to:** LO4, LO5: Create concise, relevant, evidence-linked outreach drafts with etiquette rules, stop conditions, privacy protection, and human sending authority.  
**Tools:** Approved AI assistant, text editor, Lab 5 queue and supplied synthetic message scenarios  
**Duration:** 55 minutes

---

## Goal

LO4, LO5: Create concise, relevant, evidence-linked outreach drafts with etiquette rules, stop conditions, privacy protection, and human sending authority.

## What You Will Do

You turn approved synthetic queue records into a bounded communication sequence. Each draft uses verified context, adds distinct value, avoids false familiarity and pressure, and stops on no response, decline, uncertainty, privacy concern, or relationship risk.

## What You Will Build

C386-linkedin-pack/06-outreach-and-nurture-sequence.md with invitation, welcome, value, and handoff drafts for approved synthetic segments; an evidence map; message checks; stop conditions; and a send-decision log.

## Prerequisites

- Complete Lab 5 and use only rows marked READY FOR MESSAGE DRAFT.
- Open labs/resources/northstar-message-scenarios.csv.
- No connection request or message will be sent; the exercise ends with a human decision record.

> **Data note.** Use only the supplied synthetic case files and an approved AI assistant. Do not scrape LinkedIn, use unauthorised bots or browser extensions, mass-send invitations or messages, publish automatically, or paste credentials or real personal data into prompts.

## Steps

**1. Create 06-outreach-and-nurture-sequence.md with sections for Sequence Rules, Segment Message Map, Drafts, Evidence Map, Etiquette Checks, Stop Conditions, Escalation, and Send-Decision Log.**

```text
File: C386-linkedin-pack/06-outreach-and-nurture-sequence.md
```

**2. Write the sequence purpose and non-goals. The purpose is to begin a relevant professional conversation; non-goals include maximising volume, evading platform limits, creating urgency, disguising commercial intent, or sending without owner review.**

```text
Operating principle: relevance and recipient agency are guardrails, not variables to optimise away.
```

**3. Define the relevance ladder: correct identity, verified context, professional reason, useful value, low-friction next step. State the evidence required at each rung and the fallback when it is missing.**

```text
Fallback: omit the detail, ask a neutral question, hold the draft, or stop - never invent.
```

**4. For two READY rows, ask the AI to draft a concise connection invitation. Require a plain-language reason to connect, no fabricated praise, no unsupported claim, no hard pitch, and an output count for characters so the owner can check the current product limit.**

```text
Exact limits can change. The owner verifies the current LinkedIn interface before use; the draft must remain concise regardless of the maximum.
```

**5. Draft a welcome message for use only after a connection is genuinely accepted. It should acknowledge the context, offer one useful idea or question, and avoid immediately asking for a meeting.**

```text
Status: DRAFT FOR USE ONLY AFTER VERIFIED ACCEPTANCE.
```

**6. Draft one value-adding follow-up and one optional conversation handoff. Each must contribute new value, preserve the evidence map, and make no assumption that the recipient read or agreed with an earlier message.**

```text
No response is not consent or interest. Do not send repeated variants to overcome silence.
```

**7. Apply the sequence to the seven fixed supplied scenarios. Record a safe state separately from any escalation action so a privacy, dispute, or sensitive request cannot remain active while waiting for an owner.**

```text
Return columns: scenario_id | safe state DRAFT RESPONSE / WAIT / STOP | escalation action NONE / ESCALATE TO <OWNER> | reason | owner | evidence preserved. MS-05 must be STOP plus ESCALATE TO PRIVACY OWNER; no further use of that record is permitted.
```

**8. Run the etiquette and privacy checks: recognisable sender, verified context, truthful intent, proportionate ask, no sensitive inference, no confidential data, no manipulation, easy decline, limited sequence, and named escalation.**

```text
Any failed check sets the message to STOP or RETURN FOR REVISION.
```

**9. Complete the Send-Decision Log for each draft. The human owner records recipient verification, context freshness, wording edits, current platform guidance check, decision, and reason. End the lab without sending.**

```text
| Draft ID | Recipient verified | Context current | Current guidance checked | Owner edit | Decision | Reason |
```

## Test It

Open 06-outreach-and-nurture-sequence.md. Each approved segment must have an invitation, post-acceptance welcome, value follow-up, and optional handoff with a complete evidence map. All seven fixed scenarios MS-01 through MS-07 must have a safe state plus a separate escalation action, reason, and owner. MS-05 must be STOP plus ESCALATE TO PRIVACY OWNER; declined, deletion, disputed, sensitive, and silent cases must not continue automatically. The Send-Decision Log must show no message was sent in the lab.

## Checkpoint for the Next Lab

Keep the approved drafts, routing rules, and decision log. Lab 7 combines the content and engagement artefacts into one draft-first operations workflow with a consistent approval packet.

## Troubleshooting

- **The invitation invents a shared interest:** Remove the statement, return to the evidence map, and use a modest verified context or hold the draft.
- **Every follow-up repeats the same request:** Give each touch a distinct audience value or question and stop the sequence when no new value exists.
- **A privacy request receives a marketing reply:** Set STOP, preserve the original request, avoid further use of the record, and escalate to the named privacy owner.

## Optional Challenge (+10 minutes, outside core duration)

Write two versions of the value follow-up for different readiness states and explain why the next action changes while the evidence and etiquette rules do not. Save the result in the numbered lab output.

## Reflection

What is the earliest signal that a relevant sequence has become unwanted pressure, and how should the workflow respond? Record your answer in the numbered lab output.

---

[← Lab 5](lab-05-build-the-evidence-based-prospect-segmentation-queue.md) · [Lab 7 →](lab-07-design-the-governed-content-and-engagement-operations-workflow.md)
