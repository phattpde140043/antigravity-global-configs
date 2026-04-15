---
name: code-explorer
description: "Deeply analyzes existing codebase features by tracing execution paths, mapping architecture layers, and documenting dependencies to inform new development. USE WHEN: before implementing new features in unfamiliar areas; when debugging complex behavior paths. NOT FOR: final architecture decision arbitration; code modification or refactor execution."
origin: ECC
---

# Code Explorer

Analyze existing features deeply before making design or implementation changes.

---

## Purpose

Produce an evidence-based understanding of how current code works, including entry points, execution flow, dependencies, and reusable patterns.

---

## When to Activate

- before implementing new features in unfamiliar areas
- when debugging complex behavior paths
- when planning refactors that may impact multiple modules
- when mapping dependencies and side effects for risk assessment

---

## Scope Boundaries

Use this skill for:
- entry-point discovery
- call-path tracing and layer mapping
- dependency and pattern documentation

Do NOT use this skill as primary source for:
- final architecture decision arbitration
- code modification or refactor execution

Delegation:
- use `code-architect` after discovery for implementation blueprint
- use `architect` for strategic decision-making across systems

---

## Analysis Process

1. identify feature entry points
2. trace execution path end-to-end
3. map architecture layers and boundaries
4. identify reusable patterns/anti-patterns
5. document internal/external dependencies

---

## Output Format

- exploration scope
- entry points and triggers
- execution flow (ordered steps)
- architecture insights and conventions
- key files and roles
- dependency map (internal/external)
- recommendations for new development

---

## Quality Gate

Before handoff:

- [ ] flow trace covers happy + error paths
- [ ] async boundaries and side effects identified
- [ ] dependencies verified from code evidence
- [ ] recommendations align with discovered patterns

---

## Output Contract

When activated, return:

1. feature exploration summary
2. execution-path map
3. key files and dependency map
4. reusable patterns and pitfalls
5. implementation guidance for next lane
