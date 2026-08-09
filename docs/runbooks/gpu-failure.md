# Runbook: GPU Node Failure

**Alert:** GPUNodeNotReady
**Severity:** SEV1
**Response Time:** 15 minutes

## Symptoms
- Kubernetes node status is NotReady.
- Triton inference server pods stuck in Pending.
- NVIDIA DCGM exporter missing metrics.

## Diagnosis
1. Describe the affected node.
2. Check system logs for Xid errors.

## Commands
```bash
kubectl describe node <gpu-node>
kubectl logs -n kube-system -l name=nvidia-device-plugin
```

## Mitigation
1. Cordon and drain the node.
```bash
kubectl cordon <gpu-node>
kubectl drain <gpu-node> --ignore-daemonsets --delete-emptydir-data
```
2. Auto-scaling group will replace the node.

## Verification
Ensure new node joins and pods schedule successfully.
