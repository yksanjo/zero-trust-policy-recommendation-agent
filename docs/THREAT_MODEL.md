# Threat Model

## Scope

Zero Trust Policy Recommendation Agent

## Key Threat Surface

identity, API boundaries, secrets, and supply chain dependencies

## Control Priorities

least privilege, secrets hygiene, and incident-ready audit trails

## Baseline Mitigations

1. Strong authentication and authorization on all write paths.
2. Structured audit logs for all sensitive actions.
3. Input validation and schema enforcement at API boundaries.
4. CI guardrails for tests, linting, and dependency hygiene.
