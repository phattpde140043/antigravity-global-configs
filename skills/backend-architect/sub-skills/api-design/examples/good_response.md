# Example: Golden Response for API & Interface Design

Below is a demonstration of how a Senior Backend Engineer agent must respond when asked to design a new endpoint or audit an existing interface contract.

---

## 🪐 Task Intake & Threat Model

**Request**: "Design a paginated list API to retrieve user search queries under `/api/v1/search-history`."

### 1. Analysis Phase (Zero-Trust Security & Multi-Layer Boundaries)
*   **Security Bounds (STRIDE)**: 
    *   *Information Disclosure / Elevation of Privilege*: We must prevent a tenant or user from viewing another user's search history. We will enforce strict `tenantId` and `userId` verification from the security context, rather than trusting the client payload.
*   **Layer Responsibilities**:
    *   **Controller Layer**: Handles HTTP query parameters (`pageNumber`, `pageSize`, `q`), parses basic schemas, and converts responses into the envelope format.
    *   **Service Layer**: Resolves query logic, validates business rule permissions, and performs audit logging.
    *   **Repository Layer**: Queries database asynchronously using indexes on `(tenant_id, user_id, created_at DESC)`.

---

## 🏗️ Technical Specification

### 1. Endpoint Contract
*   **Method**: `GET`
*   **Path**: `/api/v1/search-histories` (Plural noun, kebab-case, no verbs)
*   **Headers Required**:
    *   `Authorization: Bearer <token>`
*   **Query Parameters**:
    *   `pageNumber` (int, default: 1)
    *   `pageSize` (int, default: 20)
    *   `q` (string, optional - filter search term)

### 2. DTO Schemas (TypeScript)
```typescript
/**
 * Request Query DTO
 */
export interface GetSearchHistoryRequest {
  pageNumber: number;
  pageSize: number;
  q?: string;
}

/**
 * Single Search History Item
 */
export interface SearchHistoryItemResponse {
  id: string;
  queryText: string;
  resultCount: number;
  createdAt: string;
}

/**
 * Standard Envelope Response
 */
export interface PaginatedEnvelopeResponse<T> {
  data: T[];
  meta: {
    totalCount: number;
    pageNumber: number;
    pageSize: number;
    hasNextPage: boolean;
  };
}
```

---

## 💻 Multi-Layer Implementation (C# Pattern)

### 1. Controller Layer
```csharp
namespace Osp.Search.Api.Controllers;

[ApiController]
[Route("api/v1/search-histories")]
[Authorize]
public class SearchHistoryController : ControllerBase
{
    private readonly ISearchHistoryService _historyService;
    private readonly IUserContext _userContext;

    public SearchHistoryController(ISearchHistoryService historyService, IUserContext userContext)
    {
        _historyService = historyService;
        _userContext = userContext;
    }

    /// <summary>
    /// Retrieves a paginated list of search history entries for the authenticated user.
    /// </summary>
    [HttpGet]
    [ProducesResponseType(typeof(PaginatedEnvelopeResponse<SearchHistoryItemResponse>), 200)]
    [ProducesResponseType(typeof(ErrorResponse), 400)]
    [ProducesResponseType(typeof(ErrorResponse), 401)]
    public async Task<IActionResult> GetSearchHistoryAsync(
        [FromQuery] int pageNumber = 1,
        [FromQuery] int pageSize = 20,
        [FromQuery] string? q = null,
        CancellationToken cancellationToken = default)
    {
        // Basic input validation at edge
        if (pageNumber < 1 || pageSize < 1 || pageSize > 100)
        {
            return BadRequest(new ErrorResponse("INVALID_PAGINATION", "Page number and page size must be greater than 0. Max page size is 100."));
        }

        var userId = _userContext.GetCurrentUserId();
        var tenantId = _userContext.GetCurrentTenantId();

        var request = new GetSearchHistoryRequest(pageNumber, pageSize, q);
        var result = await _historyService.GetUserSearchHistoryAsync(tenantId, userId, request, cancellationToken);

        return Ok(result);
    }
}
```

### 2. Service Layer
```csharp
namespace Osp.Search.Core.Services;

public class SearchHistoryService : ISearchHistoryService
{
    private readonly ISearchHistoryRepository _historyRepository;

    public SearchHistoryService(ISearchHistoryRepository historyRepository)
    {
        _historyRepository = historyRepository;
    }

    /// <summary>
    /// Coordinates retrieval logic and handles domain business validation rules.
    /// </summary>
    public async Task<PaginatedEnvelopeResponse<SearchHistoryItemResponse>> GetUserSearchHistoryAsync(
        string tenantId,
        string userId,
        GetSearchHistoryRequest request,
        CancellationToken cancellationToken)
    {
        // Enforce tenant isolation and business validation
        if (string.IsNullOrEmpty(tenantId) || string.IsNullOrEmpty(userId))
        {
            throw new UnauthorizedAccessException("Tenant context or User context is missing.");
        }

        // Fetch data from repository layer
        var (items, totalCount) = await _historyRepository.GetHistoryPagedAsync(tenantId, userId, request.PageNumber, request.PageSize, request.Q, cancellationToken);

        // Map items to DTO responses
        var itemResponses = items.Select(x => new SearchHistoryItemResponse(
            x.Id.ToString(),
            x.QueryText,
            x.ResultCount,
            x.CreatedAt.ToString("o")
        )).ToList();

        var hasNextPage = (request.PageNumber * request.PageSize) < totalCount;

        return new PaginatedEnvelopeResponse<SearchHistoryItemResponse>(
            itemResponses,
            new PaginationMeta(totalCount, request.PageNumber, request.PageSize, hasNextPage)
        );
    }
}
```

### 3. Repository Layer
```csharp
namespace Osp.Search.Infrastructure.Repositories;

public class SearchHistoryRepository : ISearchHistoryRepository
{
    private readonly DbContext _context;

    public SearchHistoryRepository(DbContext context)
    {
        _context = context;
    }

    /// <summary>
    /// Executes the raw database read query asynchronously using optimized index parameters.
    /// </summary>
    public async Task<(List<SearchHistoryEntity> Items, int TotalCount)> GetHistoryPagedAsync(
        string tenantId,
        string userId,
        int pageNumber,
        int pageSize,
        string? q,
        CancellationToken cancellationToken)
    {
        // Build base query ensuring tenant isolation is hardcoded
        var query = _context.SearchHistories
            .AsNoTracking()
            .Where(x => x.TenantId == tenantId && x.UserId == userId);

        if (!string.IsNullOrEmpty(q))
        {
            query = query.Where(x => x.QueryText.Contains(q));
        }

        var totalCount = await query.CountAsync(cancellationToken);

        var items = await query
            .OrderByDescending(x => x.CreatedAt)
            .Skip((pageNumber - 1) * pageSize)
            .Take(pageSize)
            .ToListAsync(cancellationToken);

        return (items, totalCount);
    }
}
```

---

## ✅ Post-Generation Self-Review

*   **Convention Check**: Verified. All endpoints use kebab-case and plural nouns. Classes/Interfaces follow strict PascalCase with prefix `I`.
*   **Architecture Check**: Verified. Controllers only translate payloads, Services coordinate domain policies, and Repositories handle optimized database queries.
*   **Idempotency Check**: Verified. The retrieval is a `GET` action which is safe and idempotent.
*   **Performance & Security**: Hard tenant-isolation applied at database layer; pagination limits maximum returned items to 100 to prevent denial of service (DoS).
*   **Final Judgment**: Clean, scalable, secure, and production-ready.
