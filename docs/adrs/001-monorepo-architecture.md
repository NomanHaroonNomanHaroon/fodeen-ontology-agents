# ADR 001: Monorepo Architecture

## Status
Accepted

## Context
We need to organize multiple microservices (agents) that work together to provide ontology management, mapping, unit conversion, and inventory functionality. The system requires shared code for schemas, contracts, and utilities.

## Decision
We will use a monorepo structure with the following organization:

```
/agents/{ontology,mapping,uom,reranking,conformance,inventory}
/shared/{schemas,contracts,utils}
/data/{releases,golden}
/tests/{unit,integration,e2e}
```

## Rationale
- **Atomic changes**: Changes to shared code and multiple agents can be deployed together
- **Code reuse**: Common schemas and utilities are easily shared across agents
- **Simplified CI/CD**: Single pipeline for building, testing, and deploying
- **Developer experience**: Easy to navigate and understand the entire system
- **Consistent tooling**: Shared configuration for linting, formatting, and testing

## Consequences
- Single repository to manage (simpler than multiple repos)
- Need good tooling to run/test individual agents
- Requires clear boundaries between agents to prevent tight coupling
- All agents share the same Python version and core dependencies

## Alternatives Considered
- **Multi-repo**: Each agent in its own repository
  - Rejected: Too much overhead for managing shared code and dependencies
- **Hybrid**: Shared library in separate repo
  - Rejected: Adds complexity without significant benefits at this scale
