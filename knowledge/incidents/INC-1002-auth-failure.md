---
id: INC-1002
type: incident
service: auth-service
severity: high
status: resolved
---

# Authentication Login Failure

## Symptoms

Users were unable to log in.

Authentication requests returned HTTP 401 errors.

## Root Cause

Redis cache became unavailable.

## Resolution

1. Restored Redis availability.
2. Restarted affected authentication instances.
3. Added Redis health monitoring.

## Prevention

Create alerts for Redis connection failures.