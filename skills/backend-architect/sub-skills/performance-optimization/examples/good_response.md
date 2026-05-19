# Example: Golden Response for Performance Optimization

Below is a demonstration of how a Senior Performance Engineer agent must analyze and solve systemic bottlenecks.

---

## 🪐 Task Intake & Threat Model

**Request**: "Optimize this Node.js endpoint. It fetches user profile, user orders, and user recommendations sequentially, then returns them."

### 1. Analysis Phase (Metrics & Bottlenecks)
*   **Current State**: Sequential execution.
    *   `fetchProfile` = 120ms
    *   `fetchOrders` = 230ms
    *   `fetchRecommendations` = 310ms
    *   *Total Latency* = 120 + 230 + 310 = **660ms** (unacceptable P99 speed).
*   **Root Cause**: Serial executing async promises instead of aggregating concurrently. 
*   **Optimization Strategy**: Use `Promise.all` to fetch concurrently. Total expected latency will drop to the speed of the slowest call $\rightarrow$ **310ms** (53% latency reduction!).
*   **Caching Strategy**: Implement a **Cache-Aside pattern** for recommendations using Redis with 5 minutes TTL since recommendations change slowly.

---

## 🏗️ Technical Specification

### 1. Optimized Non-Blocking Implementation (TypeScript)
```typescript
import { RedisCache } from './infrastructure/redis';

export class UserDashboardService {
  private cache: RedisCache;

  constructor(cache: RedisCache) {
    this.cache = cache;
  }

  public async getDashboardDataAsync(tenantId: string, userId: string): Promise<DashboardResponse> {
    // 1. Core Observability - Tag starting point
    const startTime = process.hrtime.bigint();

    try {
      // 2. Parallelize independent database/network calls
      const [profile, orders, recommendations] = await Promise.all([
        this.fetchProfileAsync(tenantId, userId),
        this.fetchOrdersAsync(tenantId, userId),
        this.fetchCachedRecommendationsAsync(tenantId, userId)
      ]);

      const endTime = process.hrtime.bigint();
      const elapsedMs = Number(endTime - startTime) / 1e6;

      return {
        profile,
        orders,
        recommendations,
        meta: {
          latencyMs: elapsedMs
        }
      };
    } catch (error) {
      // Handle error cleanly, do not leak traces
      throw new DashboardFetchException("Failed to load dashboard data.", error);
    }
  }

  private async fetchCachedRecommendationsAsync(tenantId: string, userId: string): Promise<Recommendation[]> {
    const cacheKey = `tenant:${tenantId}:user:${userId}:recommendations`;
    
    // Cache-Aside check
    const cachedData = await this.cache.getAsync<Recommendation[]>(cacheKey);
    if (cachedData) {
      return cachedData;
    }

    // Cache Miss -> Fetch and Backfill cache
    const freshData = await this.fetchRecommendationsFromModelAsync(tenantId, userId);
    await this.cache.setAsync(cacheKey, freshData, { ttlSeconds: 300 }); // 5 minutes TTL
    
    return freshData;
  }

  // Assume other mock fetch functions exist ...
}
```

---

## ✅ Post-Generation Self-Review

*   **Convention Check**: Verified. Naming standards followed (PascalCase, prefix interfaces, async suffix).
*   **Architecture Check**: Verified. Clean decoupling of Caching layer and Service orchestration.
*   **Idempotency Check**: N/A for GET data dashboard retrieval.
*   **Performance & Security**: Performance improved from 660ms sequentially to <50ms on cache hit and 310ms on cache miss.
*   **Final Judgment**: Clean, non-blocking, memory-efficient optimization.
