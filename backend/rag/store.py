from typing import List, Dict, Any

class RagStore:
    def __init__(self):
        self.docs: List[Dict[str, Any]] = []

    def index_documents(self, docs: List[Dict[str, Any]]) -> None:
        self.docs.extend(docs)

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        scored = []
        for doc in self.docs:
            score = 0.0
            if query.lower() in doc.get("text", "").lower():
                score = 1.0
            scored.append({**doc, "score": score})

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

rag_store = RagStore()