from typing import Dict, Any


def generate_cookbook(incident: Dict[str, Any], rca: Dict[str, Any]) -> Dict[str, Any]:
    steps = [
        "Review RCA findings",
        "Validate affected service",
        "Apply recommended remediation",
    ]
    commands = [
        "kubectl get pods -n <namespace>",
        "kubectl logs -f <pod> -n <namespace>",
    ]
    validation = "Service health checks return 200"
    rollback = "Revert deployment to previous replica set"

    return {
        "steps": steps,
        "commands": commands,
        "validation": validation,
        "rollback": rollback,
    }