---
name: senior-qa
description: "Master QA Orchestrator. Coordinates Test Strategy, E2E Automation, Unit Testing, and TDD through specialized sub-disciplines."
expert: true
metadata:
  category: master-orchestrator
  triggers: playwright, e2e, unit-test, flaky-test, test-strategy, quality-review
---

# 🏆 Senior QA Orchestrator

The lead authority for test engineering and systemic stability. This master skill coordinates specialized testing disciplines to ensure a flake-free, high-coverage environment.

---

## 🧭 Quality Strategy
- **Test at the Right Level**: Logic (Unit), Boundaries (Integration), User Flow (E2E).
- **Behavior over Implementation**: Focus on user impact, not code structure.
- **Root Cause Culture**: Every bug must have a failing test before the fix.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing testing tasks, you **MUST** chain to the following sub-skills:

### 1. E2E Automation & UI Testing
- For **Playwright**, POM, and Flaky Mitigation:
  👉 **[E2E Testing Excellence (Playwright)](sub-skills/e2e-testing/SKILL.md)**
- For **Browser Automation** and Low-Level Interaction:
  👉 **[Browser Automation](sub-skills/browser-automation/SKILL.md)**
- For **DevTools Debugging** and Browser Analysis:
  👉 **[Browser Testing with DevTools](sub-skills/browser-testing-with-devtools/SKILL.md)**

### 2. Test Strategy & Design
- For **Test Writing**, Coverage Analysis, and Scenarios:
  👉 **[Test Engineer (Strategy)](sub-skills/test-engineer/SKILL.md)**
- For **Identifying Red Flags** and Common Pitfalls:
  👉 **[Testing Anti-Patterns](sub-skills/testing-anti-patterns/SKILL.md)**
- For **Verification Loops** and Systematic Validation:
  👉 **[Verification Loop](sub-skills/verification-loop/SKILL.md)**

### 3. TDD & Unit Testing
- For **Red-Green-Refactor** cycles and Python/Backend logic:
  👉 **[TDD Workflow](sub-skills/tdd-workflow/SKILL.md)**
- For **Testing Patterns** and specific logic validation:
  👉 **[Test Driven Development](sub-skills/test-driven-development/SKILL.md)**

### 4. Advanced Evaluation
- For **Evaluation Harnesses** and Model Scoring:
  👉 **[Eval Harness](sub-skills/eval-harness/SKILL.md)**
- For **Backtesting Frameworks** and Historical Validation:
  👉 **[Backtesting Frameworks](sub-skills/backtesting-frameworks/SKILL.md)**

---

## 🔍 Investigation Protocol
This Orchestrator uses the **[Agent Review Framework](file:///Users/macos/.antigravity-global/agent_review_framework.md)** to verify fixes.
1. **Reproduce**: Use `test-engineer` to write the failing case.
2. **Implement**: Use `tdd-workflow` to drive the fix.
3. **Validate**: Use `e2e-testing` to ensure zero regression.

---

## 🧪 Testing Strategy
- **Shift-Left**: Integrate testing into the earliest phases of development.
- **Web3 QA**: Implement Mainnet Forking, Account Impersonation, and Fuzzing (Foundry/Hardhat) for Smart Contracts.
- **Security & A11y**: Mandatory WCAG audits and vulnerability scanning in every release cycle.
- **Automated Fixing**: Use automated patterns to identify and remediate flaky or failing tests.

---

## 📈 Quality Metrics (DORA)
- **Flake Rate**: < 1%.
- **Coverage**: 80%+ on critical paths.
- **Reporting**: Detailed assessment in `docs/assessment/`.
