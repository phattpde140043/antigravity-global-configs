---
name: software-architecture
description: "Expert in Software Architecture focusing on Clean Architecture, DDD, and Systemic Integrity."
category: engineering
metadata:
  triggers: [clean-architecture, ddd, modularization, system-integrity, architecture-standards]
---

# Software Architecture Excellence

## 🎯 Objectives
1. Ensure modularization and Separation of Concerns (SoC).
2. Apply Library-First policy (Use existing libraries instead of manual utility code).
3. Control source code complexity via hard limits (Limit checks).

## 🛠️ Execution Rules
1. **Naming Standard**: 
    - PROHIBITED: `utils`, `helpers`, `common`, `shared`.
    - RECOMMENDED: `OrderCalculator`, `InvoiceGenerator`, `AuthService`.
2. **Code Limits**: 
    - Function: < 50 lines.
    - File: < 200 lines.
    - Nesting: Max 3 levels.
3. **Coding Style**:
    - Prioritize **Early Return**.
    - Use Arrow functions where applicable.
4. **Library-First Policy**: 
    - Check standard libraries (npm/nuget) before writing custom generic logic (Retry, Validation, Mapping).
    - **Justification for Custom Code**: Custom code is only allowed if:
        - Specific business logic is unique to the domain.
        - Performance-critical paths require extreme optimization.
        - Security-sensitive code requires absolute control.
        - Existing libraries would introduce excessive dependency bloat for trivial tasks.
        - Thorough evaluation (min. 3 libraries) shows no fit for requirements.

## 📋 Acceptance Criteria (AC)
- [ ] No file exceeds 200 lines.
- [ ] Module names reflect domain-specific business logic.
- [ ] No nested logic beyond 3 levels.
