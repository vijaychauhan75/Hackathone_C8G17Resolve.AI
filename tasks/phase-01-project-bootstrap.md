# Phase 01 – Project Bootstrap

## Objective
Establish repository and base architecture.

## Scope
Create monorepo-style layout with `frontend/` and `backend/`, minimal runnable scaffold, env example, and docs skeleton.

## Dependencies
None.

## Implementation Tasks
- Initialize Next.js frontend
- Initialize FastAPI backend
- Configure Tailwind + shadcn-compatible aliases
- Create environment example
- Write README + task files

## Deliverables
- `frontend/` scaffold
- `backend/` scaffold
- `docs/` and `tasks/` directories
- `.env.example`

## Acceptance Criteria
- `cd frontend && npm run dev` starts
- `cd backend && uvicorn main:app --reload` starts

## Definition of Done
- Both apps run locally
- Repo structure matches spec

## Suggested Git Commit
`feat: bootstrap project structure`