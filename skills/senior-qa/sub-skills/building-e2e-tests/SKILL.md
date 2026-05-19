---
name: building-e2e-tests
description: Use when building, implementing, or modifying E2E tests for the OSP Search multi-tenant platform — covers test structure, fixtures, assertions, API endpoints, tenant isolation patterns, and security boundary validation
---

# Building E2E Tests — OSP Search Multi-Tenant Platform

## Overview

This skill encodes all patterns, conventions, and architectural knowledge required to build E2E tests for the OSP Search multi-tenant platform. Tests validate data isolation, authentication boundaries, OWASP security, performance, and functional correctness across 12 scopes using Python + Playwright.

**Core principle:** Every test proves that Tenant A's data is invisible to Tenant B, and that every security boundary enforced by Kong + Keycloak + the .NET backend is non-bypassable.

## When to Use

- Implementing a new test from a Scope 1–12 task definition
- Adding a new API endpoint to the test coverage
- Creating fixtures for new tenants or data domains
- Writing isolation assertions for cross-tenant boundary checks
- Debugging test failures related to fixture wiring, JWT auth, or API payloads

## Architecture Quick Reference

### Platform Data Flow
```
[Client] → [Kong Gateway] → [OSP Backend API (.NET)] → [OpenSearch]
              │                    │
              ├─ Validates JWT     ├─ Reads X-Active-Tenant header
              ├─ Checks scopes    ├─ Filters queries by tenant index
              ├─ Injects X-Active-Tenant (from JWT claim)
              └─ Injects X-Internal-Secret (defense-in-depth)
```

### Test Framework Stack
| Component | Tool |
|-----------|------|
| Test runner | `pytest` with markers (`critical`, `isolation`, `auth`, etc.) |
| API testing | Playwright `APIRequestContext` (NOT `requests` library) |
| Browser testing | Playwright `BrowserContext` (Scope 10 UI tests) |
| Performance | Locust (Scope 9) |
| Contract | Schemathesis (Scope 12) |
| Config | `pydantic-settings` → `Settings` object → `.env` file |
| JWT generation | `PyJWT` + `cryptography` (fake tokens for auth boundary tests) |
| Real auth | `KeycloakAuthClient` → Resource Owner Password Grant |

### Repository Structure
```
osp-search-e2e-tests/
├── conftest.py                       # Root fixtures (JWTs, API contexts, headers)
├── tests/
│   ├── conftest.py                   # Shared helpers (assert_status, assert_no_cross_tenant, extract_records)
│   ├── tenant_isolation/             # Scope 1 (ISO-01 to ISO-17)
│   │   └── conftest.py              # alpha_data / beta_data fixtures
│   ├── authentication/               # Scope 2 (AUTH-01 to AUTH-10)
│   ├── owasp_rce/                    # Scope 3
│   ├── owasp_xss/                    # Scope 4
│   ├── owasp_sqli/                   # Scope 5
│   ├── owasp_lfi_rfi_ssrf/          # Scope 6
│   ├── security_headers/             # Scope 7
│   ├── protocol_security/            # Scope 8
│   ├── functional/                   # Scope 10
│   └── session_security/             # Scope 11
├── performance/                      # Scope 9 (Locust)
└── utils/
    ├── settings.py                   # Pydantic Settings (singleton via @lru_cache)
    ├── jwt_helper.py                 # JwtHelper + KeycloakAuthClient
    ├── tenant_context.py             # TenantContext wrapper
    ├── api_client.py                 # ApiClient with timing/logging
    └── assertions.py                 # IsolationAssertions, AuthAssertions, etc.
```

---

## Test Scopes & Counts (12 Scopes, 109+ Tests)

