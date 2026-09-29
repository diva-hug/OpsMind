---
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