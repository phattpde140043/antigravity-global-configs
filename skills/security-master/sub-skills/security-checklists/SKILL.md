---
name: security-checklists
description: "Quick reference checklists for security audits. Covers OWASP Top 10:2025, Authentication, API, and Data Protection."
---

# Security Audit Checklists

Use these checklists during PLAN, BUILD, and REVIEW phases to ensure comprehensive coverage.

## 1. OWASP Top 10:2025 Audit
- **A01: Broken Access Control** (IDOR, SSRF, missing authz).
- **A02: Security Misconfiguration** (Default credentials, exposed debug, cloud configs).
- **A03: Software Supply Chain** (Insecure dependencies, CI/CD pipeline integrity).
- **A04: Cryptographic Failures** (Weak crypto, hardcoded secrets, plain-text PII).
- **A05: Injection** (SQLi, XSS, Path Traversal, Command Injection).
- **A06: Insecure Design** (No threat modeling, flawed business logic).
- **A07: Authentication Failures** (Weak password policy, missing MFA, session issues).
- **A08: Integrity Failures** (Unsigned updates, tampered data).
- **A09: Logging & Alerting Failures** (Missing audit trails, delayed breach detection).
- **A10: Exceptional Conditions** (Fail-open on errors, unhandled security exceptions).

## 2. API Security Checklist
- [ ] Authentication required for all endpoints.
- [ ] Per-endpoint authorization (Least Privilege).
- [ ] Row-level / Tenant-level isolation verified.
- [ ] Input validation (Schema-based).
- [ ] Rate limiting (DDoS and abuse prevention).
- [ ] Security headers (CSP, HSTS, X-Frame-Options).

## 3. Authentication Checklist
- [ ] MFA required for critical/admin actions.
- [ ] Account lockout / Brute-force protection.
- [ ] Password reset tokens single-use and time-limited.
- [ ] Secure logout (Session invalidation).
- [ ] Session tokens stored securely (HttpOnly, Secure).

## 4. Exceptional Conditions (A10)
- **Fail-Closed**: Access denied on handler errors.
- **Generic Errors**: No stack traces or internals to the user.
- **Audit Failure**: Log when security checks themselves fail.

## 5. Risk Prioritization Matrix
- **Critical**: Remote Code Execution (RCE), Global Data Breach, Auth Bypass.
- **High**: Horizontal/Vertical privilege escalation, SQL Injection.
- **Medium**: CSRF, limited data exposure, information leakage.
- **Low**: Best practice recommendations, logging improvements.

---

## 6. 360 Degree Quality Audit
- **Git Hygiene**: Clear commit messages, no merge conflicts, branch up-to-date.
- **Documentation**: API docs updated, README reflects changes, breaking changes noted.
- **Regressions**: Ensure existing critical paths are covered by automated or manual smoke tests.
- **Maintainability**: Low complexity (<15), clear naming, no code duplication.

## 7. Compliance & Data Protection
- **PCI-DSS**: No storing CVV/Track data, encryption of cardholder data at rest.
- **HIPAA/GDPR**: PHI/PII anonymized in logs, consent logic verified, right-to-be-forgotten handled.
- **Secret Scanning**: Verify no credentials in `.env`, `appsettings.json`, or hardcoded constants.