| Scope | Name | Tests | Priority | Phase |
|-------|------|-------|----------|-------|
| 1 | Tenant Data Isolation | 17 | 🔴 CRITICAL | 1 |
| 2 | Authentication Boundary | 15 | 🔴 CRITICAL | 1 |
| 3 | OWASP RCE Validation | 14 | 🔴 CRITICAL | 1 |
| 4 | XSS Detection Gap | 7 | 🔴 CRITICAL | 2 |
| 5 | SQLi/NoSQL Gap | 5 | 🟡 HIGH | 2 |
| 6 | LFI/RFI/SSRF | 7 | 🟡 HIGH | 2 |
| 7 | Security Headers & Leakage | 10 | 🟡 HIGH | 2 |
| 8 | Protocol & Middleware | 8 | 🟡 HIGH | 3 |
| 9 | Performance Baseline | 7 | 🟡 HIGH | 3 |
| 10 | Functional E2E | 11 | 🟢 MEDIUM | 4 |
| 11 | Session & Cookie Security | 4 | 🟢 LOW | 4 |
| 12 | OpenAPI Contract | Dynamic | 🟢 MEDIUM | 4 |

---

## Mandatory Conventions

### 1. Configuration — NEVER Use `os.getenv()` or `load_dotenv()`

All config access goes through the `Settings` singleton:

```python
from utils.settings import get_settings
settings = get_settings()
# ✅ settings.base_url, settings.alpha_tenant_id, settings.keycloak_token_url
# ❌ os.getenv("BASE_URL"), load_dotenv()
```

### 2. Fixtures — Standard Names

| Fixture | Defined In | Scope | Purpose |
|---------|-----------|-------|---------|
| `alpha_jwt` | `conftest.py` (root) | session | Real Keycloak JWT for search365 |
| `beta_jwt` | `conftest.py` (root) | session | Real Keycloak JWT for searchsensei |
| `alpha_api` | `conftest.py` (root) | session | Playwright APIRequestContext for search365 |
| `beta_api` | `conftest.py` (root) | session | Playwright APIRequestContext for searchsensei |
| `alpha_data` | `tests/tenant_isolation/conftest.py` | session | Dict of known search365 test markers |
| `beta_data` | `tests/tenant_isolation/conftest.py` | session | Dict of known searchsensei test markers |
| `api_context` | `conftest.py` (root) | session | Bare API context (no auth headers) |
| `expired_jwt` | `conftest.py` (root) | session | Fake expired JWT for AUTH-02 |
| `tampered_jwt` | `conftest.py` (root) | session | Corrupted signature JWT for AUTH-03 |

### 3. HTTP Headers — Exact Casing

```python
headers = {
    "Authorization": f"Bearer {jwt}",
    "X-Active-Tenant": tenant_id,       # Capital X, hyphenated
    "X-Internal-Secret": secret,        # Capital X, hyphenated
    "Content-Type": "application/json",
}
```

### 4. API Payloads — Always Use `data=` (NOT `json=`)

Playwright's `APIRequestContext.post(data=dict)` serializes dicts as JSON automatically.

```python
# ✅ CORRECT — Playwright serializes to JSON
response = api.post("/search", data={"query": "*", "profile": "default"})

# ❌ WRONG — inconsistent with framework convention
response = api.post("/search", json={"query": "*"})
```

### 5. Test Markers — Always Apply Both Scope + Priority

```python
@pytest.mark.isolation    # Scope marker
@pytest.mark.critical     # Priority marker
def test_iso_01_search_search365_returns_only_alpha(...):
```

### 6. Function Naming — ISO/AUTH/RCE Prefix

```
test_iso_{number}_{description}       # Scope 1
test_auth_{number}_{description}      # Scope 2
test_rce_{number}_{description}       # Scope 3
```

---

## Tenant Data Fixtures (`alpha_data` / `beta_data`)

These are defined in `tests/tenant_isolation/conftest.py` and contain known test values that are pre-seeded in each tenant's OpenSearch index:

