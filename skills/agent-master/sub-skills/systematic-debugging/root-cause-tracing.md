# Root Cause Tracing

## Overview

Trace bugs backward through the call stack to find the original trigger. Don't fix where the error appears — fix where the bad value originates.

## The Backward Tracing Technique

```
WHEN error appears at Line N in File F:

1. IDENTIFY the bad value (what's wrong — null, wrong type, wrong data)
2. FIND where that value was assigned in this function
3. TRACE backward: Who called this function with that value?
4. REPEAT until you reach the SOURCE — the first place the bad value was created

Fix at the SOURCE, not at the SYMPTOM.
```

## Example

```
Error: NullReferenceException at SearchService.cs:142 — tenant is null

Trace backward:
  142: var results = tenant.Search(query)         ← tenant is null HERE
  138: var tenant = GetTenant(tenantId)            ← GetTenant returned null
  
  GetTenant:45: return _cache.Get(tenantId)       ← cache returned null
  GetTenant:40: if (!_cache.Contains(tenantId))   ← key not found
  
  CallerController:28: var tenantId = ExtractTenant(headers)  ← returns ""
  CallerController:25: var headers = request.Headers           ← X-Active-Tenant missing

ROOT CAUSE: Header not injected by Kong → fix at Kong config, not at SearchService
```

## Rules

1. **Never fix at the symptom** — `if (tenant == null) return empty;` hides the bug
2. **Keep tracing until you reach external input** — the source is where bad data enters the system
3. **Document the full trace** — it shows you understand the problem
4. **Each hop is a function boundary** — read the caller, not just the callee

## When to Use

- NullReferenceException / AttributeError / TypeError
- Wrong data in response (but correct status code)
- "Works for tenant A but not tenant B" (configuration difference)
- Data corruption that propagates through multiple layers
