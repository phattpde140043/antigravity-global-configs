---
name: securities-audit
description: "Expert security auditor. Performs STRIDE threat modeling, blast radius analysis, and validates security controls."
---

# Securities Audit (Tier 2)

Proactive security validation and threat-centric auditing. Ensure systems are secure-by-design and resilient against modern attack vectors.

## ⚡ Quick References (MANDATORY)
- **[OWASP Guide](references/owasp-guide.md)**: Check for the Top 10 most common vulnerabilities.
- **[API Security](references/api-security.md)**: JWT security, Rate Limiting, and Fuzz Testing.
- **[Threat Modeling](references/threat-modeling.md)**: STRIDE, PASTA, and Risk Scoring analysis.
- **[Memory Security](references/memory-security.md)**: Zeroization rules and RAM data security.
- **[Secrets Infrastructure](references/secrets-infrastructure.md)**: Vault, Cloud Managers, and CI/CD secret safety.
- **[External Audit](references/commitshow-audit.md)**: commit.show post-deployment audit tool.
- **[Multi-Tenant Safety](references/multi-tenant-safety.md)**: Golden rules for customer data isolation.
- **[SAST Patterns](references/sast-patterns.md)**: Security violation code patterns (SQLi, XSS, SSRF).

---

## 🛡️ Audit Workflow

### 1. Discovery & Triage
- Identify entry points and data flow trust boundaries.
- Perform **Mini-STRIDE** for rapid threat identification.

### 2. Deep Dive Analysis
- Verify authentication and authorization (BOLA/BFLA).
- Audit secrets management and sensitive data handling.
- Review resilience patterns (Retry/Circuit Breaker) for security impact.

### 3. Mitigation & Verification
- Propose detective, preventive, and corrective controls.
- Generate security assessment reports in `docs/assessment/`.