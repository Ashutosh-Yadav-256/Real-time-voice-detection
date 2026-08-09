# ADR 002: Triton Inference Server over TorchServe

## Status: Accepted
## Date: 2024-01-20

## Context
We need a serving engine for our PyTorch and TensorRT models that provides high throughput, low latency, and dynamic batching.

## Decision
Select NVIDIA Triton Inference Server over TorchServe.

## Consequences
Pros:
- Native support for TensorRT, ONNX, and PyTorch.
- Highly optimized dynamic batching.
- Excellent GPU utilization metrics.

Cons:
- Steeper learning curve compared to TorchServe.
- Configuration requires careful tuning.
