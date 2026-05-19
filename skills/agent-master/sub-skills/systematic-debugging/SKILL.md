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

- **[Root Cause Tracing](root-cause-tracing.md)**: Intelligent instrumentation and RCA.
- **[Defense in Depth](defense-in-depth.md)**: Debugging security-related issues.
- **[Condition-based Waiting](condition-based-waiting.md)**: Debugging race conditions and async logic.

## 🏛️ The Iron Law
> **NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST**
> 
> If you haven't completed the investigation phase and identified the exact line/state causing the issue, you cannot propose a fix. Symptom fixes are a failure of the process.

---

> If you haven't completed the investigation phase and identified the exact line/state causing the issue, you cannot propose a fix.

## 🏗️ The Operating Pipeline
You MUST complete each phase before proceeding to the next.

You MUST complete each phase before proceeding to the next. Skip phases only when explicitly justified.

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

1.  **Evidence over Guesswork**: Never change code without a falsified hypothesis.
2.  **Observability First**: Use traces and metrics before diving into code.
3.  **Reproducibility**: A bug that can't be reproduced can't be reliably fixed.
4.  **Safety First**: Use production-safe, non-invasive techniques. Never log PII.

## ⚠️ Safety Boundaries
- Do not attach interactive debuggers to production instances without approval.
- Avoid logging PII (Personally Identifiable Information) in debug logs.
- Never deploy "temporary" debug code to production permanently.

- Do not attach interactive debuggers to production without explicit approval.
- **Fail-Safe**: Always have a rollback strategy for any fix.
---

# Systematic Debugging
Transform debugging from guesswork into a disciplined engineering process. Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find the root cause before attempting fixes. Symptom fixes are a failure of the engineering process.

### Phase 1: Build a Feedback Loop
**This is the skill.** Everything else is mechanical. If you have a fast, deterministic, agent-runnable pass/fail signal for the bug, you will find the cause. If you don't have one, no amount of staring at code will save you.

Spend disproportionate effort here. **Be aggressive. Be creative. Refuse to give up.**

#### Techniques — try them in roughly this order
1. **Failing test** at whatever seam reaches the bug — unit, integration, e2e.
2. **Curl / HTTP script** against a running dev server.
3. **CLI invocation** with a fixture input, diffing stdout against a known-good snapshot.
4. **Headless browser script** (Playwright / Puppeteer) — drives the UI, asserts on DOM/console/network.
5. **Replay a captured trace.** Save a real network request / payload / event log to disk; replay it through the code path in isolation.
6. **Throwaway harness.** Spin up a minimal subset of the system (one service, mocked deps) that exercises the bug code path with a single function call.
7. **Property / fuzz loop.** If the bug is "sometimes wrong output", run 1000 random inputs and look for the failure mode.
8. **Bisection harness.** If the bug appeared between two known states, automate "boot at state X, check, repeat" so you can `git bisect run` it.
9. **Differential loop.** Run the same input through old-version vs new-version (or two configs) and diff outputs.
10. **HITL script.** Last resort. If a human must interact, structure the loop so their output feeds back to you.

Build the right feedback loop, and the bug is 90% fixed.

#### Iterate on the loop itself
Treat the loop as a product. Once you have _a_ loop, ask:

- Can I make it **faster**? (Cache setup, skip unrelated init, narrow the test scope.)
- Can I make the signal **sharper**? (Assert on the specific symptom, not "didn't crash".)
- Can I make it more **deterministic**? (Pin time, seed RNG, isolate filesystem, freeze network.)

A 30-second flaky loop is barely better than no loop. A 2-second deterministic loop is a debugging superpower.

#### Non-deterministic bugs
The goal is not a clean repro but a **higher reproduction rate**. Loop the trigger 100×, parallelise, add stress, narrow timing windows, inject sleeps. A 50%-flake bug is debuggable; 1% is not — keep raising the rate until it's debuggable.

Also see: **[Condition-based Waiting](condition-based-waiting.md)** for async/race-condition-specific patterns.

#### When you genuinely cannot build a loop
Stop and say so explicitly. List what you tried. Ask the user for:
- (a) access to the environment that reproduces it
- (b) a captured artifact (HAR file, log dump, core dump, screen recording with timestamps)
- (c) permission to add temporary production instrumentation

Do **not** proceed to Phase 2 without a loop.

### Phase 2: Reproduce & Confirm
Run the loop. Watch the bug appear.

Confirm:

- [ ] The loop produces the failure mode the **user** described — not a different failure that happens to be nearby. Wrong bug = wrong fix.
- [ ] The failure is reproducible across multiple runs (or, for non-deterministic bugs, reproducible at a high enough rate to debug against).
- [ ] You have captured the exact symptom (error message, wrong output, slow timing) so later phases can verify the fix actually addresses it.

