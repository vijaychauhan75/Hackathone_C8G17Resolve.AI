from pydantic import BaseModel


class LogIssue(BaseModel):
    line: int
    message: str
    severity: str


class Incident(BaseModel):
    id: str
    filename: str
    issues: list[LogIssue]


class RCAReport(BaseModel):
    primary_cause: str
    evidence: str
    alternative_causes: list[str]
    confidence: float


class Recommendation(BaseModel):
    recommendation: str
    confidence: float
    reason: str
    supporting_sources: list[dict]


class Cookbook(BaseModel):
    steps: list[str]
    commands: list[str]
    validation: str
    rollback: str


class JiraPayload(BaseModel):
    summary: str
    description: str