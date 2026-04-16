---
name: api-and-interface-design
description: "Guides stable API and interface design. Use when designing REST/GraphQL endpoints, resource naming, pagination, versioning, or defining type contracts between modules/frontend-backend. Includes pagination, filtering, and rate limiting patterns."
---

# API and Interface Design

## Purpose

Provide concrete implementation patterns and architectural principles for API and interface design. Good interfaces make the right thing easy and the wrong thing hard. This applies to REST APIs, module boundaries, component props, and any surface where one piece of code talks to another.

---

# When to Activate

- Designing new API endpoints or resource URLs
- Defining module boundaries or contracts between teams
- Creating component prop interfaces
- Implementing pagination (choosing offset vs cursor)
- Adding filtering, sorting, or search to list endpoints
- Planning API versioning or deprecation
- Reviewing API contract consistency

---

# Scope Boundaries

**This skill covers:**
- Resource URL naming patterns
- Pagination implementation (offset vs cursor)
- Filtering, sorting, sparse fieldsets conventions
- Collection response envelope (`meta`, `links`)
- Versioning lifecycle and deprecation strategy
- Rate limiting headers and tier design

**Already covered elsewhere (do NOT duplicate):**
- Status code table → `Search-sensei.instructions.md`
- Error response format → `Search-sensei.instructions.md`
- Swagger documentation rules → `Search-sensei.instructions.md`
- DTO-first design → `Search-sensei.instructions.md`
- Input validation → `Search-sensei.instructions.md` + `engineering-guardrails`
- Authentication/authorization → `engineering-guardrails` + `aspnetcore-framework-playbook`
- Rate limiting mandate → `engineering-guardrails`
- Security headers → `engineering-guardrails`
# Core Principles

### Hyrum's Law
> With a sufficient number of users of an API, all observable behaviors of your system will be depended on by somebody, regardless of what you promise in the contract.

- **Be intentional about what you expose.** Every observable behavior is a potential commitment.
- **Don't leak implementation details.** If users can observe it, they will depend on it.
- **Tests are not enough.** Even with perfect contract tests, "safe" changes can break real users who depend on undocumented behavior.

### The One-Version Rule
Avoid forcing consumers to choose between multiple versions of the same dependency or API. Design for a world where only one version exists at a time — extend rather than fork.

### Contract First
Define the interface before implementing it. The contract is the spec — implementation follows.

---

# Resource URL Design (REST)

## Naming Rules

```
# Resources: plural, lowercase, kebab-case nouns
/api/v1/users
/api/v1/query-rules
/api/v1/search-suggestions

# Sub-resources for ownership relationships
/api/v1/users/{id}/orders
/api/v1/tenants/{tenantId}/profiles

# Actions that don't map to CRUD (use verbs sparingly, POST only)
POST /api/v1/orders/{id}/cancel
POST /api/v1/auth/refresh
```

## Anti-Patterns

```
❌ /api/v1/getUsers              → verb in URL
❌ /api/v1/user                  → singular (use plural)
❌ /api/v1/team_members          → snake_case in URLs
❌ /api/v1/users/123/getOrders   → verb in nested resource
```

---

# HTTP Method Semantics

| Method | Idempotent | Safe | Use For |
|--------|-----------|------|---------|
| GET | Yes | Yes | Retrieve resources |
| POST | No | No | Create resources, trigger actions |
| PUT | Yes | No | Full replacement (idempotent) |
| PATCH | Yes/No | No | Partial update |
| DELETE | Yes | No | Remove a resource |
*PATCH can be made idempotent with proper implementation.
---

# Boundary Validation

Trust internal code. Validate at system edges where external input enters (API handlers, form submissions, external service responses).

> **Third-party API responses are untrusted data.** Validate their shape and content before using them. A compromised or misbehaving external service can return unexpected types or malicious content.

---

# Pagination Patterns

## Offset-Based (Simple)
`GET /api/v1/users?page=2&pageSize=20`

