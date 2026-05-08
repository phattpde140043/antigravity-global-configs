---
name: systematic-debugging
description: "Expert AI-assisted debugging specialist using observability platforms and automated root cause analysis."
---

# Systematic Debugging (Tier 2)

Transform debugging from guesswork into a disciplined engineering process. Focus on evidence-based problem solving and root cause elimination.

## ⚡ Quick References (MANDATORY)
- **[Debugging Playbook](references/debugging-playbook.md)**: The 10-step systematic workflow.
- **[Observability Stack](references/observability-stack.md)**: Tools (Sentry, DataDog, OpenTelemetry).
- **[Root Cause Tracing](references/root-cause-tracing.md)**: Intelligent instrumentation and RCA.
- **[Defense in Depth](references/defense-in-depth.md)**: Debugging security-related issues.
- **[Condition-based Waiting](references/condition-based-waiting.md)**: Debugging race conditions and async logic.

---

## 🏗️ Operating Pipeline

### 1. Triage & Hypothesis
- Analyze logs/stack traces to identify the failure pattern.
- Generate **3-5 hypotheses** with probability and falsification criteria.

### 2. Evidence Gathering
- Query the **Observability Stack** (Traces, Metrics, Logs).
- Correlate errors with system changes (deployments, config drift).

### 3. Intelligent Instrumentation
- Place targeted logpoints or conditional breakpoints at decision nodes.
- Use **Production-Safe** techniques if debugging live systems.

### 4. Root Cause & Fix
- Reconstruct the execution path and identify the bug.
- Implement the fix with a **Rollback Strategy** and risk assessment.

### 5. Verification & Prevention
- Verify the fix against the original failure symptoms.
- Add regression tests and update the troubleshooting runbooks.

---

## 🛡️ Debugging Pillars
1. **Evidence over Guesswork**: Never change code without a falsified hypothesis.
2. **Observability First**: Use traces and metrics before diving into code.
3. **Reproducibility**: A bug that can't be reproduced can't be reliably fixed.
4. **Safety**: Always use non-invasive techniques in production environments.

## ⚠️ Safety Boundaries
- Do not attach interactive debuggers to production instances without approval.
- Avoid logging PII (Personally Identifiable Information) in debug logs.
- Never deploy "temporary" debug code to production permanently.
