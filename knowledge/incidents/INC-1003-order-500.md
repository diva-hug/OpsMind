---
id: INC-1003
type: incident
service: order-service
severity: high
status: resolved
---

# Order Service HTTP 500 Errors

## Symptoms

Customers could not create orders.

The Order API returned HTTP 500 errors.

## Root Cause

Order Service could not connect to the database.

## Resolution

Database connectivity was restored and
Order Service instances were restarted.

## Prevention

Add database connectivity health checks.