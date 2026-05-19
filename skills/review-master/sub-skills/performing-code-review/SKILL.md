---
name: performing-code-review
description: "Systematic multi-pass code review framework (5 Phases). Part of the review-master discipline."
---



# Performing Code Review (The Iron Law)
**NO VERDICT WITHOUT COMPLETING ALL REVIEW PASSES.**

## 🔄 The Review Pipeline
1. **Phase 1: Reconnaissance**: Understand WHAT changed and WHY. Build a change taxonomy.
2. **Phase 2: Security Pass**: Tenant isolation, Auth/AuthZ, Secret management, Information disclosure.
3. **Phase 3: Architecture Pass**: Separation of Concerns, Error handling (RFC 7807), DI lifetimes, Middleware order.
4. **Phase 4: Bug Hunt**: Call site vs Declaration mismatch, Async/await hygiene, Resource disposal.
5. **Phase 5: Grading & Verdict**: Assign severity (Critical/High/Medium/Low) and issue Verdict (APPROVE/REQUEST CHANGES).

## 🧩 Stack-Specific Checklists
- **.NET**: Blocking async (`.Result`), Nullable misuse, EF Core N+1.
- **Python/pytest**: Fixture scoping, Playwright context disposal, xfail rationale.
- **JS/React**: Stale closures, missing `useEffect` cleanup, infinite re-renders, hydration mismatch.

## 🏁 Verdict Contract
Every review must include an Executive Summary, Change Taxonomy, Detailed Findings, and a clear Verdict with "Must Fix" (blocking) items.

# Performing Code Review


## Overview
Superficial code reviews miss critical bugs and security holes. Reviewing without structure produces inconsistent, incomplete feedback.

**Core principle:** Every review follows the same systematic passes. Evidence-based findings, not opinion. Severity-graded, actionable feedback.

**Supported stacks:**
- **C#/.NET** — ASP.NET backends, middleware pipelines, DI, Entity Framework
- **Python/pytest** — E2E test suites, Playwright, Locust, schemathesis, pydantic-settings
- **JavaScript/React.js** — React SPAs, Next.js SSR/SSG, state management, hooks, bundler config, REST/GraphQL clients

**Violating the letter of this process is violating the spirit of code review.**

## The Iron Law
```
NO VERDICT WITHOUT COMPLETING ALL REVIEW PASSES
```

If you haven't completed every pass, you cannot issue a verdict.

## When to Use
**Use for:**
- Pull request reviews (GitHub, GitLab, Bitbucket)
- Auditing code changes for security and architecture
- Evaluating developer work against best practices
- Pre-merge quality gates

**Use this ESPECIALLY when:**
- Changes touch security-critical paths (auth, tenant isolation, encryption)
- Changes modify middleware, exception handling, or request pipelines
- Changes span multiple layers (controller → service → infrastructure)
- PR is large (>10 files or >200 lines changed)
- Changes touch **test fixtures, conftest.py hierarchy, or marker strategy** (Python)
- Changes modify **Playwright context lifecycle** or **JWT fixture generation** (Python)
- Changes modify **React component lifecycle**, **custom hooks**, or **context providers** (JavaScript)
- Changes touch **authentication flows**, **token storage**, or **API client configuration** (JavaScript)
- Changes affect **bundler config** (`vite.config`, `next.config`, `webpack.config`) or **environment variable exposure** (JavaScript)

## The Review Pipeline
You MUST complete each phase sequentially. No skipping.

```
Phase 1: Reconnaissance    → Understand scope and intent
Phase 2: Security Pass     → Find vulnerabilities and data leaks
Phase 3: Architecture Pass → Evaluate design decisions and patterns
Phase 4: Bug Hunt          → Find logic errors, type mismatches, edge cases
Phase 5: Grading & Verdict → Assign severity, produce actionable feedback
```

### Phase 1: Reconnaissance
**Goal:** Understand WHAT changed and WHY before judging anything.

1. **Read the PR metadata**
   - Title, description, branch name, linked issues
   - Number of files changed, lines added/removed
   - Number of commits (single coherent change or multiple concerns?)

2. **Get the file list first**
   - Use `get_files` (not `get_diff`) to see the full scope
   - Categorize files by layer: controllers, services, middleware, models, config, tests, frontend

3. **Read the full diff**
   - Use `get_diff` to read the complete change set
   - Don't skip files — removed code is as important as added code
   - Note: What was DELETED tells you what problems existed before

