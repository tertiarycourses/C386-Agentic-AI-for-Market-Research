# Lab 1 — Build the LinkedIn Strategy, Profile, and Agent Boundary Map

**Course:** Agentic AI for Linkedin Marketing (C386)  
**Version:** v1.0 (3 August 2026)  
**Topic 1:** Getting Started with Agentic AI for LinkedIn Marketing  
**Maps to:** LO1, LO2: Define the LinkedIn decision chain, profile value stack, authorised evidence, tool roles, risks, and human-approval gates.  
**Tools:** Approved AI assistant, text editor, supplied Markdown and CSV resources  
**Duration:** 50 minutes

---

## Goal

LO1, LO2: Define the LinkedIn decision chain, profile value stack, authorised evidence, tool roles, risks, and human-approval gates.

## What You Will Do

You start the connected Northstar Advisory scenario by turning its approved synthetic brand brief, audience signals, and current-profile draft into one coherent LinkedIn foundation. You identify what an AI agent may read, draft, recommend, or never do, then map the profile value stack and the decisions a human must retain.

## What You Will Build

C386-linkedin-pack/01-foundation-profile-and-boundaries.md containing the decision chain, audience needs, profile audit, value stack, tool map, risk tiers, and approval gates.

## Prerequisites

- Create a local folder named C386-linkedin-pack.
- Open labs/resources/northstar-brand-brief.md, northstar-audience-signals.csv, and northstar-current-profile.md.
- Start a new chat in an organisation-approved AI assistant and use only the synthetic course data.

> **Data note.** Use only the supplied synthetic case files and an approved AI assistant. Do not scrape LinkedIn, use unauthorised bots or browser extensions, mass-send invitations or messages, publish automatically, or paste credentials or real personal data into prompts.

## Steps

**1. Create the foundation file with headings for Decision Chain, Audience Evidence, Profile Audit, Value Stack, Tool Map, Risk Tiers, Approval Gates, and Review Log.**

```text
File: C386-linkedin-pack/01-foundation-profile-and-boundaries.md
```

**2. Read the brand brief without AI. Under Audience Evidence, record the approved offer facts, desired action, brand constraints, proof points, audience questions, and every unknown. Label each item FACT, HYPOTHESIS, or UNKNOWN.**

```text
Rule: FACT = explicit source; HYPOTHESIS = reasonable but unproven; UNKNOWN = source is silent.
```

**3. Write one measurable decision chain that connects the business result, audience need, desired professional action, LinkedIn channel job, primary metric, and two guardrails.**

```text
Because <BUSINESS RESULT>, LinkedIn will help <AUDIENCE> solve <NEED> by encouraging <ACTION>; progress is <PRIMARY METRIC>, while protecting <GUARDRAIL 1> and <GUARDRAIL 2>.
```

**4. Ask the AI to map the audience journey from the supplied evidence. Require sources and prohibit invented demographics, testimonials, results, client names, and platform behaviour.**

```text
You are a LinkedIn marketing strategist. Use only the supplied synthetic brand brief and audience-signal rows. Return a Markdown table with stages Discover, Evaluate, Engage, Converse, Decide. Columns: stage | audience question | source ID | LinkedIn job | desired micro-action | evidence of progress | risk or unknown | human decision. Label unsupported inference HYPOTHESIS and missing information UNKNOWN. Do not invent claims, people, events, performance, or product features.

BRAND BRIEF:
<PASTE>

AUDIENCE SIGNALS:
<PASTE>
```

**5. Audit the supplied current profile. For the headline, About section, Featured evidence, Experience, and next action, record KEEP, REVISE, or OWNER TO VERIFY, the source that supports the decision, and the risk of publishing an inaccurate claim.**

```text
Required checks: identity accuracy | audience clarity | value | proof | keyword variety | readability | next action | confidentiality.
```

**6. Create a profile value stack with Identity, Audience, Value, Proof, Point of View, and Next Action. Use only approved facts; keep missing proof as UNKNOWN.**

```text
Value stack line: I help <AUDIENCE> achieve <VALUE> through <CAPABILITY>; proof: <APPROVED EVIDENCE>; point of view: <SUPPORTED STANCE>; next action: <LOW-FRICTION STEP>.
```

**7. Build a tool-role map for the AI assistant, text editor, spreadsheet, LinkedIn profile, LinkedIn native scheduler, Sales Navigator, and any organisation-approved workflow tool. Record allowed read, draft, recommend, or external-action capability, required data, risk, owner, and fallback.**

```text
Risk: LOW = synthetic/read-only; MEDIUM = internal draft or classification; HIGH = identity change, publication, invitation, message, personal data, account permission, or paid action.
```

**8. Add approval gates for profile edits, public content, connection invitations, direct messages, personal-data use, account permissions, and any unsupported claim. State the owner, evidence packet, decision options, and correction path.**

```text
Statuses: DRAFT | READY FOR HUMAN REVIEW | APPROVED BY <ROLE> | STOP - <REASON>. Silence is never approval.
```

**9. Complete the three fixed Review Log checks: AS-01, the Approved Offer section, and the unsupported '10x' headline claim. Correct any mismatch you observe; do not invent three corrections when a checked result is already accurate. Preserve expected and observed values plus the action taken.**

```text
| Item checked | Source | Expected | Observed | Result | Correction |
|---|---|---|---|---|---|
| AS-01 audience signal | northstar-audience-signals.csv#AS-01 | Exact source meaning retained | <OBSERVED> | KEEP / REVISE / STOP | <ACTION> |
| Offer statement | northstar-brand-brief.md#Approved Offer | Exact offer scope retained | <OBSERVED> | KEEP / REVISE / STOP | <ACTION> |
| '10x' result claim | No approved source | UNKNOWN and removed | <OBSERVED> | KEEP / REVISE / STOP | <ACTION> |
```

## Test It

Open 01-foundation-profile-and-boundaries.md. It must contain five audience-journey stages with a source in every row, all six profile-value elements, seven tool roles, and explicit gates for identity, publishing, invitations, messages, personal data, permissions, and unsupported claims. The Review Log must contain the fixed AS-01, Approved Offer, and unsupported '10x' checks; the first two must trace exactly to source, while '10x' must be labelled UNKNOWN and removed.

## Checkpoint for the Next Lab

Keep 01-foundation-profile-and-boundaries.md. Lab 2 converts its goal, evidence, voice, tools, risks, and human authority into a reusable prompt contract.

## Troubleshooting

- **The output is a list of LinkedIn tactics:** Return to the decision chain and require every tactic to name the audience need, desired action, source, metric, and owner decision.
- **The profile draft invents a client result:** Replace the result with UNKNOWN, record the missing source, and stop that claim from entering a draft.
- **The tool map grants automatic posting or messaging:** Change the capability to draft or recommend, assign a human owner, and add an explicit external-action gate.

## Optional Challenge (+10 minutes, outside core duration)

Add a RACI-style row for brand ownership, profile accuracy, privacy review, publishing, relationship handling, analytics, and incident correction. Save the result in the numbered lab output.

## Reflection

Which LinkedIn action creates the greatest combined identity, relationship, and privacy risk, and what should its reviewer see before deciding? Record your answer in the numbered lab output.

---

[← Labs index](README.md) · [Lab 2 →](lab-02-write-and-boundary-test-the-linkedin-g-c-a-t-e-prompt-contract.md)
