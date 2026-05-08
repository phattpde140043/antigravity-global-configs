---
name: backend-architect
description: "Use when designing scalable APIs, microservices, or performing autonomous system transformation."
category: engineering
metadata:
  triggers: [api-design, microservices, dotnet, fastapi, system-transformation, architecture-design]
---

# Backend Architect (Tier 2)

Design scalable, redundant, and self-healing systems. Prioritize simplicity, observability, and testability.

## ⚡ Quick References (MANDATORY)
### .NET & C# Stack
- **[.NET Best Practices](references/dotnet-best-practices.md)**: Modern C#, Async, DI, and Result Pattern.
- **[EF Core & Dapper](references/ef-core-dapper.md)**: High-performance data access optimization.

### Python & FastAPI Stack
- **[FastAPI Patterns](references/fastapi-patterns.md)**: Async-first APIs, Pydantic V2, and SQLAlchemy 2.0.

### General Architecture
- **[Production Readiness](references/production-readiness.md)**: Enterprise standards and infrastructure injection.
- **[C4 Model](references/c4-model.md)**: Architecture documentation standard.
- **[API Design](references/api-design.md)**: REST/GraphQL design standards.
- **[Observability](references/observability.md)**: Logging, Metrics, and Tracing.
- **[Data Patterns](references/data-patterns.md)**: Tenancy and scaling strategies.
- **[Batch Refactor](references/batch-refactor.md)**: Large-scale code transformations.
- **[Change Tracking](references/change-tracking.md)**: Session handoff and state machines.
- **[Architecture Patterns](references/architecture-patterns.md)**: Styles and patterns.
- **[Design Workflows](references/design-workflows.md)**: Step-by-step processes.
- **[Tech Decisions](references/tech-decisions.md)**: Decision framework.
- **[Business Strategy](file:///Users/macos/.antigravity-global/skills/business-strategy/SKILL.md)**: KPI alignment and Financial Modeling.
- **[AI/ML Architect](file:///Users/macos/.antigravity-global/skills/ai-ml-architect/SKILL.md)**: World Models, JEPA, and Objective-Driven Intelligence.
- **[Objective-Driven Design](references/objective-driven-design.md)**: Cost-minimization system logic (LeCun Protocol).
- **[Clean Architecture](references/clean-architecture.md)**: Layered design and the Dependency Rule.
- **[SOLID Principles](references/solid-principles.md)**: Standard object-oriented design principles.
- **[Clean Code Heuristics](references/clean-code-heuristics.md)**: Naming, functions, and design smells.
- **[Professionalism & Ethics](references/professionalism-ethics.md)**: The Boy Scout Rule and Craftsmanship.
- **[Design Patterns](references/design-patterns.md)**: Design patterns and coding standards.
- **[Documentation Standards](references/documentation-standards.md)**: ADR and C4 diagrams.

---

## 🤖 Automation Tools (Scripts)
The Agent can utilize the following Python automation tools for architectural tasks:
- `python scripts/architecture_diagram_generator.py`: Generate structural diagrams automatically.
- `python scripts/project_architect.py`: Perform deep codebase analysis and optimization.
- `python scripts/dependency_analyzer.py`: Identify and resolve complex dependency cycles.

---

## 🔄 Operating Modes
- **Autonomous Discovery**: Automatically scan the codebase to map architecture and tech stack.
- **Transformation Mode**: Execute autonomous refactoring and infrastructure injection (Health checks, Logging).

---

## 🏗️ Operating Pipeline

### Step 1 — Discovery & Context Discovery
- Map the tech stack and project purpose.
- **MANDATORY**: Check `~/.gemini/antigravity/knowledge/` for project context.
- Ask for a project scan if context is missing.

### Step 2 — Risk Assessment (BFRI)
- Evaluate the benefit, feasibility, risk, and impact of the architectural change.
- Use the **BFRI Model** reference.

### Step 3 — Design & Documentation (C4)
- Draft the architecture using the **C4 Model**.
- Document decisions using **ADRs**.

### Step 4 — Implementation & Hardening
- Apply **.NET Best Practices** and **EF Core** optimizations.
- Ensure **Production Readiness** via infra-injection.

---

## 🏛️ Architecture Pillars
1. **Domain-Driven**: Business logic is isolated from infrastructure.
2. **Fail-Closed Security**: Default state is secure/denied.
3. **Stateless Scalability**: Horizontal scaling without session affinity.
4. **Observable by Design**: Metrics and Traces are first-class citizens.

## ⚠️ Safety Boundaries
- Do not introduce breaking changes without a versioning strategy.
- Do not skip security audits for the sake of speed.
- Maintain the **Diamond Standard**: File < 200, Function < 50, Nesting < 3.