4. **Build a change taxonomy**
   - Group changes by logical concern (not by file)
   - Identify if multiple unrelated changes are bundled (flag this)
   - Map data flow: how do changes in layer A affect layer B?

**Output of Phase 1:** A mental model of what the PR does, organized by concern, not by file.

### Phase 2: Security Pass
**Goal:** Find vulnerabilities, data leaks, and isolation failures.

**MANDATORY checks — every PR, no exceptions:**

| Check | What to Look For |
|-------|-----------------|
| **Tenant isolation** | Are tenant boundaries maintained? Can tenant A access tenant B's data? |
| **Auth/AuthZ** | Are authentication checks preserved? Any bypasses introduced? |
| **Input validation** | Are user inputs validated? SQL injection, XSS, header injection? |
| **Secret management** | Hardcoded credentials? API keys in source? Fallback secrets? |
| **Information disclosure** | Stack traces in production? Internal IPs exposed? Error messages leaking implementation details? |
| **Header trust** | X-Forwarded-For trusted without validation? Host header injection? |
| **Thread safety** | Shared mutable state? DefaultRequestHeaders on shared HttpClient? Static dictionaries modified concurrently? |
| **Rate limiting** | Is abuse protection in place? Can it be bypassed? |
| **Token/session handling** | Proper expiration? Secure storage? Cancellation propagation? |
| **CORS/CSP** | Overly permissive origins? Missing security headers? |

#### Python/pytest Security Checks (additional)
| Check | What to Look For |
|-------|-----------------|
| **`.env` exposure** | Is `.env` in `.gitignore`? Are real credentials committed? Is `.env.example` sanitized? |
| **`SecretStr` usage** | Are passwords stored as `SecretStr`? Is `.get_secret_value()` only called at point-of-use, never logged? |
| **`verify=False`** | TLS certificate validation disabled on `httpx` calls? Acceptable for dev Keycloak with self-signed certs, but MUST be documented. |
| **Jupyter notebooks** | Do `.ipynb` files contain credentials, tokens, or API responses with PII? |
| **Fixture credential scope** | Are JWT fixtures `scope="session"` (cached) or `scope="function"` (new token per test)? Session-scoped is correct for performance. |
| **Token caching** | Is `_token_cache` thread-safe? Does `threading.Lock()` protect concurrent access? |
| **`lru_cache` staleness** | `@lru_cache` on `get_settings()` means config never refreshes — acceptable for test runs, but document the constraint. |
| **Hardcoded test data** | Are tenant IDs, markers, or URLs hardcoded in test files instead of coming from `Settings`? |

#### JavaScript/React.js Security Checks (additional)
| Check | What to Look For |
|-------|------------------|
| **Token storage** | Are JWTs stored in `localStorage`? (XSS-accessible — prefer `httpOnly` cookies or in-memory). Is `sessionStorage` used for sensitive tokens? |
| **`dangerouslySetInnerHTML`** | Any usage without DOMPurify sanitization? Every instance is a potential XSS vector. |
| **Environment variables** | Are `NEXT_PUBLIC_*` or `VITE_*` prefixed vars exposing secrets? Only non-sensitive config should be client-exposed. `REACT_APP_*` vars are bundled into the client JS. |
| **API keys in client bundle** | Are API keys, internal URLs, or secrets embedded in client-side code? Use `grep -r "apiKey\|api_key\|secret\|password" src/` to find leaks. |
| **CORS configuration** | Is `Access-Control-Allow-Origin: *` used? Are credentials (`withCredentials: true`) sent to wildcard origins? |
| **`eval()` / `new Function()`** | Dynamic code execution from user input? Always a critical XSS vector. |
| **Dependency supply chain** | Are `node_modules` committed? Is `package-lock.json` / `yarn.lock` present and committed? Are there `postinstall` scripts from untrusted packages? |
| **SSR data exposure (Next.js)** | Do `getServerSideProps` / `getStaticProps` return sensitive data that's serialized to `__NEXT_DATA__`? Server-only data must be filtered before return. |
| **Source maps in production** | Are `.map` files generated in production builds? They expose original source code. Check `devtool` / `productionSourceMap` config. |
| **CSP headers** | Is Content-Security-Policy set? Does it allow `unsafe-inline` or `unsafe-eval`? |
| **Iframe embedding** | Is `X-Frame-Options` or CSP `frame-ancestors` set to prevent clickjacking? |
| **Open redirect** | Does the app redirect based on URL parameters (e.g., `?redirect=`) without validating against an allowlist? |

