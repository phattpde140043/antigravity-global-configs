---
name: master-dispatcher
description: "The Global Entry Point for all Antigravity Skills. Dispatches tasks to the appropriate Master Orchestrator."
metadata:
  category: entry-point
---

# 🌐 Global Skill Dispatcher

Welcome to the Antigravity Skill Registry. This is the centralized hub for all specialized capabilities. All skills are organized into **Master Disciplines** to ensure high-fidelity orchestration and systemic integrity.

---

## 🏛️ Master Disciplines (The Orchestrators)

When starting a task, identify the relevant discipline and delegate to its **Master Orchestrator**:

### 1. 🏗️ [Backend Architect](backend-architect/SKILL.md)
- **Focus**: System Design, API Architecture, Distributed Systems, Performance.
- **Triggers**: `api-design`, `microservices`, `resilience`, `performance`.

### 2. 🛡️ [Security Master](security-master/SKILL.md)
- **Focus**: Threat Modeling, Secure Coding, Pentesting, Compliance.
- **Triggers**: `security-audit`, `threat-model`, `regulatory-compliance`.

### 3. 🏆 [Senior QA](senior-qa/SKILL.md)
- **Focus**: Test Strategy, Playwright E2E, TDD, Quality Metrics.
- **Triggers**: `e2e`, `unit-test`, `flaky-test`, `quality-review`.

### 4. ⚖️ [Review Master](review-master/SKILL.md)
- **Focus**: Code Audit, Readiness Scoring, Context Analysis.
- **Triggers**: `code-review`, `pr-review`, `quality-audit`.

### 5. 🤖 [AI & Data Master](ai-master/SKILL.md)
- **Focus**: ML Architecture, Data Engineering, Search, Media Gen.
- **Triggers**: `ai-ml`, `data-master`, `exa-search`, `deep-research`.

### 6. 🧠 [Agent Master](agent-master/SKILL.md)
- **Focus**: Core Ops, Debugging, Planning, Context Engineering.
- **Triggers**: `debugging`, `planning`, `code-generation`, `context`.

### 7. 🚀 [Product Master](product-master/SKILL.md)
- **Focus**: Business Strategy, Market Research, Stakeholder Comms.
- **Triggers**: `business-strategy`, `product-capability`, `investor`.

### 8. 🎨 [UX & Design Master](ux-master/SKILL.md)
- **Focus**: Frontend Design, UI Patterns, Accessibility.
- **Triggers**: `frontend`, `ui-ux`, `a11y`.

### 9. ✍️ [Content Master](content-master/SKILL.md)
- **Focus**: Technical Writing, Documentation, Standards.
- **Triggers**: `writing`, `documentation`, `adrs`, `standards`.

### 10. ☁️ [Infrastructure Master](infrastructure-master/SKILL.md)
- **Focus**: Cloud IaC, AWS CDK, Production Hardening.
- **Triggers**: `aws`, `cdk`, `infrastructure`, `cloud`.

---

## 🧭 Navigation Guideline
1. **Identify**: Determine the core domain of the user request.
2. **Delegate**: Open the corresponding Master Skill.
3. **Chain**: Follow the internal `Sub-Discipline Chain` within the Master Skill to reach the specific expertise required.
4. **Execute**: Maintain the Diamond Standard across all operations.
