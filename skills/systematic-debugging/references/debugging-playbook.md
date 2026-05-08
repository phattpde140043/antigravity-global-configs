# Systematic Debugging & Multi-Agent Review Playbook

## 🕵️ Phase 1: Symptom Analysis
- **Reproduce**: Identify the minimum steps to reproduce the bug (Minimal Reproducible Example).
- **Isolation**: Determine if the error belongs to the Frontend, Backend, Database, or External API.
- **Log Mining**: Trace the TraceID across systems to find the point of failure.

## 🤖 Phase 2: Multi-Agent Review Orchestration
When facing complex errors, simulate or utilize multiple Agents with different perspectives:
1. **Security Agent**: Search for potential security vulnerabilities causing the bug.
2. **Performance Agent**: Check if the bug is due to bottlenecks or resource leaks.
3. **Logic Agent**: Check for deviations between Business Requirements and Implementation.
4. **Platform Agent**: Check environmental factors (Docker, K8s, Cloud Config).

## 🧩 Phase 3: Root Cause Identification (5 Whys)
- Don't just fix the symptom. Ask "Why" at least 5 times to find the Root Cause.
- **Checklist**:
    - [ ] Is it a Logic Code error?
    - [ ] Is it a Concurrent Access error (Race Condition)?
    - [ ] Is it a Data Inconsistency error?
    - [ ] Is it a Side-effect from other systems?

## 🛠️ Phase 4: Fix & Verification
- **Fix Review**:
    - [ ] Does the solution fundamentally resolve the Root Cause?
    - [ ] Does the solution cause Regressions elsewhere?
    - [ ] Are Unit/Integration Tests in place to ensure the bug does not return?
- **Post-Mortem**: Document lessons learned and update Skill sets or ADRs.
