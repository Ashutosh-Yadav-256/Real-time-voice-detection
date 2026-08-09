# Runbook: Disaster Recovery

**Alert:** RegionDown
**Severity:** SEV1
**Response Time:** 5 minutes

## Symptoms
- Complete loss of connectivity to primary region.
- All services reporting down.

## Diagnosis
1. Confirm AWS region status.
2. Validate Route53 health checks.

## Commands
```bash
aws ec2 describe-regions
```

## Mitigation
1. Update Route53 to point to secondary region.
2. Ensure Aurora global database fails over.
3. Scale up replicas in secondary region.

## Verification
Test end-to-end flow in the secondary region.