**For each finding, classify:**
- 🚨 **CRITICAL** — Exploitable vulnerability, data leak, auth bypass
- 🔴 **HIGH** — Security weakness that should be fixed before merge
- 🟡 **MEDIUM** — Defense-in-depth improvement, hardening opportunity
- 🟢 **LOW** — Best practice suggestion, non-exploitable

### Phase 3: Architecture Pass
**Goal:** Evaluate design quality, patterns, and maintainability.

---

#### C#/.NET Architecture Checks
**Check each of these dimensions:**

1. **Separation of Concerns**
   - Controllers doing business logic? (should delegate to services)
   - Services doing HTTP response formatting? (should throw exceptions)
   - Middleware responsibilities clear and non-overlapping?

2. **Error Handling Strategy**
   - Consistent error response format across endpoints?
   - Domain exceptions vs generic exceptions?
   - Exception hierarchy follows HTTP semantics?
   - RFC 7807 Problem Details compliance?
   - Development-only stack traces?

3. **Dependency Injection**
   - Correct lifetimes? (Singleton, Scoped, Transient)
   - Captive dependency antipattern? (Scoped injected into Singleton)
   - DelegatingHandlers registered as Transient?

4. **HTTP Client Usage**
   - Using IHttpClientFactory or named/typed clients?
   - Not mutating DefaultRequestHeaders on shared instances?
   - Proper disposal of HttpRequestMessage/HttpResponseMessage?
   - Cancellation tokens propagated to SendAsync?

5. **Middleware Pipeline**
   - Correct ordering? (ForwardedHeaders → RateLimiting → Auth → Routing)
   - Each middleware has single responsibility?
   - Short-circuit paths correct?

6. **Code Reduction**
   - Did the PR remove duplication?
   - Are helper methods well-named and focused?
   - Is complexity justified or gratuitous?

---

#### Python/pytest Architecture Checks
**Check each of these dimensions when reviewing Python test code:**

> **Cross-reference:** For OSP Search E2E-specific conventions (fixture names, API endpoints, payload formats, marker rules, naming patterns), see the `building-e2e-tests` skill — it is the authoritative source. The checks below are general Python/pytest review criteria.

1. **Fixture Design & Scoping**
   - Are fixture scopes correct? `session` for expensive resources (Playwright contexts, JWT tokens), `function` for test-specific state
   - Are `yield` fixtures cleaning up properly? Every `yield context` must have `context.dispose()` / `context.close()` after yield
   - Is the conftest.py hierarchy correct? Root conftest → `tests/conftest.py` → scope-specific conftest (e.g., `tests/tenant_isolation/conftest.py`)
   - Are fixtures shadowed? A fixture in a child conftest with the same name as a parent fixture overrides silently
   - Are fixture dependency chains reasonable? Deep chains (>3 levels) are fragile and hard to debug

2. **Playwright Lifecycle Management**
   - `APIRequestContext` created via `playwright.request.new_context()` — disposed in teardown?
   - `BrowserContext` created via `browser.new_context()` — closed in teardown?
   - Session-scoped Playwright contexts share JWT tokens — is token expiry handled?
   - Browser fixtures are function-scoped (correct) — they should NOT be session-scoped (stale DOM state)

3. **Settings & Configuration Architecture**
   - All config via `pydantic-settings` `BaseSettings` → `get_settings()` singleton?
   - No raw `os.getenv()` or `load_dotenv()` calls outside `settings.py`?
   - `SecretStr` used for passwords — `.get_secret_value()` only at point-of-use?
   - `.env` file path resolved via `Path(__file__).resolve().parent.parent` — robust for any working directory?

4. **Marker Strategy**
   - Priority markers (`critical`, `high`, `medium`, `low`) — one per test, matching the Implementation Plan scope priority?
   - Scope markers (`isolation`, `auth`, `rce`, `xss`, `sqli`, etc.) — correctly categorizing tests?
   - `@pytest.mark.xfail(reason="...")` — every xfail has a documented reason referencing the specific security gap?
   - `@pytest.mark.parametrize` — test IDs descriptive for CI/CD reporting?

5. **Test Organization**
   - Tests grouped by scope in separate directories (`tenant_isolation/`, `authentication/`, `owasp_rce/`, etc.)?
   - Each scope directory has its own conftest.py with scope-specific fixtures?
   - Test file names follow `test_*.py` pattern — discoverable by pytest?
   - Test function names follow `test_<scope_id>_<description>` pattern (e.g., `test_iso_01_search_isolation`)?

