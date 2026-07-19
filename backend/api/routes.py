from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from agents.log_reader import detect_incidents
from agents.rca import generate_rca
from agents.remediation import get_recommendations
from agents.cookbook import generate_cookbook
from integrations.jira import create_jira_ticket

router = APIRouter()


@router.post("/upload-log")
async def upload_log(file: UploadFile = File(...)):
    if file.content_type not in ["text/plain", "application/octet-stream"]:
        raise HTTPException(status_code=400, detail="Only .txt and .log files are allowed")

    content = (await file.read()).decode("utf-8", errors="ignore")
    incidents = detect_incidents(content)
    return JSONResponse({
        "uploadId": "demo-upload-id",
        "filename": file.filename,
        "size": len(content),
        "incidents": incidents,
        "message": "Log uploaded successfully"
    })


@router.get("/incidents")
async def list_incidents():
    return {"incidents": []}


@router.get("/incidents/{incident_id}")
async def get_incident(incident_id: str):
    incident = {"line": 1, "message": "example", "severity": "ERROR"}
    rca = generate_rca(incident)
    remediation = get_recommendations(incident)
    cookbook = generate_cookbook(incident, rca)
    return {
        "incident": incident,
        "rca": rca,
        "remediation": remediation,
        "cookbook": cookbook,
    }


@router.post("/create-jira")
async def create_jira():
    payload = {"summary": "Incident", "description": "Example incident"}
    ticket = create_jira_ticket(payload)
    return ticket


@router.post("/notify-slack")
async def notify_slack():
    return {"status": "sent", "message": "Mock Slack notification sent"}