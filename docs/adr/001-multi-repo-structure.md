# ADR 001: Multi-Repository Structure

## Status: Accepted
## Date: 2024-01-15

## Context
We need to decide whether to use a mono-repo or a multi-repo structure for the AI Voice Detector project, which consists of multiple microservices, infrastructure code, ML pipelines, and deployment manifests.

## Decision
Adopt a multi-repo strategy with distinct repositories for services, infrastructure, ML, and deployments.

## Consequences
Pros:
- Clear separation of concerns.
- Granular access control.
- Independent CI/CD pipelines.

Cons:
- Dependency management across repositories can be challenging.
- Synchronizing cross-cutting changes requires more effort.
