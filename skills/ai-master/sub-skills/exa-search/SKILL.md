---
name: exa-search
description: "Neural search via Exa MCP for web, code, and company research. USE WHEN: user needs latest web/news information; finding code examples or API references. NOT FOR: full multi-theme research report synthesis; framework documentation resolution workflows."
origin: ECC
---

# Exa Search

Use Exa MCP as a focused retrieval layer for web, code, company, and people intelligence.

---

## Purpose

Provide fast, current, source-linked retrieval using Exa tools.
This skill emphasizes retrieval operations, not full research synthesis.

---

## When to Activate

- user needs latest web/news information
- finding code examples or API references
- company/competitor intelligence lookup
- people/profile discovery in a specific domain
- user asks search, look up, find, latest on

---

## Scope Boundaries

Use this skill for:
- selecting the right Exa tool for the query type
- applying date/domain filters for precision
- extracting full content from selected URLs
- returning concise, source-linked findings

Do NOT use this skill as primary source for:
- full multi-theme research report synthesis
- framework documentation resolution workflows
- long-form editorial writing

Delegation:
- Use deep-research when the user asks for a full cited synthesis report.
- Use documentation-lookup for library/framework API behavior via Context7.

---

## MCP Requirement

Exa MCP must be configured in the active harness.
If unavailable, state that constraint and fallback to available web retrieval tools.

---

## Tool Selection Matrix

- `web_search_exa`: broad, current web lookup
- `web_search_advanced_exa`: constrained search by domain/date
- `get_code_context_exa`: code/API snippets and technical references
- `company_research_exa`: company-focused intelligence
- `people_search_exa`: people/profile lookup
- `crawling_exa`: full-page extraction for deep reading
- `deep_researcher_start` + `deep_researcher_check`: async deep Exa research jobs

---

## Query Strategy

1. Start broad, then narrow.
2. Use 2 to 3 query variants for ambiguous topics.
3. Apply include/exclude domains for precision.
4. Add recency filters for fast-moving topics.
5. Extract full text for top URLs before concluding.

Recency defaults:
- news/current state: last 3 to 12 months
- stable references/docs: no strict date filter unless requested

---

## Execution Workflow

## Step 1: Clarify Intent

Identify one primary mode:
- web/news
- code context
- company intel
- people lookup
- async deep job

## Step 2: Run Primary Exa Search

Execute with tight query phrasing and sensible `numResults`.
Prefer 3 to 8 results first, then expand only if needed.

## Step 3: Refine with Filters

Use advanced search with:
- includeDomains for trusted sources
- excludeDomains for low-signal sources
- date boundaries for recency control

## Step 4: Deep-Read Selected URLs

Use `crawling_exa` on top candidates to verify details and capture evidence.

## Step 5: Return Findings

Provide concise findings with source links, uncertainty notes, and next-step options.

---

## Async Deep Research Pattern

Use when topic is broad and synthesis-heavy:
1. start `deep_researcher_start`
2. continue other work while running
3. poll using `deep_researcher_check`
4. summarize outputs with explicit source attribution

Rule:
- do not block interactive flow waiting idly if async job can run in background.

---

## Reliability and Safety Rules

1. Do not present unsourced factual claims.
2. Mark single-source claims as tentative.
3. Prefer reputable/official domains for sensitive claims.
4. Redact secrets from tool queries.
5. If Exa unavailable or incomplete, state limitation explicitly.

---

## Output Format

When activated, return:

1. search objective and selected Exa mode
2. key findings (bullet points)
3. source list (titles + URLs)
4. confidence and uncertainty notes
5. optional follow-up queries

---

## Related Skills

- deep-research for full multi-source synthesis workflow
- documentation-lookup for library/framework docs via Context7
