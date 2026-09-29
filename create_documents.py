from pathlib import Path


BASE_DIR = Path("knowledge")


documents = {

    # =========================================================
    # SERVICES
    # =========================================================

    "services/payment-api.md": """---
id: SERVICE-PAYMENT
type: service
service: payment-api
owner: payments-team
criticality: high
---

# Payment API

## Purpose

The Payment API processes customer payment transactions.

## Dependencies

- Payment database
- Authentication service
- Order service

## Common Problems

- HTTP 500 errors
- Database connection timeout
- High latency
- Payment processing failures

## Monitoring

Important metrics:

- Error rate
- Request latency
- Database connection utilization
""",

    "services/auth-service.md": """---
id: SERVICE-AUTH
type: service
service: auth-service
owner: identity-team
criticality: high
---

# Authentication Service

## Purpose

The Authentication Service handles user login,
token generation, and authentication validation.

## Dependencies

- User database
- Redis cache

## Common Problems

- Login failures
- Token generation errors
- Authentication timeout

## Monitoring

Monitor:

- Authentication failure rate
- Token generation latency
- Redis availability
""",

    "services/order-service.md": """---
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
""",

    "services/inventory-service.md": """---
id: SERVICE-INVENTORY
type: service
service: inventory-service
owner: inventory-team
criticality: high
---

# Inventory Service

## Purpose

The Inventory Service maintains product stock levels.

## Dependencies

- Inventory database
- Order Service

## Common Problems

- Stock synchronization failures
- Stale inventory
- Database timeout

## Monitoring

Monitor:

- Stock synchronization delay
- Database health
- Inventory update failures
""",

    "services/notification-service.md": """---
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
""",

    "services/search-service.md": """---
id: SERVICE-SEARCH
type: service
service: search-service
owner: platform-team
criticality: medium
---

# Search Service

## Purpose

The Search Service provides product search functionality.

## Dependencies

- Search index
- Product database

## Common Problems

- Search timeout
- Stale search index
- Missing products

## Monitoring

Monitor:

- Search latency
- Index freshness
- Search error rate
""",

    # =========================================================
    # INCIDENTS
    # =========================================================

    "incidents/INC-1001-payment-timeout.md": """---
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
""",

    "incidents/INC-1002-auth-failure.md": """---
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
""",

    "incidents/INC-1003-order-500.md": """---
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
""",

    "incidents/INC-1004-inventory-sync.md": """---
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
""",

    "incidents/INC-1005-notification-delay.md": """---
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
""",

    "incidents/INC-1006-search-timeout.md": """---
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
""",

    "incidents/INC-1007-payment-db.md": """---
id: INC-1007
type: incident
service: payment-api
severity: high
status: resolved
---

# Payment Database Connection Failure

## Symptoms

Payment transactions intermittently failed.

## Root Cause

Database connection limits were reached.

## Resolution

Database connection limits were increased
and connection pooling was optimized.

## Prevention

Monitor active database connections.
""",

    "incidents/INC-1008-auth-db.md": """---
id: INC-1008
type: incident
service: auth-service
severity: high
status: resolved
---

# Authentication Database Failure

## Symptoms

Some users experienced authentication failures.

## Root Cause

Authentication database response time increased.

## Resolution

Database performance was restored.

## Prevention

Add database latency monitoring.
""",

    "incidents/INC-1009-order-deployment.md": """---
id: INC-1009
type: incident
service: order-service
severity: high
status: resolved
---

# Order Service Deployment Failure

## Symptoms

Order creation failures increased immediately
after a deployment.

## Root Cause

A configuration value was incorrect in the new version.

## Resolution

The deployment was rolled back.

## Prevention

Add configuration validation to deployment pipelines.
""",

    "incidents/INC-1010-inventory-cache.md": """---
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
""",

    # =========================================================
    # RUNBOOKS
    # =========================================================

    "runbooks/payment-api-500.md": """---
id: RUNBOOK-PAYMENT-500
type: runbook
service: payment-api
---

# Payment API HTTP 500 Runbook

## Step 1

Check current Payment API status.

## Step 2

Check API error rate.

## Step 3

Check database connection utilization.

## Step 4

Check recent deployments.

## Step 5

Search historical payment incidents.

## Escalation

If database connectivity is the suspected cause,
contact the database operations team.
""",

    "runbooks/database-timeout.md": """---
id: RUNBOOK-DATABASE-TIMEOUT
type: runbook
service: database
---

# Database Timeout Runbook

## Step 1

Check database availability.

## Step 2

Check active database connections.

## Step 3

Check connection pool utilization.

## Step 4

Check database latency.

## Step 5

Review recent application deployments.

## Escalation

Escalate to the database operations team
if connection utilization remains above threshold.
""",

    "runbooks/authentication-failure.md": """---
id: RUNBOOK-AUTH-FAILURE
type: runbook
service: auth-service
---

# Authentication Failure Runbook

## Step 1

Check authentication service status.

## Step 2

Check Redis availability.

## Step 3

Check authentication error rate.

## Step 4

Check recent deployments.

## Step 5

Review previous authentication incidents.
""",

    "runbooks/order-api-500.md": """---
id: RUNBOOK-ORDER-500
type: runbook
service: order-service
---

# Order API HTTP 500 Runbook

## Step 1

Check Order API status.

## Step 2

Check database connectivity.

## Step 3

Check recent deployment history.

## Step 4

Search historical order incidents.

## Step 5

Review application logs.
""",

    "runbooks/inventory-sync-failure.md": """---
id: RUNBOOK-INVENTORY-SYNC
type: runbook
service: inventory-service
---

# Inventory Synchronization Failure

## Step 1

Check inventory worker status.

## Step 2

Check message queue backlog.

## Step 3

Check worker heartbeat.

## Step 4

Restart the worker if required.

## Step 5

Verify inventory synchronization.
""",

    "runbooks/service-degradation.md": """---
id: RUNBOOK-SERVICE-DEGRADATION
type: runbook
service: platform
---

# Service Degradation Runbook

## Step 1

Check service health.

## Step 2

Check error rate.

## Step 3

Check latency.

## Step 4

Check recent deployments.

## Step 5

Check dependent services.

## Step 6

Search previous incidents.
""",

    # =========================================================
    # ARCHITECTURE
    # =========================================================

    "architecture/system-architecture.md": """---
id: ARCH-SYSTEM
type: architecture
---

# ShopSphere System Architecture

ShopSphere is an e-commerce platform.

Main services:

- Authentication Service
- Product Search Service
- Inventory Service
- Order Service
- Payment API
- Notification Service

The Order Service depends on Payment and Inventory services.
""",

    "architecture/database-architecture.md": """---
id: ARCH-DATABASE
type: architecture
---

# Database Architecture

ShopSphere services use separate logical databases.

Payment API uses the payment database.

Order Service uses the order database.

Inventory Service uses the inventory database.

Authentication Service uses the user database.

Database connection limits and latency
are important operational metrics.
""",

    "architecture/service-dependencies.md": """---
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
""",

    # =========================================================
    # POLICIES
    # =========================================================

    "policies/incident-severity-policy.md": """---
id: POLICY-SEVERITY
type: policy
---

# Incident Severity Policy

## Critical

Complete service outage or major customer impact.

## High

Major functionality is affected and
many customers may be impacted.

## Medium

Partial functionality is affected.

## Low

Minor issue with limited customer impact.
""",

    "policies/escalation-policy.md": """---
id: POLICY-ESCALATION
type: policy
---

# Incident Escalation Policy

High severity incidents must be escalated
to the service owner.

Database-related incidents should also
involve the database operations team.

Security-related incidents must be escalated
to the security team.
""",

    "policies/deployment-policy.md": """---
id: POLICY-DEPLOYMENT
type: policy
---

# Deployment Policy

Production deployments must:

1. Pass automated tests.
2. Pass configuration validation.
3. Have rollback capability.
4. Be monitored after deployment.

If an incident begins immediately after deployment,
deployment rollback should be considered.
"""
}


def create_documents():
    for relative_path, content in documents.items():

        file_path = BASE_DIR / relative_path

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path.write_text(
            content.strip(),
            encoding="utf-8"
        )

        print(f"Created: {file_path}")


if __name__ == "__main__":
    create_documents()

    print()
    print("=" * 50)
    print("ShopSphere knowledge base created successfully!")
    print(f"Total documents: {len(documents)}")
    print("=" * 50)