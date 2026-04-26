# 🪐 Antigravity Global Configs

**Production-grade engineering instructions for AI coding agents.**

These configurations encode the workflows, quality gates, and best practices that senior engineers use when building software. They ensure that AI agents follow a disciplined process across every phase of development.

```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

---

## Commands

6 core slash commands that map to the development lifecycle defined in [`workflow.md`](./workflow.md).

| Phase | Command | Key Principle |
|-------|---------|---------------|
| **DEFINE** | `/spec` | Spec before code |
| **PLAN** | `/plan` | Small, atomic tasks |
| **BUILD** | `/build` | One slice at a time |
| **VERIFY** | `/test` | Tests are proof |
| **REVIEW** | `/review` | Improve code health |
| **SHIP** | `/ship` | Faster is safer |

---

## Core Infrastructure

The project follows a modular architecture for clear separation of concerns:

- **[`system.md`](./system.md)**: **The Behavior Model**. Defines the agent's persona, communication style, and autonomous mindset.
- **[`rules.md`](./rules.md)**: **Operational Governance**. Strictly enforces coding standards, security protocols, and scope control.
- **[`workflow.md`](./workflow.md)**: **The Gated Lifecycle**. Mandatory state machine (DEFINE → SHIP) for all non-trivial tasks.
- **[`patterns.md`](./patterns.md)**: **Communication Patterns**. Standardized templates for confusion management and change summaries.
- **[`skill-router.md`](./skill-router.md)**: **Strategic Orchestrator**. Maps tasks to specialized skillsets based on domain expertise.

---

## Quick Start

### Integration

To use these configs, ensure your Agent is pointed to this directory.

**Manual Setup:**
```bash
git clone git@github.com:phattpde140043/antigravity-global-configs.git ~/.antigravity-global
```

**Global Loader:**
Reference the files in your global instruction loader:
```markdown
- Load and apply rules.md, system.md, and workflow.md from ~/.antigravity-global/
```

---

## Specialized Skills

Under the hood, the system activates over **75** specialized skills.

### 🏗️ Strategy & Planning
| Skill | Description |
|-------|-------------|
| [architect](./skills/architect/SKILL.md) | Software architecture specialist for system design, scalability, and technical decision-making. |
| [architecture-design](./skills/architecture-design/SKILL.md) | High-level system design and architectural pattern selection. |
| [backend-architect](./skills/backend-architect/SKILL.md) | specialized in backend system design, database schemas, and API orchestration. |
| [idea-refine](./skills/idea-refine/SKILL.md) | Strategic ideation: divergent expansion and convergent refining of raw concepts. |
| [spec-driven-development](./skills/spec-driven-development/SKILL.md) | Creating structured specifications and success criteria before implementation. |
| [planning-and-task-breakdown](./skills/planning-and-task-breakdown/SKILL.md) | Decomposing approved specs into small, verifiable, vertically-sliced tasks. |
| [implementation-planning](./skills/implementation-planning/SKILL.md) | High-rigor engineering planning combining strategic architecture with tactical TDD execution. |
| [context-engineering](./skills/context-engineering/SKILL.md) | AI-human collaboration: brain dumps, confusion management, and inline planning. |
| [product-capability](./skills/product-capability/SKILL.md) | Translating PRD intent into implementation-ready capability plans. |
| [documentation-and-adrs](./skills/documentation-and-adrs/SKILL.md) | Recording architectural decisions (ADRs) and "Why over What" context. |

### 💻 Implementation & Build
| Skill | Description |
|-------|-------------|
| [frontend-patterns](./skills/frontend-patterns/SKILL.md) | React component architecture and modern frontend best practices. |
| [frontend-design](./skills/frontend-design/SKILL.md) | Create distinctive, production-grade frontend interfaces with high design quality. |
| [dotnet-patterns](./skills/dotnet-patterns/SKILL.md) | Idiomatic C# and .NET service development and library patterns. |
| [nodejs-backend](./skills/nodejs-backend/SKILL.md) | Production-grade Node.js backend engineering (Express, TypeScript, Prisma). |
| [mcp-server-patterns](./skills/mcp-server-patterns/SKILL.md) | Creating and updating Model Context Protocol servers. |
| [api-design](./skills/api-design/SKILL.md) | Contract-first design, Hyrum's Law, and boundary validation. |
| [source-driven-development](./skills/source-driven-development/SKILL.md) | Grounding implementation decisions in official documentation. |
| [documentation-lookup](./skills/documentation-lookup/SKILL.md) | Using up-to-date library and framework docs via MCP. |
| [browser-testing-with-devtools](./skills/browser-testing-with-devtools/SKILL.md) | Live runtime inspection and visual verification via DevTools. |
| [ci-cd-and-automation](./skills/ci-cd-and-automation/SKILL.md) | Pipeline logic, quality gates, and deployment strategies. |
| [nextjs-turbopack](./skills/nextjs-turbopack/SKILL.md) | Next.js 16+ and Turbopack optimization. |
| [deprecation-and-migration](./skills/deprecation-and-migration/SKILL.md) | Code lifecycle: Strangler/Adapter patterns and zombie code elimination. |
| [framework-migration](./skills/framework-migration/SKILL.md) | Expert framework and code migration engineering. |
| [code-generation](./skills/code-generation/SKILL.md) | Automated code generation patterns and templates. |
| [code-architect](./skills/code-architect/SKILL.md) | Concrete file/interface blueprinting and structural design. |
| [code-explorer](./skills/code-explorer/SKILL.md) | Navigating and understanding large, unfamiliar codebases. |

### ✅ Quality & Verification
| Skill | Description |
|-------|-------------|
| [test-driven-development](./skills/test-driven-development/SKILL.md) | Implementation of the TDD lifecycle (Red-Green-Refactor). |
| [tdd-workflow](./skills/tdd-workflow/SKILL.md) | Practical TDD execution for new features and bug fixes. |
| [test-engineer](./skills/test-engineer/SKILL.md) | QA engineer specialized in test strategy and coverage analysis. |
| [e2e-testing](./skills/e2e-testing/SKILL.md) | Playwright E2E testing patterns and Page Object Model. |
| [testing-anti-patterns](./skills/testing-anti-patterns/SKILL.md) | Identification and prevention of common testing mistakes. |
| [eval-harness](./skills/eval-harness/SKILL.md) | Formal evaluation framework for AI coding sessions. |
| [verification-loop](./skills/verification-loop/SKILL.md) | Comprehensive verification system before PR or handoff. |
| [code-reviewer](./skills/code-reviewer/SKILL.md) | Staff-level 5D review: correctness, readability, architecture, security, performance. |
| [code-review-excellence](./skills/code-review-excellence/SKILL.md) | Advanced code review practices and feedback loops. |
| [pr-review](./skills/pr-review/SKILL.md) | Deep, production-grade pull request reviews (~100 lines). |
| [csharp-reviewer](./skills/csharp-reviewer/SKILL.md) | specialized code review for C#/.NET projects. |
| [systematic-debugging](./skills/systematic-debugging/SKILL.md) | Elite investigative framework based on the Iron Law. |
| [build-error-resolver](./skills/build-error-resolver/SKILL.md) | Rapid diagnosis and resolution of build and compiler errors. |
| [coding-standards](./skills/coding-standards/SKILL.md) | KISS/DRY/YAGNI principles and code smell checks. |
| [code-simplifier](./skills/code-simplifier/SKILL.md) | Refactoring for clarity, simplicity, and maintainability. |

### 🛡️ Security & Compliance
| Skill | Description |
|-------|-------------|
| [security-and-hardening](./skills/security-and-hardening/SKILL.md) | Hardens code against vulnerabilities and untrusted data. |
| [security-auditor](./skills/security-auditor/SKILL.md) | Vulnerability detection, threat modeling, and secure coding. |
| [security-review](./skills/security-review/SKILL.md) | Practical security checklist for auth, secrets, and APIs. |
| [security-design](./skills/security-design/SKILL.md) | Building security into the design phase (STRIDE). |
| [security-checklists](./skills/security-checklists/SKILL.md) | Quick reference for OWASP Top 10:2025 audits. |
| [penetration-testing](./skills/penetration-testing/SKILL.md) | Ethical hacking methodology for security assessments. |
| [backend-security-coder](./skills/backend-security-coder/SKILL.md) | specialized security patterns for backend development. |
| [infrastructure-security](./skills/infrastructure-security/SKILL.md) | Cloud infrastructure security (AWS, IAM, Secrets). |
| [securities-audit](./skills/securities-audit/SKILL.md) | Deep security audit using multi-tenant isolation practices. |
| [regulatory-compliance](./skills/regulatory-compliance/SKILL.md) | GDPR, HIPAA, and PCI-DSS compliance implementations. |

### 🚀 Advanced & Systems Engineering
| Skill | Description |
|-------|-------------|
| [performance-optimization](./skills/performance-optimization/SKILL.md) | expert performance engineering for code, DBs, and APIs. |
| [distributed-system](./skills/distributed-system/SKILL.md) | Designing and implementing scalable distributed architectures. |
| [resilience-patterns](./skills/resilience-patterns/SKILL.md) | Applying retry, circuit breaker, and idempotency patterns. |
| [a11y-architect](./skills/a11y-architect/SKILL.md) | Designing for accessibility and inclusive user experiences. |
| [brain-context-engineering](./skills/brain-context-engineering/SKILL.md) | Advanced context management for long-running AI sessions. |
| [dmux-workflows](./skills/dmux-workflows/SKILL.md) | Multi-stream workflow orchestration for complex tasks. |
| [strategic-compact](./skills/strategic-compact/SKILL.md) | Manual context compaction to preserve relevance. |
| [agent-introspection-debugging](./skills/agent-introspection-debugging/SKILL.md) | Debugging the AI agent's own reasoning and state. |
| [workspace-surface-audit](./skills/workspace-surface-audit/SKILL.md) | Auditing and classifying workspace-specific AI instructions. |
| [backtesting-frameworks](./skills/backtesting-frameworks/SKILL.md) | Frameworks for testing strategies against historical data. |

### 🔍 Research, Business & Content
| Skill | Description |
|-------|-------------|
| [deep-research](./skills/deep-research/SKILL.md) | Comprehensive research with source synthesis and verification. |
| [exa-search](./skills/exa-search/SKILL.md) | Neural search for web, code, and company research. |
| [market-research](./skills/market-research/SKILL.md) | Competitive analysis and industry intelligence. |
| [investor-materials](./skills/investor-materials/SKILL.md) | Creating pitch decks, memos, and financial models. |
| [investor-outreach](./skills/investor-outreach/SKILL.md) | Draft cold emails and communications for fundraising. |
| [article-writing](./skills/article-writing/SKILL.md) | High-quality technical and business article generation. |
| [brand-voice](./skills/brand-voice/SKILL.md) | Maintaining consistent brand identity in communications. |
| [content-engine](./skills/content-engine/SKILL.md) | Automated content creation and distribution pipelines. |
| [conversation-analyzer](./skills/conversation-analyzer/SKILL.md) | Analyzing user interactions to improve AI performance. |

### 🌐 Platform & Specialized
| Skill | Description |
|-------|-------------|
| [x-api](./skills/x-api/SKILL.md) | X/Twitter API integration for posting and analytics. |
| [crosspost](./skills/crosspost/SKILL.md) | Cross-platform content distribution patterns. |
| [fal-ai-media](./skills/fal-ai-media/SKILL.md) | Unified media generation (Image, Video, Audio) via fal.ai. |
| [frontend-slides](./skills/frontend-slides/SKILL.md) | Create animation-rich HTML presentations. |

---

## How it Works

Every instruction follows a consistent anatomy:
- **Process over Prose**: Workflows are step-by-step actions, not just advice.
- **Verification Gates**: Every phase ends with mandatory evidence requirements (tests passing, build output).
- **Anti-Rationalization**: Explicitly rebuts common excuses for skipping quality steps.

---

## 👨‍💻 Author

**Tran Phu Phat** (phattpde140043)
- Email: [Phattp1912@gmail.com](mailto:Phattp1912@gmail.com)
- GitHub: [@phattpde140043](https://github.com/phattpde140043)

---
*Built for production-grade autonomous efficiency.*
