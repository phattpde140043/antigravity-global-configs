---
name: zoom-out
description: "Get a high-level map of the relevant modules and callers when unfamiliar with a section of code. USE WHEN: user says 'zoom out', needs broader context, or wants to understand how code fits into the bigger picture. NOT FOR: deep architecture refactoring (use `improve-codebase-architecture`)."
---

# Zoom Out

I don't know this area of code well. Go up a layer of abstraction. Give me a map of all the relevant modules and callers, using the project's domain glossary vocabulary.

## What to produce

1. **Module map** — list all modules/classes/files relevant to the area, with one-line descriptions
2. **Call graph** — who calls what, in what order (use a mermaid diagram if complex)
3. **Data flow** — what data enters, transforms, and exits this area
4. **Key interfaces** — the boundaries where this area connects to the rest of the system
5. **Domain terms** — map code names to domain glossary terms (if CONTEXT.md exists)

## Scope Boundaries

Use this skill for:
- Quick orientation in unfamiliar code
- Understanding how a module fits into the bigger picture
- Mapping callers and dependencies before making changes

Do NOT use this skill for:
- Deep architecture analysis and refactoring — use `improve-codebase-architecture`
- Designing new systems — use `system-architecture`
- Debugging — use `systematic-debugging`
