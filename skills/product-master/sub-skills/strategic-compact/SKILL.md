---
name: strategic-compact
description: "Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction. USE WHEN: long sessions approaching context pressure; multi-phase tasks (research -> plan -> implement -> test). NOT FOR: runtime debugging or failure diagnosis; test/build verification workflows."
origin: ECC
---

# Strategic Compact

Use intentional manual compaction at task boundaries to reduce context drift and token pressure.

---

## Purpose

Help long sessions preserve high-value context by compacting at meaningful milestones instead of random trigger points.

---

## When to Activate

- long sessions approaching context pressure
- multi-phase tasks (research -> plan -> implement -> test)
- switching between unrelated tasks in one session
- after completing a major milestone
- responses become slower or less coherent

---

## Scope Boundaries

Use this skill for:
- deciding when to compact
- preserving important context before compaction
- phase-based context reset strategy

Do NOT use this skill as primary source for:
- runtime debugging or failure diagnosis
- test/build verification workflows

Delegation:
- use `agent-introspection-debugging` for looping/drift failure recovery
- use `verification-loop` for quality-gate checks before handoff

---

## Why Strategic Compaction

Auto compaction may occur mid-flow and can drop relevant working context.
Strategic compaction at logical boundaries keeps intent and artifacts stable.

Best moments:
- after exploration, before implementation
- after finishing a feature milestone
- after a failed branch before trying a new strategy

Avoid:
- compacting mid-implementation when local state is still active

---

## Decision Guide

| Transition | Compact? | Reason |
|---|---|---|
| Research -> Planning | Yes | Keep distilled plan, drop noisy discovery logs |
| Planning -> Implementation | Yes | Plan survives in task list/files |
| Implementation -> Testing | Maybe | Keep if tests depend on fresh code context |
| Debugging -> New feature | Yes | Remove dead-end traces |
| Mid-implementation | No | Prevent loss of active variable/file state |

---

## Pre-Compact Checklist

Before compacting:
- persist plan in todo list or file
- persist key decisions and assumptions
- persist unresolved blockers/questions
- persist file paths and symbols currently in play

Use a short summary message with compact to preserve intent.

---

## Hook-Oriented Reminder Pattern

Optional approach:
- trigger reminder after N tool calls
- remind periodically beyond threshold
- suggestion only, never forced compaction

Recommended defaults:
- first reminder around 50 tool calls
- repeat every 20-30 calls

---

## Output Contract

When activated, return:

1. compact recommendation (now/later)
2. reason tied to current phase
3. pre-compact items to persist
4. suggested compact summary line
5. immediate next step after compact
