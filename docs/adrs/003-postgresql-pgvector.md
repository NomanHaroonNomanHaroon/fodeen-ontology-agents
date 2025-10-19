# ADR 003: PostgreSQL with pgvector Extension

## Status
Accepted

## Context
The system needs to:
- Store ontology nodes with complex relationships
- Perform vector similarity search for text-to-ontology mapping
- Handle structured data with ACID guarantees
- Support full-text search capabilities

## Decision
We will use PostgreSQL with the pgvector extension as our primary database.

## Rationale
- **Unified storage**: Single database for both structured data and vectors
- **ACID guarantees**: Strong consistency for critical data
- **Mature ecosystem**: Well-understood, battle-tested database
- **pgvector**: Native vector similarity search without external dependencies
- **Rich querying**: SQL for complex queries, JSON support for flexible schemas
- **Cost-effective**: No need for separate vector database
- **Schema support**: Natural multi-tenancy with PostgreSQL schemas

## Consequences
- Need to manage PostgreSQL upgrades and pgvector compatibility
- Vector search may not be as fast as specialized vector databases at very large scale
- Requires understanding of vector operations and indexing strategies
- All agents share the same database instance (but different schemas)

## Alternatives Considered
- **Separate vector database** (e.g., Pinecone, Weaviate):
  - Rejected: Adds operational complexity and cost
- **Elasticsearch**: For both search and storage
  - Rejected: Overkill for our use case, less suitable for structured data
- **SQLite**: Lightweight option
  - Rejected: Limited concurrency and no native vector support
