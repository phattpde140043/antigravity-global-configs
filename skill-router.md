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
| **backend-architect** | Designing scalable systems, microservices, complex refactoring, and enforcing architectural standards (50/200/3). | Line-by-line simple bug fixes; non-architectural UI changes. |
| **security-master** | Any security-sensitive task: Threat Modeling (STRIDE), Secure Coding, Pentesting, or Infrastructure Hardening. | Non-security logic; pure UI/UX styling. |
| **senior-qa** | Designing test strategies, writing E2E (Playwright), Unit tests (Pytest/Jest), TDD cycles, and investigating flaky tests. | Implementing production features (unless TDD); non-testing tasks. |
| **review-master** | Performing code audits, PR reviews, Readiness scoring (>85), and ensuring "AI Slop" removal. | Initial implementation; architecture planning from scratch. |

---

## 🛠️ Specialized Skills Map

| Skill | Use When | Not For |
|:---|:---|:---|
| a11y-architect | designing or reviewing UI components/pages; building design systems | backend security or infrastructure |
| agent-introspection-debugging | Maximum tool call or loop-limit failures; Repeated retries | unrelated tasks |
| api-design | Designing new API endpoints; defining type contracts | implementation logic |
| browser-testing-with-devtools | Building/debugging UI; visual verification; performance profiling | backend-only changes; CLI tools |
| ci-cd-and-automation | Setting up pipelines; automated quality gates; deployment strategies | local debugging only |
| build-error-resolver | build fails; TypeScript/type checker errors block progress | architecture redesign |
| code-explorer | before implementing features in unfamiliar areas | final architecture arbitration |
| documentation-and-adrs | Recording architectural decisions; writing public API docs | throwaway prototypes |
| performance-optimization | profiling slow endpoints; optimizing throughput/latency | feature development |
| framework-migration | modernizing legacy systems; upgrading major dependencies | minor bug fixes |
| verification-loop | after a feature or significant change; before opening a PR | writing test suites from scratch |

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
