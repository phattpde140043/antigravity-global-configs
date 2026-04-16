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
- **[`skill-router.md`](./skill-router.md)**: **Strategic Orchestrator**. Maps tasks to specialized skillsets.

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

Under the hood, the system activates over 40 specialized skills. Here are the key ones:

### Define & Plan
| Skill | What It Does |
|-------|-------------|
| [architect](./skills/architect/SKILL.md) | Planning new cross-cutting features and refactoring large systems. |
| [idea-refine](./skills/idea-refine/SKILL.md) | Strategic ideation: divergent expansion and convergent refining of raw concepts. |
| [spec-driven-development](./skills/spec-driven-development/SKILL.md) | Creating structured specifications and success criteria before any implementation. |
| [planning-and-task-breakdown](./skills/planning-and-task-breakdown/SKILL.md) | Decomposing approved specs into small, verifiable, vertically-sliced tasks. |
| [implementation-planning](./skills/implementation-planning/SKILL.md) | Decomposing approved specs into concrete, verifiable task lists. |
| [context-engineering](./skills/context-engineering/SKILL.md) | AI-human collaboration: brain dumps, confusion management, and inline planning. |
| [documentation-and-adrs](./skills/documentation-and-adrs/SKILL.md) | Recording architectural decisions (ADRs) and "Why over What" context. |

### Build
| Skill | What It Does |
|-------|-------------|
| [frontend-patterns](./skills/frontend-patterns/SKILL.md) | React component architecture and modern frontend best practices. |
| [dotnet-patterns](./skills/dotnet-patterns/SKILL.md) | C# / .NET service development and library patterns. |
| [source-driven-development](./skills/source-driven-development/SKILL.md) | Verifying framework patterns and API signatures against official documentation. |
| [api-and-interface-design](./skills/api-design/SKILL.md) | Contract-first design, Hyrum's Law, One-Version Rule, and boundary validation. |
| [browser-testing-with-devtools](./skills/browser-testing-with-devtools/SKILL.md) | Live runtime inspection, DOM/Console/Network analysis, and visual verification. |
| [deprecation-and-migration](./skills/deprecation-and-migration/SKILL.md) | Code lifecycle: Strangler/Adapter patterns and zombie code elimination. |
| [mcp-server-patterns](./skills/mcp-server-patterns/SKILL.md) | Creating and updating Model Context Protocol servers. |

### Verify & Review
| Skill | What It Does |
|-------|-------------|
| [test-driven-development](./skills/test-driven-development/SKILL.md) | Driving feature implementation and bug fixes with failing tests (Prove-It pattern). |
| [test-engineer](./skills/test-engineer/SKILL.md) | Designing test suites, writing coverage-focused tests, and analyzing QA gaps. |
| [tdd-workflow](./skills/tdd-workflow/SKILL.md) | Red-Green-Refactor logic for bug fixes and new features. |
| [code-reviewer](./skills/code-reviewer/SKILL.md) | Staff-level 5nd-dimension review: correctness, readability, architecture, security, performance. |
| [security-and-hardening](./skills/security-and-hardening/SKILL.md) | Treating input as hostile and protecting against OWASP vulnerabilities. |
| [security-auditor](./skills/security-auditor/SKILL.md) | Vulnerability detection, threat modeling, and practical exploit-focused hardening. |
| [security-review](./skills/security-review/SKILL.md) | Hardening authentication, authorization, and input handling. |
| [ci-cd-and-automation](./skills/ci-cd-and-automation/SKILL.md) | Pipeline logic, quality gates, feature flags, and deployment strategies. |
| [debugging-and-error-recovery](./skills/debugging-and-error-recovery/SKILL.md) | Systematic root-cause debugging (Repro, Localize, Reduce, Bisect). |
| [coding-standards-and-simplification](./skills/coding-standards/SKILL.md) | KISS/DRY/YAGNI principles, code smell checks, and simplification process. |

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
