# Fodeen Ontology Agents

Portable, test-driven ontology + multi-agent system for mapping food (and beyond) from noisy text to canonical items, units, and inventory.

[![CI](https://github.com/wildhash/fodeen-ontology-agents/workflows/CI/badge.svg)](https://github.com/wildhash/fodeen-ontology-agents/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## Overview

Fodeen Ontology Agents is a microservices-based system that provides intelligent ontology management and mapping capabilities for food inventory systems. It uses a multi-agent architecture where specialized services work together to:

- **Manage canonical ontologies** for food items, units, and properties
- **Map unstructured text** (e.g., "2 lbs apples") to structured ontology nodes
- **Convert units** between different measurement systems
- **Validate data** against ontology constraints
- **Track inventory** with semantic understanding

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Applications                       │
└──────────────┬──────────────────────────────────────────────────┘
               │
               ├──────────────┬──────────────┬──────────────┬──────┐
               │              │              │              │      │
       ┌───────▼──────┐ ┌────▼─────┐ ┌──────▼─────┐ ┌─────▼──────┐
       │  Ontology    │ │ Mapping  │ │    UoM     │ │  Reranking │
       │   Agent      │ │  Agent   │ │   Agent    │ │   Agent    │
       │  (port 8001) │ │(port 8002)│ │(port 8003) │ │(port 8004) │
       └──────┬───────┘ └────┬─────┘ └──────┬─────┘ └─────┬──────┘
              │              │              │              │
       ┌──────▼──────┐ ┌────▼─────────────────────────────▼──────┐
       │ Conformance │ │          Inventory Agent                │
       │   Agent     │ │            (port 8006)                  │
       │(port 8005)  │ └─────────────────┬────────────────────────┘
       └──────┬──────┘                   │
              │                          │
              └──────────────┬───────────┘
                             │
                    ┌────────▼─────────┐
                    │   PostgreSQL     │
                    │   + pgvector     │
                    └──────────────────┘
```

### Agent Responsibilities

| Agent | Purpose | Port |
|-------|---------|------|
| **Ontology** | Manages canonical ontology graph | 8001 |
| **Mapping** | Maps text to ontology nodes | 8002 |
| **UoM** | Unit of measure conversions | 8003 |
| **Reranking** | Improves search relevance | 8004 |
| **Conformance** | Validates data against rules | 8005 |
| **Inventory** | Tracks stock and inventory | 8006 |

## Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Make (optional, for convenience commands)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wildhash/fodeen-ontology-agents.git
   cd fodeen-ontology-agents
   ```

2. **Set up development environment**
   ```bash
   make setup
   # or manually:
   pip install -r requirements-dev.txt
   pre-commit install
   ```

3. **Start services with Docker Compose**
   ```bash
   make docker-up
   # or manually:
   docker-compose up -d
   ```

4. **Verify services are running**
   ```bash
   curl http://localhost:8001/health  # Ontology Agent
   curl http://localhost:8002/health  # Mapping Agent
   curl http://localhost:8003/health  # UoM Agent
   ```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run linting and type checks
make lint
make type-check

# Run all checks
make check
```

### Development Workflow

1. **Run a single agent locally**
   ```bash
   make run-ontology
   # Access at http://localhost:8001/docs for OpenAPI docs
   ```

2. **Format code**
   ```bash
   make format
   ```

3. **Run pre-commit hooks**
   ```bash
   make pre-commit
   ```

## Project Structure

```
fodeen-ontology-agents/
├── agents/                  # Agent services
│   ├── ontology/           # Ontology management
│   ├── mapping/            # Text-to-ontology mapping
│   ├── uom/                # Unit of measure conversions
│   ├── reranking/          # Search result reranking
│   ├── conformance/        # Data validation
│   └── inventory/          # Inventory tracking
├── shared/                  # Shared code
│   ├── schemas/            # Pydantic models
│   ├── contracts/          # API contracts
│   └── utils/              # Common utilities
├── data/                    # Data files
│   ├── releases/           # Schema definitions
│   │   ├── ontology_v1.schema.json
│   │   └── attribute_dictionary.json
│   └── golden/             # Golden test data
│       └── sample_nodes.jsonl
├── tests/                   # Test suite
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── e2e/                # End-to-end tests
├── docs/                    # Documentation
│   └── adrs/               # Architecture Decision Records
├── scripts/                 # Utility scripts
├── docker-compose.yml       # Service orchestration
├── Dockerfile              # Container definition
├── Makefile                # Development commands
└── pyproject.toml          # Python project config
```

## API Documentation

Each agent exposes OpenAPI documentation at `/docs`:

- Ontology Agent: http://localhost:8001/docs
- Mapping Agent: http://localhost:8002/docs
- UoM Agent: http://localhost:8003/docs
- Reranking Agent: http://localhost:8004/docs
- Conformance Agent: http://localhost:8005/docs
- Inventory Agent: http://localhost:8006/docs

## Technology Stack

- **Language**: Python 3.11
- **Web Framework**: FastAPI
- **Database**: PostgreSQL 16 + pgvector
- **Testing**: pytest, hypothesis, pytest-asyncio
- **Validation**: Pydantic
- **Code Quality**: ruff, black, mypy
- **CI/CD**: GitHub Actions
- **Containerization**: Docker, Docker Compose

## Configuration

Configuration is managed through environment variables:

```bash
# Database
DATABASE_URL=postgresql://fodeen:fodeen_dev@localhost:5432/fodeen_agents

# Agent-specific
AGENT_PORT=8001
ONTOLOGY_AGENT_URL=http://ontology-agent:8001
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`make check`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Architecture Decision Records

See [docs/adrs/](docs/adrs/) for key architectural decisions:

- [ADR 001: Monorepo Architecture](docs/adrs/001-monorepo-architecture.md)
- [ADR 002: Agent-Based Architecture](docs/adrs/002-agent-based-architecture.md)
- [ADR 003: PostgreSQL with pgvector](docs/adrs/003-postgresql-pgvector.md)
- [ADR 004: Testing Strategy](docs/adrs/004-testing-strategy.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