6. **Assertion Helpers**
   - Assertion classes in `utils/assertions.py` are scope-specific (`IsolationAssertions`, `AuthAssertions`, etc.)?
   - Assertions include descriptive error messages — not just `assert x == y`?
   - Response helpers (`extract_records`, `assert_no_cross_tenant`) are generic and reusable?

7. **Performance Test Architecture (Locust)**
   - User classes have realistic `wait_time` (`between(1, 3)`)?
   - Task weights reflect real usage patterns (search 3x more frequent than CRUD)?
   - JWT tokens refreshed during long-running load tests?
   - `--headless` mode used in CI/CD, `--csv` export for results?
   - Separate GitHub Actions workflow with appropriate `timeout-minutes`?

8. **Contract Test Architecture (schemathesis)**
   - Swagger spec URL configurable via env var?
   - Auth headers injected into every schemathesis request?
   - `--hypothesis-max-examples` tuned for CI timeout constraints?
   - Destructive operations (POST/DELETE) guarded against production data?

---

#### JavaScript/React.js Architecture Checks
**Check each of these dimensions when reviewing JavaScript/React.js code:**

1. **Component Architecture**
   - Are components small and focused? (single responsibility — under ~200 lines)
   - Is business logic extracted into custom hooks or utility functions, not embedded in JSX?
   - Are presentational components separated from container/smart components?
   - Is prop drilling avoided? (prefer Context, Zustand, Redux, or composition patterns)
   - Are component files co-located with their styles, tests, and types?

2. **Hooks Design & Usage**
   - Do custom hooks follow the `use*` naming convention?
   - Are hooks called at the top level only? (no conditionals, no loops, no nested functions)
   - Is `useEffect` cleanup implemented? Every subscription, timer, or event listener needs a cleanup return.
   - Are `useEffect` dependency arrays correct? Missing deps → stale closures. Extra deps → infinite re-renders.
   - Is `useMemo` / `useCallback` used appropriately? (not everywhere — only for expensive computations or stable references passed to children)

3. **State Management**
   - Is state lifted to the correct level? (as low as possible, as high as necessary)
   - Is server state (API data) separated from client state (UI state)?
   - Are data-fetching libraries used for server state? (`react-query` / `@tanstack/react-query`, `SWR`, or `RTK Query`)
   - Is global state minimal? (avoid putting everything in Redux/Zustand — prefer local state + server cache)
   - Are state updates immutable? (no direct mutation of state objects or arrays)

4. **API Client & Data Fetching**
   - Is there a centralized API client? (`axios` instance, `fetch` wrapper, or GraphQL client)
   - Are auth headers (JWT, API key) injected via interceptor/middleware, not per-call?
   - Is error handling consistent? (global error boundary + per-request error states)
   - Are loading/error/success states all handled in the UI? (no unhandled promise rejections)
   - Is request cancellation implemented? (`AbortController` for `fetch`, cancel tokens for `axios`)
   - Are API responses typed? (TypeScript interfaces or PropTypes for plain JS)

5. **Routing & Navigation**
   - Are routes protected? (auth guards on private routes, redirect to login)
   - Is code splitting used? (`React.lazy()` + `Suspense` for route-based splitting)
   - Are 404/error routes defined?
   - Is navigation state managed correctly? (no stale state after navigation)
   - Are deep links and browser back/forward handled?

6. **Build & Bundle Configuration**
   - Is tree-shaking effective? (named imports, not barrel `import * from`)
   - Are bundle sizes monitored? (webpack-bundle-analyzer, `next build` output, Vite rollup-plugin-visualizer)
   - Is code splitting configured? (dynamic imports for heavy dependencies)
   - Are environment variables properly scoped? (no secrets in `NEXT_PUBLIC_*` / `VITE_*` / `REACT_APP_*`)
   - Is the production build minified with source maps disabled?

7. **TypeScript Usage (if applicable)**
   - Are `any` types avoided? (`any` defeats the purpose of TypeScript)
   - Are component props typed with `interface` or `type`?
   - Are API response types defined and used for type narrowing?
   - Is `strict` mode enabled in `tsconfig.json`?
   - Are generic types used appropriately for reusable utilities?

8. **Testing Architecture (Jest/Vitest + React Testing Library)**
   - Are components tested by behavior, not implementation? (query by role/text, not by class/id)
   - Are custom hooks tested with `renderHook()`?
   - Is `msw` (Mock Service Worker) used for API mocking instead of manual `fetch` mocks?
   - Are test files co-located with components? (`Component.test.tsx` next to `Component.tsx`)
   - Is snapshot testing used sparingly? (only for stable, small components — not entire pages)

