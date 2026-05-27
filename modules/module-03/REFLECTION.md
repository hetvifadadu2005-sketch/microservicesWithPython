# Module 3 — Reflection

**Team name**: _______________
**Branch**: `module-03/<team-name>`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:*
The gateway is useful because the frontend only needs to communicate with one service instead of remembering different ports and URLs for every microservice. Without the gateway, the frontend would need to hardcode addresses like localhost:8001 for users and localhost:8002 for games.If a service changes ports or moves to another machine, the frontend would also need updates everywhere. With the gateway, only the routing configuration changes while the frontend stays the same. It also makes the system cleaner and easier to manage.

---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:*
User validation is critical because an activity should never be created for a user that does not exist. If this check is skipped, invalid or fake activity records could be stored in the database.The game lookup is treated differently because the activity can still exist even if the game-service is temporarily unavailable. In that case, returning "game": null is better than blocking the whole request. This approach improves reliability and allows the system to continue working during partial failures.

---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:*
When services depend on each other, the total response time becomes slower because each request adds extra waiting time. For example, if three services each take one second, the user may wait around three seconds for the full response.It also increases the risk of failures. If one service goes down completely, requests that depend on it may fail or become delayed. That is why graceful degradation and proper error handling are important in microservice systems.

---

*Keep this file. You will refer back to it during the oral presentation.*
