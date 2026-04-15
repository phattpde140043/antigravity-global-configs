---
name: frontend-design
description: "Create distinctive, production-grade frontend interfaces with high design quality. USE WHEN: building a landing page, dashboard, or app shell from scratch; upgrading bland UI into a clear visual direction. NOT FOR: framework-specific state/data architecture; backend/API concerns."
origin: ECC
---

# Frontend Design

Design and build frontend interfaces that feel intentional, distinctive, and production-ready.

---

## Purpose

Use this skill when visual direction is a first-class requirement, not just functional correctness.

---

## When to Activate

- building a landing page, dashboard, or app shell from scratch
- upgrading bland UI into a clear visual direction
- translating product narrative into concrete interface language
- implementing components/pages where typography, composition, and motion matter

---

## Scope Boundaries

Use this skill for:
- visual direction selection and execution
- typography, color, spacing, layout, and motion systems
- production-ready responsive UI implementation choices
- design quality review before handoff

Do NOT use this skill as primary source for:
- framework-specific state/data architecture
- backend/API concerns
- content distribution strategy

Delegation:
- use coding-standards for general code quality baseline
- use content-engine/crosspost for publishing workflows

---

## Core Principle

Pick one direction and commit.
A coherent point of view is better than safe-average UI.

---

## Design Workflow

## 1) Frame the Interface First

Before implementation, define:
- purpose
- audience
- emotional tone
- visual direction
- one memorable element the user should retain

Example direction set:
- brutally minimal
- editorial
- industrial
- luxury
- playful
- geometric
- retro-futurist
- soft and organic
- maximalist

Rule:
- do not casually mix competing directions.

## 2) Build a Visual System

Define system primitives:
- type scale and hierarchy
- color tokens/variables
- spacing rhythm
- layout rules
- motion rules
- surface/border/shadow language

Implementation rule:
- use CSS variables or project tokens to keep growth coherent.

## 3) Compose with Intention

Prefer:
- asymmetry when it clarifies hierarchy
- overlap for depth when readable
- deliberate whitespace for focus
- density only when product workflow needs it

Avoid defaulting to generic card grids unless justified.

## 4) Make Motion Meaningful

Animation should:
- reveal hierarchy
- stage information
- reinforce action feedback
- create one or two memorable moments

Avoid random micro-interactions with no information value.

---

## Strong Defaults

## Typography

- select fonts with character and readability
- pair expressive display with clear body text when appropriate
- avoid generic defaults in design-led surfaces

## Color

- commit to a constrained palette
- use one dominant field with selective accents
- avoid trend-driven palettes unless product strategy supports them

## Background

Use atmospheric depth when it supports intent:
- gradients
- meshes
- subtle texture/noise
- layered transparency
- restrained patterns

## Layout

- break strict grids when composition benefits
- use offsets/grouping intentionally
- preserve clear reading flow on every breakpoint

---

## Execution Guardrails

1. Preserve existing design system when working in established products.
2. Match implementation complexity to design intent.
3. Keep accessibility and responsiveness non-negotiable.
4. Ensure desktop and mobile both feel deliberate.
5. Prioritize performance for animation-heavy surfaces.

Accessibility baseline:
- sufficient contrast
- visible focus states
- keyboard navigability
- reduced-motion support when feasible

---

## Anti-Patterns

Do not ship:
- interchangeable SaaS hero clones
- generic card piles with weak hierarchy
- random accent colors without system logic
- placeholder typography
- decorative motion without UX purpose

---

## Quality Gate

Before delivery, verify:

- [ ] clear visual point of view exists
- [ ] typography, spacing, and composition feel intentional
- [ ] color and motion support product goals
- [ ] output does not look like generic AI UI
- [ ] implementation quality is production-ready
- [ ] responsive behavior is coherent across breakpoints
- [ ] accessibility basics are satisfied

---

## Output Contract

When activated, return:

1. chosen visual direction and rationale
2. design system tokens/choices
3. layout and motion plan
4. implementation notes (responsive + accessibility)
5. final design quality checklist
