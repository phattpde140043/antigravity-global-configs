# Defense in Depth

## Overview

After finding and fixing a root cause, add validation at multiple layers to prevent the same class of bug from recurring. A single fix at the source is necessary but not sufficient — defense in depth means the system catches the problem even if the primary fix regresses.

## The Pattern

```
AFTER fixing root cause at Layer N:

1. ADD validation at Layer N (the source fix)
2. ADD validation at Layer N+1 (first consumer)
3. ADD validation at Layer N+2 (second consumer, if critical)
4. ADD monitoring/logging at the boundary where you detected the issue

Each layer catches the problem independently.
```

## Example: Missing Tenant Header

```
Root cause: Kong plugin not injecting X-Active-Tenant header

Layer 1 (Kong):     Fix plugin configuration → injects header correctly
Layer 2 (Backend):  Add middleware that rejects requests without X-Active-Tenant → 400
Layer 3 (Service):  GetTenant() throws TenantNotFoundException instead of returning null
Layer 4 (Monitor):  Log warning when X-Active-Tenant is missing at middleware boundary
```

## Rules

1. **Fix the root cause first** — defense in depth is NOT a substitute for fixing the source
2. **Each layer must fail independently** — don't create dependencies between layers
3. **Fail fast, fail loud** — validation should reject bad input immediately with clear errors
4. **Log at boundaries** — every component boundary should log what enters and exits
5. **Don't overdo it** — 2-3 layers is sufficient. More creates maintenance burden.

## Application to E2E Tests

For the OSP Search E2E test framework, defense in depth means:

| Layer | What to Validate |
|-------|-----------------|
| **Settings** | `get_settings()` validates all required fields are non-empty at startup |
| **Fixtures** | `alpha_jwt` fixture asserts token is valid before yielding |
| **Test** | Each test checks `response.status == 200` before parsing body |
| **Assertions** | `IsolationAssertions` validates response structure before checking values |
