"""Single source of truth for Agentic AI for Linkedin Marketing (C386)."""

TITLE = "Agentic AI for Linkedin Marketing (C386)"
SHORT_TITLE = "Agentic AI for Linkedin Marketing (C386)"
COURSE_CODE = "C386"
VERSION = "v1.0"
VERSION_DATE = "3 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Tertiary Infotech Academy"
DAYS = 2
MODE = "Instructor-led, concept-first learning with connected hands-on labs"

# The advertised 15 instructional hours are 450 minutes per day. Each day also
# contains two 15-minute tea breaks, so the scheduled total excluding lunch is
# 480 minutes.
DAY_MINUTES = 480
INSTRUCTIONAL_HOURS = 15
CLOCK_HOURS = 16
DAILY_TIMING = "9:00 am - 6:00 pm (1-hour lunch; two 15-minute tea breaks)"
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Explain how goal-driven AI agents support LinkedIn marketing and define safe tool, evidence, and human-approval boundaries.",
    "LO2: Optimise a LinkedIn profile and write reusable prompts that preserve an authentic professional voice.",
    "LO3: Create evidence-grounded LinkedIn posts, articles, visual briefs, carousels, and a coherent content calendar.",
    "LO4: Research and segment prospects from authorised information, then draft relevant connection and nurture messages for human review.",
    "LO5: Design a draft-first content, engagement, and follow-up workflow that respects LinkedIn rules and professional etiquette.",
    "LO6: Define LinkedIn performance metrics, diagnose synthetic results, and recommend one bounded improvement with a traceable decision record.",
]

