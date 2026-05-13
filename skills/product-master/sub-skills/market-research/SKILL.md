---
name: market-research
description: "Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and decision-oriented summaries. USE WHEN: researching a market, category, company, investor, or technology trend; building TAM/SAM/SOM estimates. NOT FOR: framework/API documentation lookup; purely technical implementation guidance."
origin: ECC
---

# Market Research

Produce research that supports decisions, not research theater.

---

## Purpose

Use this skill for decision-oriented business research: market, competition, investor fit, and technology/vendor landscape.

---

## When to Activate

- researching a market, category, company, investor, or technology trend
- building TAM/SAM/SOM estimates
- comparing competitors or adjacent products
- preparing investor dossiers before outreach
- pressure-testing a thesis before building, funding, or entering a market

---

## Scope Boundaries

Use this skill for:
- business and strategic research synthesis
- market sizing and competitive mapping
- investor/fund fit assessment
- recommendation framing under uncertainty

Do NOT use this skill as primary source for:
- framework/API documentation lookup
- purely technical implementation guidance
- social/content copywriting

Delegation:
- use `deep-research` when a broad evidence synthesis report is requested
- use `exa-search` for targeted retrieval-heavy lookup tasks
- use `investor-outreach` for outbound investor communications

---

## Research Standards

1. Every important claim needs a source.
2. Prefer recent data and flag stale data.
3. Include contrarian evidence and downside scenarios.
4. Translate findings into a decision, not just a summary.
5. Separate fact, inference, and recommendation explicitly.

---

## Core Workflow

1. define decision question and success criteria
2. break into focused research questions
3. collect multi-source evidence
4. score source quality and recency
5. synthesize findings with implications
6. produce recommendation with caveats and alternatives

---

## Common Research Modes

## Investor/Fund Diligence

Collect:
- fund size, stage, typical check size
- portfolio relevance and overlap
- public thesis and recent activity
- fit and mismatch rationale
- potential red flags and process risks

## Competitive Analysis

Collect:
- product reality vs marketing claims
- pricing, distribution, and positioning clues
- funding/investor history if public
- traction signals if public
- strengths, weaknesses, and whitespace opportunities

## Market Sizing

Use:
- top-down anchors from credible reports/datasets
- bottom-up sanity checks from realistic GTM assumptions
- explicit assumptions for each logical jump

## Technology/Vendor Research

Collect:
- how it works and integration model
- operational trade-offs and adoption signals
- lock-in, security, compliance, and reliability risk
- expected total cost and team complexity impact

---

## Decision Framing

For each conclusion include:
- evidence summary
- confidence level (high/medium/low)
- what would change the decision
- immediate next action

If evidence is weak, say so and recommend the minimum additional research needed.

---

## Output Format

Default structure:
1. executive summary
2. key findings
3. implications for decision
4. risks and caveats
5. recommendation
6. sources

Optional appendix:
- assumptions table
- scenario grid
- competitor comparison matrix

---

## Quality Gate

Before delivery:

- [ ] all material numbers are sourced or clearly labeled as estimates
- [ ] stale data is explicitly flagged
- [ ] recommendation follows from evidence
- [ ] counterarguments and risks are represented
- [ ] output makes a concrete decision easier

---

## Hard Bans

Do not ship:
- unsourced market numbers presented as fact
- one-sided analysis with no downside cases
- recommendations disconnected from evidence
- hidden assumptions in sizing math

---

## Output Contract

When activated, return:

1. decision question and scope
2. synthesized findings with source-backed claims
3. recommendation with confidence and caveats
4. key risks and disconfirming evidence
5. clear next-step options
