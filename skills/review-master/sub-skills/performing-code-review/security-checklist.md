# Security Review Checklist

Deep-dive checklist organized by attack surface. Use during Phase 2 (Security Pass).

## Authentication & Authorization

- [ ] Auth middleware preserved — no endpoints became publicly accessible
- [ ] Token validation logic unchanged or improved — not weakened
- [ ] Session expiration handling correct — expired tokens rejected, not silently accepted
- [ ] OAuth/OIDC flows complete — no steps skipped in token exchange
- [ ] API key management — no hardcoded keys, no fallback test credentials
- [ ] Role-based access control — authorization checks match endpoint sensitivity
- [ ] JWT claims validated — issuer, audience, expiration, signature all checked

## Multi-Tenant Isolation

- [ ] Tenant context resolved server-side — not from client-controlled parameters
- [ ] Cross-tenant access prevented — tenant A cannot read/write tenant B's data
- [ ] Tenant validation in middleware — early pipeline, before any data access
- [ ] Header injection detection — multi-value tenant headers rejected
- [ ] Tenant mismatch logged as CRITICAL — security audit trail maintained
- [ ] Database queries scoped to tenant — no unscoped queries introduced
- [ ] Cache keys include tenant — tenant data cannot leak between cache entries

## Information Disclosure

- [ ] Stack traces — only in development, never in production responses
- [ ] Error messages — generic in production, no internal paths/class names
- [ ] Logging — no PII, secrets, or tokens logged at INFO level or above
- [ ] Internal URLs — infrastructure topology not exposed in responses or logs
- [ ] Upstream error bodies — bounded/truncated before inclusion in responses
- [ ] Response headers — no server version, framework version, debug headers in production

## Input Validation

- [ ] User input validated — length limits, format checks, type coercion
- [ ] SQL injection — parameterized queries, no string concatenation
- [ ] XSS — output encoding, Content-Security-Policy headers
- [ ] Path traversal — file paths validated, no `../` exploitation
- [ ] Header injection — CRLF injection in custom headers prevented
- [ ] JSON deserialization — type limits, depth limits, size limits

## HTTP Client Security

- [ ] Shared HttpClient — no DefaultRequestHeaders mutation (thread safety)
- [ ] Per-request headers — Authorization, API keys set on HttpRequestMessage
- [ ] TLS validation — certificate validation not disabled
- [ ] Timeout configuration — reasonable timeouts to prevent resource exhaustion
- [ ] Response size limits — upstream response bodies bounded before parsing
- [ ] Cancellation propagation — client disconnect cancels upstream calls

## Rate Limiting & DoS Protection

- [ ] Rate limiting enabled — requests per IP/user/path bounded
- [ ] IP resolution — trusts ForwardedHeadersMiddleware, not raw X-Forwarded-For
- [ ] Rate limit headers — Retry-After returned to clients (RFC 6585)
- [ ] Configuration — thresholds configurable, not hardcoded
- [ ] Audit logging — rate limit violations logged for security monitoring
- [ ] Log volume — per-request audit logs at appropriate level (Debug, not Info)

## Error Handling Security

- [ ] Exception hierarchy — domain exceptions mapped to correct HTTP status codes
- [ ] Catch guards — `catch (Exception ex) when (ex is not DomainException)` prevents swallowing
- [ ] RFC 7807 compliance — `application/problem+json` with type, title, status, detail
- [ ] TraceId propagation — every error response includes correlation ID
- [ ] No catch-all silencing — no empty `catch { }` blocks hiding failures

## Middleware Pipeline

- [ ] ForwardedHeaders FIRST — before any IP-dependent middleware
- [ ] Rate limiting EARLY — before auth to protect against brute force
- [ ] Auth middleware BEFORE routing — no unauthenticated access to protected routes
- [ ] Exception handler WRAPS all — catches errors from every layer
- [ ] CORS properly configured — no wildcard origins in production

## Cryptography & Secrets

- [ ] No hardcoded secrets — API keys, passwords, connection strings from config/vault
- [ ] No test credentials — no fallback/default passwords in production code
- [ ] Secure comparison — timing-safe comparison for tokens/secrets
- [ ] Key rotation — secrets can be rotated without code changes

---

## Python Settings & Credentials (E2E test projects)

- [ ] `.env` in `.gitignore` — real credentials never committed to git
- [ ] `.env.example` committed — sanitized template with placeholder values only
- [ ] `SecretStr` for passwords — `pydantic.SecretStr` used for all password fields in `Settings`
- [ ] `.get_secret_value()` point-of-use only — never logged, never stored in plain-text variables
- [ ] No `os.getenv()` calls — all env access goes through `Settings` object via `get_settings()`
- [ ] No `load_dotenv()` calls — `pydantic-settings` handles `.env` loading internally
- [ ] `DOTENV_PATH` override — CI/CD can point to alternate `.env` files
- [ ] Jupyter notebooks clean — `.ipynb` files contain no credentials, tokens, or API responses with PII
- [ ] `lru_cache` documented — `@lru_cache` on `get_settings()` means config is read-once per process

