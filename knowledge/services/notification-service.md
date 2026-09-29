---
id: SERVICE-NOTIFICATION
type: service
service: notification-service
owner: messaging-team
criticality: medium
---

# Notification Service

## Purpose

The Notification Service sends email and SMS notifications.

## Dependencies

- Email provider
- SMS provider
- Message queue

## Common Problems

- Delayed notifications
- Failed email delivery
- Queue backlog

## Monitoring

Monitor:

- Queue size
- Delivery success rate
- Processing latency