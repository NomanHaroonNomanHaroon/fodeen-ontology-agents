# Quick Start Guide

Get up and running with Fodeen Ontology Agents in 5 minutes.

## Prerequisites

- Python 3.11+ installed
- Docker and Docker Compose installed
- Git installed

## 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/wildhash/fodeen-ontology-agents.git
cd fodeen-ontology-agents

# Install dependencies
make setup

# Or manually:
pip install -r requirements-dev.txt
pre-commit install
```

## 2. Start Services

### Using Docker Compose (Recommended)

```bash
# Start all services
make docker-up

# View logs
make docker-logs

# Stop all services
make docker-down
```

Services will be available at:
- Ontology Agent: http://localhost:8001
- Mapping Agent: http://localhost:8002
- UoM Agent: http://localhost:8003
- Reranking Agent: http://localhost:8004
- Conformance Agent: http://localhost:8005
- Inventory Agent: http://localhost:8006
- PostgreSQL: localhost:5432

### Running Individual Agents Locally

```bash
# Terminal 1: Start ontology agent
make run-ontology

# Terminal 2: Start mapping agent
make run-mapping

# Terminal 3: Start UoM agent
make run-uom
```

## 3. Verify Installation

```bash
# Check all agents are healthy
curl http://localhost:8001/health
curl http://localhost:8002/health
curl http://localhost:8003/health
```

## 4. Explore APIs

Each agent provides interactive API documentation:

- Ontology: http://localhost:8001/docs
- Mapping: http://localhost:8002/docs
- UoM: http://localhost:8003/docs
- Reranking: http://localhost:8004/docs
- Conformance: http://localhost:8005/docs
- Inventory: http://localhost:8006/docs

## 5. Run Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test file
pytest tests/unit/test_ontology_agent.py -v
```

## 6. Development Workflow

```bash
# Format code
make format

# Run linting
make lint

# Run type checking
make type-check

# Run all checks
make check

# Run pre-commit hooks
make pre-commit
```

## Example Usage

### Create an Ontology Node

```bash
curl -X POST http://localhost:8001/api/v1/nodes \
  -H "Content-Type: application/json" \
  -d '{
    "id": "food_apple",
    "label": "Apple",
    "category": "food_item",
    "attributes": {
      "perishable": true,
      "storage_temp": "refrigerated"
    }
  }'
```

### Map Text to Ontology

```bash
curl -X POST http://localhost:8002/api/v1/map \
  -H "Content-Type: application/json" \
  -d '{
    "text": "2 lbs of apples"
  }'
```

### Convert Units

```bash
curl -X POST http://localhost:8003/api/v1/convert \
  -H "Content-Type: application/json" \
  -d '{
    "value": 2.0,
    "from_unit": "lb",
    "to_unit": "kg"
  }'
```

## Common Tasks

### Viewing Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f ontology-agent
```

### Database Access

```bash
# Connect to PostgreSQL
docker-compose exec postgres psql -U fodeen -d fodeen_agents

# Run init script
make db-init
```

### Clean Up

```bash
# Remove temporary files
make clean

# Stop and remove containers
docker-compose down -v
```

## Troubleshooting

### Port Already in Use

If ports 8001-8006 are already in use, modify the port mappings in `docker-compose.yml`.

### Database Connection Issues

Ensure PostgreSQL is running and healthy:

```bash
docker-compose ps postgres
```

### Import Errors

Make sure you're in the project root and have installed dependencies:

```bash
pip install -r requirements-dev.txt
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## Next Steps

- Read the [Architecture Decision Records](docs/adrs/) to understand design decisions
- Explore the [data files](data/) to see sample ontology nodes
- Check out the [test suite](tests/) for usage examples
- Contribute by opening issues or pull requests

## Getting Help

- Check existing [issues](https://github.com/wildhash/fodeen-ontology-agents/issues)
- Review [documentation](docs/)
- Contact the maintainers
