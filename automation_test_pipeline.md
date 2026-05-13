# 🧪 Automation Test Pipeline (TAP) - Strategy & Execution

This document defines the lifecycle and execution pipeline for **Long-term Automated Testing**. This is a **Continuous Quality Gate** orchestrated by the `testing-workflow` skill, operating independently of the agent's task-specific verification loops.

---

## 1. Objective
To ensure the **OSP Search AI** ecosystem remains stable, secure, and performant through automated, repeatable, and environment-agnostic testing cycles.

## 2. Test Taxonomy (The Pyramid)

| Level | Type | Scope | Tooling | Required Master Discipline |
| :--- | :--- | :--- | :--- | :--- |
| **L1** | Unit/Component | Logic, UI components. | Pytest / Vitest | `@senior-qa` (TDD) |
| **L2** | Integration | Service-to-service, API. | Playwright | `@senior-qa` (Test Engineer) |
| **L3** | E2E / UI | User flows, Isolation. | Playwright | `@senior-qa` (E2E Excellence) |
| **L4** | Security | IDOR, XSS, RCE. | OWASP ZAP | `@security-master` (Pentesting) |
| **L5** | Performance | Latency, Load. | k6 / JMeter | `@backend-architect` (Perf Optimization) |

---

## 3. The Pipeline Stages

### 🟢 Stage 1: The Local Gate (Pre-Commit)
*Goal: Catch simple errors before they reach the cloud.*
- **Linting**: Static analysis (`@agent-master`).
- **Unit Tests**: Logic and UI components (`@senior-qa`).
- **Test Generation**: Automated drafting of test skeletons (`@agent-master`).

### 🟡 Stage 2: The Pull Request Gate (CI)
*Goal: Validate integration and prevent regressions in shared branches.*
- **Build Verification**: Compile in clean environment (`@agent-master`).
- **Smoke E2E**: Critical user journeys (`@senior-qa`).
- **Security Audit**: Dependency scans (`@security-master`).
- **PR Integrity**: Automated code review (`@review-master`).

### 🔴 Stage 3: The Deep Regression (Nightly/Scheduled)
*Goal: Comprehensive coverage without slowing down development.*
- **Full E2E Suite**: All 100+ scenarios (`@senior-qa`).
- **Multi-Tenant Isolation (ISO)**: Cross-tenant data checks (`@security-master`).
- **Anti-Pattern Scan**: Detect brittle tests (`@senior-qa`).

### 🟣 Stage 4: The Release Gate (Pre-Production)
*Goal: Final sign-off for deployment.*
- **Performance Baseline**: P99 latency checks (`@backend-architect`).
- **Resilience Testing**: Chaos engineering light (`@backend-architect`).
- **Compliance Audit**: Regulatory checks (`@security-master`).

---

## 4. Multi-Tenant Isolation Protocol (MTIP)
Automation tests **MUST** validate isolation for every new feature:
1. **Tenant Alpha** creates a resource (e.g., a Search Profile).
2. **Tenant Beta** attempts to Read, Update, or Delete Alpha's resource using its ID.
3. **Requirement**: System must return `401 Unauthorized`, `403 Forbidden`, or `404 Not Found`.
4. **Tooling**: Use standard `TenantContext` and `EntityHelper` fixtures to automate this flow.

---

## 5. Reporting & Observability
- **Dashboards**: Allure HTML reports hosted on CI artifacts.
- **Notifications**: Slack/Teams alert to `#eng-alerts`.
- **Traces**: Playwright traces and videos for 1-click debugging.

---

## 6. Flaky Test Management
Flaky tests are the "broken windows" of automation.
1. **Detection**: Marked as **FLAKY** if passing only on retry.
2. **Quarantine**: Moved to `quarantine/` folder; do not block the pipeline.
3. **SLA**: Must be fixed or deleted within **72 hours**.

---

## 7. Ownership & Maintenance
- **QA/SDET**: Maintains the framework and infrastructure.
- **Developers**: Write tests for new features (Definition of Done).
- **Agent**: Assists in generating test boilerplate and fixing failures.

---

## 8. Agent-Assisted Automation Flow
1. **Test Generation**: Create corresponding test cases in the automation suite.
2. **Impact Analysis**: Evaluate if existing tests need updating.
3. **Failure Resolution**: Diagnose and fix regressions using `@agent-master`.

---

## 9. Troubleshooting & Debugging Skills
When the pipeline fails, the following Master Disciplines must be applied:

| Scenario | Master Discipline |
| :--- | :--- |
| **Pipeline Failure** | `@agent-master` (Systematic Debugging) |
| **Flaky Test** | `@senior-qa` (Testing Anti-Patterns) |
| **Build Error** | `@agent-master` (Build Error Resolver) |
| **Security Leak** | `@security-master` (Security Audit) |
| **Fix Cleanup** | `@agent-master` (Code Simplifier) |
| **Resilience Drop** | `@backend-architect` (Resilience Patterns) |

---

## 10. Verification Loop
Every fix must be verified using the `@senior-qa` (Verification Loop) sub-skill, ensuring the fix is permanent and doesn't introduce secondary regressions.
