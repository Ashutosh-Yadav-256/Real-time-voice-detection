# Runbook: High End-to-End Latency

**Alert:** HighE2ELatency
**Severity:** SEV2
**Response Time:** 15 minutes

## Symptoms
- p99 latency > 200ms for 5+ minutes
- Grafana E2E latency panel shows spike

## Diagnosis
1. Identify bottleneck stage in Grafana
2. Check Kafka consumer lag
3. Check GPU utilization
4. Check pod resource usage

## Commands
```bash
kubectl get pods -n production
kubectl exec -it kafka-client -- kafka-consumer-groups --bootstrap-server kafka:9092 --describe --group all
kubectl top pods -n production
kubectl describe node gpu-node-1
```

## Mitigation
Scale the affected service:
```bash
kubectl scale deployment inference-router --replicas=10 -n production
```

## Verification
Monitor Grafana dashboards for latency drop.
