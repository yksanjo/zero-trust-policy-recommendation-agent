# Zero Trust Policy Recommendation Agent

Generate and validate least-privilege access recommendations.

## Vertical

security

## Production MVP Deliverables

1. HTTP API for health and risk assessment.
2. Deterministic scoring service with explainable reasons.
3. Domain-specific threat model baseline.
4. CI gates for lint and tests.
5. Container packaging for deployment.

## Local Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
make test
make run
```

## API

- `GET /health`
- `POST /v1/assess`
