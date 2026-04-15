---
name: deep-research
description: "Multi-source deep research using web search and page extraction tools. Synthesizes findings into cited reports with source attribution. USE WHEN: user asks for in-depth research or investigation; competitive analysis, technology evaluation, market sizing. NOT FOR: brand voice derivation; social content adaptation."
origin: ECC
---

# Deep Research

Produce thorough, cited research reports from multiple web sources with explicit source attribution.

---

## Purpose

This skill is for evidence-heavy research and synthesis.
It is not a creative writing style skill.

---

## When to Activate

- user asks for in-depth research or investigation
- competitive analysis, technology evaluation, market sizing
- due diligence on companies, tools, or trends
- questions that require multi-source synthesis, not single-source summary
- prompts like: research, deep dive, investigate, current state

---

## Scope Boundaries

Use this skill for:
- defining research questions
- gathering sources across multiple domains
- cross-checking claims
- writing cited reports with confidence levels and gaps

Do NOT use this skill as primary source for:
- brand voice derivation
- social content adaptation
- opinion-only writing without evidence

Delegation:
- Use article-writing after research when user wants polished long-form output.

---

## Tooling Strategy

Preferred search/extraction stack:
- Exa tools (if available)
- Firecrawl tools (if available)

Fallback stack (always available in many environments):
- web fetch tools for reading pages
- browser open tools for source verification
- read-only subagent for broad parallel exploration

Rule:
- Do not block research only because one provider is missing.
- Use available tools and explicitly state methodology constraints.

---

## Workflow

## Step 1: Clarify Objective (Fast)

Ask up to 2 quick questions when needed:
- final use: learning, decision, or publication
- required depth and timeline

If user says just research it, proceed with sensible defaults.

## Step 2: Build Research Plan

Break topic into 3 to 5 sub-questions.
Each sub-question should be answerable with observable evidence.

## Step 3: Multi-Source Collection

For each sub-question:
- run 2 to 3 keyword variations
- mix overview, technical, and recent-news intent
- target 15 to 30 unique sources overall for broad topics

Source quality priority:
1. official docs, standards, filings, academic sources
2. reputable analysis and established media
3. vendor blogs and specialist publications
4. forums and social posts (context only, not primary proof)

## Step 4: Deep Read Key Sources

Read full content for top sources, not just snippets.
Target at least 3 to 5 full reads for medium-depth tasks.

## Step 5: Synthesize with Evidence

For each major finding:
- include claim
- include supporting citation(s)
- mark confidence: high, medium, low
- flag unverified or single-source claims

## Step 6: Deliver by Length

- short topic: full report in chat
- long topic: executive summary in chat plus full report body

---

## Parallelization Pattern

For broad topics, split sub-questions into parallel research tracks, then merge.

Example split:
1. market and ecosystem
2. technical architecture and trade-offs
3. regulation, risk, and outlook

Then reconcile overlaps and contradictions in one synthesis pass.

---

## Output Format

Use this structure:

```markdown
# [Topic]: Research Report
Generated: [date] | Sources reviewed: [N] | Confidence: [High/Medium/Low]

## Executive Summary
[3-6 sentences]

## Key Findings
### 1. [Theme]
- Finding with citation
- Supporting evidence with citation

### 2. [Theme]
...

## Contradictions and Uncertainty
- [What sources disagree on]
- [What remains unclear]

## Practical Takeaways
- [Actionable takeaway 1]
- [Actionable takeaway 2]
- [Actionable takeaway 3]

## Sources
1. [Title](url) - [one-line relevance]
2. ...

## Methodology
- Sub-questions investigated: [...]
- Query families used: [...]
- Source constraints or gaps: [...]
```

---

## Quality Rules

1. Every meaningful claim must have at least one citation.
2. Mark single-source claims as tentative.
3. Prefer sources from last 12 months unless historical context is required.
4. Separate facts from inference and forecast.
5. If evidence is insufficient, explicitly say insufficient data found.
6. Do not invent figures, quotes, or references.

---

## Hard Bans

Delete and rewrite if present:
- unsourced factual assertions
- fabricated citations
- confidence claims without evidence
- contradictory conclusions without acknowledgement

---

## Output Contract

When activated, return:

1. research framing and sub-questions
2. synthesized findings with citations
3. confidence and uncertainty notes
4. clear next-step recommendations or open gaps
