# OWASP Top 10: Security Reference

## A01: Broken Access Control
- **Issue**: Users can access resources they shouldn't (BOLA/BFLA).
- **Prevention**: Enforce authorization at every endpoint and resource access.

## A02: Cryptographic Failures
- **Issue**: Using weak hashes (MD5, SHA1) or plain-text storage.
- **Prevention**: Use strong encryption (AES-256) and hashing (Argon2, BCrypt).

## A03: Injection
- **Issue**: SQLi, XSS, Command Injection.
- **Prevention**: Use parameterized queries, ORMs, and output encoding.

## A04: Insecure Design
- **Issue**: Flaws in the system architecture (Missing Threat Model).
- **Prevention**: Use Security-by-Design and STRIDE modeling.

## A05: Security Misconfiguration
- **Issue**: Default passwords, open ports, verbose error messages.
- **Prevention**: Hardened configurations and environment-specific settings.

## A06: Vulnerable and Outdated Components
- **Issue**: Using libraries with known CVEs.
- **Prevention**: Regular `npm audit` or `dotnet list package --vulnerable`.

## A07: Identification and Authentication Failures
- **Issue**: Weak passwords, missing MFA, session hijacking.
- **Prevention**: Strong password policies and MFA.

## A08: Software and Data Integrity Failures
- **Issue**: Insecure deserialization or unverified software updates.
- **Prevention**: Digitally sign updates and avoid untrusted data deserialization.

## A09: Security Logging and Monitoring Failures
- **Issue**: Missing logs for critical events or lack of alerting.
- **Prevention**: Implement structured logging and anomaly alerting.

## A10: Server-Side Request Forgery (SSRF)
- **Issue**: Server fetches untrusted URLs provided by users.
- **Prevention**: Use allow-lists for external domains and sanitize input.


---

## 🔗 Related References
- **[API Security](api-security.md)**
- **[SAST Patterns](sast-patterns.md)**
- **[Threat Modeling](threat-modeling.md)**
