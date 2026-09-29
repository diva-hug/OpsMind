---
id: INC-1006
type: incident
service: search-service
severity: medium
status: resolved
---

# Search Service Timeout

## Symptoms

Product searches took more than 10 seconds.

## Root Cause

The search index contained stale and inefficient indexes.

## Resolution

The search index was rebuilt.

## Prevention

Schedule regular index health checks.