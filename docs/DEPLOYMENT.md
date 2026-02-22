# Deployment Guide

## Runtime

- Python 3.10+
- Container-compatible service
- Stateless API process

## Commands

```bash
pip install -e .[dev]
pytest -q
python -m src.main
```

## Readiness Checklist

1. CI passing on default branch.
2. Health endpoint monitored.
3. Secrets injected via environment.
4. Rollback plan validated.
