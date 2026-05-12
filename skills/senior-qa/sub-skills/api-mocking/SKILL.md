---
name: api-mocking
description: "Expert in creating realistic mock services for development, testing, and demos. Simulates real API behavior, auth flows, and error scenarios to enable parallel development."
---

# API Mocking Specialist

Build robust, realistic mock APIs to accelerate development and testing cycles.

## Core Philosophy
A good mock should be indistinguishable from the real service during the development phase.

## 🏗️ Mock Design Patterns

### 1. Contract-Driven Mocking
- Base the mock on the **OpenAPI/Swagger** or **GraphQL Schema**.
- Ensure field types, formats, and mandatory fields match the production spec exactly.

### 2. Scenario-Based Mocking
Define "Happy Path" and "Error" scenarios:
- `200 OK`: Standard success.
- `400 Bad Request`: Validation failure.
- `401 Unauthorized`: Missing/expired token.
- `403 Forbidden`: Insufficient permissions.
- `404 Not Found`: Resource missing.
- `429 Too Many Requests`: Rate limit simulation.
- `500 Server Error`: Unexpected failure.

### 3. Stateful Mocks
Simulate state transitions:
- Create resource -> Get resource (should succeed).
- Delete resource -> Get resource (should return 404).

## 🛠️ Implementation Heuristics
- **Deterministic Fixtures**: Use stable data for reliable tests.
- **Latency Simulation**: Add artificial delay (`100ms - 2000ms`) to test UI loading states and race conditions.
- **Dynamic Content**: Use faker libraries for realistic names, dates, and IDs.
- **Auth Simulation**: Validate presence of `Authorization` header even if token content isn't fully verified.

## 📋 Verification Checklist
- [ ] Does the mock match the latest API specification?
- [ ] Are error shapes (JSON structure) consistent with the real API?
- [ ] Can the mock simulate edge cases (latency, timeouts)?
- [ ] Is there a clear way to switch between test scenarios?
- [ ] Are production secrets excluded from mock data?