9. **E2E Testing Architecture (Cypress / Playwright)**
   - Are E2E tests separated from unit/integration tests? (e.g., `cypress/` or `e2e/` directory)
   - Is Page Object Model (POM) or equivalent abstraction used? (selectors encapsulated, not scattered in test files)
   - Are selectors resilient? (`data-testid` attributes preferred over CSS classes or text content)
   - Is test data isolated? (each test creates and cleans up its own data — no shared mutable state)
   - Are API calls intercepted for deterministic tests? (`cy.intercept()` in Cypress, `page.route()` in Playwright)
   - Is authentication handled via API login (not UI login) for speed? (set cookies/tokens directly)
   - Are visual regression tests used? (Percy, Chromatic, or Playwright `toHaveScreenshot()`)
   - Is CI/CD integration configured? (`cypress run --record` or `npx playwright test --reporter=html`)
   - Are flaky test retries configured? (`retries` in Cypress config, `retries` in Playwright config)
   - Is parallel execution configured for CI? (`--parallel` in Cypress, `--workers` in Playwright)

---

#### Next.js-Specific Architecture Checks
**Additional checks for Next.js projects (App Router and Pages Router):**

1. **Server vs Client Components (App Router)**
   - Are components defaulting to Server Components? (only `'use client'` where interactivity is needed)
   - Is `'use client'` pushed as far down the tree as possible? (avoid making entire pages client components)
   - Are Server Actions used for form submissions and mutations? (not API routes for simple CRUD)
   - Is `'use server'` only on functions that should run server-side? (no accidental exposure of server logic)

2. **Data Fetching Patterns**
   - `getServerSideProps` / `getStaticProps` (Pages Router) — are they returning only serializable, non-sensitive data?
   - Server Components (App Router) — are `async` components fetching data directly without client-side state?
   - Is ISR (Incremental Static Regeneration) used where appropriate? (`revalidate` option configured)
   - Are `generateStaticParams` / `getStaticPaths` returning all expected paths for dynamic routes?

3. **SSR Security**
   - Does `__NEXT_DATA__` contain sensitive data? (inspect page source in production build)
   - Are API keys and database credentials used only in server-side code? (not imported in client components)
   - Is `next.config.js` `headers()` / `middleware.ts` used for security headers (CSP, HSTS, X-Frame-Options)?
   - Are environment variables without `NEXT_PUBLIC_` prefix inaccessible from client bundles?

4. **Middleware & Edge Runtime**
   - Is `middleware.ts` used for auth checks, redirects, and geolocation — not for heavy computation?
   - Is the edge runtime constraint respected? (no Node.js APIs like `fs`, `path`, `crypto` in middleware)
   - Are middleware matchers (`config.matcher`) specific? (not matching static assets or `_next/`)

### Phase 4: Bug Hunt
**Goal:** Find logic errors, constructor mismatches, edge cases.

---

#### C#/.NET Bug Hunt
**Systematic checks:**

| Category | What to Verify |
|----------|---------------|
| **Constructor arguments** | Do argument positions match parameter names? Named vs positional confusion? |
| **Pattern matching** | Valid C# syntax? Correct variable binding? |
| **Null handling** | Null checks where needed? Nullable reference types consistent? |
| **Resource disposal** | `using` statements on HttpRequestMessage, HttpResponseMessage, streams? |
| **Async/await** | ConfigureAwait where needed? Task.Run misuse? Deadlock potential? |
| **Exception swallowing** | Empty catch blocks? `catch { }` without logging? |
| **Off-by-one** | Boundary conditions in loops, pagination, array access? |
| **String comparison** | Ordinal vs OrdinalIgnoreCase where appropriate? |
| **Logging** | Structured logging with `{Placeholder}` not `$"{interpolation}"`? Correct log levels? |
| **Dead code** | Unused variables? Unreachable branches? Assigned-but-never-read? |
| **Compile errors** | Invalid syntax that won't compile? Missing using statements? |

**For constructor argument mismatches specifically:**
```
ALWAYS verify: Does the CALL SITE match the DECLARATION?

// Declaration
RemoteServiceException(string message, string errorCode, object details)

// Call site — CHECK each positional argument maps to correct parameter
new RemoteServiceException("TokenEndpoint", "Token endpoint returned 401", 401)
//                          ^^^^^^^^        ^^^^^^^^^^^^^^^^^^^^^^^^        ^^^
//                          message?        errorCode?                     details?
//                          This looks like a SERVICE NAME, not a MESSAGE
```

