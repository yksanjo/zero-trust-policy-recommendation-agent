from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

DOMAIN = "security"
PROJECT = "zero-trust-policy-recommendation-agent"


class AssessRequest(BaseModel):
    content: str = Field(min_length=3)
    source: str = Field(default="telemetry")


class AssessResponse(BaseModel):
    project: str
    domain: str
    risk_score: float
    severity: str
    reasons: list[str]
    recommended_actions: list[str]
    generated_at: str


def _score_signal(content: str) -> tuple[float, list[str]]:
    text = content.lower()
    indicators = {
        "critical": 0.35,
        "breach": 0.35,
        "exploit": 0.25,
        "outage": 0.20,
        "malware": 0.30,
        "anomaly": 0.15,
        "ransomware": 0.40,
        "exfiltration": 0.30,
    }
    score = 0.05
    reasons: list[str] = []
    for word, weight in indicators.items():
        if word in text:
            score += weight
            reasons.append(f"matched-indicator:{word}")

    score = min(score, 1.0)
    if not reasons:
        reasons.append("baseline-signal-assessment")
    return score, reasons


def _severity(score: float) -> str:
    if score >= 0.8:
        return "critical"
    if score >= 0.6:
        return "high"
    if score >= 0.3:
        return "medium"
    return "low"


def _actions(severity: str) -> list[str]:
    if severity == "critical":
        return ["open-incident", "notify-oncall", "enforce-containment"]
    if severity == "high":
        return ["open-ticket", "notify-service-owner", "increase-monitoring"]
    if severity == "medium":
        return ["queue-review", "collect-more-context"]
    return ["log-observation"]


app = FastAPI(title=PROJECT, version="0.2.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": PROJECT, "domain": DOMAIN}


@app.post("/v1/assess", response_model=AssessResponse)
def assess(payload: AssessRequest) -> AssessResponse:
    score, reasons = _score_signal(payload.content)
    severity = _severity(score)
    return AssessResponse(
        project=PROJECT,
        domain=DOMAIN,
        risk_score=score,
        severity=severity,
        reasons=reasons,
        recommended_actions=_actions(severity),
        generated_at=datetime.now(timezone.utc).isoformat(),
    )
