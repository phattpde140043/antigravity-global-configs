# 🪐 Antigravity Global Configs

**Production-grade engineering instructions for AI coding agents.**

These configurations encode the workflows, quality gates, and best practices that senior engineers use when building software.

---

## 🏗️ Master Orchestrators (The Brains)

The system uses a **Conductor-Musician** pattern. These **11 primary Master Skills** orchestrate specialized sub-disciplines to ensure high-fidelity results.

| Master Skill | Responsibility |
|:---|:---|
| [**backend-architect**](./skills/backend-architect/SKILL.md) | **System Lead**. Microservices, Scalability, and Clean Architecture standards. |
| [**data-master**](./skills/data-master/SKILL.md) | **Data Lead**. Databases (PostgreSQL, ClickHouse, Redis), SQL/query tuning, schema & migration design, and AI data (RAG, vector search). |
| [**security-master**](./skills/security-master/SKILL.md) | **Security Lead**. Threat Modeling, Secure Coding, Pentesting, and Hardening. |
| [**senior-qa**](./skills/senior-qa/SKILL.md) | **Quality Lead**. E2E (Playwright), Unit Testing, TDD, and Flaky Mitigation. |
| [**review-master**](./skills/review-master/SKILL.md) | **Audit Lead**. Readiness Scoring (>85), AI Slop Scan, and PR Excellence. |
| [**ai-master**](./skills/ai-master/SKILL.md) | **AI Lead**. ML Architecture, Deep Research, and Search (Exa/Tavily). |
| [**agent-master**](./skills/agent-master/SKILL.md) | **Agent Lead**. Core Operations, Debugging, Planning, and Context Engineering. |
| [**product-master**](./skills/product-master/SKILL.md) | **Product Lead**. Business Strategy, Market Research, and Stakeholder Comms. |
| [**ux-master**](./skills/ux-master/SKILL.md) | **UX Lead**. Frontend Design, UI Patterns, and Accessibility. |
| [**content-master**](./skills/content-master/SKILL.md) | **Content Lead**. Technical Writing, Documentation, and Standards. |
| [**infrastructure-master**](./skills/infrastructure-master/SKILL.md) | **Infra Lead**. Cloud IaC, AWS CDK, Docker, and Production Hardening. |

### Specialized Masters
Narrower-domain orchestrators, invoked directly when their domain applies:

| Master Skill | Domain |
|:---|:---|
| [**workflow-automation**](./skills/workflow-automation/SKILL.md) | Third-party integrations & automation (Salesforce, Telegram, Git, Square, …). |
| [**game-development-master**](./skills/game-development-master/SKILL.md) | Game engines & ECS (Bevy). |
| [**quantum-engineering**](./skills/quantum-engineering/SKILL.md) | Quantum circuits (Cirq). |

> Empty placeholder masters have been retired to [`archive/empty-masters/`](./archive/empty-masters/). A master with zero sub-skills does not belong in `skills/` (see [Rule 20](./rules.md) — *Router Must Not Lie*).

---

## 🛠️ Specialized Sub-Disciplines (The Musicians)

Master Skills delegate deep-dive tasks to specialized sub-skills.

### 🏗️ Architect & Backend Cluster
- [Software Architecture](./skills/backend-architect/sub-skills/software-architecture/SKILL.md)
- [Architecture Design](./skills/backend-architect/sub-skills/architecture-design/SKILL.md)
- [API Design](./skills/backend-architect/sub-skills/api-design/SKILL.md)
- [Performance Optimization](./skills/backend-architect/sub-skills/performance-optimization/SKILL.md)

### 🗄️ Data & Storage Cluster
- [PostgreSQL Development](./skills/data-master/sub-skills/postgresql/SKILL.md)
- [PostgreSQL Optimization](./skills/data-master/sub-skills/postgresql-optimization/SKILL.md)
- [ClickHouse Engineering](./skills/data-master/sub-skills/cc-skill-clickhouse-io/SKILL.md)
- [Redis CLI Reference](./skills/data-master/sub-skills/redis-cli/SKILL.md)
- [Vector Search](./skills/data-master/sub-skills/vector-search/SKILL.md)

### 🛡️ Security & Compliance Cluster
- [Security Design & STRIDE](./skills/security-master/sub-skills/security-design/SKILL.md)
- [Backend Security Coder](./skills/security-master/sub-skills/backend-security-coder/SKILL.md)
- [Regulatory Compliance](./skills/security-master/sub-skills/regulatory-compliance/SKILL.md)

### ✅ QA & Testing Cluster
- [E2E Testing Excellence](./skills/senior-qa/sub-skills/e2e-testing/SKILL.md)
- [TDD Workflow](./skills/senior-qa/sub-skills/tdd-workflow/SKILL.md)
- [Verification Loop](./skills/senior-qa/sub-skills/verification-loop/SKILL.md)

### 🧠 Agent Ops & Debugging Cluster
- [Systematic Debugging](./skills/agent-master/sub-skills/systematic-debugging/SKILL.md)
- [Implementation Planning](./skills/agent-master/sub-skills/implementation-planning/SKILL.md)
- [Context Engineering](./skills/agent-master/sub-skills/context-engineering/SKILL.md)
- [Code Generation](./skills/agent-master/sub-skills/code-generation/SKILL.md)

---

## 🛰️ Core Infrastructure

- **[`system.md`](./system.md)**: **The Behavior Model**. Agent persona and communication style.
- **[`rules.md`](./rules.md)**: **Operational Governance**. Strict standards and security.
- **[`workflow.md`](./workflow.md)**: **The Gated Lifecycle**. Mandatory (DEFINE → SHIP) phases.
- **[`skill-router.md`](./skill-router.md)**: **The Dispatcher**. Maps tasks to the correct Orchestrator.

---

## 👨‍💻 Author

**Tran Phu Phat** (phattpde140043)
- Email: [Phattp1912@gmail.com](mailto:Phattp1912@gmail.com)
- GitHub: [@phattpde140043](https://github.com/phattpde140043)

---
*Built for production-grade autonomous efficiency.*
