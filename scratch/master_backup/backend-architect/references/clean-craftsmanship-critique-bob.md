# Clean Craftsmanship & SOLID Critique: The Uncle Bob Review Protocol

Use this protocol to perform a professional, craftsmanship-oriented critique of the code's health and structure. Standing "outside the flow," evaluate the implementation through the lens of maintainability, professionalism, and the SOLID principles.

## 🧼 Hygiene & Integrity Lenses
When reviewing, ask these four "Uncle Bob Questions":

### 1. The Boy Scout Lens
*"Is the code left better than it was found? Does this change introduce 'Rot' (Rigidity, Fragility) or does it clean up the surroundings?"*
- Reject "quick hacks" that increase technical debt.
- Demand that the author cleans up minor surrounding issues (Boy Scout Rule).

### 2. Dependency Integrity (The Clean Architecture)
*"Do the dependencies point inward? Is the business logic (Entities/Use Cases) protected from external frameworks (DB, UI, API)?"*
- Reject business logic that depends on specific library details or database schemas.
- Ensure the "Dependency Rule" is strictly followed.

### 3. SOLID & SRP
*"Does every module have only 'one reason to change'? Are we following the SOLID principles, or are we building 'God Objects'?"*
- Evaluate Single Responsibility (SRP) and Open-Closed (OCP) principles.
- Reject large, multi-purpose classes and functions.

### 4. TDD & Professionalism
*"Is this change professional? Is it covered by 'F.I.R.S.T.' tests? Would you bet your career on the quality of this specific commit?"*
- Reject code without adequate unit tests.
- Focus on test "cleanliness" and meaningful naming.

---

## 🛠️ The Critique Workflow (Craftsmanship Review)

### Step 1: Smells Identification
Scan for the "4 Design Smells":
1. **Rigidity**: Is it hard to change?
2. **Fragility**: Does it break in unrelated places?
3. **Immobility**: Is it hard to reuse?
4. **Viscosity**: Is it easier to do the "wrong" thing than the "right" thing?

### Step 2: The Stepdown Rule
Read the code like a newspaper. High-level policies first, low-level details last. Does it follow a logical "Stepdown Rule"?

### Step 3: Naming & Intent
Review every variable and function name. Do they reveal intent without disinformation?

### Step 4: SRP Audit
Identify the "Actor" for each class. If there is more than one actor per class, recommend splitting it.

---

## 🏁 The Final Verdict (The Uncle Bob Gate)
A change only passes the Uncle Bob Review if:
- [ ] It follows **Clean Architecture** (Inward dependencies).
- [ ] It is **SOLID Compliant** (especially SRP).
- [ ] It has **High Hygiene** (Boy Scout Rule applied).
- [ ] It is **Professionally Tested** (Clean, meaningful tests).
