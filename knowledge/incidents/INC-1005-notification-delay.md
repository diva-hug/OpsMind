---
id: INC-1005
type: incident
service: notification-service
severity: medium
status: resolved
---

# Notification Delivery Delay

## Symptoms

Customers received order confirmation emails late.

## Root Cause

Message queue backlog increased significantly.

## Resolution

Additional notification workers were started.

## Prevention

Configure alerts when queue backlog exceeds threshold.