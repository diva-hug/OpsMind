---
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