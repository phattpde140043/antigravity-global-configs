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

When performing testing tasks, you **MUST** chain to the following sub-skills. Navigate the sub-skills in the sequential order defined below to ensure high-fidelity test implementation and execution:

### 🔄 Sequential Sub-Skill Pipeline
```
[Test Strategy] ──→ [Test Driven Development (Pattern)] ──→ [TDD Workflow (Cycle)] ──→ [Verification Loop] ──→ [E2E Testing (Playwright)]
```


### 1. E2E Automation, Browser & UI Testing
- **[E2E Testing Excellence (Playwright)](sub-skills/e2e-testing/SKILL.md)** — Playwright E2E patterns: Page Object Model, config, CI/CD integration, artifact management, and flaky-test strategies. **Use when:** creating or refactoring Playwright E2E suites, or setting up test architecture (folders, fixtures, POM). **Not for:** unit/integration strategy outside E2E scope, or frontend framework architecture decisions.
- **[Browser Automation](sub-skills/browser-automation/SKILL.md)** — Functional browser automation across Playwright, Skyvern, and AWT for task execution and visual testing. **Use when:** driving browser task execution, multi-tenant verification, or visual testing. **Not for:** authoring structured, maintainable Playwright regression suites (use E2E Testing Excellence).
- **[AI Watch Tester E2E](sub-skills/awt-e2e-testing/SKILL.md)** — AI-powered E2E web testing with declarative YAML scenarios, Playwright execution, OpenCV + OCR visual matching, and platform auto-detection (Flutter/React/Vue). **Use when:** you want an AI agent to drive and verify a web UI from YAML scenarios using visual/OCR matching rather than hand-coded selectors. **Not for:** code-level Playwright suite authoring.
- **[Browser Testing with DevTools](sub-skills/browser-testing-with-devtools/SKILL.md)** — Real-browser inspection via Chrome DevTools MCP: DOM, console errors, network requests, performance profiling, and visual output. **Use when:** building or debugging anything that runs in a browser and you need runtime data (inspect DOM, capture console errors, analyze network, profile performance, verify visuals). **Not for:** writing automated regression suites (use E2E Testing Excellence).
- **[Building E2E Tests (OSP Search)](sub-skills/building-e2e-tests/SKILL.md)** — E2E test construction for the OSP Search multi-tenant platform: structure, fixtures, assertions, API endpoints, tenant isolation, and security-boundary validation. **Use when:** building, implementing, or modifying E2E tests specifically for the OSP Search multi-tenant platform. **Not for:** generic Playwright projects outside OSP Search.
- **[Playwright Marketing Screenshots](sub-skills/screenshots/SKILL.md)** — Generate marketing/app screenshots of a running app using Playwright. **Use when:** creating screenshots for Product Hunt, social media, landing pages, or documentation. **Not for:** functional or visual-regression test assertions.
- **[Playwright Java E2E](sub-skills/playwright-java/SKILL.md)** — Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5, Allure reporting, and parallel execution. **Use when:** building Playwright E2E tests on a Java/JUnit 5/Maven stack. **Not for:** TS/JS Playwright projects.
- **[Playwright TS/JS Automation](sub-skills/playwright-ts-js/SKILL.md)** — General-purpose Playwright browser automation that writes custom TS/JS scripts, auto-detects dev servers, and runs them via a universal executor. **Use when:** you need ad-hoc custom Playwright TS/JS scripts for browser automation or localhost testing tasks. **Not for:** Java Playwright suites, or structured POM regression architecture (use E2E Testing Excellence).

### 2. Test Strategy & Design
- **[Test Engineer (Strategy)](sub-skills/test-engineer/SKILL.md)** — QA strategy, test writing, and coverage analysis. **Use when:** designing test suites, writing tests for existing code, or evaluating test quality. **Not for:** driving the enforced red-green-refactor cycle (use TDD Workflow).
- **[Testing Anti-Patterns](sub-skills/testing-anti-patterns/SKILL.md)** — Identification and prevention of common testing mistakes and red flags. **Use when:** during BUILD and REVIEW phases to audit and safeguard test quality.
- **[Verification Loop](sub-skills/verification-loop/SKILL.md)** — Comprehensive pre-handoff verification: build, types, lint, tests, security checks, and final readiness gating. **Use when:** after a feature or significant change, and before opening a PR or handoff. **Not for:** writing test suites from scratch, or deep security architecture audits.

