---
id: ARCH-DEPENDENCIES
type: architecture
---

# Service Dependencies

Order Service
    -> Payment API
    -> Inventory Service

Payment API
    -> Payment Database

Authentication Service
    -> User Database
    -> Redis

Inventory Service
    -> Inventory Database

Notification Service
    -> Message Queue