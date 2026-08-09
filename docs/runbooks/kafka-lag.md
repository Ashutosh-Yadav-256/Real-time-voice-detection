# Runbook: Kafka Consumer Lag

**Alert:** HighKafkaConsumerLag
**Severity:** SEV3
**Response Time:** 1 hour

## Symptoms
- Consumer lag exceeds 10,000 messages.
- Processing delay reported by users.

## Diagnosis
1. Check event-consumer logs for errors.
2. Check network bandwidth between broker and consumer.

## Commands
```bash
kubectl exec -ti kafka-client -- kafka-consumer-groups --bootstrap-server kafka:9092 --group event-consumer-group --describe
```

## Mitigation
Scale the consumer deployment.
```bash
kubectl scale deployment event-consumer -n production --replicas=5
```

## Verification
Watch the consumer lag metric decrease.
