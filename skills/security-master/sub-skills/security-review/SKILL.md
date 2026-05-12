---
name: security-review
description: "Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. Provides a practical security checklist and remediation patterns. USE WHEN: implementing authentication/authorization; handling user input or file uploads. NOT FOR: deep architecture-level threat modeling across large systems; compliance legal interpretation."
origin: ECC
---

# Security Review

Apply practical security checks and remediation patterns before shipping code that touches trust boundaries.

---

## Purpose

Use this skill for implementation-time security review across auth, input handling, secret management, API surfaces, and sensitive operations.

---

## When to Activate

- implementing authentication/authorization
- handling user input or file uploads
- creating API endpoints and mutation paths
- working with secrets or credentials
- payment, financial, identity, or other sensitive workflows
- integrating third-party APIs or webhook ingestion

---

## Scope Boundaries

Use this skill for:
- security checklist-driven implementation review
- common vulnerability prevention patterns
- pre-deploy security readiness checks

Do NOT use this skill as primary source for:
- deep architecture-level threat modeling across large systems
- compliance legal interpretation
- replacing dedicated penetration testing

Delegation:
- use `securities-audit` for deep OWASP/multi-tenant audit passes
- use `coding-standards` for non-security general code quality checks

---

## Security Checklist

## 1) Secrets Management

- no hardcoded keys/tokens/passwords
- environment-based secret loading only
- fail fast when required secrets are missing
- ensure secret files are ignored and not committed

## 2) Input Validation

- validate all external input with schema-first validation
- whitelist allowed values and types
- bound length/range for user-controlled fields
- file uploads: validate size, MIME, extension

## 3) Injection Prevention

- use parameterized queries or ORM-safe query builders
- never concatenate user input into SQL/NoSQL/query filters
- validate and sanitize dynamic query operators

## 4) Authentication and Authorization

- secure token/session storage strategy
- enforce authorization before protected operations
- implement role/permission checks explicitly
- apply row-level or tenant-level access controls where relevant

## 5) XSS and Content Injection

- sanitize user-provided rich content
- avoid unsafe HTML rendering paths
- configure CSP and security headers where applicable

## 6) CSRF and Session Safety

- protect state-changing operations with CSRF strategy as needed
- enforce secure cookie attributes (`HttpOnly`, `Secure`, `SameSite`)

## 7) Rate Limiting and Abuse Controls

- baseline rate limits on public APIs
- stricter limits for expensive/sensitive endpoints
- capture abuse telemetry for investigation

## 8) Sensitive Data Exposure

- redact secrets/PII in logs
- avoid leaking internals in user-facing errors
- return generic error responses with trace correlation

## 9) Dependency Security

- monitor and remediate vulnerable dependencies
- pin versions and keep lock files committed
- run dependency audit in CI

## 10) External Integration Trust

- verify signatures for inbound webhooks/events
- validate outbound URLs to reduce SSRF risk
- apply timeout/retry/circuit controls on third-party calls

---

## Security Testing Baseline

Include tests for:
- auth required on protected routes
- authorization denial for insufficient roles
- invalid input rejection
- rate limiting behavior
- error payload hygiene (no secret leakage)

---

## Pre-Deployment Gate

Before production release:

- [ ] secrets handling verified
- [ ] input validation coverage in place
- [ ] authz checks verified for sensitive actions
- [ ] rate limiting configured
- [ ] secure headers/cookie settings reviewed
- [ ] dependency audit passed or accepted exceptions documented
- [ ] logs/errors do not leak sensitive details

---

## Hard Bans

Do not ship:
- hardcoded secrets
- unauthenticated sensitive endpoints
- raw stack traces in client responses
- unsanitized user HTML rendering
- direct string concatenation in database queries

---

## Output Contract

When activated, return:

1. security risk summary by severity
2. checklist results (pass/fail)
3. concrete remediation actions
4. residual risks and compensating controls
5. deployment readiness status