---

#### Python/pytest Bug Hunt
| Category | What to Verify |
|----------|---------------|
| **`__init__` parameter order** | Do positional args at call sites match the `__init__` declaration? Especially `TenantContext(tenant_id, tenant_name, api)` |
| **`None` handling** | `getattr()` with `None` default — is `None` checked before `.get_secret_value()`? |
| **Fixture scoping bugs** | `scope="session"` fixture depending on `scope="function"` fixture? (pytest error at collection time) |
| **`yield` teardown missing** | Fixture uses `yield` but no cleanup code after yield? Or cleanup code that can raise? |
| **Playwright disposal** | `APIRequestContext.dispose()` and `BrowserContext.close()` called in fixture teardown? Leaked contexts = leaked TCP connections |
| **`response.json()` on non-JSON** | Calling `.json()` on a non-200 response that returns HTML? (e.g., 502 from gateway) |
| **String vs bytes** | `response.text()` returns `str`, `response.body()` returns `bytes` — mixing them causes comparison bugs |
| **Mutable default args** | `def func(data={})` — mutable defaults are shared across calls |
| **`assert` in helpers** | `assert` in non-test helper functions is stripped by `python -O` — use `raise AssertionError()` or custom exceptions |
| **Import cycles** | `utils/settings.py` → `utils/jwt_helper.py` → `utils/settings.py`? Circular imports cause `ImportError` |
| **Logging** | `logger.info("msg %s", val)` NOT `logger.info(f"msg {val}")` — f-strings evaluate even if log level is disabled |
| **`verify=False` propagation** | Is TLS verification disabled only for dev Keycloak, or does it leak to other `httpx` calls? |
| **Playwright `data=` vs `json=`** | `api.post(path, data={...})` — Playwright's `data=` accepts dict and serializes as JSON. Don't pass `json=` (it's not `requests` library) |

**For fixture dependency bugs specifically:**
```python

```

# BUG: session-scoped fixture depending on function-scoped fixture
@pytest.fixture(scope="session")
def alpha_api(playwright, base_url, alpha_jwt):  # alpha_jwt is session-scoped ✅
    ...

# BUG: This would FAIL if alpha_jwt were function-scoped


# because session fixtures cannot depend on function fixtures
```

---

```

#### JavaScript/React.js Bug Hunt
| Category | What to Verify |
|----------|---------------|
| **Stale closures** | Does a `useEffect` or event handler reference a state variable without including it in the dependency array? The handler will use the stale initial value. |
| **Missing `useEffect` cleanup** | `setInterval`, `addEventListener`, WebSocket connections, or subscriptions created in `useEffect` — is the cleanup function returned? Leaked listeners = memory leaks. |
| **Infinite re-render loops** | `useEffect` that sets state it depends on? `useMemo` with unstable dependency (new object/array on every render)? |
| **Key prop errors** | Using array index as `key` in lists that can reorder, add, or remove items? Use stable unique IDs. Missing `key` prop entirely? |
| **Unhandled promise rejections** | `async` calls in `useEffect` without `.catch()` or try/catch? `onClick={async () => { await fetch(...) }}` without error handling? |
| **Race conditions in async effects** | Two rapid state changes trigger two fetches — does the component use the result of the SECOND fetch, not the first (stale) one? Use `AbortController` or boolean flag. |
| **Direct state mutation** | `state.items.push(newItem)` instead of `setState([...state.items, newItem])`? React won't detect the change and won't re-render. |
| **Incorrect dependency arrays** | Empty `[]` when effect depends on props/state (runs once, stale data). Object/array in deps without `useMemo` (runs every render). |
| **Event handler recreation** | Passing `() => handleClick(id)` as prop causes child re-renders every render. Wrap with `useCallback` if child is memoized. |
| **`undefined` vs `null` confusion** | Optional chaining (`?.`) returns `undefined`, but API might return `null`. `value ?? fallback` handles both; `value \|\| fallback` treats `0` and `""` as falsy. |
| **TypeScript type narrowing** | Type assertion (`as Type`) instead of type guard (`if ('prop' in obj)`)? Assertions bypass runtime safety. |
| **Import order / circular deps** | Circular imports between modules cause `undefined` at runtime. Check for `A → B → A` import chains. |
| **Environment variable typos** | `process.env.REACT_APP_API_URL` — typo means `undefined` at runtime, no compile error. Same for `import.meta.env.VITE_*`. |
| **SSR hydration mismatch (Next.js)** | Server renders one thing, client renders another → hydration error. Common with `window`/`document` access, `Date.now()`, or `Math.random()` in render. |

**For stale closure bugs specifically:**
```jsx
// BUG: count is captured at 0 and never updates
useEffect(() => {
  const id = setInterval(() => {
    console.log(count);  // Always logs 0!
    setCount(count + 1); // Always sets to 1!
  }, 1000);
  return () => clearInterval(id);
}, []);  // ← Empty deps: count is stale

// FIX: Use functional update
useEffect(() => {
  const id = setInterval(() => {
    setCount(prev => prev + 1);  // Uses latest value
  }, 1000);
  return () => clearInterval(id);
}, []);
```

### Phase 4.5: Test Quality Review (Python test projects and JavaScript test-heavy PRs)
**Goal:** Evaluate the quality, reliability, and maintainability of test code itself.

**Skip this phase for non-test codebases.**

| Check | What to Verify |
|-------|-----------------|
| **Test independence** | Each test must run standalone — no ordering dependencies. `pytest --randomly-seed=12345` should not break tests. |
| **Assertion specificity** | `assert response.status == 200` > `assert response.ok` — specific assertions produce better failure messages. |
| **xfail rationale** | Every `@pytest.mark.xfail` MUST have `reason="..."` referencing the specific security gap (e.g., "no cookie inspection middleware"). Bare `xfail` is NEVER acceptable. |
| **Marker accuracy** | `@pytest.mark.critical` tests must truly be production-blocking. Cross-reference with the Implementation Plan priority column. |
| **Scope isolation** | Scope 3 (RCE) tests should NOT accidentally test Scope 7 (headers) concerns. Each test validates ONE thing. |
| **Data seeding** | Tests must not depend on pre-existing data that may change. Document required seed data in conftest.py or README. |
| **Cleanup/teardown** | CRUD tests (ISO-12/13) that create resources MUST clean up in teardown — even if the test fails. |
| **Parametrize quality** | `@pytest.mark.parametrize` IDs must be descriptive for CI reports. Use `pytest.param(..., id="rce_semicolon")`. |
| **Response validation** | Tests should validate response structure (schema), not just status codes. `response.json()["isSuccess"]` > just `response.status == 200`. |
| **Negative test completeness** | For each positive test, is there a corresponding negative test? (e.g., ISO-01 searches as alpha, ISO-02 as beta) |
| **Timeout handling** | Long-running tests (Locust, schemathesis) must have `timeout-minutes` in CI and `pytest.mark.timeout` decorators. |
| **Error message quality** | Assertion messages must help debugging: include tenant ID, endpoint, and actual vs expected values. |

---

### Phase 5: Grading & Verdict
**Grade each dimension independently:**

| Category | Grade | Criteria |
|----------|-------|----------|
| Security | A-F | Vulnerabilities found, isolation maintained, secrets handled |
| Architecture | A-F | Design quality, separation of concerns, patterns |
| Code Quality | A-F | Readability, consistency, best practices |
| Error Handling | A-F | Consistency, information disclosure, RFC compliance |
| Testing | A-F | Coverage, edge cases, regression tests |

**Issue the verdict:**

| Verdict | Criteria |
|---------|----------|
| **APPROVE** | No bugs, no security issues, good architecture. Minor suggestions only. |
| **APPROVE with comments** | No bugs, no security issues. Has non-blocking suggestions worth noting. |
| **REQUEST CHANGES** | Has bugs, security issues, or architectural problems that must be fixed. |

**Structure the final output:**

```markdown

# PR #N — Security & Architecture Review


## Executive Summary
One paragraph: what the PR does, overall quality assessment.

## Change Taxonomy
Table: numbered change areas with file counts and impact grades.

## Detailed Findings (per change area)
For each area: what changed, assessment with evidence, specific code references.

## Bugs Found (if any)
Numbered, with code snippets showing the bug and the fix.

## Data Separation & Isolation Checklist
Table: every isolation concern with pass/fail status.

## Best Practices Assessment
Table: category grades with brief justification.

## Verdict
Clear recommendation with:
- 🚨 Must Fix (blocking)
- ⚠️ Should Fix (important but not blocking)
- 💡 Suggestions (non-blocking improvements)
```

## GitHub MCP Integration
**Gathering data (use these tools in order):**

```
1. pull_request_read(method="get")        → PR metadata, title, description
2. pull_request_read(method="get_files")  → File list for scope assessment
3. pull_request_read(method="get_diff")   → Full diff for analysis
4. get_file_contents(path, ref)           → Read specific files in PR branch
5. search_code(query, repo)              → Search for patterns across codebase
```

**Publishing the review:**

```
Use add_issue_comment(owner, repo, issue_number, body)
→ Posts a comprehensive review as a PR comment
→ Use full markdown formatting with tables, code blocks, alerts
```

**DO NOT use browser tools for PR review. Use GitHub MCP exclusively.**

## Red Flags — STOP and Re-examine
- Reviewing without reading the full diff first
- Approving because "it looks reasonable"
- Skipping security pass because "it's just a refactor"
- Not checking constructor argument order
- Not verifying pattern match syntax
- Trusting that removed try/catch blocks are handled by middleware without checking
- Ignoring deleted code (what was removed is as important as what was added)
- "It compiles so it's correct"

## Common Rationalizations
| Excuse | Reality |
|--------|---------|
| "PR is too large to review thoroughly" | Large PRs ESPECIALLY need thorough review. Flag the size, but review fully. |
| "I trust this developer" | Trust doesn't replace verification. Bugs don't care about seniority. |
| "It's just logging changes" | Logging changes can leak secrets, expose internal topology, impact performance. |
| "The tests pass" | Tests only cover what they test. Security gaps rarely have test coverage. |
| "It's a refactor, no behavior change" | Refactors frequently introduce subtle behavioral changes. Check edge cases. |
| "Too many files to check constructors" | Constructor mismatches cause runtime crashes. ALWAYS verify argument order. |

## Anti-Patterns in Code Review


### ❌ Rubber Stamping
"LGTM" without reading the diff.

### ❌ Style-Only Reviews
Commenting on formatting while missing security holes.

### ❌ Vague Feedback
"This could be improved" without saying HOW.

### ❌ Opinion Without Evidence
"I don't like this pattern" without explaining the technical risk.

### ❌ Approval with Unresolved Concerns
Approving while noting "should fix later" — if it matters, REQUEST CHANGES.

### ❌ Incomplete Scope
Reviewing only the files you understand while skipping unfamiliar layers.

## Quick Reference


### C#/.NET Reviews
| Phase | Key Activities | Output |
|-------|---------------|--------|
| **1. Recon** | Read metadata, file list, full diff, categorize | Change taxonomy |
| **2. Security** | Tenant isolation, auth, secrets, info disclosure, thread safety | Severity-graded findings |
| **3. Architecture** | SoC, error handling, DI, HTTP clients, middleware order | Design assessment |
| **4. Bug Hunt** | Constructor args, pattern match, null handling, resource disposal | Bug list with fixes |
| **5. Verdict** | Grade dimensions, classify issues, structure output | Actionable review comment |

### Python/pytest Reviews
| Phase | Key Activities | Output |
|-------|---------------|--------|
| **1. Recon** | Read metadata, file list, full diff, categorize by scope | Change taxonomy |
| **2. Security** | `.env` exposure, `SecretStr`, `verify=False`, Jupyter notebooks, fixture cred handling | Severity-graded findings |
| **3. Architecture** | Fixture scoping, conftest hierarchy, Playwright lifecycle, markers, Locust/schemathesis design | Design assessment |
| **4. Bug Hunt** | `__init__` args, fixture scoping, `yield` teardown, `response.json()` safety, mutable defaults | Bug list with fixes |
| **4.5 Test Quality** | Test independence, xfail rationale, assertion specificity, scope isolation, cleanup | Test quality assessment |
| **5. Verdict** | Grade dimensions, classify issues, structure output | Actionable review comment |

### JavaScript/React.js Reviews
| Phase | Key Activities | Output |
|-------|---------------|--------|
| **1. Recon** | Read metadata, file list, full diff, categorize by component/feature | Change taxonomy |
| **2. Security** | Token storage, `dangerouslySetInnerHTML`, env var exposure, CSP, source maps, open redirect | Severity-graded findings |
| **3. Architecture** | Component design, hooks usage, state management, API client, routing, bundle config, TypeScript, testing, Next.js SSR | Design assessment |
| **4. Bug Hunt** | Stale closures, missing cleanup, infinite loops, key props, race conditions, state mutation, hydration | Bug list with fixes |
| **5. Verdict** | Grade dimensions, classify issues, structure output | Actionable review comment |

## The Bottom Line
**Every PR gets the same systematic treatment.**

Five passes. Evidence-based findings. Severity-graded issues. Actionable verdicts.

No shortcuts for code review. The bugs you miss in review become the incidents you debug in production.
