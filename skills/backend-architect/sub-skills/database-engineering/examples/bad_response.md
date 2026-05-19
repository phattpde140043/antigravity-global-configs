# Example: Bad Response (Anti-Patterns to Avoid)

Below is an anti-pattern example of how a low-quality agent might handle database query tuning and migrations. This response violates clean code standards, introduces blocking locks, and contains security flaws.

---

## ❌ Why This Response is Rejected

### 1. Blocking Exclusive Table Locks (DDL locking)
*   The agent runs standard `CREATE INDEX idx_status ON transactions(status)`. On a 10M row table, this locks the table for up to 30 minutes, knocking out the entire production app.

### 2. SQL Injection Vulnerability (Security Risk)
*   Concatenates raw parameters directly in the SQL statement string without binding or parameterization.

### 3. Mixing Layers
*   Places raw SQL query strings directly in the API routes rather than delegating database operations to a clean Repository Layer.

---

## ❌ Anti-Pattern Source Code Example

```javascript
// src/routes/transactions.js
const express = require('express');
const router = express.Router();
const db = require('../db');

// ❌ Mixing routing with raw DB queries.
router.get('/transactions', async (req, res) => {
  const status = req.query.status; // Untrusted input

  // ❌ CRITICAL: SQL Injection vulnerability!
  const query = `SELECT * FROM transactions WHERE status = '${status}'`; 
  
  try {
    const results = await db.execute(query); // ❌ Un-parameterized query
    res.json(results);
  } catch (err) {
    res.status(500).send(err.stack); // ❌ Leaking DB system details to client!
  }
});

// ❌ BLOCKING MIGRATION (DDL lock)
// Inside migration.sql:
// CREATE INDEX idx_transactions_status ON transactions(status); 
// ❌ Violates Execution Contract: locks the high-traffic transactions table exclusively!
```
