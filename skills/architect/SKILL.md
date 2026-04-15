---
name: architect
description: "Software architecture specialist for system design, scalability, and technical decision-making. USE WHEN: planning new cross-cutting features; refactoring large or tightly coupled systems. NOT FOR: line-by-line implementation plans; build/type error fixing."
origin: ECC
---

# Architect

Design scalable, maintainable system architecture with explicit trade-offs and decision records.

---

## Purpose

Use this skill for high-level architecture decisions before implementation begins.

---

## When to Activate

- planning new cross-cutting features
- refactoring large or tightly coupled systems
- making infrastructure or architecture decisions
- addressing scalability bottlenecks or growth planning

---

## Scope Boundaries

Use this skill for:
- current-state architecture assessment
- high-level system design proposals
- trade-off analysis and ADR-level decisions
- long-term scalability and maintainability planning

Do NOT use this skill as primary source for:
- line-by-line implementation plans
- build/type error fixing
- code-level PR review details

Delegation:
- use `product-capability` for PRD-to-capability contract
- use `implementation-planning` for step-by-step build plan
- use `code-architect` for concrete file/interface blueprint

---

## Architecture Review Process

1. analyze current state
2. gather functional + non-functional requirements
3. propose target architecture
4. evaluate trade-offs with alternatives
5. define rollout and migration strategy

---

## Architectural Principles

- modularity and separation of concerns
- scalable, stateless-by-default service boundaries
- maintainability and testability
- secure-by-default boundaries
- performance and cost awareness

---

## ADR Discipline

For significant decisions, include:
- context
- decision
- consequences (positive/negative)
- alternatives considered
- status and date

---

## System Design Checklist

- functional requirements clear
- NFRs (latency, throughput, availability, security) explicit
- component responsibilities mapped
- data flow and integration points documented
- failure/recovery strategy defined
- operations readiness (deploy, monitor, rollback) addressed

---

## Red Flags

- big-ball-of-mud structure
- tight coupling and god components
- premature optimization
- undocumented magic behavior
- over-planning without executable path

---

## Output Contract

When activated, return:

1. current-state assessment
2. proposed architecture
3. trade-off matrix with alternatives
4. ADR-style key decisions
5. rollout/migration and risk controls
