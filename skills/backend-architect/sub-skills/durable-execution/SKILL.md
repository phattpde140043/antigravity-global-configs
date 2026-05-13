---
name: durable-execution
description: "Master of fault-tolerant, reliable application development using Durable Workflows and DBOS. Focuses on ensuring logic completes despite failures, reboots, or network issues."
---

# Durable Execution & Reliable Workflows

Build systems that are "invincible" to common failures using durable execution patterns.

## 🏗️ Core Philosophy
In a durable execution environment, functions are guaranteed to complete. If a process crashes, the system resumes exactly where it left off.

## 🚀 DBOS & Durable SDK Patterns
- **Workflows**: Orchestrate multiple steps. They are durable, idempotent, and resumable.
- **Steps**: Individual units of work (e.g., DB write, API call). Steps are recorded; if a workflow retries, successful steps are not re-executed.
- **Determinism**: Workflows **MUST** be deterministic. Non-deterministic logic (e.g., `Date.now()`, random numbers, external API calls) must always be wrapped in a **Step**.

## 🛡️ Reliability Patterns
- **Idempotency**: Ensure that re-running a process has no unintended side effects.
- **State Machines**: Use durable workflows to manage long-running business processes (e.g., multi-day approval flows).
- **Concurrency Control**: Use durable queues and locks provided by the framework instead of standard library primitives.

## 📋 Verification Checklist
- [ ] Are all non-deterministic operations (I/O, time) wrapped in Steps?
- [ ] Is the workflow logic deterministic?
- [ ] Are external API calls idempotent or handled with proper retry logic?
- [ ] Is the system state persisted automatically by the durable framework?
- [ ] Are long-running processes modeled as Resumable Workflows?