LO_TITLES = [
    "Agent Foundations",
    "Profile & Prompts",
    "Content System",
    "Prospecting",
    "Governed Workflow",
    "Measure & Improve",
]

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Agentic AI for LinkedIn Marketing",
        subtitle="LinkedIn strategy | AI agents and tools | profile and personal brand | effective prompting",
        concepts=[
            ("Goal before tool", "Begin with the business result, audience need, desired professional action, and evidence of success."),
            ("Agent loop", "A bounded agent observes approved context, reasons against instructions, drafts an output, checks it, and hands off."),
            ("Model, tools, instructions", "The model interprets; tools retrieve or act; instructions define scope, quality, and stop conditions."),
            ("Human authority", "Profile edits, public posts, invitations, messages, and account changes remain explicit human decisions."),
            ("Professional identity", "A useful profile connects credible experience, audience value, proof, and a clear next action without keyword stuffing."),
            ("Evidence boundary", "Approved facts, labelled hypotheses, and unknowns are kept distinct so fluent output is not mistaken for truth."),
            ("Prompt contract", "Goal, Context, Audience, Task, Evidence, and Evaluation turn a vague request into a reusable operating instruction."),
            ("Responsible use", "No scraping, unauthorised bots, mass messaging, credential sharing, deceptive claims, or inauthentic engagement."),
        ],
        teaching_sections=[
            dict(
                title="LinkedIn Marketing as a Decision System",
                paragraphs=[
                    "LinkedIn activity is useful only when it supports a defined professional or business result. A decision chain connects the result to an audience need, a desired action, a channel job, and a metric. This prevents an agent from optimising for visible activity while ignoring whether the right people are learning, trusting, or taking the intended next step.",
                    "For example, a consultancy seeking qualified discovery calls may use profile visits and relevant replies as leading indicators, but it should not call an impression a lead. The profile, content, and outreach system must all point to the same value proposition and next action.",
                ],
                visual=[
                    ("Business result", "What must improve for the organisation?"),
                    ("Audience need", "What useful problem can the brand help solve?"),
                    ("Desired action", "What observable next step matters?"),
                    ("Evidence", "Which metric indicates progress without overstating causality?"),
                ],
            ),
            dict(
                title="What Makes a Marketing Workflow Agentic",
                paragraphs=[
                    "A single AI-generated post is assistance, not an agent. An agentic workflow manages a multi-step goal: retrieve authorised context, choose a routine, produce a draft, evaluate it against rules, request missing information, and stop or hand control back when risk is high.",
                    "The safest beginner pattern is recommendation-only. The agent may read approved synthetic files, draft artefacts, and recommend actions. It cannot publish, invite, message, collect personal data, or change account settings. This design is useful because it improves repeatability without giving away human accountability.",
                ],
                visual=[
                    ("Observe", "Read approved brief, profile, signals, or results."),
                    ("Reason", "Apply goal, evidence rules, and decision criteria."),
                    ("Draft", "Create a structured recommendation or content draft."),
                    ("Check & hand off", "Validate, log, and pause for the authorised person."),
                ],
            ),
            dict(
                title="Profile and Personal-Brand Value Stack",
                paragraphs=[
                    "The introduction section is the first profile area many visitors see. A strong headline states credible role or capability, the audience or problem served, and a differentiating proof point. The About section expands this into a concise story: current focus, audience value, evidence, point of view, and invitation to continue the conversation.",
                    "Optimisation is not keyword repetition. LinkedIn advises members to keep profiles rich, accurate, and complete and to avoid keyword stuffing, inflated experience, and using a personal profile as an advertisement. Every AI edit therefore needs a source note and an accuracy check by the profile owner.",
                ],
                visual=[
                    ("Identity", "What you genuinely do and can substantiate."),
                    ("Audience", "Who benefits and what they care about."),
                    ("Value", "The useful outcome you help create."),
                    ("Proof", "Specific experience, examples, or evidence you may claim."),
                ],
            ),
            dict(
                title="The G-C-A-T-E Prompt Contract",
                paragraphs=[
                    "A prompt contract is a reusable instruction set, not a one-off clever phrase. G-C-A-T-E names the Goal, Context, Audience, Task, Evidence, and Evaluation requirements. It also defines allowed tools, output shape, human gates, and failure behaviour.",
                    "A good contract makes missing information visible. If a proof point is absent, the agent writes UNKNOWN or asks for it; it does not invent a client result. Evaluation criteria should include factual support, professional relevance, voice match, platform fit, and a clear next action.",
                ],
                visual=[
                    ("G - Goal", "Name the decision or useful outcome."),
                    ("C/A - Context & Audience", "Supply approved facts and reader needs."),
                    ("T/E - Task & Evidence", "Specify output and traceable inputs."),
                    ("E - Evaluation", "Define checks, limits, and stop conditions."),
                ],
            ),
            dict(
                title="Risk Tiers and Approval Gates",
                paragraphs=[
                    "Risk increases when a workflow moves from synthetic analysis to external action. Reading a supplied brand brief is low risk; drafting a profile or message is medium risk; publishing, inviting, messaging, processing personal data, or changing account settings is high risk.",
                    "An approval gate states the action, owner, evidence packet, decision options, and rollback. A useful status vocabulary is DRAFT, READY FOR HUMAN REVIEW, APPROVED BY ROLE, and STOP - REASON. The agent must never treat silence as approval.",
                ],
                visual=[
                    ("Low", "Synthetic or approved read-only analysis."),
                    ("Medium", "Drafts and recommendations that remain internal."),
                    ("High", "External action, personal data, identity, or reputation."),
                    ("Gate", "Named owner reviews evidence before any high-risk step."),
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Content Creation and Personal Branding with AI",
        subtitle="Ideas and hooks | posts and articles | content calendar | visuals and carousels | authentic voice",
        concepts=[
            ("Audience job", "Every item answers a professional question, reduces uncertainty, or enables a useful next step."),
            ("Content pillars", "A small set of repeatable themes makes the brand recognisable without becoming repetitive."),
            ("Hook-to-value", "The opening earns attention; the body delivers evidence or insight; the close offers a proportionate next action."),
            ("Format fit", "Short posts, articles, documents, images, and video serve different depth and consumption needs."),
            ("Series logic", "A calendar sequences ideas so one item prepares the audience for the next instead of publishing isolated pieces."),
            ("Voice fingerprint", "Sentence rhythm, vocabulary, stance, examples, and boundaries make a draft sound like the real professional."),
            ("Creative brief", "A visual or carousel starts with one message, a slide-by-slide hierarchy, accessibility, and rights checks."),
            ("Review before release", "Fact, claim, voice, rights, confidentiality, and relevance checks occur before scheduling or publication."),
        ],
        teaching_sections=[
            dict(
                title="The Audience-Value-Action Content Model",
                paragraphs=[
                    "Useful LinkedIn content begins with the audience's professional question, not with a format or a request to promote an offer. The content provides one clear value unit such as a framework, interpretation, example, checklist, or informed point of view, then proposes a proportionate action.",
                    "A post about procurement risk might explain three warning signs and invite readers to compare their own process. The call to action should match readiness: reflect, comment, save, read, follow, or begin a relevant conversation. A strong draft does not force every reader directly into a sales call.",
                ],
                visual=[
                    ("Audience question", "What is the reader trying to decide or do?"),
                    ("Value unit", "What insight, example, or tool will help?"),
                    ("Proof", "Which approved evidence supports the point?"),
                    ("Proportionate action", "What natural next step fits readiness?"),
                ],
            ),
            dict(
                title="Hooks, Bodies, and Credible Calls to Action",
                paragraphs=[
                    "A hook creates a relevant information gap without exaggeration. It can name a costly misconception, a surprising but supported observation, a concrete problem, or a useful promise. The body must then pay off that promise with evidence, reasoning, and a practical takeaway.",
                    "The close should not undermine trust with a generic pitch. It can invite a specific professional response, offer a useful resource, or name the next item in a series. Claims, client outcomes, and quotations must be traceable to approved sources before they appear in any draft.",
                ],
                visual=[
                    ("Hook", "Earn attention with relevance, not clickbait."),
                    ("Tension", "Name the decision, misconception, or risk."),
                    ("Value", "Deliver evidence, framework, or example."),
                    ("Close", "Invite a fitting response or next step."),
                ],
            ),
            dict(
                title="Choose the Right LinkedIn Format",
                paragraphs=[
                    "A short post is suited to one focused idea; an article supports sustained reasoning; a document post can turn a framework into a swipeable sequence; an image can make a single relationship memorable; and video can demonstrate a process or point of view. Format follows the audience job.",
                    "LinkedIn supports text, images, video, polls, events, documents, and articles. Interface details can change, so the workflow should store the content objective and source material independently of a specific button or layout. The human publisher verifies the current interface at release time.",
                ],
                visual=[
                    ("Short post", "One idea, fast context, discussion."),
                    ("Article", "Longer argument, evidence, and depth."),
                    ("Document/carousel", "Sequenced framework or tutorial."),
                    ("Image/video", "Visual explanation, proof, or demonstration."),
                ],
            ),
            dict(
                title="Build a Voice Fingerprint",
                paragraphs=[
                    "Authenticity can be specified. A voice fingerprint describes preferred vocabulary, sentence length, stance, level of formality, recurring examples, claims the author will not make, and words that feel unlike them. Approved writing samples are stronger evidence than vague labels such as professional or engaging.",
                    "AI should propose alternatives, not erase the author's point of view. The owner compares the draft with the voice fingerprint, rewrites at least one passage, and records why. This review loop gradually improves the instruction set without pretending the model has become the person.",
                ],
                visual=[
                    ("Sound", "Rhythm, formality, and preferred vocabulary."),
                    ("Substance", "Point of view, examples, and evidence style."),
                    ("Boundaries", "Banned clichés, unsupported claims, private topics."),
                    ("Human edit", "Owner restores nuance and accountability."),
                ],
            ),
            dict(
                title="Content Calendar as a Learning Sequence",
                paragraphs=[
                    "A content calendar is a hypothesis about how ideas compound. It balances content pillars, audience stages, formats, evidence availability, and production capacity. Each item has an objective, owner, source, review status, planned date, and intended measurement.",
                    "The calendar should preserve slack for timely responses and should not automate publication simply because a date arrived. LinkedIn's native scheduler can hold approved posts, but the final owner still reviews facts, tone, links, media, audience, and timing before scheduling.",
                ],
                visual=[
                    ("Plan", "Pillar, audience stage, value, format, source."),
                    ("Create", "Draft copy and visual direction."),
                    ("Review", "Fact, voice, rights, privacy, and relevance."),
                    ("Schedule & learn", "Human schedules; metrics inform the next cycle."),
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Lead Generation and Outreach with AI Agents",
        subtitle="Prospect research | segmentation | personalised invitations and messages | nurture sequences | social-selling etiquette",
        concepts=[
            ("Authorised evidence", "Use supplied, consented, or legitimately accessible information; never scrape profiles or infer sensitive traits."),
            ("Ideal-customer criteria", "Segment by relevant business context, need, fit, timing, and relationship evidence rather than surface popularity."),
            ("Reason to connect", "A message earns attention by naming genuine context and a relevant professional reason."),
            ("Personalisation", "Use only a small number of verified details; do not create false familiarity or pretend an event occurred."),
            ("Invitation etiquette", "Quality and recognisability matter more than volume; excessive or unwanted invitations can restrict an account."),
            ("Nurture progression", "Each touch adds new value and gives the recipient an easy way to decline or disengage."),
            ("Intent and risk", "Questions, objections, complaints, privacy requests, and sensitive topics require different handling and escalation."),
            ("Human send", "The agent drafts and prioritises; the account owner checks the recipient, context, wording, and timing before sending."),
        ],
        teaching_sections=[
            dict(
                title="Evidence-Based Prospecting Without Scraping",
                paragraphs=[
                    "Prospect research begins with an ideal-customer hypothesis and authorised evidence. Useful fields include organisation type, role relevance, publicly stated business context, relationship path, observed need, source, date, confidence, and an explicit reason to engage.",
                    "The workflow must not use scripts, browser extensions, or bots to copy LinkedIn profiles or activity. LinkedIn's User Agreement prohibits scraping and unauthorised automated access. In this course, all prospect work uses synthetic records so learners can practise segmentation without processing a real person's data.",
                ],
                visual=[
                    ("Criteria", "Role, organisation, need, fit, timing."),
                    ("Source", "Authorised record with date and provenance."),
                    ("Confidence", "Observed fact, supported inference, or unknown."),
                    ("Reason", "A relevant, professional basis for engagement."),
                ],
            ),
            dict(
                title="Segmentation as a Decision Rule",
                paragraphs=[
                    "A segment is useful when it changes the next action. A simple decision table can combine fit, evidence strength, relationship context, urgency, and risk to produce PRIORITISE, NURTURE, HOLD, or DO NOT CONTACT. The rule should be explainable and reversible.",
                    "AI may summarise or apply the rule, but it should not invent missing attributes or infer protected or sensitive characteristics. Low confidence should lower the action, not trigger more aggressive data collection.",
                ],
                visual=[
                    ("Prioritise", "Strong fit, relevant context, adequate evidence."),
                    ("Nurture", "Potential fit, value can be offered without pressure."),
                    ("Hold", "Missing evidence, weak timing, or owner review needed."),
                    ("Do not contact", "No relevant reason, opt-out, or unacceptable risk."),
                ],
            ),
            dict(
                title="The Relevance Ladder for Outreach",
                paragraphs=[
                    "Personalisation is not inserting a first name into a generic pitch. Relevance grows from identity, to genuine context, to a specific professional reason, to useful value, and only then to a low-friction next step. Each rung must be true and appropriate to use.",
                    "If the only available detail is a job title, the message should remain modest. The agent must not fabricate a shared interest, praise content it has not been given, or imply that it reviewed private activity.",
                ],
                visual=[
                    ("Identity", "Correct person and role."),
                    ("Context", "A verified shared event, topic, or business situation."),
                    ("Value", "A relevant idea, question, or resource."),
                    ("Next step", "A small, optional action with no pressure."),
                ],
            ),
            dict(
                title="Connection, Message, and Nurture Sequence",
                paragraphs=[
                    "A connection invitation explains who the sender is and why the connection is relevant. After acceptance, a first message should continue the context rather than immediately switch to a hard pitch. Later touches should add distinct value and stop when the recipient declines, does not engage, or the evidence becomes stale.",
                    "LinkedIn places limits and restrictions on invitations to protect member experience, and advises context and personalisation. Exact product limits can vary by account and time. The workflow therefore never sets a volume target designed to evade restrictions; it emphasises quality, relevance, and owner judgement.",
                ],
                visual=[
                    ("Invite", "Recognisable identity and genuine reason."),
                    ("Welcome", "Acknowledge acceptance; continue the context."),
                    ("Value", "Share one useful insight or ask a relevant question."),
                    ("Stop or hand off", "Respect no response, decline, risk, or live interest."),
                ],
            ),
            dict(
                title="Social-Selling Etiquette and Escalation",
                paragraphs=[
                    "Professional outreach protects the recipient's agency. Messages are accurate, concise, specific, and easy to ignore or decline. The sender does not create false urgency, disguise commercial intent, repeat unanswered requests indefinitely, or move personal data into unapproved tools.",
                    "Escalation is part of the workflow. Legal questions, privacy requests, complaints, sensitive personal circumstances, high-value commercial commitments, and requests outside the sender's authority go to a named human owner with the original context preserved.",
                ],
                visual=[
                    ("Relevant", "Clear professional reason and audience value."),
                    ("Respectful", "No pressure, deception, or false familiarity."),
                    ("Bounded", "Limited sequence with stop conditions."),
                    ("Escalated", "Sensitive or high-impact cases go to the owner."),
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Automating and Scaling LinkedIn with AI Agents",
        subtitle="Agentic content and engagement workflows | scheduling and follow-up | measurement | responsible scale",
        concepts=[
            ("Workflow states", "Intake, validate, draft, review, approve, schedule, observe, and learn are explicit states with owners."),
            ("Allowed automation", "Automate internal preparation and analysis; use LinkedIn's authorised features or approved integrations for external actions."),
            ("Approval packet", "The reviewer sees source evidence, draft, checks, risks, intended audience, and proposed action in one place."),
            ("Operational trace", "Every run records inputs, version, reviewer, decision, action, timestamp, and exception."),
            ("Metric definition", "Impressions, reach, reactions, comments, reposts, saves, sends, profile viewers, and followers answer different questions."),
            ("Rates need denominators", "Engagement and conversion rates are meaningful only when numerator, denominator, scope, and period are explicit."),
            ("Diagnose before changing", "Check data quality, audience mix, content, distribution, and downstream action before blaming the agent."),
            ("Bounded scale", "Change one controlled variable, define a guardrail, owner, observation window, cooldown, and rollback."),
        ],
        teaching_sections=[
            dict(
                title="A Draft-First LinkedIn Operations Workflow",
                paragraphs=[
                    "A governed workflow separates internal automation from external platform action. The agent can collect an approved brief, validate required fields, draft content or replies, run checks, and assemble a review packet. A human then approves, revises, or stops the item.",
                    "External action uses LinkedIn's own features or an organisation-approved integration operating within current terms and permissions. Unauthorised bots that send messages, create engagement, or access the service are outside the workflow boundary.",
                ],
                visual=[
                    ("Intake", "Approved request, sources, owner, and due date."),
                    ("Draft", "Agent creates a structured internal artefact."),
                    ("Review", "Human checks evidence, voice, risk, and timing."),
                    ("Release", "Authorised feature executes; result is logged."),
                ],
            ),
            dict(
                title="Approval Packet and Exception Path",
                paragraphs=[
                    "Approval fails when the reviewer has to reconstruct the context. A compact packet includes the objective, intended audience, source links, draft, evaluation results, known unknowns, risk tier, proposed action, and rollback or correction path.",
                    "Exceptions are normal. Missing evidence returns to intake; a policy concern stops the run; a voice mismatch returns for revision; an urgent complaint escalates to an owner. The workflow records why the path changed so later improvement is based on evidence.",
                ],
                visual=[
                    ("Context", "Goal, audience, source, owner."),
                    ("Draft", "Exact proposed post, message, or response."),
                    ("Checks", "Fact, voice, policy, privacy, rights, timing."),
                    ("Decision", "Approve, revise, stop, or escalate with reason."),
                ],
            ),
            dict(
                title="LinkedIn Measurement Tree",
                paragraphs=[
                    "Discovery metrics describe exposure; engagement metrics describe interaction; profile activity describes movement toward the professional identity; and business outcomes describe what happened beyond LinkedIn. These layers should be reported separately.",
                    "LinkedIn notes that member post analytics are estimates and may include the author's own activity. A sound report states the source, extraction date, scope, and limitations. It never converts an estimated impression directly into revenue without an evidence bridge.",
                ],
                visual=[
                    ("Discovery", "Impressions, members reached, in/out of network."),
                    ("Engagement", "Reactions, comments, reposts, saves, sends, link visits."),
                    ("Profile action", "Profile viewers and followers attributed to a post."),
                    ("Business outcome", "Qualified replies, meetings, opportunities, or another owned result."),
                ],
            ),
            dict(
                title="Metric Formulas and Interpretation",
                paragraphs=[
                    "A rate is a contract between a numerator and denominator. For a simple synthetic exercise, engagement rate may be defined as total selected interactions divided by impressions. Reply rate may be replies divided by messages sent. The definition must be recorded because tools and teams may include different interactions.",
                    "Small denominators, short windows, outliers, and changed audience mix can create unstable rates. Report counts beside rates, compare like with like, and avoid declaring a winner from one post or one outreach batch.",
                ],
                visual=[
                    ("Engagement rate", "Selected interactions / impressions x 100."),
                    ("Profile-view rate", "Profile viewers from post / impressions x 100."),
                    ("Reply rate", "Replies / messages sent x 100."),
                    ("Outcome rate", "Qualified outcomes / relevant opportunities x 100."),
                ],
            ),
            dict(
                title="Responsible Scaling Loop",
                paragraphs=[
                    "Scaling is a controlled learning loop, not more output. The team validates the data, diagnoses the likely bottleneck, chooses one change, predicts the effect, names a guardrail, obtains approval, observes for a defined window, and then holds, adapts, or rolls back.",
                    "A bounded recommendation includes the owner, change limit, observation window, cooldown, stop threshold, and rollback. The agent recommends; it does not change publishing frequency, messaging activity, or account behaviour on its own.",
                ],
                visual=[
                    ("Validate", "Check completeness, definitions, and comparability."),
                    ("Diagnose", "Identify the most plausible constrained bottleneck."),
                    ("Propose", "Change one variable with predicted effect and guardrail."),
                    ("Observe", "Human approves; record result, cooldown, and rollback."),
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Agent foundations, profile, prompting, and content systems",
    2: "Prospecting, outreach, governed workflows, and improvement",
}


def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:00", "9:20", 20, "admin", "Welcome, outcomes, learning approach, and responsible-use boundary"),
            ("9:20", "10:10", 50, "topic", "Topic 1 - LinkedIn strategy, AI-agent foundations, tools, and human authority"),
            ("10:10", "10:25", 15, "break", "Tea break"),
            ("10:25", "11:10", 45, "topic", "Topic 1 - Profile value stack, personal brand, evidence, and G-C-A-T-E prompting"),
            ("11:10", "12:00", 50, "lab", "Hands-on: " + lab_titles([1])),
            ("12:00", "13:00", 60, "lab", "Hands-on: " + lab_titles([2])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:00", 60, "topic", "Topic 2 - Audience value, content pillars, hooks, posts, and articles"),
            ("15:00", "15:45", 45, "lab", "Hands-on: " + lab_titles([3])),
            ("15:45", "16:00", 15, "break", "Tea break"),
            ("16:00", "16:40", 40, "topic", "Topic 2 - Voice, visuals, carousels, content calendars, and review"),
            ("16:40", "17:40", 60, "lab", "Hands-on: " + lab_titles([4])),
            ("17:40", "18:00", 20, "recap", "Day 1 recap, artifact checkpoint, and retrieval practice"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:00", "9:15", 15, "recap", "Day 1 retrieval practice and connected-artifact check"),
            ("9:15", "10:15", 60, "topic", "Topic 3 - Authorised prospect research, segmentation, relevance, and fit"),
            ("10:15", "10:30", 15, "break", "Tea break"),
            ("10:30", "11:15", 45, "topic", "Topic 3 - Connection messages, nurture sequences, etiquette, and escalation"),
            ("11:15", "12:05", 50, "lab", "Hands-on: " + lab_titles([5])),
            ("12:05", "13:00", 55, "lab", "Hands-on: " + lab_titles([6])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:00", 60, "topic", "Topic 4 - Draft-first content, engagement, scheduling, and follow-up workflows"),
            ("15:00", "15:45", 45, "lab", "Hands-on: " + lab_titles([7])),
            ("15:45", "16:00", 15, "break", "Tea break"),
            ("16:00", "16:45", 45, "topic", "Topic 4 - Analytics, diagnosis, controlled experiments, and responsible scale"),
            ("16:45", "17:40", 55, "lab", "Hands-on: " + lab_titles([8])),
            ("17:40", "18:00", 20, "recap", "Course recap, implementation commitments, and next steps"),
        ]),
    }


COURSE_OVERVIEW = dict(
    section_title="Agentic LinkedIn Marketing Fundamentals",
    concepts_title="Four Ideas to Keep in View",
    concepts=[
        ("Strategy", "Tie profile, content, outreach, and measurement to one decision chain."),
        ("Evidence", "Keep approved facts, labelled hypotheses, and unknowns distinct."),
        ("Human authority", "External actions stay behind named approval gates."),
        ("Learning loop", "Validate, diagnose, propose one change, observe, and record."),
    ],
    framework_title="The G-C-A-T-E Agent Contract",
    framework=[
        ("Goal", "Define the decision and useful outcome."),
        ("Context & Audience", "Supply approved sources and reader needs."),
        ("Task & Evidence", "Specify the output and traceability rules."),
        ("Evaluation", "Set checks, permissions, stop conditions, and handoff."),
    ],
    statement=dict(
        headline="Automate preparation; preserve professional judgement.",
        body="The agent researches approved inputs, drafts, checks, and recommends. A person owns identity, relationships, publication, messaging, and correction.",
        kicker="OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Brand & Content", ["Profile value stack", "Voice fingerprint", "Content kit and calendar"]),
        ("Prospect & Outreach", ["Evidence-based segments", "Personalised draft sequence", "Etiquette and escalation"]),
        ("Operate & Improve", ["Draft-first workflow", "Approval packet", "Metric-led improvement loop"]),
    ],
    arc_title="The Connected Learning Arc",
    arc=[
        "Frame the goal, profile, evidence, tools, and authority boundary.",
        "Turn those decisions into a tested reusable prompt contract.",
        "Create content and a calendar using the same voice and evidence.",
        "Segment synthetic prospects and draft respectful outreach.",
        "Design a governed workflow, measure results, and recommend one bounded improvement.",
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide is the self-contained study text for Agentic AI for Linkedin Marketing (C386). "
    "It explains the strategy, agent-design, personal-brand, content, prospecting, outreach, workflow, and measurement concepts before the connected labs that apply them."
)
LG_INTRO2 = (
    "Across eight labs you build one synthetic Northstar Advisory LinkedIn marketing pack. Each output becomes an input to the next lab. "
    "All profile edits, posts, invitations, messages, scheduling, and account actions remain drafts or simulations until an authorised person reviews and executes them."
)

LG_SETUP = dict(
    needs=[
        "A laptop, text or Markdown editor, and spreadsheet application.",
        "An organisation-approved generative AI assistant such as ChatGPT, Microsoft Copilot, Claude, or Google Gemini.",
        "The synthetic files in labs/resources; no real prospect, customer, employee, or account data is required.",
        "Optional view-only access to your own LinkedIn profile or Page for interface orientation; do not change or publish anything during a lab unless your trainer explicitly authorises it.",
    ],
    verify_text="Confirm that you can open Markdown and CSV files and create a local folder named C386-linkedin-pack. You do not need an API key, browser extension, scraper, or messaging automation tool.",
    verify_code="Folder: C386-linkedin-pack\nFiles: 01-foundation-profile-and-boundaries.md through 08-performance-diagnosis-and-improvement.md",
    conventions=[
        "Use FACT, HYPOTHESIS, and UNKNOWN labels whenever source support differs.",
        "Use DRAFT, READY FOR HUMAN REVIEW, APPROVED BY <ROLE>, and STOP - <REASON> for workflow status.",
        "Use synthetic records and placeholder values; never paste passwords, cookies, access tokens, private messages, or real prospect data into an AI tool.",
        "Treat LinkedIn interfaces and product limits as changeable; verify current official help before workplace use.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic case files and an approved AI assistant. Do not scrape LinkedIn, use unauthorised bots or browser extensions, mass-send invitations or messages, publish automatically, or paste credentials or real personal data into prompts."
)

LABS_SETUP = [
    "Start from the repository root so paths such as labs/resources/<file> resolve consistently.",
    "Confirm access to an organisation-approved AI assistant, a text or Markdown editor, and a spreadsheet application that can open CSV files.",
    "Create the local working folder C386-linkedin-pack; keep all numbered outputs and review logs inside it.",
    "Use only the supplied synthetic resources. No live LinkedIn action, real prospect data, scraper, browser automation, credential, or API key is required.",
]

REJOIN_PATHS = [
    (2, "01-foundation-profile-and-boundaries.md", "Five journey stages, six profile-value elements, seven tool roles, and all high-risk human gates pass Lab 1 Test It."),
    (3, "01-foundation-profile-and-boundaries.md + 02-linkedin-agent-contract.md", "The contract cites sources, labels unknowns, remains draft-only, and blocks all six denied or unsafe test requests."),
    (4, "03-profile-voice-and-content-kit.md", "Eight voice dimensions, three headline options, one About draft, four posts, article outline, and six-page carousel all have evidence and human edits."),
    (5, "01-foundation-profile-and-boundaries.md + 04-content-calendar-and-workflow.md", "Audience, value, status vocabulary, and human scheduling boundary are explicit and current."),
    (6, "05-prospect-segmentation-queue.md", "Only PRIORITISE or NURTURE rows with verified contact basis are READY FOR MESSAGE DRAFT; all holds and stops are preserved."),
    (7, "04-content-calendar-and-workflow.md + 06-outreach-and-nurture-sequence.md", "Content and outreach drafts carry sources, checks, owners, stop conditions, and no external action."),
    (8, "01-foundation-profile-and-boundaries.md + 04-content-calendar-and-workflow.md + 07-governed-operations-workflow.md", "Primary metric and guardrails are defined; approval packet and trace schema pass all six Lab 7 simulations."),
]

LG_WRAPUP = dict(
    title="Wrap-Up - From Drafts to a Governed Operating System",
    intro="Your completed C386-linkedin-pack is a connected operating design, not a collection of isolated prompts.",
    sections=[
        dict(title="What the pack proves", bullets=[
            "Strategy, profile, content, prospecting, outreach, workflow, and metrics point to the same audience value and business result.",
            "Every agent task has approved inputs, an output schema, checks, permissions, stop conditions, and a named human owner.",
            "Every recommendation can be traced to evidence and reversed or revised without hidden external action.",
        ]),
        dict(title="Before workplace use", bullets=[
            "Replace synthetic inputs only with data your organisation is authorised to use.",
            "Verify current LinkedIn terms, help guidance, account permissions, and product behaviour.",
            "Run a small draft-only pilot, review errors, and approve each external action manually.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "Re-run the eight labs with a different synthetic B2B offer to test whether the system generalises.",
    "Ask a colleague to review three random facts, one profile claim, one content draft, and one outreach draft against the evidence packet.",
    "Pilot one approved content series with a human publisher and record the current LinkedIn interface and metric definitions.",
    "Review invitation, messaging, privacy, and automation rules before any real outreach workflow is considered.",
]

LG_GLOSSARY = [
    ("Agent", "A system that uses a model, tools, and instructions to manage a multi-step goal within defined guardrails."),
    ("Approval gate", "A workflow stop where a named person reviews evidence and decides whether an external action may proceed."),
    ("Content pillar", "A repeatable subject area that connects audience needs, brand expertise, and business relevance."),
    ("Evidence boundary", "The rule that separates approved facts, supported inference, and unknown information."),
    ("Engagement rate", "A defined set of interactions divided by a stated denominator, usually impressions, multiplied by 100."),
    ("G-C-A-T-E", "Goal, Context, Audience, Task, Evidence, and Evaluation - a reusable prompt-contract structure."),
    ("Human-in-the-loop", "A design in which a person reviews or decides before a consequential action."),
    ("Impressions", "LinkedIn's estimate of the number of times a post was shown."),
    ("Members reached", "LinkedIn's estimate of distinct members and Pages that saw a post."),
    ("Nurture sequence", "A bounded series of relevant, value-adding contacts with explicit stop conditions."),
    ("Personalisation", "The use of verified and appropriate context to make communication relevant without fabricating familiarity."),
    ("Rollback", "The predefined response that returns a workflow to a safe state after an unwanted result."),
    ("Voice fingerprint", "A documented description of vocabulary, rhythm, stance, examples, and boundaries that characterise a person's writing."),
]

NEXT_STEPS = dict(
    title="Continue Responsibly",
    items=[
        "Keep the agent recommendation-only until evidence quality and review consistency are demonstrated.",
        "Verify current LinkedIn help and terms before any operational change.",
        "Measure the complete decision chain, not just impressions or activity volume.",
        "Use small controlled changes with an owner, guardrail, observation window, and rollback.",
    ],
)

THANK_YOU = dict(
    body="You can now design a useful, evidence-grounded LinkedIn marketing workflow in which AI accelerates preparation and people retain responsibility for identity, relationships, and external action.",
    kicker="C386 | KEEP THE HUMAN ACCOUNTABLE",
)

VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release of slides, Learner Guide, Lesson Plan, and eight connected labs.", TRAINER),
]