```csharp
// Implementation logic
public async Task<PagedResponse<T>> GetPagedAsync(int page, int pageSize)
{
    var totalCount = await _dbSet.CountAsync();
    var data = await _dbSet
        .Skip((page - 1) * pageSize)
        .Take(pageSize)
        .ToListAsync();

    return new PagedResponse<T>(data, totalCount, page, pageSize);
}
```

- **Pros**: 
    - Easiest to implement.
    - Supports "Jump to Page N" functionality.
    - Stateless on the server.
- **Cons**: 
    - **Performance**: O(N) complexity for database scan (becomes very slow at high page numbers).
    - **Inconsistency**: If items are added/deleted while paging, items can be skipped or appear twice.

## Cursor-Based (Scalable)
`GET /api/v1/users?cursor=eyJpZCI6MTIzfQ&limit=20`

```csharp
// Implementation logic
public async Task<PagedResponse<T>> GetCursorPagedAsync(string? cursor, int limit)
{
    var decoded = DecodeCursor(cursor); // e.g., extracts LastId
    
    var query = _dbSet.AsQueryable();
    if (decoded != null) {
        query = query.Where(x => x.Id > decoded.LastId);
    }

    var data = await query
        .OrderBy(x => x.Id)
        .Take(limit)
        .ToListAsync();

    var nextCursor = data.Count == limit ? EncodeCursor(data.Last().Id) : null;
    
    return new PagedResponse<T>(data, TotalCount: -1, Cursor: nextCursor);
}
```

- **Pros**: 
    - **Performance**: O(1) or O(log N) with proper indexing. Scalable to millions of records.
    - **Consistency**: Guaranteed unique results even with concurrent inserts/deletes.
- **Cons**: 
    - Harder to implement.
    - Does not support "Jump to Page N" (forward/backward navigation only).

## When to Use Which

| Use Case | Type | Reason |
|----------|------|--------|
| Admin dashboards, small datasets (<10K) | Offset | Users expect page numbers |
| Infinite scroll, feeds, large datasets | Cursor | Performance at scale |
| Search results | Offset | Users expect page numbers |
| Audit logs, event streams | Cursor | Append-only, high volume |
---

# Collection Response Envelope

Always return collections within a top-level object to allow for metadata expansion without breaking the contract.

```json
{
  "data": [
    { "id": "task_1", "title": "First task" },
    { "id": "task_2", "title": "Second task" }
  ],
  "meta": {
    "totalCount": 150,
    "page": 1,
    "pageSize": 20,
    "hasNextPage": true,
    "cursor": "eyJpZCI6MjB9"
  }
}
```

---

# Filtering, Sorting, and Search

- **Filtering**: Use query parameters matching the field name or a structured filter object.
  - `GET /api/v1/tasks?status=completed&priority=high`
- **Sorting**: Use a `sort` parameter with `+` (asc) or `-` (desc) prefixes.
  - `GET /api/v1/tasks?sort=-createdAt,+title`
- **Search**: Use a `q` or `search` parameter for full-text search.
  - `GET /api/v1/tasks?q=antigravity`

## Filtering Conventions

```
# Simple equality
GET /api/v1/orders?status=active&customerId=abc-123

# Multiple values (comma-separated → server splits to list)
GET /api/v1/products?category=electronics,clothing

# Date range (use explicit param names)
GET /api/v1/orders?createdFrom=2025-01-01&createdTo=2025-12-31
```

```csharp
// ASP.NET Core — use a query DTO
public record OrderFilterRequest(
    string? Status = null,
    string? CustomerId = null,
    DateTime? CreatedFrom = null,
    DateTime? CreatedTo = null);

public async Task<ActionResult> GetOrdersAsync([FromQuery] OrderFilterRequest filter)
{
    var query = _context.Orders.AsNoTracking();

    if (!string.IsNullOrEmpty(filter.Status))
        query = query.Where(o => o.Status == filter.Status);

    if (filter.CreatedFrom.HasValue)
        query = query.Where(o => o.CreatedAt >= filter.CreatedFrom.Value);

    // ... apply other filters
}
```

## Sorting Convention

