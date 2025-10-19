# ADR 002: Agent-Based Architecture

## Status
Accepted

## Context
The system needs to handle multiple concerns: ontology management, text-to-ontology mapping, unit conversions, result reranking, data validation, and inventory tracking. These concerns have different scaling requirements and update frequencies.

## Decision
We will implement a microservices architecture with specialized agents:

1. **Ontology Agent**: Manages the canonical ontology graph
2. **Mapping Agent**: Maps unstructured text to ontology nodes
3. **UoM Agent**: Handles unit of measure conversions
4. **Reranking Agent**: Improves search result relevance
5. **Conformance Agent**: Validates data against ontology rules
6. **Inventory Agent**: Manages stock and inventory operations

Each agent:
- Runs as an independent FastAPI service
- Has its own database schema
- Exposes a REST API
- Can be scaled independently

## Rationale
- **Separation of concerns**: Each agent has a single, well-defined responsibility
- **Independent scaling**: Agents can be scaled based on their individual load
- **Fault isolation**: Failure in one agent doesn't cascade to others
- **Technology flexibility**: Agents can use different libraries/approaches as needed
- **Team autonomy**: Different teams can own different agents

## Consequences
- Increased operational complexity (multiple services to deploy/monitor)
- Need for inter-agent communication mechanisms
- Requires distributed tracing and monitoring
- Each agent needs its own testing suite

## Alternatives Considered
- **Monolithic application**: Single service handling all concerns
  - Rejected: Would be harder to scale and maintain
- **Serverless functions**: Each operation as a function
  - Rejected: Adds cold start latency and complexity for this use case
