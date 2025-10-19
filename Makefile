.PHONY: help install install-dev setup clean lint format type-check test test-cov docker-build docker-up docker-down docker-logs db-init pre-commit

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements-dev.txt
	pre-commit install

setup: install-dev ## Complete development setup
	@echo "Development environment setup complete!"

clean: ## Clean up temporary files and caches
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ .coverage coverage.xml

lint: ## Run linting checks
	ruff check agents/ shared/ tests/

format: ## Format code with black and ruff
	black agents/ shared/ tests/
	ruff check --fix agents/ shared/ tests/

type-check: ## Run type checking with mypy
	mypy agents/ shared/

test: ## Run tests
	pytest tests/ -v

test-cov: ## Run tests with coverage report
	pytest tests/ -v --cov --cov-report=term-missing --cov-report=html

test-watch: ## Run tests in watch mode
	pytest-watch tests/ -v

docker-build: ## Build Docker images
	docker-compose build

docker-up: ## Start all services with Docker Compose
	docker-compose up -d

docker-down: ## Stop all services
	docker-compose down

docker-logs: ## Show logs from all services
	docker-compose logs -f

docker-restart: docker-down docker-up ## Restart all services

db-init: ## Initialize database (requires postgres to be running)
	PGPASSWORD=fodeen_dev psql -h localhost -U fodeen -d fodeen_agents -f scripts/init-db.sql

pre-commit: ## Run pre-commit hooks on all files
	pre-commit run --all-files

check: lint type-check test ## Run all checks (lint, type-check, test)

ci: check ## Run CI pipeline locally

# Agent-specific targets
run-ontology: ## Run ontology agent locally
	uvicorn agents.ontology.main:app --host 0.0.0.0 --port 8001 --reload

run-mapping: ## Run mapping agent locally
	uvicorn agents.mapping.main:app --host 0.0.0.0 --port 8002 --reload

run-uom: ## Run UoM agent locally
	uvicorn agents.uom.main:app --host 0.0.0.0 --port 8003 --reload

run-reranking: ## Run reranking agent locally
	uvicorn agents.reranking.main:app --host 0.0.0.0 --port 8004 --reload

run-conformance: ## Run conformance agent locally
	uvicorn agents.conformance.main:app --host 0.0.0.0 --port 8005 --reload

run-inventory: ## Run inventory agent locally
	uvicorn agents.inventory.main:app --host 0.0.0.0 --port 8006 --reload
