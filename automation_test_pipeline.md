# 🧪 Automation Test Pipeline (TAP) - Strategy & Execution

This document defines the lifecycle and execution pipeline for **Long-term Automated Testing**. This is a **Continuous Quality Gate** orchestrated by the `testing-workflow` skill, operating independently of the agent's task-specific verification loops.

---

## 1. Objective
To ensure the **OSP Search AI** ecosystem remains stable, secure, and performant through automated, repeatable, and environment-agnostic testing cycles.

## 2. Test Taxonomy (The Pyramid)

| Level | Type | Scope | Frequency | Tooling | Required Skill |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L1** | Unit/Component | Logic, UI components. | Every Commit | Jest / Pytest / xUnit | `tdd-workflow` / `frontend-unit-testing` / `python-unit-testing` |
| **L2** | Integration | Service-to-service, API. | Every PR | Playwright / Postman | `nodejs-backend` / `test-engineer` |
| **L3** | E2E / UI | User flows, Isolation. | Daily / Merge | Playwright | `e2e-testing` / `browser-automation` / `test-generator` |
| **L4** | Security | IDOR, XSS, RCE. | Weekly | OWASP ZAP | `securities-audit` / `penetration-testing` |
| **L5** | Performance | Latency, Load. | Bi-weekly | k6 / JMeter | `performance-optimization` |

---

## 3. The Pipeline Stages

### 🟢 Stage 1: The Local Gate (Pre-Commit)
*Goal: Catch simple errors before they reach the cloud.*
- **Linting**: Static analysis (`coding-standards`).
- **Unit Tests**: Logic and UI components (`tdd-workflow`, `frontend-unit-testing`, `python-unit-testing`).
- **Test Generation**: Automated drafting of test skeletons (`test-generator`).
- **Plan Verification**: Ensure test coverage in `implementation-planning` or `test-engineer`.

### 🟡 Stage 2: The Pull Request Gate (CI)
*Goal: Validate integration and prevent regressions in shared branches.*
- **Build Verification**: Compile in clean environment (`build-error-resolver`).
- **Smoke E2E**: Critical user journeys (`browser-automation`).
- **Security Audit**: Dependency scans (`securities-audit`).
- **PR Integrity**: Automated code review (`pr-review`).

### 🔴 Stage 3: The Deep Regression (Nightly/Scheduled)
*Goal: Comprehensive coverage without slowing down development.*
- **Full E2E Suite**: All 100+ scenarios (`e2e-testing`, `test-engineer`).
- **Multi-Tenant Isolation (ISO)**: Cross-tenant data checks (`security-and-hardening`).
- **Visual Regression**: UI consistency checks.
- **Anti-Pattern Scan**: Detect brittle tests (`testing-anti-patterns`).

### 🟣 Stage 4: The Release Gate (Pre-Production)
*Goal: Final sign-off for deployment.*
- **Performance Baseline**: P99 latency checks (`performance-optimization`).
- **Resilience Testing**: Chaos engineering light (`resilience-patterns`).
- **Compliance Audit**: Regulatory checks (`regulatory-compliance`).

---

## 4. Multi-Tenant Isolation Protocol (MTIP)
Automation tests **MUST** validate isolation for every new feature:
1. **Tenant Alpha** creates a resource (e.g., a Search Profile).
2. **Tenant Beta** attempts to Read, Update, or Delete Alpha's resource using its ID.
3. **Requirement**: System must return `401 Unauthorized`, `403 Forbidden`, or `404 Not Found`.
4. **Tooling**: Use standard `TenantContext` and `EntityHelper` fixtures to automate this flow.

---

## 5. Reporting & Observability
- **Dashboards**: Allure HTML reports hosted on CI artifacts or dedicated S3/GCS buckets.
- **Notifications**: 
  - 🔴 **FAIL**: Immediate Slack/Teams alert to `#eng-alerts`.
  - 🟢 **PASS**: Summary report to `#eng-status`.
- **Traces**: Playwright traces, videos, and console logs attached to failed E2E tests for 1-click debugging.

---

## 6. Flaky Test Management
Flaky tests are the "broken windows" of automation.
1. **Detection**: If a test fails once but passes on retry (auto-retry count = 2), it is marked as **FLAKY**.
2. **Quarantine**: Flaky tests are moved to a `quarantine/` folder or tagged `@flaky`. They still run but do not block the pipeline.
3. **SLA**: Flaky tests must be investigated and fixed or deleted within **72 hours**.

---

## 7. Ownership & Maintenance
- **QA/SDET**: Maintains the framework, runners, and infrastructure.
- **Backend/Frontend Developers**: Write tests for new features as part of the "Definition of Done".
- **Agent**: Assists in generating test boilerplate, documenting scenarios, and fixing failures identified by TAP.

---

## 8. Agent-Assisted Automation Flow
While this pipeline is independent of task-level verification, the **Agent** plays a critical role in its maintenance:

1. **Test Generation**: When implementing a new feature, the Agent MUST create a corresponding test case in the automation suite using the `templates/test_case.md` template.
2. **Impact Analysis**: For every change, the Agent must evaluate if existing automation tests in the pipeline need updating.
3. **Failure Resolution**: If the TAP (Stage 3/4) fails, the Agent can be tasked to diagnose and fix the regression using the `DEBUGGING Mode` (Level 4).

> [!IMPORTANT]
> **Task Verification** (Phase 4) is for *correctness of the current change*.
> **Automation Pipeline** (TAP) is for *integrity of the entire system*.
> Do not confuse the two. Every feature must have BOTH.

---

## 9. Troubleshooting & Debugging Skills
When the pipeline fails, the following skills must be strictly applied for resolution:

| Scenario | Strict Skill Application |
| :--- | :--- |
| **Pipeline Failure** | `systematic-debugging` / `testing-workflow` |
| **Flaky Test** | `testing-anti-patterns` / `e2e-testing` (flake-fixing) |
| **Build Error** | `build-error-resolver` |
| **Security Leak** | `security-auditor` / `securities-audit` |
| **Fix Cleanup** | `code-simplifier` (reduce noise after emergency fix) |
| **Resilience Drop** | `resilience-patterns` |

---

## 10. Verification Loop
Every fix applied to a TAP failure must be verified using the `verification-loop` skill, ensuring the fix is permanent and doesn't introduce secondary regressions.
