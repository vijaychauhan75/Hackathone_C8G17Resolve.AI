# Hackathone_C8G17Resolve.AI

Multi-Agent DevOps Incident Analysis Suite powered by LangGraph.

## Structure

- `frontend/` - Next.js 15 + Tailwind + shadcn/ui
- `backend/` - FastAPI + LangGraph
- `docs/` - Architecture docs
- `tasks/` - Phase task files

## Getting Started

### Frontend
cd frontend
npm run dev

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

## Environment
Copy `.env.example` to `.env` and configure secrets.