# Phase 06 – RAG Pipeline

## Objective
Build knowledge retrieval.

## Scope
Confluence/Google Drive ingestion, LanceDB indexing, and weekly incremental sync.

## Dependencies
- Phase 5 complete

## Implementation Tasks
- Ingestion adapters
- Chunking + embedding
- LanceDB store
- Weekly re-index modified docs

## Deliverables
- Working RAG retrieval for remediation

## Acceptance Criteria
- Queries return grounded sources or “no docs found”

## Definition of Done
- RAG pipeline indexes and retrieves docs

## Suggested Git Commit
`feat: implement RAG pipeline`