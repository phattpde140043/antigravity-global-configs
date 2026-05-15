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

## 🏛️ The Iron Law

> **NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST**
> 
> If you haven't completed the investigation phase and identified the exact line/state causing the issue, you cannot propose a fix. Symptom fixes are a failure of the process.

---

## 🏗️ The Operating Pipeline

You MUST complete each phase before proceeding to the next.

### Phase 1: Investigation & Evidence Gathering
*Before attempting ANY fix, you must gather facts.*

1. **Triage & Hypothesis**: Analyze logs/stack traces. Generate **3-5 initial hypotheses** with falsification criteria.
2. **Reproduce Consistently**: Determine the exact steps to trigger the bug. If not reproducible, you cannot verify the fix.
3. **Evidence Gathering**: Query the **Observability Stack** (Traces, Metrics, Logs).
4. **Intelligent Instrumentation**: Place targeted logpoints. Trace bad values backward from the crash point to their origin. Fix at the source, not the symptom.

### Phase 2: Pattern Analysis
*Understand the system context before touching code.*

1. **Find Working Examples**: Locate similar code that works. What is the difference?
2. **Compare Against References**: Read reference implementations COMPLETELY. Don't skim.
3. **Understand Dependencies**: Identify what settings, config, or environmental assumptions this code makes.

### Phase 3: Hypothesis & Minimal Testing
*Use the scientific method.*

1. **Form Single Hypothesis**: State clearly: "I think X is the root cause because Y."
2. **Test Minimally**: Make the **SMALLEST** possible change to test the hypothesis (one variable at a time).
3. **Verify**: If the change doesn't work, **REVERT IT** immediately. Do not stack failed fixes.

### Phase 4: Implementation & Prevention
*Fix the root cause and ensure it never returns.*

1. **Create Failing Test Case**: Automated test (TDD) that fails without the fix and passes with it.
2. **Implement Single Fix**: Address the root cause. No "while I'm here" refactoring.
3. **Verification**: Ensure no other tests are broken and the symptom is fully resolved.
4. **Architectural Questioning**: If 3+ fixes have failed, **STOP**. This indicates an architectural flaw, not a simple bug. Discuss with your human partner.

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
