---
name: security-design
description: "Security architecture design, threat modeling (STRIDE), and security requirement extraction. Use during DEFINE and PLAN phases to build security into the design."
---

# Security Architecture and Design

Build security into the system from the start rather than bolting it on later.

## 1. Threat Modeling (STRIDE)

For every new feature or architectural change, identify threats using the STRIDE categories:

| Category | Security Property | Definition |
| :--- | :--- | :--- |
| **S**poofing | Authenticity | Pretending to be something or someone else. |
| **T**ampering | Integrity | Modifying data or code. |
| **R**epudiation | Non-repudiability | Claiming you didn't do something. |
| **I**nformation Disclosure | Confidentiality | Exposing data to unauthorized parties. |
| **D**enial of Service | Availability | Exhausting resources to crash the system. |
| **E**levation of Privilege | Authorization | Gaining higher access level than intended. |

---

## 2. Security Requirement Extraction

Transform identified threats into actionable requirements:

### Workflow
1. **Identify Assets**: What are we protecting? (e.g., User PII, API Keys, Tenant Data).
2. **Define Boundaries**: Where does trust change? (e.g., Browser to API, API to Database).
3. **Map Threats**: Apply STRIDE to each boundary.
4. **Write Requirements**: Convert mitigations into "Must-have" features.

### Example: Protect "User Password Reset"
- **Threat**: Spoofing (Attacker resets another user's password).
- **Requirement**: "Password reset tokens MUST be cryptographically secure (High Entropy), time-limited (15 mins), and single-use."
- **Mitigation**: Use a cryptographically secure random number generator (CSPRNG).

---

## 3. Trust Boundary Analysis
Mark every point where data enters the system from an untrusted source:
- Public APIs.
- Third-party webhooks.
- User-uploaded files.
- Internal service-to-service calls (Zero Trust).

---

## 4. Security User Stories (As-a-I-want-so-that)
- **As a** system administrator, **I want** all administrative actions logged, **so that** we have a non-repudiable audit trail for compliance.
- **As a** user, **I want** my data encrypted at rest, **so that** it remains confidential even if the physical storage is compromised.
