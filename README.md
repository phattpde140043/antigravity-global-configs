# 🪐 Antigravity Global Configs

**Production-grade engineering instructions for AI coding agents.**

These configurations encode the workflows, quality gates, and best practices that senior engineers use when building software.

---

## 🏗️ Master Orchestrators (The Brains)

The system uses a **Conductor-Musician** pattern. These 4 Master Skills orchestrate specialized sub-disciplines.

| Master Skill | Responsibility |
|:---|:---|
| [backend-architect](./skills/backend-architect/SKILL.md) | **System Lead**. Microservices, Scalability, and Clean Architecture standards. |
| [security-master](./skills/security-master/SKILL.md) | **Security Lead**. Threat Modeling, Secure Coding, Pentesting, and Hardening. |
| [senior-qa](./skills/senior-qa/SKILL.md) | **Quality Lead**. E2E (Playwright), Unit Testing, TDD, and Flaky Mitigation. |
| [review-master](./skills/review-master/SKILL.md) | **Audit Lead**. Readiness Scoring (>85), AI Slop Scan, and PR Excellence. |

---

## 🛠️ Specialized Sub-Disciplines (The Musicians)

The Master Skills delegate deep-dive tasks to these specialized skills located in their respective `sub-skills/` directories.

### 🛡️ Security Cluster
- [Backend Security Coder](./skills/security-master/sub-skills/backend-security-coder/SKILL.md)
- [Infrastructure Security](./skills/security-master/sub-skills/infrastructure-security/SKILL.md)
- [Penetration Testing](./skills/security-master/sub-skills/penetration-testing/SKILL.md)
- [Security Design & STRIDE](./skills/security-master/sub-skills/security-design/SKILL.md)

### ✅ QA & Testing Cluster
- [E2E Testing Excellence](./skills/senior-qa/sub-skills/e2e-testing/SKILL.md)
- [TDD Workflow](./skills/senior-qa/sub-skills/tdd-workflow/SKILL.md)
- [Test Engineer Strategy](./skills/senior-qa/sub-skills/test-engineer/SKILL.md)
- [Testing Anti-Patterns](./skills/senior-qa/sub-skills/testing-anti-patterns/SKILL.md)

### 🔍 Review & Audit Cluster
- [Code Review Excellence](./skills/review-master/sub-skills/code-review-excellence/SKILL.md)
- [C# Reviewer](./skills/review-master/sub-skills/csharp-reviewer/SKILL.md)
- [Vibe Code Auditor](./skills/review-master/sub-skills/vibe-code-auditor/SKILL.md)
- [PR Review Template](./skills/review-master/sub-skills/pr-review/SKILL.md)

### 📐 Architecture Cluster
- [Software Architecture](./skills/backend-architect/sub-skills/software-architecture/SKILL.md)
- [Architecture Design](./skills/backend-architect/sub-skills/architecture-design/SKILL.md)
- [Code Architect](./skills/backend-architect/sub-skills/code-architect/SKILL.md)

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
