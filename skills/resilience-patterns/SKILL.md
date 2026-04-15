---
name: resilience-patterns
description: "Apply resilience patterns (retry, circuit breaker, timeout, idempotency, outbox) to ensure system reliability and fault tolerance in distributed environments. USE WHEN: the request clearly matches the resilience-patterns domain. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# Resilience Patterns Skill

## Purpose

Ensure system stability, fault tolerance, and graceful degradation when dealing with:

- External services (AI providers, search APIs)
- Network failures
- High latency systems
- Distributed transactions

---

# When to Use

Use this skill when:

- Calling external APIs (OpenAI, Azure Search, third-party)
- Handling background jobs
- Processing async workflows
- Designing distributed systems
- Observing timeout / retry / instability issues

---

# Step 1 — Failure Mode Analysis

Identify:

- What can fail?
  - Network timeout
  - Service unavailable
  - Partial failure
- What is impact?
  - Data loss?
  - Duplicate execution?
  - User-facing failure?

---

# Step 2 — Choose Pattern

## Retry (Transient failures)

Use when:
- Timeout
- 5xx errors

Rules:
- Use exponential backoff
- Limit retries (max 3–5)
- Avoid retry storm

ASP.NET Core (Polly):

```csharp
Policy
  .Handle<HttpRequestException>()
  .WaitAndRetryAsync(3, retry => TimeSpan.FromSeconds(Math.Pow(2, retry)));

Circuit Breaker

Use when:

Service repeatedly failing

Behavior:

Open → stop calls
Half-open → test recovery
Closed → normal
Policy
  .Handle<Exception>()
  .CircuitBreakerAsync(5, TimeSpan.FromSeconds(30));
Timeout
Always define timeout for external calls
NEVER rely on default infinite timeout
Idempotency (CRITICAL)

Required for:

POST APIs
Background jobs
Retryable operations

Rules:

Use idempotency key
Ensure same request does NOT create duplicates
Outbox Pattern (CRITICAL for consistency)

Use when:

DB + message queue involved

Flow:

Save data + event in same DB transaction
Background worker publishes event

Prevents:

Data inconsistency
Lost events
Bulkhead Isolation
Isolate critical services
Prevent one failure cascading

Example:

Separate thread pool for AI calls
Step 3 — Async & Background Safety
NEVER use
Task.Run(() => DoWork());
Use
IHostedService
BackgroundService
Queue-based processing
Step 4 — Multi-Tenant Safety
Retry MUST NOT mix tenant context
Always pass tenant explicitly
Step 5 — Observability
Log retry attempts
Log circuit breaker state
Track failure rate
Output Requirement

You MUST:

Identify failure scenarios
Choose appropriate pattern
Justify trade-offs
Provide safe implementation
Ensure no duplicate execution
Ensure tenant isolation
Ensure observability
