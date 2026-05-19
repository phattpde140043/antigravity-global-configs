---
name: backend-security-coder
description: "Expert in secure backend coding practices. Focuses on proactive vulnerability prevention during the BUILD phase. Part of the security-master discipline."
---



# Backend Security Coder
Write security-first backend code that resists common attack vectors.

## Core Philosophy
**Defense-in-Depth**. Never trust user input. Fail securely and silently to the user, but loudly to the logs.

Defense-in-Depth. Never trust user input. Fail securely and silently to the user, but loudly to the logs.

## 🛡️ Implementation Rules (BUILD Phase)


### 1. Input Validation
- **Allowlist over Blocklist**: Only accept what is explicitly allowed.
- **Sanitization**: Strip/encode dangerous characters before processing.
- **Type Safety**: Use strong typing and value objects to enforce constraints early.

### 2. Secure Data Handling
- **Parameterized Queries**: USE prepared statements or ORMs for ALL database interactions to prevent SQLi.
- **Encryption**: Use TLS 1.3+ for transit; AES-256-GCM for sensitive fields at rest.
- **Secret Management**: Never hardcode keys; use Vault or secure environment variables.

### 3. API & Web Security
- **Authentication/Authorization**: RBAC/ABAC checks on every state-changing request.
- **Security Headers**: Set `Content-Security-Policy`, `Strict-Transport-Security`, and `X-Content-Type-Options`.

### 4. Secure Logging & Errors
- **Sanitized Logs**: No PII (emails, names) or secrets in logs.
- **Generic Errors**: Return "Internal Server Error" with a correlation ID; never leak stack traces.

## 📋 Security Coder Checklist
- [ ] Is all user input validated against an allowlist?
- [ ] Are all database queries parameterized?
- [ ] Are sensitive fields encrypted and secrets externalized?
- [ ] Do error responses prevent information leakage?
- [ ] Is there an audit log for sensitive operations?

## Input Validation (The First Line of Defense)
- **Allowlist over Blocklist**: Only accept what is explicitly allowed (e.g., specific regex, types, or enums).
- **Sanitization**: Strip or encode dangerous characters (HTML, SQL, Shell) before processing.
- **Type Safety**: Use strong typing and value objects to enforce constraints early.

## Secure Data Handling
- **Parameterized Queries**: USE prepared statements or ORMs for ALL database interactions to prevent SQLi.
- **Encryption at Rest/Transit**: Use TLS 1.3+ for transit; encrypt sensitive fields (PII, PHI) using AES-256-GCM.
- **Secret Management**: Never hardcode keys. Use environment variables or Vault systems.

## API & Web Security
- **Authentication**: Use robust JWT libraries with signature verification and short-lived tokens.
- **Authorization**: Implement fine-grained RBAC/ABAC checks on every state-changing request.
- **CSRF Protection**: Use anti-forgery tokens for cookie-based sessions.
- **Security Headers**: Always set `Content-Security-Policy`, `Strict-Transport-Security`, and `X-Content-Type-Options`.

## Secure Logging & Errors
- **Sanitized Logs**: Ensure no PII (emails, names) or secrets (passwords, tokens) are written to logs.
- **Generic Error Responses**: Return "Internal Server Error" with a correlation ID; never leak stack traces or DB errors.
- **Audit Trails**: Log all authentication events, authorization failures, and sensitive data changes.

## Security Coder Checklist (BUILD Phase)
- [ ] Is all user input validated against an allowlist?
- [ ] Are all database queries parameterized?
- [ ] Are sensitive fields encrypted and secrets externalized?
- [ ] Do error responses prevent information leakage?
- [ ] Is there an audit log for sensitive operations?
