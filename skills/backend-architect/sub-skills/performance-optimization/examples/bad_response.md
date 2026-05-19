# Example: Bad Response (Anti-Patterns to Avoid)

Below is an anti-pattern example of how a low-quality agent might handle performance optimization tasks. This response sequentializes async operations, lacks lists pagination, and performs expensive calculations in line.

---

## ❌ Why This Response is Rejected

### 1. Serial Await Execution (LCP/INP bottleneck)
*   The agent uses `await` on every independent call consecutively. This blocks the thread, serialization latency adds up (`120ms + 230ms + 310ms`), turning the response slow and laggy.

### 2. Missing Pagination (Memory Exhaustion)
*   Loads all user logs directly from the database into the memory array (`db.query('SELECT * FROM logs')`) without cursor limits or offset bounds, risking Node.js process Out Of Memory (OOM) crashes.

### 3. Lack of Caching
*   Queries expensive model recommendations on every single HTTP load without caching, overloading downstream recommendation microservices.

---

## ❌ Anti-Pattern Source Code Example

```javascript
// src/controllers/dashboard.js
const express = require('express');
const router = express.Router();
const db = require('../db');

router.get('/dashboard', async (req, res) => {
  try {
    // ❌ CRITICAL ERROR: Sequential await blocks!
    // These 3 calls are independent. Running them sequentially is extremely slow!
    const profile = await db.query('SELECT * FROM profiles WHERE id = 1'); // 120ms
    const orders = await db.query('SELECT * FROM orders WHERE user_id = 1');  // 230ms
    const recs = await db.query('SELECT * FROM recs WHERE user_id = 1');      // 310ms

    // ❌ Unbounded Database Read (No Pagination)
    // Risk of fetching 100,000 logs into JS memory and crashing the service!
    const logs = await db.query('SELECT * FROM logs'); 

    res.json({
      profile,
      orders,
      recs,
      logs
    });
  } catch (error) {
    res.status(500).send(error.message);
  }
});
```
