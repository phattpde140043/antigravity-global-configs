---
description: "Skill routing map with explicit USE WHEN and NOT FOR boundaries. Orchestrated by Master Disciplines."
---

# 🛰️ Skill Router

## Routing Rules

1. **Orchestrator First**: Always start with a Master Orchestrator (Security, QA, Review, Architect) for complex tasks.
2. **Match Intent**: Match user intent against the USE WHEN clause.
3. **Chain Delegation**: If a Master Skill is selected, it will automatically chain to the relevant sub-skills.

---

## 🏆 Master Orchestrators (Primary Entry Points)

| Master Skill | Use When | Not For |
|:---|:---|:---|
| **backend-architect** | System design, microservices, complex refactoring, and architectural standards (50/200/3). | Simple bug fixes; UI styling. |
| **security-master** | Security audits, threat modeling (STRIDE), secure coding, and regulatory compliance. | Pure UI/UX; non-security logic. |
| **senior-qa** | Test strategy, E2E (Playwright), Unit tests, TDD cycles, and flaky test investigation. | Production features (unless TDD). |
| **review-master** | Code audits, PR reviews, readiness scoring (>85), and context analysis. | Initial architecture planning. |
| **ai-master** | ML architecture, data pipelines, advanced search (Exa), and deep research. | Simple CRUD logic; UI design. |
| **agent-master** | Core operations, systematic debugging, context engineering, and planning. | Domain-specific business logic. |
| **product-master** | Business strategy, product discovery, investor materials, and brand voice. | Deep technical implementation. |
| **ux-master** | Frontend design, UI patterns, accessibility (a11y), and presentations. | Backend infra; security audits. |
| **content-master** | Technical writing, ADRs, documentation lookup, and coding standards. | Code implementation. |
| **infrastructure-master** | Cloud IaC, AWS CDK, and production infrastructure hardening. | Application-level business logic. |

---

## 🛠️ Specialized Skills Map (Delegated by Masters)

| Skill | Master Discipline | Use When |
|:---|:---|:---|
| `grill-with-docs` | **content-master** | Stress-test an existing plan against the domain model, glossary, and ADRs. USE WHEN: user wants to challenge a plan against their project's language and documented decisions, or validate terminology consistency. NOT FOR: initial ideation or brainstorming (use `brainstorming`); writing implementation plans (use `writing-plans`). |
| `reviewing-cicd-pipelines` | **infrastructure-master** | Reviewing GitHub Actions workflows, CI/CD pipeline changes, or deployment configs — workflow syntax, secret injection, environment targeting, and pipeline security. |
| `zoom-out` | **agent-master** | Get a high-level map of the relevant modules and callers when unfamiliar with a section of code. USE WHEN: user says 'zoom out', needs broader context, or wants to understand how code fits into the bigger picture. NOT FOR: deep architecture refactoring (use `improve-codebase-architecture`). |
| `to-issues` | **agent-master** | Break a plan, spec, or PRD into independently-grabbable issues using vertical-slice (tracer bullet) methodology. USE WHEN: user wants to convert a plan into issues, create implementation tickets, or break down work. NOT FOR: writing the plan itself (use `writing-plans`); creating a PRD (use `to-prd`). |
| `finishing-a-development-branch` | **agent-master** | Implementation is complete and tests pass; decide how to integrate the work — structured merge / PR / cleanup options. NOT FOR: writing the plan (use `writing-plans`). |
| `prototype` | **agent-master** | Build a throwaway prototype to answer a design question before committing to real code. USE WHEN: user wants to prototype, sanity-check a data model, mock up a UI, explore design options, or says 'prototype this'. NOT FOR: full implementation (use `executing-plans`); brainstorming ideas (use `brainstorming`). |
| `improve-codebase-architecture` | **backend-architect** | Find deepening opportunities in EXISTING codebases — shallow→deep module refactors for testability and AI-navigability. USE WHEN: user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable. NOT FOR: designing new systems from scratch (use `system-architecture`); initial brainstorming (use `brainstorming`). |
| `using-superpowers` | **agent-master** | Starting a conversation or task — establishes how to discover and invoke the right skills before responding (Skill-tool invocation before any action). |
| `handoff` | **agent-master** | Compact the current conversation into a handoff document for a fresh agent session to continue. USE WHEN: ending a long session, switching contexts, or preparing for another agent to pick up work. NOT FOR: writing plans (use `writing-plans`); creating PRDs (use `to-prd`). |
| `python-best-practices` | **backend-architect** | Writing or refactoring Python and you want modern idiomatic patterns — typing, packaging, project structure, and tooling. |
| `building-e2e-tests` | **senior-qa** | Building, implementing, or modifying E2E tests — test structure, fixtures, assertions, API endpoints, tenant-isolation and security-boundary validation. |
| `system-architecture` | **backend-architect** | Use when designing new systems, features, REST/GraphQL APIs, or making high-level technical decisions. Covers architecture design, API & interface design, and tech-stack-specific patterns (.NET, FastAPI). USE WHEN: designing new systems, refactoring architecture, designing APIs, or making backend architecture decisions. NOT FOR: pre-implementation brainstorming (use `brainstorming`), writing implementation plans (use `writing-plans`), or code review (use `performing-code-review`). |
| `api-design` | **backend-architect** | Designing new API endpoints and type contracts. |
| `performance-optimization` | **backend-architect** | Profiling slow endpoints and optimizing throughput. |
| `regulatory-compliance` | **security-master** | GDPR, SOC2, HIPAA, and industry-standard audits. |
| `browser-automation` | **senior-qa** | Low-level browser interaction and automation scripts. |
| `workspace-surface-audit` | **review-master** | Mapping codebase exposure and context discovery. |
| `exa-search` | **ai-master** | High-fidelity web search and neural discovery. |
| `systematic-debugging` | **agent-master** | Root cause analysis and step-by-step resolution. |
| `implementation-planning` | **agent-master** | Creating phased, dependency-ordered task lists. |
| `frontend-design` | **ux-master** | Building premium, high-aesthetic UI systems. |
| `documentation-and-adrs` | **content-master** | Recording critical architectural decisions. |

