# ADR 003: Kafka over Kinesis

## Status: Accepted
## Date: 2024-02-05

## Context
We need a highly scalable, durable, and low-latency message broker for streaming audio events through our pipeline.

## Decision
Adopt Apache Kafka instead of Amazon Kinesis.

## Consequences
Pros:
- Open-source and cloud-agnostic.
- Extremely high throughput and low latency.
- Rich ecosystem of connectors and stream processing frameworks.

Cons:
- Requires managing Kafka clusters (or using a managed service like MSK which adds cost).
- More complex to operate than Kinesis.
