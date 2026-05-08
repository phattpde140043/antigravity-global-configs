---
name: error-resilience
description: "Expert in Observability, Error Tracking, and System Recovery patterns."
category: engineering
metadata:
  triggers: [observability, error-tracking, system-recovery, structured-logging, tracing, circuit-breaker]
---

# Error Resilience & Observability

## 🎯 Objectives
1. Implement Structured Logging and Correlation IDs across the entire system.
2. Establish self-healing mechanisms (Retry, Circuit Breaker).
3. Perform deep Root Cause Analysis (RCA).

## 🛠️ Execution Workflow
1. **Tracing Implementation**: Attach Correlation IDs to every request header and log context.
2. **Structured Logging**: Ensure log output is JSON with full metadata (Service, Version, TraceId).
3. **Resilience Patterns**: 
    - Implement Exponential Backoff for API calls.
    - Configure Circuit Breakers for external dependencies.
4. **Investigation (RCA)**: Use the "Five Whys" and "Error Taxonomy" methods to classify errors (Critical, High, Medium, Low).

## 📋 Acceptance Criteria (AC)
- [ ] 100% of logs are structured JSON.
- [ ] TraceId is propagated across all services.
- [ ] Risk points (Network/DB) have Retry/Breaker mechanisms implemented.
