---
name: handoff
description: "Compact the current conversation into a handoff document for a fresh agent session to continue. USE WHEN: ending a long session, switching contexts, or preparing for another agent to pick up work. NOT FOR: writing plans (use `writing-plans`); creating PRDs (use `to-prd`)."
argument-hint: "What will the next session be used for?"
---

# Handoff

Write a handoff document summarising the current conversation so a fresh agent can continue the work.

## Scope Boundaries

Use this skill for:
- End-of-session context preservation
- Preparing for another agent or session to pick up work
- Capturing decisions, progress, and open questions

Do NOT use this skill for:
- Writing implementation plans — use `writing-plans`
- Creating PRDs — use `to-prd`
- Full context engineering — use `brain-context-engineering`

## Process

### 1. Summarize the session
Capture:
- **Goal**: What the session set out to accomplish
- **Progress**: What was completed, with file paths and key decisions
- **Open questions**: Unresolved decisions or ambiguities
- **Blocked items**: What couldn't be completed and why
- **Next steps**: What the next session should focus on

### 2. Reference, don't duplicate
Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

### 3. Suggest skills
If applicable, suggest which skills the next session should use.

### 4. Save the handoff
Save the handoff document to a discoverable location:
- `docs/handoffs/YYYY-MM-DD-<topic>.md` if the project has a docs structure
- Or alongside the artifacts the session produced

### 5. Tailor to the next session
If the user specifies what the next session will focus on, tailor the document accordingly — emphasize the relevant context and suppress the irrelevant.

## Template

```markdown
# Handoff — [Topic]

**Date:** YYYY-MM-DD
**Previous session goal:** [What we set out to do]

## Completed
- [x] Item 1 — [brief description, link to file/commit]
- [x] Item 2

## In Progress
- [/] Item 3 — [current state, what's left]

## Open Questions
1. [Decision needed about X — options are A or B]
2. [Clarification needed from user about Y]

## Blocked
- [Item blocked by Z — needs [action] to unblock]

## Next Steps
1. [First thing the next session should do]
2. [Second thing]

## Suggested Skills
- `skill-name` — for [reason]

## Key Files
- `path/to/file` — [what it is]
```
