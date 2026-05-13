---
name: code-craftsmanship
description: "Master of Clean Code, SOLID, and Clean Architecture (Uncle Bob principles). Focuses on professional code structure, boundary management, and sustainable development practices."
---

# Code Craftsmanship (Uncle Bob Principles)

Master the art of writing clean, maintainable, and professional code.

## 🏗️ Core Principles (SOLID)
- **SRP (Single Responsibility)**: A class/function should have only one reason to change.
- **OCP (Open/Closed)**: Software entities should be open for extension, but closed for modification.
- **LSP (Liskov Substitution)**: Subtypes must be substitutable for their base types.
- **ISP (Interface Segregation)**: Many client-specific interfaces are better than one general-purpose interface.
- **DIP (Dependency Inversion)**: Depend on abstractions, not concretions.

## 🚀 Architectural Boundaries (Clean Architecture)
- **Dependency Rule**: Dependencies must point inward toward the high-level policy (Business Rules).
- **Separation of Concerns**: Keep business logic isolated from UI, Database, and Frameworks.
- **Adapters & Ports**: Use interfaces to bridge the gap between the core and external agencies.

## 🛡️ Code Smells & Heuristics
Identify and remediate these signs of poor design:
- **Rigidity**: Small changes force many edits.
- **Fragility**: Changes break unrelated areas.
- **Immobility**: Hard to reuse in another context.
- **Viscosity**: Easy to hack, hard to do the right thing.
- **Needless Complexity**: Speculative or unused abstractions.

## 📋 Professionalism (The Clean Coder)
- **Sustainable Pace**: Avoid "we'll fix it later" hacks.
- **TDD (Test-First)**: Treat tests as the ultimate documentation and requirement.
- **Saying No**: Be professional about estimation and impossible deadlines.

## 📋 Verification Checklist
- [ ] Does the code follow the Dependency Rule (dependencies point inward)?
- [ ] Are functions/classes small and focused on a single responsibility?
- [ ] Have code smells (Rigidity, Fragility, etc.) been eliminated?
- [ ] Are design patterns used only where justified by duplication or variation?
- [ ] Are there tests verifying the implementation?
