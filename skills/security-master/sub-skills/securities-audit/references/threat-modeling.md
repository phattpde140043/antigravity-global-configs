# Threat Modeling & Risk Assessment

## 🛡️ STRIDE Methodology
Use STRIDE to categorize threats during the design phase:
- **S**poofing: User A pretending to be User B.
- **T**ampering: Modifying data in transit or in the DB.
- **R**epudiation: Users performing actions without system evidence (logs).
- **I**nformation Disclosure: Leaking sensitive logs or PII.
- **D**enial of Service: Crashing the system with junk requests.
- **E**levation of Privilege: Regular users gaining Admin rights.

## 🍝 PASTA Methodology
A simulation-based attack process to assess risk:
1. Define Objectives.
2. Define Technical Scope.
3. Application Decomposition.
4. Threat Analysis.
5. Vulnerability Analysis.
6. Attack Simulation.
7. Impact Analysis.

## 🌳 Attack Trees
Construct hierarchical diagrams of steps an attacker needs to take to achieve an end goal (e.g., gaining DB access).

## 📊 Risk Scoring (DREAD Model)
Prioritize vulnerabilities based on:
- **D**amage: How bad is the impact?
- **R**eproducibility: How easy is it to repeat?
- **E**xploitability: How easy is it to launch?
- **A**ffected Users: How many people are impacted?
- **D**iscoverability: How easy is it to find?

## 📋 Security Architecture Review Checklist
- [ ] Has the DFD (Data Flow Diagram) clearly identified all Trust Boundaries?
- [ ] Is all input from External Systems treated as Untrusted?
- [ ] Are Fail-Closed mechanisms implemented for all security systems?
- [ ] Has the Blast Radius been minimized through Micro-segmentation?