```
# Single field (prefix - for descending)
GET /api/v1/products?sort=-createdAt

# Multiple fields (comma-separated)
GET /api/v1/products?sort=-featured,price,-createdAt
```

## Full-Text Search

```
# Use 'q' parameter for search
GET /api/v1/products?q=wireless+headphones
```

## Sparse Fieldsets

```
# Return only specified fields (reduces payload)
GET /api/v1/users?fields=id,name,email
```

---

# Versioning Strategy

## URL Path Versioning (Preferred)

```
/api/v1/users
/api/v2/users
```

## Lifecycle Rules

1. **Start with v1** — don't version until you need to
2. **Maximum 2 active versions** — current + previous
3. **Non-breaking changes** (no new version needed):
   - Adding new fields to responses
   - Adding new optional query parameters
   - Adding new endpoints
4. **Breaking changes** (require new version):
   - Removing or renaming fields
   - Changing field types
   - Changing URL structure
   - Changing authentication method
5. **Deprecation**:
   - Add `Sunset` header: `Sunset: Sat, 01 Jul 2026 00:00:00 GMT`
   - Return `410 Gone` after sunset date

```csharp
// ASP.NET Core — add Sunset header for deprecated version
app.MapGet("/api/v1/users", handler)
   .WithMetadata(new DeprecatedAttribute())
   .AddEndpointFilter(async (ctx, next) =>
   {
       ctx.HttpContext.Response.Headers["Sunset"] = "Sat, 01 Jul 2026 00:00:00 GMT";
       ctx.HttpContext.Response.Headers["Deprecation"] = "true";
       return await next(ctx);
   });
```

---
# Rate Limiting & Quotas

## Response Headers
APIs should signal rate limit status to clients via standard headers:
- `X-RateLimit-Limit`: The quota limit in the current window.
- `X-RateLimit-Remaining`: The remaining quota in the current window.
- `X-RateLimit-Reset`: The time at which the quota resets.

## Rate Limiting Tiers (Example)
| Tier | Limit | Use Case |
|------|-------|----------|
| Anonymous | 60/min | Public browsing |
| Authenticated User | 1000/min | Standard app usage |
| Internal/Service | 5000/min | System-to-system |

---

# TypeScript Interface Patterns

### Use Discriminated Unions for Variants
```typescript
type TaskStatus =
  | { type: 'pending' }
  | { type: 'in_progress'; assignee: string; startedAt: Date }
  | { type: 'completed'; completedAt: Date; completedBy: string };
```

## Tier Design

| Tier | Limit | Window | Apply To |
|------|-------|--------|----------|
| Anonymous | 30/min | Per IP | Public search endpoints |
| Authenticated | 100/min | Per user | Standard API access |
| Service-to-Service | 1000/min | Per service | Internal / operation APIs |

```csharp
// ASP.NET Core 7+ RateLimiter
builder.Services.AddRateLimiter(options =>
{
    options.AddFixedWindowLimiter("authenticated", opt =>
    {
        opt.PermitLimit = 100;
        opt.Window = TimeSpan.FromMinutes(1);
        opt.QueueLimit = 0;
    });

    options.OnRejected = async (context, token) =>
    {
        context.HttpContext.Response.StatusCode = 429;
        context.HttpContext.Response.Headers["Retry-After"] = "60";
        await context.HttpContext.Response.WriteAsJsonAsync(new
        {
            code = "rate_limit_exceeded",
            message = "Rate limit exceeded. Try again in 60 seconds."
        }, token);
    };
});
```

---

# API Design Checklist

Before shipping a new endpoint, verify items NOT already covered by project instructions:

- [ ] Resource URL follows naming conventions (plural, kebab-case, no verbs)
- [ ] Correct HTTP method used with proper idempotency semantics
- [ ] List endpoints have pagination (offset or cursor, chosen by use case)
- [ ] Filtering uses query DTO, not inline string parsing
- [ ] Collection responses include `meta` (total, page) or cursor info
- [ ] Rate limiting tier assigned and headers returned
- [ ] Versioned under `/api/v1/` path
- [ ] Backward compatibility verified (no breaking changes without version bump)
