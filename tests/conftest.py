"""Pytest configuration and shared fixtures."""

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def ontology_client() -> TestClient:
    """Create test client for ontology agent."""
    from agents.ontology.main import app

    return TestClient(app)


@pytest.fixture
def mapping_client() -> TestClient:
    """Create test client for mapping agent."""
    from agents.mapping.main import app

    return TestClient(app)


@pytest.fixture
def uom_client() -> TestClient:
    """Create test client for UoM agent."""
    from agents.uom.main import app

    return TestClient(app)


@pytest.fixture
def reranking_client() -> TestClient:
    """Create test client for reranking agent."""
    from agents.reranking.main import app

    return TestClient(app)


@pytest.fixture
def conformance_client() -> TestClient:
    """Create test client for conformance agent."""
    from agents.conformance.main import app

    return TestClient(app)


@pytest.fixture
def inventory_client() -> TestClient:
    """Create test client for inventory agent."""
    from agents.inventory.main import app

    return TestClient(app)