---

## 🔗 Master Delegation Chains

When a task exceeds a specialized skill's scope, delegate to the Master Orchestrators:

| Specialized Skill | Exceeds Scope When | Delegate To (Master) |
|:---|:---|:---|
| build-error-resolver | fix requires architectural change | **backend-architect** |
| verification-loop | security gaps found in audit | **security-master** |
| performance-optimization | bottleneck is architectural | **backend-architect** |
| tdd-workflow | tests require E2E browser automation | **senior-qa** |
| implementation-planning | output needs post-merge audit | **review-master** |
| any-skill | security context is required | **security-master** |

---

## 🔄 Sequential Chaining Rules

Master Orchestrators and specialized sub-skills follow strict sequence pathways to ensure comprehensive, high-quality development lifecycle management.

### 1. Master Skill Sequence
Refer to the following chain for the next recommended Master Orchestrator:

| Completed Master Skill | Recommended Successor | Purpose / Next Phase |
|:---|:---|:---|
| **product-master** | **backend-architect** | Translate business requirements & user stories into architecture designs & APIs. |
| **backend-architect** | **security-master** | Threat model (STRIDE) the architecture design before starting the TDD cycle. |
| **security-master** | **senior-qa** | Convert mitigated threat vectors into regression & E2E tests (TDD). |
| **senior-qa** | **agent-master** | Implement the core logic of the codebase (BUILD phase). |
| **agent-master** | **ux-master** (if UI) or **review-master** | Polish user experience/aesthetics or initiate the code readiness review council. |
| **ux-master** | **review-master** | Validate design accessibility, performance, and complete a final slop scan. |
| **review-master** | **content-master** | Update architectural records, documentation (ADRs), and logs. |
| **content-master** | **infrastructure-master** | Deploy application stacks and stateful resources using IaC/CDK. |
| **infrastructure-master** | **review-master** (Post-Merge) | Execute automated external audits (`npx commitshow audit`) and sign off. |

### 2. Sub-Skill Pipeline
When executing a Master Orchestrator, navigate its sub-skills sequentially using the `──→` pipeline defined within its `SKILL.md`.

---

## Notes
- This file guides selection; source-of-truth remains each Master's **SKILL.md**.
- Master Skills will perform internal chaining to their respective `sub-skills/` folders.
