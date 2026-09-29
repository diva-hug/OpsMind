---
id: SERVICE-ORDER
type: service
service: order-service
owner: orders-team
criticality: high
---

# Order Service

## Purpose

The Order Service creates and manages customer orders.

## Dependencies

- Payment API
- Inventory Service
- User database

## Common Problems

- HTTP 500 errors
- Order creation failures
- Slow order processing

## Monitoring

Monitor:

- Order creation success rate
- API latency
- Database errors