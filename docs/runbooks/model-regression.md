# Runbook: Model Regression

**Alert:** ModelAccuracyDrop
**Severity:** SEV2
**Response Time:** 30 minutes

## Symptoms
- False positive rate spikes above 5%
- Precision or recall drops significantly

## Diagnosis
1. Check the data distribution of recent inferences.
2. Ensure data drift metrics are not firing.
3. Validate if a new model version was recently deployed.

## Commands
```bash
kubectl logs -l app=model-monitor -n production
```

## Mitigation
Rollback to previous model version via GitOps.
```bash
git revert <commit-id>
git push
```

## Verification
Confirm the deployed model tag in Triton Inference Server and monitor accuracy.
