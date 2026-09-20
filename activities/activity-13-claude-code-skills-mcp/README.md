# Activity 13 — Claude Code Skills and MCP Audit

LO2 · C386 · v1.0

# Goal

A reproducible research workspace stores evidence, code and review rules. A local read-only MCP connector or CSV fallback supplies synthetic channel metrics; a custom Skill defines research checks without granting tools or overriding permissions.

# Before you start

Use a copied activity folder,Claude Cowork or Claude Code as specified,and a spreadsheet or Python3 for independent checks. No production credentials are needed. Product access varies;CSV fallback remains valid.

# Mock data and assets

mock-data/tool-results.csv
All named customers,competitors,campaigns and values are fictional. Assets include brand,source,measurement and decision contracts.

# Mechanism

User question -> reviewed Skill -> approved read-only MCP tool -> schema validation -> deterministic calculation -> source-linked report -> reviewer. CSV fallback tests the same data contract.
The Cowork ebooks and Coupler custom-workflow examples inform reusable instruction packaging; current Anthropic Code documentation governs Skill paths and MCP configuration. Windsor’s analytics context motivates currency,time-zone and grain checks before aggregation.

# Worked calculation

Lead rates: paid 5%,organic 4%,email 8%,direct 1%; total 96/2400=4%. A Skill’s instructions do not create connector access.

# Step-by-step

1. Read assets/research-context.md and assets/market-evidence-audit/SKILL.md;inspect the read-only MCP server source.
2. Copy the activity folder to a dedicated working directory;open a terminal there and run python3 validate.py for actual CSV metric checks.
3. Run python3 test_mcp.py. Verify actual local initialize,tools/list and tools/call responses;no live account is connected.
4. For Claude Code,use the current official installation and launch claude inside the copy. Place the reviewed Skill under .claude/skills/market-evidence-audit/SKILL.md.
5. Register the local server only after reviewing its single read-only tool: claude mcp add --transport stdio --scope project synthetic-market-metrics -- python3 "$PWD/mcp_metrics_server.py". Review the project configuration before approving.
6. Within Claude Code,inspect /mcp and allow only read_synthetic_metrics. Submit Prompt1 and compare returned source IDs M01–M04 to the CSV.
7. For Cowork custom Skills,zip assets/market-evidence-audit with SKILL.md at the root;ensure Code execution and file creation is enabled,then open Customize > Skills > + > Create skill > Upload a skill and upload the ZIP. Enable it and verify the task actually used it;copying .claude files does not install a Cowork Skill.
8. Review generated code,run its calculation,and verify5%,4%,8%,1%,overall 4%. Save output,tool provenance and human review;state local protocol test versus actual Claude connector invocation separately.

# Prompt1

Build a reproducible synthetic research analysis. Read the supplied Skill and tool-results.csv. Preserve source IDs, validate schema and calculate rates. If MCP is unavailable, use CSV fallback and record it. Do not install or connect to a live account without authorisation.

# Prompt2

Challenge the previous result. Find denominator errors,unsupported claims,bias,privacy risks and unexecuted tool boundaries. Cite exact row IDs or fields. Revise the report without inventing data.

# Acceptance evidence

Four source IDs retained; rates 5%,4%,8%,1%,overall 4%; local MCP initialize/list/call test passes; Skill front matter valid; Claude invocation separately evidenced;no live account claimed.

# Failure and recovery

The agent treats the Skill as permission to access a production account. Instruction reuse and tool authorisation are separate controls.
Inspect tool scope and data destinations; use read-only synthetic connector, no secrets in repository. Require approval for new network endpoints and use local fallback if account access is unavailable.

# Submit

SKILL.md,analysis.py and tool-audit.md
Save outputs in this working copy. Keep an execution note stating which product actions actually ran and which used fallback.
