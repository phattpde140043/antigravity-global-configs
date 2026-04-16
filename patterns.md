---
description: "Micro-patterns for Agent-to-Human communication and Git operations. Used to maintain transparency, scope discipline, and high-quality context."
---

# Agent Communication & Execution Patterns

## 1. The Confusion Management Pattern
Even with good context, you will encounter ambiguity. **Do NOT silently pick an interpretation.** Surface it explicitly:

```markdown
**CONFUSION:**
The spec calls for REST endpoints, but the existing codebase uses GraphQL for routing (src/graphql/user.ts).

**Options:**
A) Follow the spec — add REST endpoint, potentially deprecate GraphQL later.
B) Follow existing patterns — use GraphQL, update the spec.
C) Ask — this seems like an intentional decision I shouldn't override.

→ Which approach should I take?
```

## 2. The Missing Requirement Pattern
Don't invent requirements. If a case is not covered:
1. Check existing code for precedent.
2. If no precedent exists, stop and ask.

```markdown
**MISSING REQUIREMENT:**
The spec defines task creation but doesn't specify what happens with duplicate titles.

**Options:**
A) Allow duplicates (simplest).
B) Reject with validation error (strictest).
C) Append a number suffix like "Task (2)" (most user-friendly).

→ Which behavior do you want?
```

## 3. The Inline Planning Pattern (Micro-Plans)
For multi-step tasks within the `BUILD` phase, emit a lightweight plan before executing:

```markdown
**PLAN:**
1. Add Zod schema for task creation.
2. Wire schema into POST /api/tasks route.
3. Add test for validation error response.
→ Executing unless you redirect.
```
*This catches wrong directions before you've built on them.*

## 4. The Change Summary Pattern
After any modification, provide a structured summary. This proves you exercised scope discipline:

```markdown
**CHANGES MADE:**
- `src/routes/tasks.ts`: Added validation middleware to POST endpoint.
- `src/lib/validation.ts`: Added TaskCreateSchema using Zod.

**THINGS I DIDN'T TOUCH (intentionally):**
- `src/routes/auth.ts`: Has similar validation gap but out of scope.
- `src/middleware/error.ts`: Error format could be improved (requires separate task).

**POTENTIAL CONCERNS:**
- The Zod schema is strict — rejects extra fields. Confirm this is desired.
```

## 5. Git & Code Sizing Baseline
- **Atomic Commits:** Each commit must do one logical thing. Do not bundle refactoring with new features.
- **Sizing:** Target ~100 lines per commit/PR. Changes over 1000 lines are too large and must be split.
- **The Save Point Pattern:** Always verify code builds and tests pass before committing. If you break something and can't fix it in 1 step, revert to the last working commit.
