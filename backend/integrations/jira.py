from typing import Dict, Any


def create_jira_ticket(payload: Dict[str, Any]) -> Dict[str, Any]:
    # Mock Jira ticket creation for hackathon
    return {
        "key": "MOCK-123",
        "url": "https://jira.example.com/browse/MOCK-123",
        "payload": payload,
    }