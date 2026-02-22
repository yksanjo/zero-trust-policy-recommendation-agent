# Architecture - Zero Trust Policy Recommendation Agent

## Core components

1. API boundary
2. Domain services
3. Persistence and adapters
4. Policy and authorization hooks
5. Telemetry and audit logging

## Data flow

1. Request enters API boundary.
2. Input validation and policy checks execute.
3. Domain service processes the request.
4. Structured audit/metric events are emitted.
5. Response returns with trace metadata.
