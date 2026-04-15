---
name: documentation-lookup
description: "Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup questions, API references, code examples, or when the user names a framework (for example React, Next.js, Prisma). USE WHEN: setup or configuration questions for a specific library/framework; API reference lookups and method behavior questions. NOT FOR: architecture decisions unrelated to library API details; broad market research or competitive analysis."
origin: ECC
---

# Documentation Lookup (Context7)

Use live documentation for libraries/frameworks instead of relying on model memory when correctness depends on current API behavior.

---

## Purpose

Provide accurate, current answers for setup, API usage, and code examples with source-backed references.

---

## When to Activate

- setup or configuration questions for a specific library/framework
- API reference lookups and method behavior questions
- code generation requests tied to library-specific syntax
- user explicitly names a library/framework/version

Typical triggers:
- React, Next.js, Prisma, Supabase, Express, Tailwind, Vue, Svelte, etc.

---

## Scope Boundaries

Use this skill for:
- resolving correct docs source
- retrieving current API guidance
- citing version-relevant behavior in answers

Do NOT use this skill as primary source for:
- architecture decisions unrelated to library API details
- broad market research or competitive analysis
- style-only content tasks

---

## Preferred Tool Flow (Context7)

### Step 1: Resolve Library ID

Use `resolve-library-id` first.
Inputs:
- `libraryName`: library name from user request
- `query`: full user question for better ranking

Rule:
- Do not call `query-docs` before resolving a valid library ID.

### Step 2: Select Best Match

Choose one result using:
1. closest name match
2. highest benchmark score
3. source reputation
4. version alignment (if user requested specific version)

### Step 3: Query Docs

Use `query-docs` with:
- resolved `libraryId`
- specific user task/question

Call budget:
- max 3 total Context7 calls per user question (resolve and query combined where practical).
- if unclear after budget is exhausted, state uncertainty and provide best-supported answer.

### Step 4: Answer with Evidence

- provide concise answer based on fetched docs
- include minimal relevant snippet
- mention library/version when behavior is version-dependent

---

## Fallback Strategy (When Context7 is Unavailable)

If Context7 tools are not available in the current harness:
1. use available web/documentation fetch tools
2. prioritize official documentation sites
3. explicitly state the fallback method and confidence level
4. avoid definitive claims when docs cannot be verified

Rule:
- never fabricate API signatures or options.

---

## Security and Privacy Rules

- redact secrets from queries before tool calls
- never send API keys, tokens, passwords, or internal credentials
- do not paste private code unless user explicitly requests and approves

---

## Quality Rules

1. Prefer official docs over community summaries.
2. Respect version differences and deprecations.
3. Include only relevant options; avoid dumping large blocks.
4. Flag uncertainty instead of guessing.
5. Keep examples runnable and minimal.

---

## Output Format

When activated, return:

1. library resolved (and version if relevant)
2. direct answer to user question
3. minimal code example (if requested/useful)
4. notes on version caveats/deprecations
5. source attribution (doc page or provider)

---

## Examples

- "How do I configure Next.js middleware in v15?"
- "How do I query Prisma relations with include/select?"
- "What are Supabase auth methods and when to use each?"
- "How should I set Tailwind container and breakpoints in v4?"
