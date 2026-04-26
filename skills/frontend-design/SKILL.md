---
name: frontend-design
description: "Create distinctive, production-grade frontend interfaces with high design quality. USE WHEN: building a landing page, dashboard, or app shell from scratch; upgrading bland UI into a clear visual direction. NOT FOR: framework-specific state/data architecture; backend/API concerns."
origin: ECC
---

# Frontend Design

Design and build frontend interfaces that feel intentional, distinctive, and production-ready.

## Diamond Standard Pillar: Aesthetic
This skill is the primary driver for the **Aesthetic** pillar of the **Diamond Standard**. Every interface created must aim for **Premium Design Quality**, avoiding generic templates and AI-generated cliches.

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

---

## Design Language: Antigravity / Weightless

Use this design language when the product calls for **spatial depth, immersive dashboards, or premium motion-heavy surfaces**.

### Stack
- **Animation**: GSAP + ScrollTrigger (scroll-linked motion, staggered entrances)
- **3D**: React Three Fiber (R3F) or CSS 3D transforms (`rotateX`, `rotateY`, `perspective`)
- **Styling**: Tailwind CSS (layout) + custom CSS for complex 3D transforms

### Visual Principles

| Principle | Implementation |
| --- | --- |
| **Weightlessness** | Cards float with layered soft shadows: `box-shadow: 0 20px 40px rgba(0,0,0,0.05)` |
| **Spatial Depth** | Z-axis layering via CSS `perspective`. Background deep, foreground pops. |
| **Glassmorphism** | `backdrop-filter: blur(12px)` + semi-transparent borders + subtle translucency |
| **Isometric Snap** | Tilt grids: `transform: rotateX(60deg) rotateZ(-45deg)` for dashboard card grids |

### Motion Rules

- **Never instant:** All state changes (hover, focus, active) → minimum `0.3s ease-out`
- **Scroll entrances:** GSAP ScrollTrigger — elements float in from Y-axis with slight rotation
- **Staggered load:** Card grids stagger by `0.1s` — never appear all at once
- **Parallax:** Background elements move slower than foreground elements on scroll

### Performance Constraints (Non-Negotiable)

```css
/* ✅ Offload to GPU — use for all animated elements */
.animated-card { will-change: transform; }

/* ❌ NEVER animate continuously */
/* box-shadow and filter are expensive — animate with opacity trick instead */
.card:hover { opacity: 0.95; } /* NOT: box-shadow transition on every frame */
```

- `will-change: transform` on every GSAP-animated element
- Do NOT continuously animate `box-shadow` or `filter` — animate `opacity` instead
- Always honor `prefers-reduced-motion: reduce` — disable all GSAP animations for these users:

```javascript
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReduced) { gsap.from('.card', { y: 40, opacity: 0, stagger: 0.1 }); }
```

