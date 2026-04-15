---
name: product-capability
description: "Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service work starts. USE WHEN: PRD/roadmap note exists but implementation constraints are vague; feature crosses multiple services/repos/teams. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
origin: ECC
---

# Product Capability

Turn product intent into explicit engineering constraints and an implementation-facing capability contract.

---

## Purpose

Use this skill when requirements are directionally clear but constraints, interfaces, and invariants are still implicit.

---

## When to Activate

- PRD/roadmap note exists but implementation constraints are vague
- feature crosses multiple services/repos/teams
- architecture/data/lifecycle implications are unresolved
- review loops keep surfacing hidden assumptions repeatedly
- a durable cross-session artifact is needed before coding

---

## Canonical Artifact

Prefer existing durable location if present:
- `PRODUCT.md`
- `docs/product/`
- program spec directory

If no capability manifest exists, create one from:
- `docs/examples/product-capability-template.md` (or equivalent repo template)

Goal:
- one reusable capability artifact, not fragmented planning notes.

---

## Non-Negotiables

1. Do not invent product truth; mark unknowns explicitly.
2. Separate user-visible promises from implementation details.
3. Label fixed policy vs architecture preference vs open decision.
4. Call out conflicts with existing constraints directly.
5. Keep capability constraints durable and reusable.

---

## Inputs

Read only what is necessary:
1. product intent (PRD, issue, discussion, founder note)
2. current architecture (contracts, schemas, workflows)
3. existing product context docs
4. delivery constraints (auth, billing, compliance, rollout, performance)

---

## Core Workflow

## 1) Restate Capability

Compress into one precise statement:
- actor
- new capability after release
- outcome change

If this statement is weak, implementation will drift.

## 2) Resolve Constraints

Extract must-hold constraints:
- business rules
- scope boundaries
- invariants
- trust boundaries
- data ownership
- lifecycle transitions
- rollout/migration constraints
- failure and recovery expectations

## 3) Define Implementation Contract

Produce SRS-style contract with:
- capability summary
- non-goals
- actors and surfaces
- states and transitions
- interfaces and I/O
- data model implications
- security/billing/policy constraints
- observability/operator requirements
- open questions blocking implementation

## 4) Handoff Decision

End with explicit handoff state:
- ready for implementation
- needs architecture review
- needs product clarification

---

## Output Format

Return in this order:

```text
CAPABILITY
- one-paragraph restatement

CONSTRAINTS
- fixed rules, invariants, boundaries

IMPLEMENTATION CONTRACT
- actors
- surfaces
- states and transitions
- interface/data implications

NON-GOALS
- explicitly out of scope

OPEN QUESTIONS
- blockers and unresolved product decisions

HANDOFF
- next action and owning lane
```

---

## Quality Gate

Before handoff:

- [ ] capability statement is concrete and testable
- [ ] constraints are explicit and non-contradictory
- [ ] policy vs preference vs open decisions are separated
- [ ] interface and state transitions are implementation-ready
- [ ] unresolved items are clearly marked with owner/decision needed

---

## Related Lanes

- `implementation-planning` for execution breakdown after capability lock
- `architecture-design` for major structural trade-offs
- `api-design` when capability surfaces require API contract design
