from typing import Dict, Any

def generate_rca(incident: Dict[str, Any]) -> Dict[str, Any]:
    message = incident.get("message", "")
    severity = incident.get("severity", "ERROR")

    primary_cause = "Application error based on log analysis"
    evidence = f"Log line: {message}"
    alternative_causes = ["Infrastructure issue", "Dependency failure"]
    confidence = 0.85 if severity == "ERROR" else 0.7

    return {
        "primary_cause": primary_cause,
        "evidence": evidence,
        "alternative_causes": alternative_causes,
        "confidence": confidence,
    }