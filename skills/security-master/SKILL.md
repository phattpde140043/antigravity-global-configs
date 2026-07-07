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


### 1. Threat Modeling & Security Design (DESIGN Phase)
- **[Securities Audit (STRIDE)](sub-skills/securities-audit/SKILL.md)** — STRIDE threat modeling, blast-radius analysis, and security-control validation. **Use when:** enumerating and prioritizing attack vectors across trust boundaries during design. **Not for:** writing or remediating application code.
- **[Security Architecture & Design](sub-skills/security-design/SKILL.md)** — security architecture design, STRIDE modeling, and security-requirement extraction. **Use when:** in DEFINE/PLAN phases deriving user stories, security requirements, and boundary analysis before build. **Not for:** post-build code fixes or live exploitation.
- **[Security Auditor](sub-skills/security-auditor/SKILL.md)** — security-engineer review spanning vulnerability detection, threat modeling, and secure-coding practice. **Use when:** performing security-focused code review, threat analysis, or hardening recommendations on existing code.

### 2. Secure Coding & Hardening (BUILD Phase)
- **[Backend Security Coder](sub-skills/backend-security-coder/SKILL.md)** — secure backend coding and data-handling practices for proactive vulnerability prevention. **Use when:** writing or reviewing backend/service code during the BUILD phase.
- **[Security & Hardening](sub-skills/security-and-hardening/SKILL.md)** — hardens code against vulnerabilities at the point of input and integration. **Use when:** handling untrusted user input, authentication, data storage, sessions, or third-party integrations.
- **[Broken Authentication Remediation](sub-skills/broken-authentication/SKILL.md)** — identifies and fixes authentication and session-management weaknesses. **Use when:** addressing session hijacking, credential stuffing, insecure cookies, or OAuth vulnerabilities.
- **[Security Review (Checklist)](sub-skills/security-review/SKILL.md)** — practical security checklist and remediation patterns for common features. **Use when:** adding auth/authorization, handling user input or file uploads, managing secrets, or building API/payment endpoints. **Not for:** deep architecture-level threat modeling across large systems, or compliance/legal interpretation.
- **[Security Checklists](sub-skills/security-checklists/SKILL.md)** — quick-reference audit checklists for OWASP Top 10:2025, authentication, API, and data protection. **Use when:** you need a fast go/no-go list to verify defensive controls during a review. **Not for:** offensive testing or tool execution.
- **[Solidity Security](sub-skills/solidity-security/SKILL.md)** — secure Solidity development patterns and EVM smart-contract vulnerability prevention. **Use when:** writing or auditing smart contracts for reentrancy, access-control, and other on-chain flaws.

### 3. SAST & Static Analysis
- **[SAST Engineering](sub-skills/sast-engineering/SKILL.md)** — authors custom Semgrep rules to detect vulnerabilities and dangerous patterns. **Use when:** creating detection rules to enforce security standards in the pipeline.
- **[SAST Configuration](sub-skills/sast-configuration/SKILL.md)** — sets up and tunes SAST tooling and custom rules across languages. **Use when:** configuring Semgrep/SonarQube/security linters or filtering scan findings.
- **[Variant Analysis](sub-skills/variant-analysis/SKILL.md)** — pattern-based hunting for similar vulnerabilities across a codebase using CodeQL/Semgrep. **Use when:** you have an initial finding and need to track its variants across large repositories, or run systematic semantic audits.

