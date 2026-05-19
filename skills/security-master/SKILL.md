---
name: security-master
description: "Master Security Orchestrator. Coordinates Threat Modeling, Secure Coding, Pentesting, and Cloud Hardening through specialized sub-disciplines."
metadata:
  category: master-orchestrator
  triggers: security-audit, vulnerability-scan, threat-modeling, secure-coding
---

# 🛡️ Security Master Orchestrator

The central authority and dispatcher for all security-related activities. This master skill orchestrates deep-dive specialized sub-disciplines to ensure full-stack security.

---

## 🧭 High-Level Strategy
- **Defense-in-Depth**: Layered security across Design, Code, and Infrastructure.
- **Threat Modeling**: Master **STRIDE** and **Attack Tree Construction** to visualize and prioritize attack vectors.
- **API Security Mastery**: Implement dedicated **API Security Testing** (OWASP API Top 10) for all service-to-service interactions.
- **Fail-Closed**: Default system state is always secure/denied.
- **Audit-Ready**: Every change must produce a security assessment report.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing specific security tasks, you **MUST** chain to the following sub-skills for deep expertise. Navigate the sub-skills in the sequential order defined below to ensure structured secure implementation:

### 🔄 Sequential Sub-Skill Pipeline
```
[Securities Audit (STRIDE)] ──→ [Security Architecture & Design] ──→ [SAST Engineering] ──→ [Backend Security Coder] ──→ [Security Review]
```


### 1. Strategy & Threat Modeling (DESIGN Phase)
- For **STRIDE** and Risk Assessment: 
  👉 **[Securities Audit (Tier 2)](sub-skills/securities-audit/SKILL.md)**
- For **User Stories** and Boundary Analysis: 
  👉 **[Security Architecture & Design](sub-skills/security-design/SKILL.md)**

### 2. Secure Coding & Implementation (BUILD Phase)
- For **SAST Rules** and Semgrep Detections:
  👉 **[SAST Engineering](sub-skills/sast-engineering/SKILL.md)**
- For **Backend Security** and Data Handling: 
  👉 **[Backend Security Coder](sub-skills/backend-security-coder/SKILL.md)**
- For **Review Checklists** and Injection prevention: 
  👉 **[Security Review (Checklist)](sub-skills/security-review/SKILL.md)**
- For **Broken Authentication Remediation** (session hijacking, credential stuffing, secure cookies, OAuth vulnerabilities):
  👉 **[Broken Authentication Remediation](sub-skills/broken-authentication/SKILL.md)**
- For **Static Application Security Testing (SAST) Rule Configuration** (Semgrep rules, security linters, SonarQube filters):
  👉 **[SAST Configuration](sub-skills/sast-configuration/SKILL.md)**
- For **PCI DSS Payment Security Compliance** (cardholder data protection, network hardening, PCI compliance audits):
  👉 **[PCI Compliance](sub-skills/pci-compliance/SKILL.md)**

### 3. Offensive Security & Pentesting
- For **Scanning, Exploitation, and Hardening**: 
  👉 **[Penetration Testing Methodology](sub-skills/penetration-testing/SKILL.md)**
- For **Reverse Engineering, Anti-Debugging, and Obfuscation**:
  👉 **[Anti-Reversing Techniques](sub-skills/anti-reversing-techniques/SKILL.md)**
- For **Binary Analysis, Instrumentation, and Buffer Overflow Exploitation** (GDB, Ghidra, radare2, shellcode):
  👉 **[Binary Analysis Patterns](sub-skills/binary-analysis-patterns/SKILL.md)**
- For **AWS Cloud Penetration Testing & Privilege Escalation** (IAM enum, SSRF to metadata, Lambda code extraction):
  👉 **[AWS Penetration Testing](sub-skills/aws-penetration-testing/SKILL.md)**
- For **Offensive Security Vulnerability Scanners** (Nmap, Nikto, OWASP ZAP, active host discovery):
  👉 **[Scanning Tools](sub-skills/scanning-tools/SKILL.md)**
