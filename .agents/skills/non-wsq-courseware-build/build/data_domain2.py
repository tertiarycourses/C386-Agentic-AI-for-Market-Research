"""Topic 2 - content creation, personal brand, and calendar."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Create the LinkedIn Voice, Profile, and Multi-Format Content Kit",
        objective="LO2, LO3: Apply the prompt contract to create an evidence-grounded profile draft, voice fingerprint, posts, article outline, and carousel brief.",
        desc=(
            "You build a recognisable content foundation for Northstar Advisory using the same audience value, proof, and action defined in Labs 1 and 2. "
            "The AI produces alternatives, while you restore the human point of view and verify every claim, example, quotation, and visual direction."
        ),
        build="C386-linkedin-pack/03-profile-voice-and-content-kit.md containing the voice fingerprint, reviewed headline and About drafts, four post concepts, one article outline, one six-page carousel brief, evidence maps, and review log.",
        services="Approved AI assistant, text editor, Labs 1-2 outputs and supplied writing samples",
        duration="45 minutes",
        prerequisites=[
            "Complete Labs 1 and 2 and keep their source labels and permission boundaries.",
            "Open labs/resources/northstar-writing-samples.md and northstar-brand-brief.md.",
            "Do not publish or edit a live profile; all outputs remain internal drafts.",
        ],
        steps=[
            ("Create 03-profile-voice-and-content-kit.md with sections for Voice Fingerprint, Profile Drafts, Content Matrix, Article Outline, Carousel Brief, Evidence Map, and Review Log.", "File: C386-linkedin-pack/03-profile-voice-and-content-kit.md"),
            ("Analyse the supplied writing samples without imitating any outside author. Record sentence rhythm, preferred vocabulary, level of formality, stance, example style, recurring structures, banned clichés, and claims the owner will not make.", "Voice rule: describe observable patterns from the supplied samples; do not guess personality traits."),
            ("Use the released G-C-A-T-E contract to produce three headline options and one About draft. Require source tags and a concise explanation of the trade-off in each headline.", "Profile output: Headline A/B/C | audience value | verified proof | trade-off; About: focus -> audience problem -> approach -> proof -> point of view -> next action."),
            ("Review the profile drafts against the Lab 1 value stack. Remove keyword stuffing, unsupported results, false authority, generic superlatives, and any sentence that could describe almost any consultant.", "Owner review labels: KEEP | REWRITE IN MY VOICE | REMOVE - NO EVIDENCE | OWNER TO VERIFY."),
            ("Create a four-item content matrix: practical framework post, contrarian-but-supported observation, client-safe process story, and question-led discussion. For each, define audience question, content pillar, hook, value unit, evidence source, format, and proportionate next action.", "No invented client story or quotation. A process story must be explicitly synthetic or based on the approved source."),
            ("Draft the four short posts. Keep each focused on one idea, make the hook pay off, cite the internal evidence map, and preserve one deliberate human edit in every draft.", "Required footer in the working file: HUMAN EDIT: <what changed and why>. Do not add that footer to a future published post."),
            ("Create an article outline with title, reader promise, thesis, three sections, evidence needed, counterpoint, practical takeaway, and next action. Mark unsupported evidence needs UNKNOWN instead of fabricating them.", "Article purpose: help operations leaders decide when a process is ready for AI-supported improvement."),
            ("Create a six-page document-carousel brief. Give each page one message, suggested visual hierarchy, on-slide text, speaker note, accessibility note, and evidence reference. Keep text readable and do not use copyrighted images without rights.", "Pages: 1 promise | 2 problem | 3 framework | 4 worked example | 5 checklist | 6 next step."),
            ("Run the evidence, voice, privacy, rights, relevance, and action-boundary checks. Record a distinct human edit for exactly eight named artefacts: the selected headline, About draft, four short posts, article outline, and carousel brief. Also record at least one rejected AI suggestion.", "| Artefact ID | Artefact | Check | Source or rule | Human edit | Rejected AI suggestion if any | Status |\nRequired artefacts: HEADLINE-SELECTED | ABOUT-01 | POST-01 | POST-02 | POST-03 | POST-04 | ART-01 | CAR-01"),
        ],
        slide_steps=[
            ("Derive a voice fingerprint and profile draft from approved writing samples, value, and proof - then let the owner restore nuance.", "SOURCE PATTERN -> AI ALTERNATIVES -> HUMAN VOICE"),
            ("Build posts, article structure, and carousel as one evidence-linked content kit with fact, voice, privacy, rights, and relevance checks.", "HOOK -> VALUE -> PROOF -> PROPORTIONATE ACTION"),
        ],
        test=(
            "Open 03-profile-voice-and-content-kit.md. It must contain eight voice dimensions, three headline options, one About draft, four complete post drafts, an article outline, and a six-page carousel brief. "
            "Every factual claim must map to an approved source or be removed. The selected headline, About draft, POST-01 through POST-04, ART-01, and CAR-01 must each contain a documented human edit, and no item may be marked for publication."
        ),
        checkpoint="Keep the reviewed kit. Lab 4 sequences the four posts, article, and carousel into a fourteen-day calendar and a draft-first production workflow.",
        troubleshooting=[
            ("All four posts sound alike", "Change the audience question, value unit, structure, and format while keeping the same voice fingerprint and evidence boundary."),
            ("The About section reads like an advertisement", "Restore professional identity, audience value, evidence, and point of view; remove urgency, broad promises, and repeated service keywords."),
            ("Carousel pages are paragraphs", "Give each page one claim, one visual relationship, and one supporting sentence; move detailed explanation into speaker notes."),
        ],
        challenge="Create a second version of one post for a different audience stage, then explain which evidence and call to action changed and which voice rules stayed constant.",
        reflection="Where did your human rewrite add judgement or lived perspective that the AI draft could not safely infer?",
    ),
    dict(
        num=4,
        topic=2,
        title="Build the Fourteen-Day Content Calendar and Draft-First Workflow",
        objective="LO3, LO5: Sequence the content kit into a coherent calendar and design a governed workflow from intake through human scheduling and learning.",
        desc=(
            "You turn the reviewed content kit into a two-week learning sequence rather than a queue of unrelated posts. "
            "You define dependencies, owners, source freshness, review gates, native-scheduling handoff, exception paths, and the signals that will inform the next cycle."
        ),
        build="C386-linkedin-pack/04-content-calendar-and-workflow.md with a fourteen-day calendar, content dependencies, production board, approval packet, native-scheduling checklist, exception routes, and readiness test.",
        services="Approved AI assistant, text editor or spreadsheet, Labs 1-3 outputs",
        duration="60 minutes",
        prerequisites=[
            "Complete Lab 3 and retain only drafts that passed the evidence, voice, privacy, rights, and relevance checks.",
            "Choose a human Brand Owner and Publisher role for the simulation.",
            "Keep all scheduling and publication steps as a handoff; do not connect an account or publish during the lab.",
        ],
        steps=[
            ("Create 04-content-calendar-and-workflow.md with sections for Calendar Logic, Fourteen-Day Calendar, Production Board, Approval Packet, Scheduling Checklist, Exceptions, and Readiness Test.", "File: C386-linkedin-pack/04-content-calendar-and-workflow.md"),
            ("Define the sequence hypothesis: which audience question opens the series, how each item builds knowledge or trust, where the article and carousel add depth, and what the audience should understand by day fourteen.", "Sequence sentence: If the audience sees <ITEMS IN ORDER>, it can move from <INITIAL QUESTION> to <USEFUL DECISION> without requiring a sales claim."),
            ("Ask the AI to propose a fourteen-day calendar using only POST-01 through POST-04, ART-01, and CAR-01 plus two explicitly labelled engagement-listening days. Pin POST-01 to Day 2, CAR-01 to Day 7, and ART-01 to Day 12 so the fixed readiness fixtures always exist. An engagement-listening day is an internal simulation: review supplied synthetic scenarios, capture questions, and recommend a future draft; do not open LinkedIn, comment, react, message, or perform any live action. Require content ID, pillar, audience stage, objective, source, format, owner, review date, planned date, next action, and metric.", "Fixed fixtures: Day 2 = POST-01; Day 7 = CAR-01; Day 12 = ART-01. Constraint: no new claim or idea may be added silently; additions must be HYPOTHESIS and require owner approval. Engagement-listening rows use format SIMULATED REVIEW and state NO LIVE LINKEDIN ACTION."),
            ("Review pacing and dependencies. Avoid repeating the same pillar or format on consecutive release days, protect production capacity, and leave space to respond to relevant discussion.", "Calendar rule: quality and readiness override a planned date; a missing source or owner sends the item to HOLD."),
            ("Create the production-state board with BACKLOG, SOURCE READY, DRAFTING, BRAND REVIEW, FACT REVIEW, READY TO SCHEDULE, SCHEDULED BY HUMAN, PUBLISHED, and LEARNING CAPTURED.", "Each item records: content ID | state | owner | source version | draft version | decision | timestamp | next safe action."),
            ("Build a compact approval packet for one post and the carousel. Include objective, audience, exact draft, source evidence, check results, known unknowns, media rights, accessibility, proposed timing, risk, and correction path.", "Decision options: APPROVE AS WRITTEN | APPROVE WITH EDIT | RETURN FOR REVISION | STOP."),
            ("Write the LinkedIn native-scheduling handoff. The human publisher confirms identity, audience visibility, text, links, media, alt text, time zone, date, current platform support, and final approval before using LinkedIn's scheduler.", "The workflow may prepare the checklist; only the authorised human opens LinkedIn and schedules."),
            ("Define exception routes for stale evidence, voice mismatch, missing rights, confidential information, platform-interface change, negative feedback, broken link, and an item that misses its date.", "Exception format: trigger | safe state | owner | evidence preserved | correction or rollback | restart condition."),
            ("Run the readiness test on fixed calendar rows Day 2, Day 7, and Day 12. Trace each from source to draft to review packet to proposed schedule and learning metric; record every gap and set the affected row to HOLD until fixed. Add a change-evidence table for every correction.", "Readiness result: READY FOR HUMAN SCHEDULING or HOLD - <REASON>.\n| Item | Before | After | Source or reason | Reviewer | Timestamp |"),
        ],
        slide_steps=[
            ("Sequence reviewed artefacts by audience question and learning dependency, with a source, owner, review date, action, and metric for every row.", "CONTENT KIT -> FOURTEEN-DAY LEARNING SEQUENCE"),
            ("Move each item through explicit states and a complete approval packet; hand approved drafts to a human using LinkedIn's native scheduler.", "DRAFT -> CHECK -> APPROVE -> HUMAN SCHEDULE -> OBSERVE"),
        ],
        test=(
            "Open 04-content-calendar-and-workflow.md. The calendar must cover fourteen days, include all six reviewed artefacts plus two engagement days, name a source and owner for every planned item, and use the defined production states. "
            "Fixed rows Day 2, Day 7, and Day 12 must trace through a complete review packet to either READY FOR HUMAN SCHEDULING or a specific HOLD reason; the change-evidence table must capture corrections, and no automated publication or live engagement action may exist."
        ),
        checkpoint="Keep the calendar and workflow. Labs 5 and 6 reuse its audience evidence, brand voice, status vocabulary, and human gates for prospect segmentation and outreach drafts.",
        troubleshooting=[
            ("The calendar is just a daily posting quota", "Rebuild it around audience questions, content dependencies, production capacity, and learning; use empty days where no item is ready."),
            ("The schedule handoff assumes the interface is fixed", "Store the purpose and checklist independently, then require the publisher to verify the current LinkedIn interface and feature support."),
            ("Reviewers cannot tell what changed", "Add source version, draft version, previous decision, exact human edit, reviewer, and timestamp to the production record."),
        ],
        challenge="Add a contingency branch for a timely industry development: define what may be drafted quickly, what evidence is required, and which existing item moves without breaking the sequence.",
        reflection="Which calendar dependency most protects trust, and what would the audience experience if that dependency were ignored?",
    ),
]
