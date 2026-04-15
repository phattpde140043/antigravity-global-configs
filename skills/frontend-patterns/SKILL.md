---
name: frontend-patterns
description: "Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. USE WHEN: building React components and feature modules; deciding state management approach. NOT FOR: high-concept visual direction and art direction; backend/API contract design."
origin: ECC
---

# Frontend Development Patterns

Practical implementation patterns for React and Next.js applications with strong maintainability, performance, and UX foundations.

---

## Purpose

Use this skill for frontend engineering decisions: component architecture, state/data flow, rendering strategy, forms, performance, and accessibility.

---

## When to Activate

- building React components and feature modules
- deciding state management approach
- implementing client/server data fetching
- improving frontend performance and rendering behavior
- building robust forms and validation flows
- implementing navigation and route-aware UX
- enforcing accessibility and responsive interaction patterns

---

## Scope Boundaries

Use this skill for:
- React/Next implementation patterns
- state and async data patterns
- performance and a11y engineering decisions

Do NOT use this skill as primary source for:
- high-concept visual direction and art direction
- backend/API contract design
- generic coding conventions not specific to frontend

Delegation:
- use frontend-design for visual system and aesthetic direction
- use coding-standards for cross-project code quality baseline
- use documentation-lookup for version-specific framework API behavior

---

## Core Principles

1. Prefer composition over inheritance.
2. Keep components focused and testable.
3. Co-locate state with the closest consumer by default.
4. Make data flow explicit and predictable.
5. Optimize only after identifying real bottlenecks.

---

## Component Architecture Patterns

## Composition First

- build small primitives and compose upward
- avoid monolithic components with mixed concerns
- expose intent-driven props, not implementation details

## Compound Components

Use for cohesive UI families (Tabs, Dropdown, Menu, Accordion) where shared state and API ergonomics matter.

## Container and Presentational Split (When Helpful)

- container handles data, orchestration, and side effects
- presentational component handles rendering and interactions
- do not force this split for trivial components

## Error Boundaries

Wrap unstable or high-risk UI islands to prevent full app crashes.

---

## State Management Patterns

## Local State First

Use `useState`/`useReducer` before introducing global stores.

## Context Carefully

- use context for stable cross-tree concerns (theme, auth session, feature flags)
- avoid high-frequency mutable data in broad context providers

## External Stores

Adopt store libraries when:
- state crosses many feature boundaries
- updates are frequent and context causes re-render pressure
- devtools/time-travel/debugging requirements are explicit

Selection rule:
- prefer simplest tool that satisfies scope and performance constraints.

---

## Data Fetching Patterns

## Next.js Rendering Strategy

Choose intentionally:
- server components for data-heavy, cache-friendly paths
- client components for highly interactive stateful UI
- hybrid when interactivity is localized

## Query Lifecycle

- define loading, error, empty, and success states explicitly
- support refetch and stale data handling
- use request deduping/caching where available

## Mutation Strategy

- optimistic updates only when rollback strategy exists
- reconcile server truth after mutation completion

---

## Form and Validation Patterns

1. keep source-of-truth clear (controlled vs library-managed)
2. validate at field-level and submit-level
3. keep schema validation close to form contract
4. return actionable, field-specific errors
5. disable duplicate submits during pending mutation

---

## Performance Patterns

## Rendering

- memoize expensive derived values
- memoize callbacks passed to deep child trees when needed
- avoid unnecessary state lifts that trigger broad re-renders

## Loading and Bundles

- split heavy routes/components
- lazy load non-critical UI
- virtualize long lists/grids

## Measurement

- profile before and after optimization
- treat perceived performance (skeletons/progressive reveal) as product concern

---

## Routing and Navigation

- make route transitions predictable and cancellable
- preserve user intent on back/forward navigation
- maintain query params for filter/search experiences when appropriate
- guard protected routes with clear fallback states

---

## Accessibility Patterns

- keyboard-first interactions for all actionable controls
- semantic roles and ARIA only when semantics are insufficient
- visible focus indicators
- accessible names for inputs/buttons
- focus management for modals/drawers/dialogs
- support reduced motion where feasible

---

## Testing-Oriented Frontend Practices

- prefer stable selectors for test automation (`data-testid` when needed)
- separate business logic from rendering glue for easier unit tests
- cover critical user flows with E2E where behavior spans routing/network

---

## Anti-Patterns

Avoid:
- prop drilling through many layers without composition/context strategy
- global state for purely local concerns
- arbitrary timeout-based synchronization in UI logic
- premature memoization everywhere
- inaccessible custom controls without keyboard support

---

## Quality Gate

Before shipping, verify:

- [ ] component responsibilities are clear
- [ ] state ownership is minimal and intentional
- [ ] loading/error/empty states are covered
- [ ] key interactions are accessible via keyboard
- [ ] performance hotspots are measured, not guessed
- [ ] responsive behavior is consistent across breakpoints

---

## Output Contract

When activated, return:

1. recommended frontend pattern choices (with rationale)
2. state/data/rendering strategy
3. performance and accessibility considerations
4. concrete implementation plan or refactor steps
5. risks and follow-up checks
