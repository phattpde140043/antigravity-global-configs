---
name: performance-optimization
description: "Optimize system performance, query efficiency, caching strategy, and scalability for high-load backend systems. USE WHEN: the request clearly matches the performance-optimization domain. NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# Performance Optimization Skill

## Purpose

Ensure:

- Low latency
- High throughput
- Cost efficiency
- Scalability

---

# When to Use

Use when:

- Working with large datasets
- Designing APIs
- Handling search / AI queries
- Observing slow queries or high cost

---

# Step 1 — Identify Bottleneck

Check:

- DB query time
- Network latency
- CPU usage
- Memory usage
- External API calls

---

# Step 2 — Query Optimization

## MUST Rules

- NEVER query inside loop (N+1)
- ALWAYS use projection
- ALWAYS use pagination

Example:

```csharp
.Select(x => new UserListItem(x.Id, x.Name))

Indexing
Ensure indexes for:
WHERE
JOIN
ORDER BY
Azure Table / Search
ALWAYS use PartitionKey
ALWAYS filter by tenant
Step 3 — Caching Strategy
Choose Cache Type
Type	Use Case
IMemoryCache	Single instance
Redis (IDistributedCache)	Multi-instance
Patterns
Cache Aside
Check cache
If miss → load DB
Store cache
Cache Rules
Define TTL
Avoid stale data
Handle cache invalidation
DO NOT
Cache sensitive data
Cache without expiration
Step 4 — API Optimization
Use pagination (MANDATORY)
Avoid large payloads
Use compression
Step 5 — Async & Parallelism
Use async/await properly
Parallelize independent calls
Step 6 — External Calls Optimization
Batch requests
Avoid duplicate calls
Use caching layer for external APIs
Step 7 — AI / Search Optimization
Limit token usage
Avoid unnecessary prompts
Cache responses if safe
Step 8 — Cost Optimization

Evaluate:

DB queries cost
AI API cost
Storage cost
Step 9 — Metrics

Track:

Response time
Throughput
Error rate
Output Requirement

You MUST:

Identify bottleneck
Propose optimization strategy
Explain trade-offs (latency vs cost vs complexity)
Apply caching / batching where needed
Ensure scalability
Ensure tenant isolation
Ensure observability

