---
id: INC-1010
type: incident
service: inventory-service
severity: medium
status: resolved
---

# Inventory Cache Inconsistency

## Symptoms

Some products displayed incorrect stock counts.

## Root Cause

Cache values were not invalidated after stock updates.

## Resolution

The affected cache entries were cleared.

## Prevention

Add cache invalidation checks to inventory updates.