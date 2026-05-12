# API Security & Testing (Diamond Standard)

## 🛡️ API Security Best Practices
- **JWT Hardening**:
    - Use `RS256` (Asymmetric) instead of `HS256`.
    - Short-lived tokens (Access Token < 1h) + Long-lived Refresh Tokens.
    - Validate `iss` (issuer), `aud` (audience), and `exp` (expiration).
- **Rate Limiting**: Implement by User ID and IP to prevent Brute-force & DoS attacks.
- **Input Sanitization**: Use Schema Validation (Zod, FluentValidation) to block Injections at the API gateway.
- **Secure Headers**: Configure `Helmet.js`, `HSTS`, and `Content-Security-Policy`.
- **Secrets Management**: 
    - Absolutely NO hardcoding of API keys or DB passwords.
    - Use Environment Variables or Secret Managers (AWS Secrets Manager, HashiCorp Vault).
    - Periodically scan the codebase for leaked secrets (GitGuardian, TruffleHog).
- **CSRF & XSS Protection**:
    - Use `HttpOnly` and `SameSite=Strict` for cookies.
    - Sanitize all input HTML data (DOMPurify).
    - Implement CSRF Tokens for state-changing operations.
- **Row Level Security (RLS)**: Enforce authorization at the Database layer to prevent cross-user/tenant data access.

## 🔍 API Security Testing
- **Fuzzing**: Test with garbage data, massive payloads, or special characters to find crashes or logic flaws.
- **OWASP API Top 10**: Focus on:
    - **BOLA** (Broken Object Level Authorization): Accessing others' resources via ID.
    - **BFLA** (Broken Function Level Authorization): Calling admin APIs with a regular account.
    - **Mass Assignment**: Updating unauthorized fields (e.g., `isAdmin: true`).
- **Bug Bounty Mindset**: Always test scenarios like:
    - "If I change the ID in the URL, can I see someone else's data?"
    - "If I send an array instead of a string, does the system fail?"

## 🧪 API Observability
- **Distributed Tracing**: Attach `X-Correlation-ID` throughout services.
- **Anomaly Detection**: Monitor for unusual traffic patterns (e.g., 1000 401 errors in 1 minute).


---

## 🔗 Related References
- **[OWASP Guide](owasp-guide.md)**
- **[Secrets Infrastructure](secrets-infrastructure.md)**
- **[Threat Modeling](threat-modeling.md)**
