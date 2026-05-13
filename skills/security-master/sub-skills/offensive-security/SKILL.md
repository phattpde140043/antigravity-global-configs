---
name: offensive-security
description: "Expert in offensive security testing and penetration testing. Focuses on XSS, HTML Injection, SQLi, and filter bypass techniques for authorized assessments."
---

# Offensive Security & Pentesting

Master the techniques of professional security assessment and vulnerability exploitation.

## 🚀 Offensive Techniques
- **XSS & Injection**: Exploit stored, reflected, and DOM-based vectors. Bypass WAFs using encoding/obfuscation.
- **Network Forensics (Wireshark)**:
    - **Capture & Filter**: Use display filters to isolate suspicious traffic (e.g., `tcp.flags.syn == 1`).
    - **Malware Analysis**: Identify Command & Control (C2) beaconing and unusual DNS queries.
    - **Stream Reconstruction**: Follow TCP/HTTP streams to exfiltrate plaintext credentials.
- **Windows Privilege Escalation**: Identify misconfigured services, vulnerable kernel drivers, and weak file permissions to gain System access.

## 🏗️ Attack Vectors
- **Stored XSS**: Identify inputs that persist (Comments, Profiles) to target other users.
- **Reflected XSS**: Find parameters reflected in responses (Search, Errors) for phishing/session hijacking.
- **DOM-Based XSS**: Analyze client-side scripts that process user-controlled sources (Location Hash, URL parameters).
- **HTML Injection**: Inject malicious tags to hijack forms, overlay content, or exfiltrate data via CSS.

## 🚀 Exploitation & Impact
- **Session Hijacking**: Capture `document.cookie` (if not HttpOnly) or LocalStorage.
- **Phishing Overlays**: Inject fake login forms into trusted domains.
- **Keylogging**: Inject scripts to capture user keystrokes in specific input fields.

## 🛡️ Bypass Techniques
- **Encoding**: Use HTML entity, Hex, or Unicode encoding to bypass basic WAFs.
- **Obfuscation**: Use JavaScript string concatenation or `atob()` for Base64 execution.
- **Alternative Tags**: Use `<svg>`, `<body>`, or `<details>` event handlers when `<script>` is blocked.

## 📋 Verification Checklist
- [ ] Is the testing authorized and within the defined scope?
- [ ] Have Stored, Reflected, and DOM vectors been analyzed?
- [ ] Are remediation steps provided for each discovered flaw?
- [ ] Is a Proof-of-Concept (PoC) provided to demonstrate business impact?
- [ ] Are bypass techniques documented for any existing security controls?
