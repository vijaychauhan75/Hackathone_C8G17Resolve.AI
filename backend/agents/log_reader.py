from typing import List, Dict

def detect_incidents(log_content: str) -> List[Dict]:
    lines = log_content.splitlines()
    incidents = []
    for idx, line in enumerate(lines, 1):
        if "ERROR" in line or "FATAL" in line or "TIMEOUT" in line:
            incidents.append({
                "line": idx,
                "message": line.strip(),
                "severity": "ERROR",
            })
    return incidents