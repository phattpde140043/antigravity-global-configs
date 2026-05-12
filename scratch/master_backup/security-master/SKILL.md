---
name: security-master
description: "Master Discipline for Security. Covers STRIDE Threat Modeling, Secure Coding (BUILD), Vulnerability Audit (REVIEW), Pentesting (OFFENSIVE), and Infrastructure/Cloud Hardening."
metadata:
  category: discipline
  triggers: security-audit, vulnerability-scan, threat-modeling, secure-coding
risk: safe
source: consolidated
date_added: "2026-05-12"
---

# 🛡️ Security Master Discipline

The central authority for ensuring architectural integrity, data safety, and resilience against adversarial threats. Follows the **Agent Review Framework**.

---

## 🏗️ PART 1: STRATEGY & DESIGN (STRIDE)

Build security into the system from the start rather than bolting it on later.

### 1. Threat Modeling (STRIDE)
| Category | Security Property | Definition |
| :--- | :--- | :--- |
| **S**poofing | Authenticity | Pretending to be something/someone else. |
| **T**ampering | Integrity | Modifying data or code. |
| **R**epudiation | Non-repudiability | Claiming you didn't do something. |
| **I**nformation Disclosure | Confidentiality | Exposing data to unauthorized parties. |
| **D**enial of Service | Availability | Exhausting resources to crash the system. |
| **E**levation of Privilege | Authorization | Gaining higher access than intended. |

### 2. Trust Boundary Analysis (TBA)
1. **Identify Assets**: What are we protecting? (e.g., User PII, API Keys, Tenant Data).
2. **Define Boundaries**: Where does trust change? (e.g., Browser to API, API to Database).
3. **Map Threats**: Apply STRIDE to each boundary.
4. **Write Requirements**: Convert mitigations into "Must-have" features.

### 3. Security User Stories
- **As a** system administrator, **I want** all administrative actions logged, **so that** we have a non-repudiable audit trail for compliance.
- **As a** user, **I want** my data encrypted at rest, **so that** it remains confidential even if the physical storage is compromised.

---

## 🏗️ PART 2: SECURE CODING (BACKEND)

### 1. Input Validation (The First Line of Defense)
- **Allowlist over Blocklist**: Only accept what is explicitly allowed.
- **Sanitization**: Strip or encode dangerous characters (HTML, SQL, Shell).
- **Type Safety**: Use strong typing and value objects.

### 2. Secure Data Handling
- **Parameterized Queries**: USE prepared statements for ALL database interactions.
- **Encryption**: TLS 1.3+ for transit; AES-256-GCM for sensitive fields at rest.
- **Secret Management**: Never hardcode keys. Use environment variables or Vault.

### 3. API & Web Security
- **Authentication**: Robust JWT libraries with signature verification.
- **Authorization**: Fine-grained RBAC/ABAC on every request.
- **CSRF Protection**: Anti-forgery tokens for cookie-based sessions.
- **Security Headers**: CSP, HSTS, X-Content-Type-Options.

### 4. External Integration Trust
- **Webhooks**: ALWAYS verify signatures of inbound payloads.
- **SSRF**: Validate and allowlist all outbound URLs.

---

## 🏗️ PART 3: VULNERABILITY AUDIT (REVIEW)

### 1. Severity Classification
| Severity | Criteria | Action |
|----------|----------|--------|
| **Critical** | Exploitable remotely, leads to data breach | Fix immediately |
| **High** | Significant data exposure | Fix before release |
| **Medium** | Limited impact, requires auth | Fix in current sprint |
| **Low** | Theoretical risk | Schedule for next sprint |

### 2. Audit Report Format
```markdown
## Security Audit Report
### Summary
- Critical: [count] | High: [count] | Medium: [count] | Low: [count]
### Findings
#### [CRITICAL] [Finding title]
- **Location:** [file:line]
- **Description:** [What the vulnerability is]
- **Impact:** [What an attacker could do]
- **Proof of concept:** [How to exploit it]
- **Recommendation:** [Specific fix with code example]
```

### 3. Secure Logging & Errors
- **Sanitized Logs**: No PII (emails, names) or secrets (passwords, tokens).
- **Generic Error Responses**: Return "Internal Server Error" with correlation ID.

---

## 🏗️ PART 4: PENETRATION TESTING (OFFENSIVE)

### 1. Reconnaissance & Scanning
- **Nmap**: Stealth TCP: `nmap -sS <target>` | Version: `nmap -sV <target>`
- **Web Scanning**: `nikto -h http://target` | `gobuster dir -u http://target -w wordlist.txt`

### 2. Exploitation (Authorized Only)
- **SQL Injection**: `sqlmap -u "http://target/page?id=1" --dbs --batch`
- **Brute Force**: `hydra -l admin -P wordlist.txt ssh://target`
- **Metasploit**: `msfconsole` -> `search type:exploit name:service`.

---

## 🏗️ PART 5: INFRASTRUCTURE SECURITY

### 1. AWS Audit CLI
- `aws iam get-credential-report`
- `aws iam get-account-summary`
- `aws ec2 describe-security-groups --filters Name=ip-permission.cidr,Values='0.0.0.0/0'`
- `aws secretsmanager rotate-secret --secret-id <id>`

### 2. Supply Chain Security (SCA)
- **NPM**: `npm audit`
- **Python**: `pip-audit` or `safety check`.
- **Go**: `govulncheck ./...`.
- **SBOM**: Maintain CycloneDX/SPDX manifests using `trivy` or `syft`.

---

## 📋 SECURITY CHECKLIST (MANDATORY)
- [ ] Secrets handling verified (no hardcoded keys).
- [ ] Input validation coverage (Schema-first).
- [ ] Authz checks verified for sensitive actions (Multi-tenancy).
- [ ] Rate limiting configured.
- [ ] Secure headers/cookie settings reviewed.
- [ ] Logs/errors do not leak sensitive details.

---

## 📚 REFERENCES
- **[OWASP Top 10](references/owasp-guide.md)**, **[Threat Modeling](references/threat-modeling.md)**, **[Multi-Tenant Safety](references/multi-tenant-safety.md)**, **[API Security](references/api-security.md)**, **[Secrets Infrastructure](references/secrets-infrastructure.md)**, **[SAST Patterns](references/sast-patterns.md)**, **[Memory Security](references/memory-security.md)**.