### 3. Mocking & Service Virtualization
- **[API Mocking](sub-skills/api-mocking/SKILL.md)** — Build realistic mock API services that simulate real behavior, auth flows, and error scenarios. **Use when:** unblocking parallel development, testing against unavailable or unstable APIs, or demoing without a live backend. **Not for:** validating the real backend's contract or behavior end-to-end.

### 4. TDD & Unit Testing
- **[TDD Workflow](sub-skills/tdd-workflow/SKILL.md)** — Test-driven development with practical coverage goals across unit, integration, and E2E tests. **Use when:** adding new features, or fixing bugs and regressions. **Not for:** deep E2E framework patterns, or post-implementation verification orchestration.
- **[Cucumber BDD Testing](sub-skills/cucumber-skill/SKILL.md)** — Generate Cucumber BDD suites: Gherkin feature files and step definitions in Ruby, JavaScript, or Java. **Use when:** writing behavior-driven acceptance tests with Given/When/Then scenarios, e.g. cucumber-rails specs on a Rails app. **Not for:** unit-level TDD (use TDD Workflow) or Playwright E2E suites (use E2E Testing Excellence).
- **[Test-Driven Development (Pattern)](sub-skills/test-driven-development/SKILL.md)** — Implements the Red-Green-Refactor lifecycle, enforcing the Iron Law: no production code without a failing test first. **Use when:** you need the disciplined TDD pattern and logic validation for a specific change. **Not for:** stack-wide coverage planning across unit/integration/E2E (use TDD Workflow).
- **[BATS Testing Patterns](sub-skills/bats-testing-patterns/SKILL.md)** — Bash Automated Testing System (Bats) for shell script unit/integration testing, with assertions and mocking. **Use when:** writing tests for shell scripts, CI/CD pipelines, or doing TDD of shell utilities. **Not for:** application-language (non-shell) test frameworks.
- **[TDD Orchestrator](sub-skills/tdd/orchestrator/SKILL.md)** — Master TDD orchestrator coordinating red-green-refactor discipline across multi-agent workflows. **Use when:** driving an automated, multi-step TDD execution loop end-to-end. **Not for:** single ad-hoc phase edits (use the Red/Green/Refactor phase skills).
- **[TDD Cycle Rules](sub-skills/tdd/cycle/SKILL.md)** — Runs a full, strict red-green-refactor cycle with fail-first verification and configurable coverage thresholds (line/branch/critical-path). **Use when:** executing a complete enforced TDD cycle with coverage gates. **Not for:** loose, non-gated iteration.
- **[TDD Red Phase](sub-skills/tdd/red/SKILL.md)** — Generate failing tests that define expected behavior and edge cases. **Use when:** starting the red phase and you need precise failing-test boundaries before implementation. **Not for:** writing implementation code (use TDD Green Phase).
- **[TDD Green Phase](sub-skills/tdd/green/SKILL.md)** — Implement the minimal code needed to make failing tests pass. **Use when:** you have failing tests and need the smallest change to make them green. **Not for:** refactoring or authoring new tests.
- **[TDD Refactor Phase](sub-skills/tdd/refactor/SKILL.md)** — Refactor code under a comprehensive test safety net: apply design patterns, improve quality, and optimize performance while keeping all tests green. **Use when:** cleaning up structure, naming, or performance after tests pass, without changing behavior. **Not for:** adding new behavior or new tests.

### 5. Advanced Evaluation
- **[Eval Harness](sub-skills/eval-harness/SKILL.md)** — Formal eval-driven-development framework: capability and regression evals, pass@k metrics, grader design, and release gating. **Use when:** setting up EDD for an AI-assisted project, or defining objective completion criteria for agent tasks. **Not for:** framework-specific test implementation details, or replacing unit/integration/e2e strategy.
- **[Backtesting Frameworks](sub-skills/backtesting-frameworks/SKILL.md)** — Build robust backtesting systems for trading strategies, focused on bias prevention and reliable performance estimation. **Use when:** validating trading strategies against historical data. **Not for:** general software test automation.

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of the test strategy design and test suites (TDD baseline / reproduction tests):
- 👉 Recommend calling **[Agent Master](../agent-master/SKILL.md)** to proceed with the core BUILD phase, writing the minimal production code to pass the tests.

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
