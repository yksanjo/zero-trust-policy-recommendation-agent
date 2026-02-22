from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_health_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"


def test_assess_signal() -> None:
    response = client.post(
        "/v1/assess",
        json={"content": "critical breach anomaly detected on gateway", "source": "siem"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["risk_score"] >= 0.5
    assert payload["severity"] in {"medium", "high", "critical"}
    assert len(payload["recommended_actions"]) >= 1
