---
id: INC-1007
type: incident
service: payment-api
severity: high
status: resolved
---

# Payment Database Connection Failure

## Symptoms

Payment transactions intermittently failed.

## Root Cause

Database connection limits were reached.

## Resolution

Database connection limits were increased
and connection pooling was optimized.

## Prevention

Monitor active database connections.