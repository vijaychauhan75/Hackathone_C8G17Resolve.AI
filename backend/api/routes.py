from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from agents.log_reader import detect_incidents

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
