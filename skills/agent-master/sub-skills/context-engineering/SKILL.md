---
name: context-engineering
description: "Optimizes agent context setup. Use when starting a new session, switching between tasks, or when agent output quality degrades. Use to curate rules, specs, and source files for focused execution."
---

# Context Engineering

## Overview

Feed agents the right information at the right time. Context is the single biggest lever for agent output quality. Context engineering is the practice of deliberately curating what the agent sees and how it's structured.

## The Context Hierarchy

1. **Rules Files (CLAUDE.md, rules.md)**: Persistent, project-wide.
2. **Spec / Architecture Docs**: Loaded per feature/session.
3. **Relevant Source Files**: Loaded per task.
4. **Error Output / Test Results**: Loaded per iteration.

## Context Packing Strategies

### The Brain Dump
At session start, provide everything the agent needs in a structured block (Tech stack, Spec excerpt, Files involved, Related patterns, Gotchas).

### Selective Include
Only include what's relevant to the current task. Aim for <2,000 lines of focused context per task. Including too many files causes the agent to lose focus.

## Confusion Management (Critical)

Even with good context, ambiguity happens. How you handle it determines quality.

### When Context Conflicts
**Do NOT** silently pick one interpretation. Surface it:
- "The spec says X, but the existing code uses Y. Should I follow the spec or the existing pattern?"

### When Requirements Are Incomplete
If the spec doesn't cover a case:
1. Check existing code for precedent.
2. **Stop and ask** before inventing requirements.

### Inline Planning Pattern
Emit a lightweight plan before execution:
- "PLAN: 1. Add schema. 2. Update route. 3. Add test. -> Executing unless you redirect."

## Anti-Patterns
- **Context Starvation**: Agent invents APIs or ignores conventions.
- **Context Flooding**: Agent loses focus due to >5,000 lines of irrelevant context.
- **Silent Confusion**: Agent guesses when it should ask.

## Verification
- [ ] Rules file exists and covers stack and conventions.
- [ ] Context is refreshed when switching major tasks.
- [ ] Agent references actual project files (not hallucinations).
- [ ] Ambiguity is surfaced explicitly to the user.
