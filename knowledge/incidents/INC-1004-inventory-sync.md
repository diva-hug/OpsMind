---
id: INC-1004
type: incident
service: inventory-service
severity: medium
status: resolved
---

# Inventory Synchronization Failure

## Symptoms

Product stock values were outdated.

## Root Cause

The inventory synchronization worker stopped processing
messages from the order queue.

## Resolution

The worker was restarted and queued messages
were processed successfully.

## Prevention

Monitor worker heartbeat and queue backlog.