## Python Test Infrastructure Security

- [ ] JWT fixtures session-scoped — `scope="session"` to avoid excessive token generation
- [ ] Token cache thread-safe — `threading.Lock()` protects `_token_cache` in `KeycloakAuthClient`
- [ ] Token expiry buffer — cached tokens refreshed 30s before expiry (not at expiry)
- [ ] `verify=False` documented — TLS disabled only for dev Keycloak self-signed certs, with inline comment
- [ ] `verify=False` scoped — only affects Keycloak `httpx.post()` calls, not Playwright API contexts
- [ ] Playwright contexts disposed — `APIRequestContext.dispose()` and `BrowserContext.close()` in teardown
- [ ] Test logs scrubbed — JWT tokens, passwords, and `X-Internal-Secret` not logged at INFO level
- [ ] Fixture creds isolated — alpha and beta tenant credentials never mixed in the same fixture

## Python Dependency Security

- [ ] `requirements.txt` pinned — exact versions (e.g., `pytest==9.0.3`), no unpinned ranges
- [ ] No `pip install` in test code — dependencies managed via `requirements.txt` only
- [ ] `playwright install` in CI — browser binaries installed in CI pipeline, not committed to git
- [ ] `schemathesis` version pinned — API fuzzing tool should not auto-update (breaking schema changes)

---

## JavaScript Client-Side Security

- [ ] Token storage — JWTs NOT in `localStorage` (XSS-accessible); prefer `httpOnly` cookies or in-memory with refresh token rotation
- [ ] `dangerouslySetInnerHTML` — every usage sanitized with DOMPurify; search for `dangerouslySetInnerHTML` across entire codebase
- [ ] `eval()` / `new Function()` — never used with user-controlled input; flagged by ESLint `no-eval` rule
- [ ] `innerHTML` / `outerHTML` — DOM manipulation without React; potential XSS if content is user-derived
- [ ] Environment variables — `NEXT_PUBLIC_*`, `VITE_*`, `REACT_APP_*` contain ONLY non-sensitive config; grep build output to verify
- [ ] Source maps — disabled in production (`devtool: false` in webpack, `productionSourceMap: false` in Vue, `build.sourcemap: false` in Vite)
- [ ] CSP headers — `Content-Security-Policy` set; no `unsafe-inline` or `unsafe-eval` unless absolutely necessary with nonces
- [ ] `X-Frame-Options` — set to `DENY` or `SAMEORIGIN` to prevent clickjacking
- [ ] Open redirect — URL parameters (`?redirect=`, `?next=`, `?returnUrl=`) validated against an allowlist of internal paths
- [ ] `window.postMessage` — origin validated in `message` event listeners; never `*` as target origin when sending
- [ ] `target="_blank"` — has `rel="noopener noreferrer"` to prevent reverse tabnapping (React 16.9+ does this automatically)
- [ ] CORS on API — `Access-Control-Allow-Origin` is NOT `*` when `credentials: true`; specific allowed origins listed

## JavaScript Dependency & Build Security

- [ ] `package-lock.json` / `yarn.lock` committed — ensures reproducible installs, prevents supply chain attacks
- [ ] `node_modules` NOT committed — in `.gitignore`
- [ ] No `postinstall` scripts from untrusted packages — audit with `npm ls --json | jq '.dependencies | to_entries[] | select(.value.scripts.postinstall)'`
- [ ] `npm audit` / `yarn audit` clean — no critical or high vulnerabilities in dependency tree
- [ ] Pinned dependency versions — no `*` or `latest` in `package.json`; use exact versions or `^` with lockfile
- [ ] No CDN-loaded scripts — all dependencies via `npm`; CDN scripts bypass integrity checks and introduce MITM risk
- [ ] Subresource Integrity (SRI) — if external resources are unavoidable, `integrity` attribute with SHA hash is present

---

## Severity Classification

| Severity | Criteria | Action |
|----------|----------|--------|
| 🚨 CRITICAL | Exploitable vulnerability, data leak, auth bypass | Block merge, fix immediately |
| 🔴 HIGH | Security weakness, missing validation, thread safety | Block merge, fix before deploy |
| 🟡 MEDIUM | Defense-in-depth gap, hardening opportunity | Fix in this PR or track as follow-up |
| 🟢 LOW | Best practice, non-exploitable improvement | Non-blocking suggestion |
