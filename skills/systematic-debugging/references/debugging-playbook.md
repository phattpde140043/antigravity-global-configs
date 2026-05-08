# Systematic Debugging Playbook (10-Step Workflow)

Transform debugging from guesswork into a disciplined engineering process. Use this workflow for complex, intermittent, or production-grade issues.

## 🔄 The 10-Step Debugging Cycle

### 1. Initial Triage & Hypotheses
- Analyze stack traces and error patterns.
- Identify affected components and environment (Dev/Staging/Prod).
- Generate **3-5 ranked hypotheses** with probability scores.

### 2. Observability Data Collection
- Gather logs (ELK/Loki), Traces (Jaeger/HoneyComb), and Metrics (Prometheus/DataDog).
- Correlate error spikes with deployment timelines or resource exhaustion.

### 3. Hypothesis Falsification
- For each hypothesis, define **falsification criteria**.
- Design controlled experiments to prove or disprove the hypothesis.

### 4. Strategy Selection
- **Interactive**: For local reproduction (VS Code Debugger).
- **Observability-Driven**: For production (Trace analysis).
- **Time-Travel**: For complex state (rr, Redux DevTools).
- **Statistical**: For rare edge cases (Delta debugging).

### 5. Intelligent Instrumentation
- AI-assisted placement of logpoints and conditional breakpoints.
- Focus on decision nodes where behavior diverges and state mutation points.

### 6. Production-Safe Techniques
- Use **Dynamic Instrumentation** (OpenTelemetry attributes).
- Implement **Feature-Flagged Debug Logging** for specific user cohorts.

### 7. Root Cause Analysis (RCA)
- Reconstruct the full execution path.
- Identify "smells" and similar bug patterns from the history.

### 8. Fix Implementation & Risk Assessment
- Generate the fix with an impact assessment.
- Define a **Rollback Strategy** in case the fix fails in production.

### 9. Verification & Regression Testing
- Run the test suite.
- Compare post-fix performance against the baseline.
- Ensure no new edge cases are introduced.

### 10. Prevention & Runbook Update
- Generate regression tests.
- Update the **Knowledge Base** and troubleshooting runbooks.
