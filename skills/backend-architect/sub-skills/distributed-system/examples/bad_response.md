# Example: Bad Response (Anti-Patterns to Avoid)

Below is an anti-pattern example of how a low-quality agent might handle distributed operations. This response violates transactional consistency and exposes the system to network split-brain risks.

---

## ❌ Why This Response is Rejected

### 1. Dual-Write Anti-Pattern (Split-Brain Risk)
*   The agent publishes an event directly to RabbitMQ inside the DB transaction. If the DB fails to commit, the event has already been published to the broker! The secondary services will process an account that does not exist.
*   If RabbitMQ is slow, it keeps the database connection transaction open, exhausting the pool.

### 2. Missing Idempotence check on Consumer
*   The message listener processes billing immediately without checking for duplicate delivery. If RabbitMQ retries delivery (a normal event), the user gets billed twice.

### 3. Lack of Timeouts & Resilience
*   Direct HTTP/gRPC synchronous calls to other services without a circuit breaker or timeout limits, causing cascade failures.

---

## ❌ Anti-Pattern Source Code Example

```javascript
// src/controllers/billing.js
const express = require('express');
const router = express.Router();
const db = require('../db');
const rabbitmq = require('../rabbitmq');

router.post('/billing', async (req, res) => {
  // ❌ Transaction block
  const tx = await db.beginTransaction();
  try {
    await tx.query('INSERT INTO accounts VALUES (...)');
    
    // ❌ CRITICAL DUAL-WRITE ERROR!
    // Publishing network message INSIDE database transaction!
    await rabbitmq.publish('account_created', { id: 123 }); 
    
    await tx.commit(); // If this commits fail, rabbitmq message is already gone!
    res.sendStatus(201);
  } catch (err) {
    await tx.rollback();
    res.status(500).send(err);
  }
});

// ❌ NON-IDEMPOTENT CONSUMER
rabbitmq.subscribe('account_created', async (msg) => {
  // ❌ CRITICAL: processes immediately. 
  // If RabbitMQ delivers this message twice, the customer is billed twice!
  await db.query('UPDATE balance SET amount = amount - 10'); 
});
```