```python
@pytest.fixture(scope="session")
def alpha_data():
    return {
        "tenant_id": setting.alpha_tenant_id,         # "search365"
        "unique_marker": setting.alpha_tenant_marker,  # From .env
        "known_setting_key": "search365_custom_theme",
        "fastlink_title": "Search365 Internal Portal",
        "fastlink_id": "fl-search365-001",
        "navigation_name": "Search365 Main Nav",
        "synonym_term": "search365-synonym",
        "suggestion_term": "search365-suggestion",
        "profile_name": "search365-intranet",
        "control_panel_name": "Search365 Admin Panel",
        "user_group_id": "ug-search365-admins",
        "rule_trigger_word": "search365-trigger",
        "rule_pinned_result_id": "pinned-search365-001",
    }
```

**Rule:** Every test asserts that `beta_data["field"]` is NOT in the response when authenticated as alpha, and vice versa.

---

## API Endpoint Reference (Key Domains)

| Domain | Read Endpoint | Method | Response Field | Isolation Test |
|--------|--------------|--------|---------------|----------------|
| Search | `/search` | POST | `results` | ISO-01, ISO-02 |
| Settings | `/settings/search` | POST | `result` | ISO-03, ISO-04 |
| Fast Links | `/fastLinks/search` | POST | `result` | ISO-05 |
| Navigations | `/navigations/search` | POST | `result` | ISO-06 |
| Synonyms | `/synonyms/search` | POST | `result` | ISO-07 |
| Profiles | `/availableProfiles` | GET | direct array | ISO-08 |
| Control Panel | `/controlPanel/search` | POST | `result` | ISO-09 |
| User Groups | `/userGroups/search` | POST | `result` | ISO-10 |
| Permissions | `/userPermission/search` | GET | `result` | ISO-11 |
| Query Rules | `/queryrules/search` | POST | `result` | ISO-15 |
| Suggestions | `/suggestions/search` | POST | `result` | ISO-16 |
| Analytics | `/api/analytics/usage` | GET | varies | ISO-17 |
| CRUD (write) | `/fastLinks/update` | PUT | `message` | ISO-12 |
| CRUD (delete) | `/fastLinks/deleteById/{id}` | DELETE | `message` | ISO-13 |
| History | `/search/history` | POST | `results` | ISO-14 |

**Kong scopes pattern:** `osp:[domain]:[action]` (e.g., `osp:search:execute`, `osp:settings:read`)

### API Response Pattern

Most OSP API responses use a standard wrapper:
```json
{"isSuccess": true, "error": "", "status": 200, "result": [...]}
```
Access data via `body.get("result", [])` — NOT `body.get("data", [])`. The `Search` domain is the exception, using `results` (plural).

**Storage note:** UserGroups and UserPermissions are stored in Azure Table Storage (not OpenSearch) with tenant-scoped tables via `TableStoragePrefix` (e.g., `search365_UserGroups`). Permissions contain `view`/`edit`/`delete` arrays of group names.

---

## Writing a New Isolation Test (Template)

```python
import pytest
from playwright.sync_api import APIRequestContext


@pytest.mark.isolation
@pytest.mark.critical
def test_iso_XX_domain_tenant_isolation(
    api_context_search365: APIRequestContext,  # Or alpha_api
    beta_data,
):
    """ISO-XX: [Domain] as Search365 must not see SearchSensei's [domain] data."""

    # 1. Call the API as Search365
    response = api_context_search365.post("/domain/search", data={"query": ""})
    assert response.status == 200

    # 2. Parse response
    body = response.json()
    records = body.get("result", [])  # Most OSP APIs use "result", /search uses "results"

    # 3. Assert NO cross-tenant leakage
    for record in records:
        assert record.get("key_field") != beta_data["expected_field"]
        assert beta_data["unique_marker"] not in str(record)
```

### CRUD Isolation Pattern (ISO-12/13)

```python
def test_iso_12_create_invisible(api_context_search365, api_context_searchsensei):
    unique_id = f"TEST_{uuid.uuid4()}"

    # 1. Tenant A creates
    resp = api_context_search365.put("/fastLinks/update", data={...})
    assert resp.status == 200

    # 2. Tenant B cannot see it
    read = api_context_searchsensei.post("/fastLinks/search", data={"query": unique_id})
    assert len(read.json().get("data", [])) == 0
```

