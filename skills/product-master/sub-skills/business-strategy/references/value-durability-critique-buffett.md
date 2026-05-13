# Value & Durability Critique: The Buffett Review Protocol

Use this protocol to perform a disciplined, "defense-first" critique. Standing "outside the flow," evaluate the implementation through the lens of simplicity, competitive moats, and long-term durability.

## 🛡️ Value & Safety Lenses
When reviewing, ask these four "Buffett Questions":

### 1. The Circle of Competence Lens
*"Are we building something we actually understand? Or are we drifting into 'Complexity Fog' to chase a trend?"*
- Reject over-engineered solutions that the team doesn't fully grasp.
- Favor clarity over "shiny" technology.

### 2. The Economic Moat
*"Does this architectural change build a durable competitive advantage? Does it make the system harder for competitors to disrupt?"*
- Evaluate if the change protects core assets (data, logic, security) or creates new vulnerabilities.

### 3. Margin of Safety
*"What is the worst-case scenario if this fails? Do we have enough 'margin' (redundancy, error handling, rollback) to survive a catastrophic error?"*
- Demand proof of robustness and failure isolation.

### 4. Simplicity over Sophistication
*"Is this the simplest way to win? Most mistakes come from doing too much, not too little."*
- Challenge unnecessary abstractions and "enterprise-grade" overhead that doesn't add direct value.

---

## 🛠️ The Critique Workflow (Disciplined Review)

### Step 1: Inversion (The "What if it Fails?" Test)
Invert the goal. Instead of "how do we make this succeed," ask "how could this change destroy the project?" Focus on preventing those failures.

### Step 2: The 20-Year Durability Test
If we didn't touch this code for 20 years, would it still be running? Is it built on "cigar butts" (dying tech) or "marvelous businesses" (durable patterns)?

### Step 3: Margin Check
Review the error handling and boundary conditions. Is there a "Margin of Safety" for edge cases and unexpected inputs?

### Step 4: Circle Check
Is the implementation straying outside the team's "Circle of Competence"? If so, recommend simplification or bringing in specialized expertise.

---

## 🏁 The Final Verdict (The Buffett Gate)
A change only passes the Buffett Review if:
- [ ] It is **Within our Circle of Competence**.
- [ ] It protects a **Durable Moat** (Competitive Advantage).
- [ ] It has a clear **Margin of Safety**.
- [ ] It favors **Simplicity over Sophistication**.
