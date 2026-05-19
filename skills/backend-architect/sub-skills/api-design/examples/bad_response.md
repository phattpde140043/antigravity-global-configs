# Example: Bad Response (Anti-Pattern / AI Slop to Avoid)

Below is an anti-pattern example of how a low-quality agent might respond to the same request. This response violates clean code standards, lacks tenant isolation, contains AI slop placeholders, and mixes architectural layers.

---

## ❌ Why This Response is Rejected

### 1. Architectural Violations (Mega-File / Mixed Layers)
*   The agent dumps controller route, business rules, database connection, and helper classes in a single block without layer segregation.
*   The database is queried directly inside the routing layer.

### 2. Missing Security & Tenant Isolation (Critical Vulnerability)
*   The request accepts `userId` from the URL or query parameters without verifying against token contexts.
*   There is NO tenant context validation. User A can easily retrieve User B's history by changing the `userId` in the request (IDOR).

### 3. Missing Pagination & Raw Array Envelope
*   Returns the raw database list array directly to the client: `res.json(data)`. If the search history has 100,000 entries, it will crash the server and browser.
*   No pagination limits or envelopes.

### 4. AI Slop & Code Placeholders
*   Contains lazy placeholders like `// TODO: Implement error handling` and `// ... rest of code goes here`.

---

## ❌ Anti-Pattern Source Code Example

```javascript
// src/controllers/history.js
const express = require('express');
const router = express.Router();
const db = require('../utils/helpers'); // Poor helper naming convention

// ❌ Verb in URL, mixing singular/plural, no versioning path
router.get('/getHistory', async (req, res) => {
  try {
    const userId = req.query.userId; // ❌ Directly trusting client input without authorization checks!

    // ❌ Querying database directly inside the router layer (Mixing layers)
    const sql = `SELECT * FROM search_history WHERE user_id = '${userId}'`; // ❌ CRITICAL: SQL Injection Vulnerability!
    
    const results = await db.query(sql);

    // ❌ returning raw array database directly without data/meta envelope
    // ❌ Missing pagination! Returns all entries at once
    res.status(200).json(results); 
  } catch (error) {
    // ❌ Swallowing error details or exposing system crash stack traces
    console.log(error); 
    res.status(500).json({ error: "Something went wrong" }); // Generic useless error message
  }
});

// ❌ Lazy code placeholder (AI Slop)
function validateUser(id) {
  // TODO: implement this helper later (TECH-12)
  return true;
}

module.exports = router;
```
