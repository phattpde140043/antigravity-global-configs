---
description: "Mandatory gated workflow for all non-trivial tasks. The agent owns this state machine and drives all transitions autonomously."
---

# Global Workflow Lifecycle

## 1. Autonomous State Machine

You own the state machine. Do NOT wait for the user to tell you what phase to enter. Evaluate state yourself and drive transitions:

```
DEFINE ──→ PLAN ──→ BUILD ──→ VERIFY ──→ REVIEW ──→ SHIP
```

**Evaluation logic (run this before every response):**

1. Are requirements unclear or ambiguous?
   → **State: DEFINE**. Draft a Spec. Surface assumptions. Ask open questions.
2. Is the Spec approved but no detailed implementation plan exists?
   → **State: PLAN**. Produce a phased, dependency-ordered task list.
3. Is the Plan approved BY THE USER and tasks remain?
   → **State: BUILD**. ONLY enter this state after explicit User confirmation.
4. Is the current task complete?
   → **State: VERIFY**. Run tests, build check, manual verification.
5. Is all implementation verified?
   → **State: REVIEW**. Perform Self-Review checklist (see rules.md).
6. Is Review clean?
   → **State: SHIP**. Prepare PR, finalize artifacts.

---

## 2. Phase Details

### Phase 1: DEFINE — The Spec
**When to activate**: The request touches more than one file, requirements are vague, architectural choices must be made, or the task takes >15 mins.
**Rules**:
1. Write all assumptions explicitly before asking for code.
2. Reframe vague requirements as testable Success Criteria.
3. Do not write any production code until the Spec is approved.

### Phase 2: PLAN — The Implementation Plan
**When to activate**: Immediately after Spec approval.
**Rules**:
1. Decompose into vertical slices (feature path end-to-end).
2. Order tasks by dependency: foundations first.
3. Each task: max ~5 files; must have Acceptance Criteria + Verification step.
4. Add explicit explicit explicit human Checkpoints after every 2–3 tasks.
5. Flag HIGH RISK tasks and schedule them early (Fail Fast).

### Phase 3: BUILD — Incremental Implementation
**Gated Entry**: You MUST NOT enter this phase without a "Go" or "Approved" from the User regarding the current Implementation Plan.
**Rules**:
1. Implement ONE task at a time. Never implement ahead.
2. Touch ONLY files within the current task scope.
3. Before writing code, ask: "What is the simplest thing that could work?"

### Phase 4: VERIFY — Quality Control
**Micro-verify (After each task)**:
- Existing tests pass, build succeeds, new functionality works.
**Macro-verify (After all tasks)**:
- Full test suite passes, zero "AI Slop" (no placeholders, generic TODOs).

**Stop-the-Line Rule**:
When an error occurs: STOP -> PRESERVE output -> DIAGNOSE (reproduce, localize, reduce) -> FIX root cause -> GUARD with test -> RESUME.

### Phase 5: REVIEW — Self-Audit
Before proposing to Ship, run the mandatory Self-Review from `rules.md` (Convention, Architecture, Performance, Security, Final Judgment).

---

## 3. Standard Templates

### Spec Template
```markdown
# Spec: [Feature Name]
## Objective: [What we're building, why, and for whom]
## Success Criteria: [Specific, testable targets]
## Tech Stack & Constraints: [Frameworks, rules]
## Boundaries: [Always do / Ask first / Never do]
## Assumptions: [List every assumption. User must confirm]
## Open Questions: [Unresolved items]
```

### Implementation Plan Template
```markdown
# Implementation Plan: [Name]
## Tasks:
### Phase 1: [Foundation]
- [ ] Task 1.1: [Title] — Verify: [Command/Action]
- [ ] Task 1.2: [Title] — Verify: [Command/Action]
### ✅ Checkpoint: [Target state]
```
