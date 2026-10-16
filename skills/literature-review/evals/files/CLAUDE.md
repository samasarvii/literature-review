# Project rules

Settled decisions (do not re-litigate):
- Every tool call that writes to a database, sends a message, or spends money requires explicit human confirmation. No allowlist, no auto-approve, ever.
- Read-only tools (search, fetch, read file) never require confirmation.
- Agents run with a 30-call budget per task; exceeding it stops the task.

Stack: Python 3.12, FastAPI, Postgres, Claude API. Internal ops tooling, ~20 users.
