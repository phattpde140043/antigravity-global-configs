---
name: coding-standards
description: "Core quality baseline. Focuses on KISS, DRY, YAGNI, Poka-Yoke, and Idempotency. Part of the agent-master discipline."
---

# Coding Standards (Senior Excellence)

## 💎 The Diamond Standard
1. **Scalable**: Zero technical debt, growth-ready.
2. **Secure**: Zero-Trust by default, OWASP compliant.
3. **Aesthetic**: Clean, balanced, and harmonious code.

## 🛠️ Core Principles
- **Poka-Yoke (Error Proofing)**: Design systems where invalid states are unrepresentable (e.g., using Discriminated Unions/Enums instead of strings).
- **Idempotency by Design**: Mutation operations must be safe to retry. Handle "Conflict" as "Success" if the state is already as desired.
- **Kaizen (Boy Scout Rule)**: Always leave the code cleaner than you found it. Small, compound improvements.
- **TDD Iron Law**: Write a failing test before any production code. No test = No code.
- **Chesterton's Fence**: Understand WHY code exists before simplifying or removing it.

## 📏 Clean Code Mandate
- **Small Functions**: Aim for **< 20 lines**. Max 50.
- **SRP**: One function, one responsibility.
- **Naming**: Intention-revealing names. Booleans should be predicates (`isReady`, `hasAccess`).
- **Early Returns**: Use guard clauses to eliminate nesting (Max 3 levels).

## 🧪 Verification
- All tests pass.
- Linter and Build are green.
- Refactoring is separate from feature work.
