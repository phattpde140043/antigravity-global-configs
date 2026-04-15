---
name: distributed-system
description: "Design scalable distributed systems using CQRS, event-driven architecture, saga patterns, and eventual consistency. USE WHEN: the request clearly matches the distributed-system domain. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# Distributed System Design Skill

## Purpose

Design systems that are:

- Scalable
- Resilient
- Decoupled
- Consistent (eventually)

---

# When to Use

Use when:

- Multi-service architecture
- High-scale systems
- Async workflows
- Complex business processes

---

# Step 1 — Identify System Type

- Monolith → keep simple
- Distributed → apply patterns

---

# Step 2 — Choose Architecture Pattern

## CQRS (Command Query Responsibility Segregation)

Separate:

- Write model (commands)
- Read model (queries)

Benefits:
- Scalability
- Performance

Trade-off:
- Complexity
- Eventual consistency

---

## Event-Driven Architecture

- Use events instead of direct calls

Example:

UserCreated → SendEmail → UpdateSearchIndex


---

## Saga Pattern (CRITICAL for distributed transactions)

Use when:
- Multiple services involved

Types:

### Orchestration
- Central controller

### Choreography
- Event-driven

---

## Event Sourcing (Optional)

- Store events instead of state

Use when:
- Audit is critical
- History tracking required

---

# Step 3 — Consistency Model

- Strong consistency → simple systems
- Eventual consistency → distributed systems

---

# Step 4 — Message Queue Design

Use:

- Azure Service Bus / Kafka / RabbitMQ

Rules:

- Messages MUST be idempotent
- Include tenant context
- Include correlation ID

---

# Step 5 — Failure Handling

- Retry with backoff
- Dead-letter queue
- Monitoring

---

# Step 6 — Multi-Tenant Isolation (CRITICAL)

- NEVER mix tenant data
- Include tenant in:
  - events
  - messages
  - queries

---

# Step 7 — Data Ownership

- Each service owns its DB
- No shared DB across services

---

# Step 8 — API vs Event Decision

| Use API | Use Event |
|--------|----------|
| Need immediate response | Async processing |
| Strong consistency | Eventual consistency |

---

# Step 9 — Observability

- Distributed tracing
- Correlation ID
- Logging across services

---

# Step 10 — Trade-offs

You MUST evaluate:

- Latency vs consistency
- Complexity vs scalability
- Cost vs reliability

---

# Output Requirement

You MUST:

1. Identify system boundaries
2. Choose architecture pattern
3. Define data flow
4. Handle failure scenarios
5. Explain trade-offs clearly
6. Ensure tenant isolation
7. Ensure observability


