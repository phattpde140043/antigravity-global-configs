# Data Reliability: Caching & Idempotency

## 📦 Caching Strategies
- **Cache-Aside (Lazy Loading)**: 
    1. Check Cache.
    2. If miss, fetch from DB.
    3. Update Cache and return result.
- **Rules**:
    - Always set a **TTL** (Time-To-Live).
    - Have an **Invalidation** strategy when data changes.
    - Warn against **Cache Stampede** (multiple requests fetching miss data simultaneously).

## 🆔 Idempotency
- **Concept**: Ensure that if a request is sent multiple times (e.g., due to retries), the result and side effects occur only once.
- **Implementation**:
    - Use an **Idempotency-Key** in the Header.
    - Store the result of the first request in DB/Cache indexed by the Key.
    - Subsequent requests with the same Key receive the cached result without re-executing business logic.

## 📥 Outbox Pattern
- **Concept**: Ensure atomicity between Database updates and Message/Event publishing.
- **Flow**: Save the Event into an `Outbox` table within the same Transaction as the main data -> A Background Worker reads the `Outbox` table and publishes to the Message Bus.
