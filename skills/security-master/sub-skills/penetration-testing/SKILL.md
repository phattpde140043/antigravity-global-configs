---
name: penetration-testing
description: "Ethical hacking methodology for security assessments. Covers Reconnaissance, Scanning, Exploitation, Maintaining Access, and Reporting."
---

# Penetration Testing Methodology

Assess system security by simulating real-world attacks. Always require written authorization.

## 1. Reconnaissance (Passive & Active)
Gather target information without direct interaction where possible.
- **WHOIS/DNS**: `whois domain.com`, `dig domain.com ANY`.
- **Google Dorks**: `site:domain.com filetype:config`, `site:domain.com inurl:admin`.
- **OSINT**: theHarvester, Shodan.

## 2. Scanning (Enumeration)
Active enumeration of services and ports.
- **Nmap**:
  - Stealth TCP: `nmap -sS target`
  - Version Detection: `nmap -sV target`
  - Vuln Scan: `nmap --script=vuln target`
- **Port Reference**: 22 (SSH), 445 (SMB), 3306 (MySQL), 3389 (RDP), 5432 (PostgreSQL).

## 3. Vulnerability Analysis
Validate scanning results and identify entry points.
- **Web Scanning**: `nikto -h http://target`, `gobuster dir -u http://target -w wordlist.txt`.
- **Logic Analysis**: Mapping trust boundaries and state machine bypasses.

## 4. Exploitation (Authorized Only)
Gain access to verify the vulnerability.
- **Metasploit (MSF)**:
  - `msfconsole` -> `search type:exploit name:service`.
  - `use exploit/...`, `set RHOSTS ...`, `set PAYLOAD ...`, `exploit`.
- **SQL Injection**: `sqlmap -u "http://target/page?id=1" --dbs --batch`.
- **Brute Force**: `hydra -l admin -P wordlist.txt ssh://target`.

## 5. Maintaining Access & Pivoting
- **Persistence**: Meterpreter, SSH authorized keys, Cron jobs.
- **Pivoting**: Using a compromised host to access internal network segments.

## 6. Professional Reporting
Deliver actionable findings to stakeholders.
- **Executive Summary**: High-level risk and business impact.
- **Technical Detail**: Reproduceable steps (POC), severity, and remediation steps.
- **Classification**: CRITICAL (Data leak), HIGH (Injection), MEDIUM (DoS), INFO.

## Ethical Boundaries
- Never test without written permission.
- Stay within the defined scope.
- Report unauthorized access attempts immediately.
- Clean up all test files and backdoors before concluding.
