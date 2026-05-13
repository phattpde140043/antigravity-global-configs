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

## Notes
- This file guides selection; source-of-truth remains each Master's **SKILL.md**.
- Master Skills will perform internal chaining to their respective `sub-skills/` folders.