> **Cleanup note:** Teardown for write-heavy tests (ISO-12) is deferred. Use unique UUIDs to avoid collisions.

---

## Kong Authentication Architecture (Scope 2)

Kong enforces auth via 4 plugins at the service level (ALL routes):

| Plugin | Priority | Purpose |
|--------|----------|----------|
| `jwt` | High | Validates JWT signature (RS256 vs Keycloak public key), verifies `exp` claim |
| `jwt-scope-guard` | 900 | Extracts scopes from `authorizations` claim, matches route tags, handles tenant routing |
| `request-transformer` | - | Strips client `X-Internal-Secret`, injects Kong's real value |
| `pre-function` | - | Strips `/kong/api` prefix from path |

### Two Auth Flows (UI vs M2M)

| Flow | JWT Claim | Tenant Resolution |
|------|-----------|-------------------|
| **End-User (UI)** | `active_tenant` (string) | Kong auto-extracts from JWT via `forward_claims` → `X-Active-Tenant` header |
| **M2M (Service Account)** | `tenants` (array) | Client MUST send `X-Active-Tenant` header; Kong validates against `tenants` claim |

**Key behaviors:**
- Normal users: `X-Active-Tenant` header from client is **overwritten** by Kong with JWT claim value
- M2M without `X-Active-Tenant` header → **400**
- M2M with wrong `X-Active-Tenant` (not in `tenants` list) → **403**
- Wildcard `*` in `authorizations` claim bypasses scope checks (for batch service accounts)
- No rate limiting is configured in Kong or backend
- No `/health` endpoint exists in the backend; `HomeController` redirects to `/swagger`
- Backend OIDC auth is disabled (`IsEnabled: false`); Kong is the sole auth enforcer

---

## Writing an Auth Boundary Test (Template)

### Basic rejection test (AUTH-01/02/03)
```python
@pytest.mark.auth
@pytest.mark.critical
def test_auth_XX_scenario(playwright, base_url):
    """AUTH-XX: [Scenario] must be rejected."""

    # Create context with specific invalid auth
    context = playwright.request.new_context(
        base_url=base_url,
        extra_http_headers={"Authorization": f"Bearer {expired_jwt}"},
    )

    response = context.post("/search", data={"query": "test"})
    assert response.status == 401

    context.dispose()
```

### M2M tenant validation test (AUTH-04b/04c)
```python
@pytest.mark.auth
@pytest.mark.critical
def test_auth_04b_m2m_missing_tenant_header(m2m_jwt, playwright, base_url):
    """AUTH-04b: M2M service account without X-Active-Tenant header → 400."""

    context = playwright.request.new_context(
        base_url=base_url,
        extra_http_headers={"Authorization": f"Bearer {m2m_jwt}"},
        # Note: deliberately NOT setting X-Active-Tenant
    )

    response = context.post("/search", data={"query": "test"})
    assert response.status == 400
    assert "X-Active-Tenant" in response.json().get("message", "")

    context.dispose()
```

---

## Assertion Classes (`utils/assertions.py`)

| Class | Scope | Key Methods |
|-------|-------|-------------|
| `IsolationAssertions` | 1 | `assert_no_cross_tenant()`, `assert_crud_invisible_cross_tenant()` |
| `AuthAssertions` | 2 | `assert_unauthorized()`, `assert_bad_request()`, `assert_tenant_enforced_from_jwt()` |
| `SecurityHeaderAssertions` | 7 | `assert_no_server_info()`, `assert_no_stack_trace()`, `assert_no_internal_paths()` |
| `RceAssertions` | 3 | `assert_rce_blocked()`, `assert_no_command_output()` |
| `StatusAssertions` | All | `assert_status()`, `assert_ok()`, `assert_method_not_allowed()` |

---

