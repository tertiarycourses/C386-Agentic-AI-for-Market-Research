# Lab 4 — Build the Fourteen-Day Content Calendar and Draft-First Workflow

**Course:** Agentic AI for Linkedin Marketing (C386)  
**Version:** v1.0 (3 August 2026)  
**Topic 2:** Content Creation and Personal Branding with AI  
**Maps to:** LO3, LO5: Sequence the content kit into a coherent calendar and design a governed workflow from intake through human scheduling and learning.  
**Tools:** Approved AI assistant, text editor or spreadsheet, Labs 1-3 outputs  
**Duration:** 60 minutes

---

## Goal

LO3, LO5: Sequence the content kit into a coherent calendar and design a governed workflow from intake through human scheduling and learning.

## What You Will Do

You turn the reviewed content kit into a two-week learning sequence rather than a queue of unrelated posts. You define dependencies, owners, source freshness, review gates, native-scheduling handoff, exception paths, and the signals that will inform the next cycle.

## What You Will Build

C386-linkedin-pack/04-content-calendar-and-workflow.md with a fourteen-day calendar, content dependencies, production board, approval packet, native-scheduling checklist, exception routes, and readiness test.

## Prerequisites

- Complete Lab 3 and retain only drafts that passed the evidence, voice, privacy, rights, and relevance checks.
- Choose a human Brand Owner and Publisher role for the simulation.
- Keep all scheduling and publication steps as a handoff; do not connect an account or publish during the lab.

> **Data note.** Use only the supplied synthetic case files and an approved AI assistant. Do not scrape LinkedIn, use unauthorised bots or browser extensions, mass-send invitations or messages, publish automatically, or paste credentials or real personal data into prompts.

## Steps

**1. Create 04-content-calendar-and-workflow.md with sections for Calendar Logic, Fourteen-Day Calendar, Production Board, Approval Packet, Scheduling Checklist, Exceptions, and Readiness Test.**

```text
File: C386-linkedin-pack/04-content-calendar-and-workflow.md
```

**2. Define the sequence hypothesis: which audience question opens the series, how each item builds knowledge or trust, where the article and carousel add depth, and what the audience should understand by day fourteen.**

```text
Sequence sentence: If the audience sees <ITEMS IN ORDER>, it can move from <INITIAL QUESTION> to <USEFUL DECISION> without requiring a sales claim.
```

**3. Ask the AI to propose a fourteen-day calendar using only POST-01 through POST-04, ART-01, and CAR-01 plus two explicitly labelled engagement-listening days. Pin POST-01 to Day 2, CAR-01 to Day 7, and ART-01 to Day 12 so the fixed readiness fixtures always exist. An engagement-listening day is an internal simulation: review supplied synthetic scenarios, capture questions, and recommend a future draft; do not open LinkedIn, comment, react, message, or perform any live action. Require content ID, pillar, audience stage, objective, source, format, owner, review date, planned date, next action, and metric.**

```text
Fixed fixtures: Day 2 = POST-01; Day 7 = CAR-01; Day 12 = ART-01. Constraint: no new claim or idea may be added silently; additions must be HYPOTHESIS and require owner approval. Engagement-listening rows use format SIMULATED REVIEW and state NO LIVE LINKEDIN ACTION.
```

**4. Review pacing and dependencies. Avoid repeating the same pillar or format on consecutive release days, protect production capacity, and leave space to respond to relevant discussion.**

```text
Calendar rule: quality and readiness override a planned date; a missing source or owner sends the item to HOLD.
```

**5. Create the production-state board with BACKLOG, SOURCE READY, DRAFTING, BRAND REVIEW, FACT REVIEW, READY TO SCHEDULE, SCHEDULED BY HUMAN, PUBLISHED, and LEARNING CAPTURED.**

```text
Each item records: content ID | state | owner | source version | draft version | decision | timestamp | next safe action.
```

**6. Build a compact approval packet for one post and the carousel. Include objective, audience, exact draft, source evidence, check results, known unknowns, media rights, accessibility, proposed timing, risk, and correction path.**

```text
Decision options: APPROVE AS WRITTEN | APPROVE WITH EDIT | RETURN FOR REVISION | STOP.
```

**7. Write the LinkedIn native-scheduling handoff. The human publisher confirms identity, audience visibility, text, links, media, alt text, time zone, date, current platform support, and final approval before using LinkedIn's scheduler.**

```text
The workflow may prepare the checklist; only the authorised human opens LinkedIn and schedules.
```

**8. Define exception routes for stale evidence, voice mismatch, missing rights, confidential information, platform-interface change, negative feedback, broken link, and an item that misses its date.**

```text
Exception format: trigger | safe state | owner | evidence preserved | correction or rollback | restart condition.
```

**9. Run the readiness test on fixed calendar rows Day 2, Day 7, and Day 12. Trace each from source to draft to review packet to proposed schedule and learning metric; record every gap and set the affected row to HOLD until fixed. Add a change-evidence table for every correction.**

```text
Readiness result: READY FOR HUMAN SCHEDULING or HOLD - <REASON>.
| Item | Before | After | Source or reason | Reviewer | Timestamp |
```

## Test It

Open 04-content-calendar-and-workflow.md. The calendar must cover fourteen days, include all six reviewed artefacts plus two engagement days, name a source and owner for every planned item, and use the defined production states. Fixed rows Day 2, Day 7, and Day 12 must trace through a complete review packet to either READY FOR HUMAN SCHEDULING or a specific HOLD reason; the change-evidence table must capture corrections, and no automated publication or live engagement action may exist.

## Checkpoint for the Next Lab

Keep the calendar and workflow. Labs 5 and 6 reuse its audience evidence, brand voice, status vocabulary, and human gates for prospect segmentation and outreach drafts.

## Troubleshooting

- **The calendar is just a daily posting quota:** Rebuild it around audience questions, content dependencies, production capacity, and learning; use empty days where no item is ready.
- **The schedule handoff assumes the interface is fixed:** Store the purpose and checklist independently, then require the publisher to verify the current LinkedIn interface and feature support.
- **Reviewers cannot tell what changed:** Add source version, draft version, previous decision, exact human edit, reviewer, and timestamp to the production record.

## Optional Challenge (+10 minutes, outside core duration)

Add a contingency branch for a timely industry development: define what may be drafted quickly, what evidence is required, and which existing item moves without breaking the sequence. Save the result in the numbered lab output.

## Reflection

Which calendar dependency most protects trust, and what would the audience experience if that dependency were ignored? Record your answer in the numbered lab output.

---

[← Lab 3](lab-03-create-the-linkedin-voice-profile-and-multi-format-content-kit.md) · [Lab 5 →](lab-05-build-the-evidence-based-prospect-segmentation-queue.md)
