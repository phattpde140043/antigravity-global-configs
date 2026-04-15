---
name: api-design
description: "REST API design patterns for resource naming, pagination strategies, filtering/sorting conventions, versioning lifecycle, and rate limiting implementation. Complements existing status code and error response rules. USE WHEN: Designing new API endpoints or resource URLs; Implementing pagination (choosing offset vs cursor). NOT FOR: unrelated tasks outside this scope or tasks better served by a more specific skill."
---

# API Design Patterns

## Purpose

Provide concrete implementation patterns for API design decisions beyond status codes and error formats (which are already enforced by project instructions).

---

# When to Activate

- Designing new API endpoints or resource URLs
- Implementing pagination (choosing offset vs cursor)
- Adding filtering, sorting, or search to list endpoints
- Planning API versioning or deprecation
- Implementing rate limiting response headers
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

---

# Resource URL Design

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
❌ /api/v1/users/search          → use query param instead: /api/v1/users?q=term
```

---

# HTTP Method Semantics

| Method | Idempotent | Safe | Use For |
|--------|-----------|------|---------|
| GET | Yes | Yes | Retrieve resources |
| POST | No | No | Create resources, trigger actions |
| PUT | Yes | No | Full replacement |
| PATCH | No* | No | Partial update |
| DELETE | Yes | No | Remove a resource |

*PATCH can be made idempotent with proper implementation.

---

# Pagination Patterns

## Offset-Based (Simple)

```
GET /api/v1/users?page=2&pageSize=20
```

```csharp
// ASP.NET Core implementation
public async Task<ActionResult<PagedResponse<UserResponse>>> GetUsersAsync(
    [FromQuery] int page = 1,
    [FromQuery] int pageSize = 20)
{
    var query = _context.Users.AsNoTracking();
    var total = await query.CountAsync();

    var items = await query
        .OrderByDescending(u => u.CreatedAt)
        .Skip((page - 1) * pageSize)
        .Take(pageSize)
        .Select(u => UserResponse.FromEntity(u))
        .ToListAsync();

    return Ok(new PagedResponse<UserResponse>(items, total, page, pageSize));
}
```

**Pros:** Easy to implement, supports "jump to page N"
**Cons:** Slow on large offsets, inconsistent with concurrent inserts

## Cursor-Based (Scalable)

```
GET /api/v1/users?cursor=eyJpZCI6MTIzfQ&limit=20
```

```csharp
// ASP.NET Core implementation
public async Task<ActionResult<CursorResponse<UserResponse>>> GetUsersAsync(
    [FromQuery] string? cursor = null,
    [FromQuery] int limit = 20)
{
    var decodedCursor = cursor != null
        ? DecodeCursor(cursor)
        : null;

    var query = _context.Users.AsNoTracking();

    if (decodedCursor != null)
        query = query.Where(u => u.Id.CompareTo(decodedCursor.Value) > 0);

    var items = await query
        .OrderBy(u => u.Id)
        .Take(limit + 1) // fetch one extra to determine has_next
        .Select(u => UserResponse.FromEntity(u))
        .ToListAsync();

    var hasNext = items.Count > limit;
    if (hasNext) items.RemoveAt(items.Count - 1);

    var nextCursor = hasNext ? EncodeCursor(items.Last().Id) : null;

    return Ok(new CursorResponse<UserResponse>(items, hasNext, nextCursor));
}
```

**Pros:** Consistent O(1) performance, stable with concurrent inserts
**Cons:** Cannot jump to arbitrary page, opaque cursor

## When to Use Which

| Use Case | Type | Reason |
|----------|------|--------|
| Admin dashboards, small datasets (<10K) | Offset | Users expect page numbers |
| Infinite scroll, feeds, large datasets | Cursor | Performance at scale |
| Search results | Offset | Users expect page numbers |
| Audit logs, event streams | Cursor | Append-only, high volume |

---

# Collection Response Envelope

```csharp
// Offset-based response
public record PagedResponse<T>(
    IReadOnlyList<T> Data,
    int Total,
    int Page,
    int PageSize)
{
    public int TotalPages => (int)Math.Ceiling((double)Total / PageSize);
    public bool HasNext => Page < TotalPages;
    public bool HasPrevious => Page > 1;
}

// Cursor-based response
public record CursorResponse<T>(
    IReadOnlyList<T> Data,
    bool HasNext,
    string? NextCursor);
```

---

# Filtering, Sorting, and Search

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

# Rate Limiting Response Headers

```
HTTP/1.1 200 OK
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000

# When exceeded (429 status code defined in project instructions)
HTTP/1.1 429 Too Many Requests
Retry-After: 60
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
