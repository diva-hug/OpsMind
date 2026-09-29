---
id: INC-1001
type: incident
service: payment-api
severity: high
status: resolved
---

# Payment API Database Timeout

## Symptoms

Customers received HTTP 500 errors while making payments.

Payment response latency increased above 30 seconds.

## Root Cause

The database connection pool was exhausted
during a traffic spike.

## Resolution

1. Increased database connection pool size.
2. Restarted payment-api instances.
3. Added database connection monitoring.

## Prevention

Alert when database connection utilization
crosses 80%.