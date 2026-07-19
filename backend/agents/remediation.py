from typing import Dict, Any, List
from rag.store import rag_store


def get_recommendations(incident: Dict[str, Any]) -> Dict[str, Any]:
    query = incident.get("message", "")
    sources = rag_store.retrieve(query, top_k=5)

    recommendations = []
    for src in sources:
        recommendations.append({
            "recommendation": f"Review documentation: {src.get('title', 'Unknown')}",
            "confidence": src.get("score", 0.0),
            "reason": "Retrieved from knowledge base",
            "supporting_sources": [src],
        })

    if not recommendations:
        recommendations.append({
            "recommendation": "No supporting documentation found.",
            "confidence": 0.0,
            "reason": "Knowledge base returned no matches",
            "supporting_sources": [],
        })

    jira_payload = {
        "summary": incident.get("message", "Incident"),
        "description": incident.get("message", ""),
    }

    return {
        "recommendations": recommendations,
        "jira_payload": jira_payload,
    }