Also gather evidence from the **Observability Stack** (Traces, Metrics, Logs). Correlate errors with recent system changes (deployments, config drift).

Do not proceed until you reproduce the bug.

### Phase 3: Hypothesise & Pattern Analysis
Generate **3–5 ranked hypotheses** before testing any of them. Single-hypothesis generation anchors on the first plausible idea.

Each hypothesis must be **falsifiable**: state the prediction it makes.

> Format: "If <X> is the cause, then <changing Y> will make the bug disappear / <changing Z> will make it worse."

If you cannot state the prediction, the hypothesis is a vibe — discard or sharpen it.

**Show the ranked list to the user before testing.** They often have domain knowledge that re-ranks instantly ("we just deployed a change to #3"), or know hypotheses they've already ruled out. Don't block on it — proceed with your ranking if the user is AFK.

#### Pattern Analysis
Before testing hypotheses, understand the system context:

1. **Find Working Examples**: Locate similar code that works. What is the difference?
2. **Compare Against References**: Read reference implementations COMPLETELY. Don't skim.
3. **Understand Dependencies**: Identify what settings, config, or environmental assumptions this code makes.

### Phase 4: Instrument & Test
Each probe must map to a specific prediction from Phase 3. **Change one variable at a time.**

Tool preference:

1. **Debugger / REPL inspection** if the env supports it. One breakpoint beats ten logs.
2. **Targeted logs** at the boundaries that distinguish hypotheses.
3. Never "log everything and grep".

**Tag every debug log** with a unique prefix, e.g. `[DEBUG-a4f2]`. Cleanup at the end becomes a single grep. Untagged logs survive; tagged logs die.

**Performance regressions:** Logs are usually wrong for perf bugs. Instead: establish a baseline measurement (timing harness, `performance.now()`, profiler, query plan), then bisect. Measure first, fix second.

If the change doesn't work, **REVERT IT** immediately. Do not stack failed fixes.

### Phase 5: Fix & Regression Test
Write the regression test **before the fix** — but only if there is a **correct seam** for it.

A correct seam is one where the test exercises the **real bug pattern** as it occurs at the call site. If the only available seam is too shallow, a regression test there gives false confidence.

**If no correct seam exists, that itself is a finding.** Note it — the codebase architecture is preventing the bug from being locked down.

If a correct seam exists:

1. Turn the minimised repro into a failing test at that seam.
2. Watch it fail.
3. Apply the fix. Address the root cause — no "while I'm here" refactoring.
4. Watch it pass.
5. Re-run the Phase 1 feedback loop against the original (un-minimised) scenario.
6. Ensure no other tests are broken.

**Architectural Questioning**: If 3+ fixes have failed, **STOP**. This indicates an architectural flaw, not a simple bug. Discuss with your human partner before continuing.

### Phase 6: Cleanup & Post-Mortem
Required before declaring done:

- [ ] Original repro no longer reproduces (re-run the Phase 1 loop)
- [ ] Regression test passes (or absence of correct seam is documented)
- [ ] All `[DEBUG-...]` instrumentation removed (`grep` the prefix)
- [ ] Throwaway prototypes deleted (or moved to a clearly-marked debug location)
- [ ] The hypothesis that turned out correct is stated in the commit / PR message — so the next debugger learns

**Then ask: what would have prevented this bug?** If the answer involves architectural change (no good test seam, tangled callers, hidden coupling), note it in the PR and consider follow-up refactoring.

---

## 🚩 Red Flags (STOP and Return to Phase 1)
- "Quick fix for now, investigate later."
- "Just try changing X and see if it works."
- "I don't fully understand why this works, but it does."
- **Each fix reveals a new problem in a different place.**
- **You've tried 2+ fixes and the issue persists.**

## 🗣️ Partner Signals (Watch for these)
- *"Is that not happening?"* (You assumed without verifying)
- *"Stop guessing"* (You're proposing fixes without understanding)
- *"Ultrathink this"* (Question fundamentals, not just symptoms)

---

## 📊 Supporting Techniques & Rationalizations


### Techniques
- **Backward Tracing**: Start from the error and work up the stack.
- **Environment Parity**: Check for differences between Dev/Staging/Prod.
- **Binary Search (Git Bisect)**: Find the exact commit that introduced the bug.

### Common Rationalizations
| Excuse | Reality |
| :--- | :--- |
| "Emergency, no time for process" | Systematic debugging is **FASTER** than thrashed guessing. |
| "Issue is simple" | Simple issues have root causes too. Process prevents regressions. |
| "Reference too long" | Partial understanding guarantees future bugs. |
| "One more fix attempt" | 3+ failures = Architectural problem. Question the pattern. |

---

## 🚀 Real-World Impact
- **First-time fix rate**: 95% (Systematic) vs 40% (Random).
- **Time to resolution**: 15-30m vs 2-3 hours of thrashing.
- **Regression rate**: Near zero.