- For **Burp Suite Professional Web Penetration Testing** (intercepting proxy, intruder, repeater, active scans):
  👉 **[Burp Suite Testing](sub-skills/burp-suite-testing/SKILL.md)**
- For **Burp Suite Project XML Parsing & Remediation** (vulnerability parsing, reporting automation):
  👉 **[Burpsuite Project Parser](sub-skills/burpsuite-project-parser/SKILL.md)**
- For **Penetration Testing Standard Checklists** (systematic security assessment checklists, scoping protocols):
  👉 **[Pentest Checklist](sub-skills/pentest-checklist/SKILL.md)**
- For **Offensive Pentesting CLI Commands Cheatsheet** (Nmap, Metasploit, hydra command cheatsheets):
  👉 **[Pentest Commands](sub-skills/pentest-commands/SKILL.md)**
- For **EVM Smart Contract Security Audits** (Solidity vulnerability patterns, reentrancy attacks, access control checks):
  👉 **[Solidity Security](sub-skills/solidity-security/SKILL.md)**
- For **SQL Injection (SQLi) Vulnerability Testing** (payloads formulation, bypass techniques, manual validation):
  👉 **[SQL Injection Testing](sub-skills/sql-injection-testing/SKILL.md)**
- For **SQLmap Automated Database Penetesting** (sqlmap command parameters, DBMS takeover, hash cracking):
  👉 **[SQLmap Database Pentesting](sub-skills/sqlmap-database-pentesting/SKILL.md)**
- For **SSH Protocol Penetration Testing & Auditing** (SSH keys leakage, weak ciphers checking, brute-force validation):
  👉 **[SSH Penetration Testing](sub-skills/ssh-penetration-testing/SKILL.md)**
- For **Red Team Tactical Engagements** (lateral movement, network evasion, active directories compromise):
  👉 **[Red Team Tactics](sub-skills/red-team-tactics/SKILL.md)**
- For **Red Team Exploitation Tools & C2** (command and control setup, payload compilation, post-exploitation scripts):
  👉 **[Red Team Tools](sub-skills/red-team-tools/SKILL.md)**
- For **Binary Reverse Engineering** (binary disassemblers, Ghidra pipelines, ELF/PE header analysis, stack patching):
  👉 **[Reverse Engineering](sub-skills/reverse-engineer/SKILL.md)**
- For **CodeQL Variant Audits & Analyses** (writing custom semantic queries, variant tracking across large repositories):
  👉 **[Variant Analysis](sub-skills/variant-analysis/SKILL.md)**

### 4. Cloud & Infrastructure
- For **AWS Hardening** and **SCA (Supply Chain)**: 
  👉 **[Infrastructure Security Reference](sub-skills/infrastructure-security/SKILL.md)**

### 5. Compliance & Governance
- For **Regulatory Compliance** (GDPR, SOC2, HIPAA, etc.):
  👉 **[Regulatory Compliance](sub-skills/regulatory-compliance/SKILL.md)**
- For **AI File Provenance & Trust Auditing** (AKF native file metadata, EU AI Act, SOX):
  👉 **[AKF Trust Metadata](sub-skills/akf-trust-metadata/SKILL.md)**

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of the threat modeling and security architecture review:
- 👉 Recommend calling **[Senior QA](../senior-qa/SKILL.md)** next to translate the identified security boundaries and abuse cases into targeted regression and security unit/integration test cases (TDD).

---

## 🛡️ Coordination Protocol (V8 Framework)
This Orchestrator follows the **[Agent Review Framework](file:///Users/macos/.antigravity-global/agent_review_framework.md)**.
- **Step 1**: Context Discovery (Phase 0).
- **Step 2**: Trigger the relevant Sub-Discipline Chain.
- **Step 3**: Consolidate findings into a Master Security Assessment.

---

## 📋 Master Security Checklist
- [ ] Has the relevant Sub-Discipline been chained?
- [ ] Is there a STRIDE analysis for the Trust Boundaries?
- [ ] Are all "Hard Bans" (Hardcoded secrets, etc.) verified?
- [ ] Is the infrastructure/dependency audit passed?