### 4. Offensive Security & Penetration Testing (Authorized Testing)
- **[Penetration Testing Methodology](sub-skills/penetration-testing/SKILL.md)** — end-to-end ethical-hacking methodology covering recon, scanning, exploitation, maintaining access, and reporting. **Use when:** planning or running a full authorized security assessment.
- **[Offensive Security (Web)](sub-skills/offensive-security/SKILL.md)** — authorized offensive web testing focused on XSS, HTML injection, SQLi, and filter-bypass techniques. **Use when:** actively probing web input handling for injection/XSS during an authorized assessment.
- **[Pentest Checklist](sub-skills/pentest-checklist/SKILL.md)** — structured checklist for scoping, executing, and following up on penetration tests. **Use when:** defining engagement scope and ensuring remediation coverage. **Not for:** ad-hoc tool command lookup (see Pentest Commands).
- **[Pentest Commands](sub-skills/pentest-commands/SKILL.md)** — command reference for scanning, exploitation, password cracking, and web-testing tools. **Use when:** you need quick tool-command lookup (Nmap, Metasploit, hydra) mid-assessment.
- **[Scanning Tools](sub-skills/scanning-tools/SKILL.md)** — selection and usage of network, vulnerability, web, and wireless scanners. **Use when:** performing active host discovery or vulnerability scanning (Nmap, Nikto, OWASP ZAP) and choosing the right scanner.
- **[Red Team Tactics](sub-skills/red-team-tactics/SKILL.md)** — MITRE ATT&CK-based attack phases, detection evasion, and reporting. **Use when:** planning lateral movement, evasion, or Active Directory compromise in an authorized red-team engagement.
- **[Red Team Tools](sub-skills/red-team-tools/SKILL.md)** — tool workflows for recon, vulnerability discovery, and post-exploitation/C2. **Use when:** setting up command-and-control, compiling payloads, or automating attack-surface coverage in an authorized engagement.
- **[Burp Suite Testing](sub-skills/burp-suite-testing/SKILL.md)** — web-app testing with Burp Suite (intercepting proxy, repeater, intruder, active scans). **Use when:** intercepting/modifying HTTP traffic and running manual or automated web scans.
- **[Burpsuite Project Parser](sub-skills/burpsuite-project-parser/SKILL.md)** — searches and extracts data from Burp `.burp` project files via the command line. **Use when:** regex-searching captured requests/responses, dumping proxy history or site map, or automating findings extraction from a Burp project.
- **[SQL Injection Testing](sub-skills/sql-injection-testing/SKILL.md)** — manual SQL injection assessment: payload crafting, bypass techniques, and validation. **Use when:** manually testing and validating SQLi and input-sanitization on web apps.
- **[SQLmap Database Pentesting](sub-skills/sqlmap-database-pentesting/SKILL.md)** — automated SQLi detection and exploitation with SQLMap. **Use when:** automating DBMS takeover, data extraction, or hash cracking via sqlmap parameters.
- **[SSH Penetration Testing](sub-skills/ssh-penetration-testing/SKILL.md)** — SSH service assessment: enumeration, credential attacks, tunneling, and post-exploitation. **Use when:** auditing SSH for weak ciphers, key leakage, or brute-forceable credentials.
- **[AWS Penetration Testing](sub-skills/aws-penetration-testing/SKILL.md)** — offensive AWS testing: IAM enumeration, privilege escalation, SSRF-to-metadata, S3/Lambda exploitation, and persistence. **Use when:** running an authorized red-team assessment against an AWS environment. **Not for:** defensive AWS hardening (see Infrastructure Security).

### 5. Reverse Engineering & Binary Analysis
- **[Reverse Engineering](sub-skills/reverse-engineer/SKILL.md)** — binary analysis, disassembly, and decompilation with IDA Pro, Ghidra, radare2, and x64dbg. **Use when:** reversing ELF/PE binaries, running Ghidra pipelines, or patching/analyzing compiled code.
- **[Binary Analysis Patterns](sub-skills/binary-analysis-patterns/SKILL.md)** — patterns for analyzing compiled binaries, reading assembly, and reconstructing program logic. **Use when:** instrumenting binaries or working through buffer-overflow/shellcode exploitation (GDB, Ghidra, radare2).
- **[Anti-Reversing Techniques](sub-skills/anti-reversing-techniques/SKILL.md)** — dual-use anti-debugging and obfuscation analysis/bypass techniques. **Use when:** conducting in-scope malware analysis, CTFs, or authorized pentests that must understand or defeat protections. **Not for:** bypassing protections without written authorization or for piracy.

### 6. Cloud & Infrastructure
- **[Infrastructure Security Reference](sub-skills/infrastructure-security/SKILL.md)** — defensive cloud reference for AWS compliance (CIS/PCI-DSS/HIPAA), IAM hardening, and secrets/supply-chain (SCA) management. **Use when:** auditing or hardening cloud identity, configuration, and dependencies. **Not for:** offensive cloud exploitation (see AWS Penetration Testing).

### 7. Compliance & Governance
- **[PCI Compliance](sub-skills/pci-compliance/SKILL.md)** — PCI DSS controls for payment processing and cardholder-data protection. **Use when:** designing or auditing cardholder-data handling, network segmentation, and PCI DSS compliance.
- **[Regulatory Compliance](sub-skills/regulatory-compliance/SKILL.md)** — business-logic controls and checklists for GDPR, HIPAA, and PCI-DSS. **Use when:** designing privacy controls, audit trails, or healthcare/payment data-handling requirements.
- **[AKF Trust Metadata](sub-skills/akf-trust-metadata/SKILL.md)** — AI-native file format stamping trust scores, source provenance, and compliance metadata into 20+ formats. **Use when:** you need file-level provenance and trust auditing for EU AI Act, SOX, or HIPAA.

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
