# Strategic Critique: The Gates Review Protocol

Use this protocol to perform a cold, systemic critique of architectural changes. Standing "outside the flow," evaluate the implementation through the lens of long-term scalability and business systems.

## 🧠 Systemic Analysis Lenses
When reviewing, ask these four "Gates Questions":

### 1. The Scalability Lens
*"Does this work for 1 million users? 1 billion? Does the complexity stay linear, or does it explode?"*
- Reject "clever" solutions that don't scale.
- Prefer solutions that simplify the system as they grow.

### 2. Platform vs. Tool
*"Is this just a feature, or is it a gravitational platform that others can build upon?"*
- Evaluate if the change creates an ecosystem or just solves a one-off problem.

### 3. Marginal Cost of Intelligence/Code
*"What is the marginal cost of this implementation? Does adding the next feature or tenant cost near-zero, or does it require linear effort?"*
- Favor automation and near-zero marginal cost architectures.

### 4. Second-Order Effects
*"What happens after this is deployed? What are the unintended consequences in 5 years?"*
- Analyze regulatory risks, technical debt accumulation, and "backlash" from other system components.

---

## 🛠️ The Critique Workflow (Cold Review)

### Step 1: Decomposition
Decompose the implementation into its independent variables. Identify the real constraint (the "Chokepoint").

### Step 2: Probability Assessment (Bayesian)
What is the probability that our current assumptions are wrong? Update the design based on the "Worst Case" data.

### Step 3: Conflict as Respect
If the critique is aggressive, it means the idea is worthy of debate. Challenge the "consensus" solutions. Look for where the team might be "blinded" by their current success.

### Step 4: The 10-Year Scenario
Model the architectural state in 10 years. Is the current implementation a dead-end or a foundation?

---

## 🏁 The Final Verdict (The Gates Gate)
A change only passes the Gates Review if:
- [ ] It is **Observable by Design** (we can measure its failure).
- [ ] It has **Near-Zero Marginal Cost** at scale.
- [ ] It addresses the **Real Constraint**, not the symptom.
- [ ] It avoids **Systemic Backlash** (Security, Performance, Debt).