## JWT Generation (`utils/jwt_helper.py`)

| Method | Use Case | Test ID |
|--------|----------|---------|
| `KeycloakAuthClient.get_tenant_token("ALPHA")` | Real JWT from Keycloak | All Scope 1 |
| `JwtHelper.generate_expired_token()` | Expired JWT | AUTH-02 |
| `JwtHelper.generate_tampered_token()` | Corrupted signature | AUTH-03 |
| `JwtHelper.generate_no_tenant_token()` | Missing active_tenant | AUTH-04 |
| `JwtHelper.generate_spoofed_tenant_token()` | Header spoofing attempt | AUTH-05 |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using `json=` instead of `data=` | Always use `data=` — Playwright auto-serializes dicts to JSON |
| Using `os.getenv()` for config | Use `get_settings()` singleton |
| Using `api_context_alpha` in fixture params | Actual fixture name is `alpha_api` in root conftest |
| Checking `not in profiles` when response is list-of-objects | Extract field first: `[p.get("name") for p in profiles]` |
| Forgetting both markers | Always apply scope marker + priority marker |
| Hardcoding tenant markers | Load from `settings.alpha_tenant_marker` via fixture |
| Using `requests` library | Use Playwright `APIRequestContext` exclusively |
| Lowercase headers `x-active-tenant` | Use `X-Active-Tenant` (HTTP convention) |
| Using `body.get("data", [])` for response data | Most OSP APIs use `result` field: `body.get("result", [])`. Only `/search` uses `results` |
| Treating permissions as global/shared | Permissions are tenant-scoped (separate Azure Table Storage tables per tenant) |
| Expecting 404 from cross-tenant delete | Backend returns 200 with `isSuccess: false`, not 404 |
| Assuming `/health` is unauthenticated | JWT plugin runs at service level — ALL routes require auth, including health |
| Testing rate limiting (AUTH-10) | No rate-limiting plugin is configured — skip or `xfail` |
| Using same tenant flow for UI and M2M tests | UI users have `active_tenant` claim (auto-forwarded); M2M service accounts use `tenants[]` + `X-Active-Tenant` header |

---

## CI/CD Environment Variables

All secrets are injected via GitHub Actions secrets. The `Settings` object reads them automatically (env vars take priority over `.env` file):

```
BASE_URL, INTERNAL_SECRET,
KEYCLOAK_TOKEN_URL, KEYCLOAK_CLIENT_ID, KEYCLOAK_REALM,
ALPHA_TENANT_ID, ALPHA_TENANT_USERNAME, ALPHA_TENANT_PASSWORD,
ALPHA_TENANT_PROFILE, ALPHA_TENANT_MARKER,
BETA_TENANT_ID, BETA_TENANT_USERNAME, BETA_TENANT_PASSWORD,
BETA_TENANT_PROFILE, BETA_TENANT_MARKER
```

---

## GitHub Project Integration

- **Repository:** `Search-Sensei/osp-search-e2e-tests`
- **Project Board:** `OSP Search AI project` (Project #8)
- **Issue prefix:** `OSP Search AI E2E Test- Scope X -`
- **Labels:** `scope-1`, `critical`, `isolation` (for Scope 1 tasks)
- Each test has a matching GitHub issue with a 9-section task definition

## Reference Documents

| Document | Purpose |
|----------|---------|
| `analyze-reports/OSP Platform — Complete E2E Reference Guide.md` | Single source of truth for all API endpoints, security flows, tenant architecture |
| `analyze-reports/E2E Test Implementation Plan — OSP Search Multi-Tenant Platform (v3).md` | Master plan with all 12 scopes, test IDs, phased delivery |
| `analyze-reports/scopes/OSP Search AI E2E Test - Scope 1 Tasks.md` | Detailed 9-section task definitions for all 17 Scope 1 tests |
| `analyze-reports/Python E2E & Performance Testing Framework Setup.md` | Complete code reference for all utils, conftest files, CI/CD pipelines |
