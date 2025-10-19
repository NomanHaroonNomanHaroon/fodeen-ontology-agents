"""Unit tests for ontology agent."""

from fastapi.testclient import TestClient


def test_health_endpoint(ontology_client: TestClient) -> None:
    """Test health check endpoint."""
    response = ontology_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "ontology-agent"


def test_root_endpoint(ontology_client: TestClient) -> None:
    """Test root endpoint."""
    response = ontology_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_list_nodes_empty(ontology_client: TestClient) -> None:
    """Test listing nodes returns empty list initially."""
    response = ontology_client.get("/api/v1/nodes")
    assert response.status_code == 200
    assert response.json() == []


def test_get_node_not_found(ontology_client: TestClient) -> None:
    """Test getting non-existent node returns 404."""
    response = ontology_client.get("/api/v1/nodes/nonexistent")
    assert response.status_code == 404


def test_create_node(ontology_client: TestClient) -> None:
    """Test creating a node."""
    node_data = {
        "id": "test_001",
        "label": "Test Item",
        "category": "food_item",
        "attributes": {},
    }
    response = ontology_client.post("/api/v1/nodes", json=node_data)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == "test_001"
    assert data["label"] == "Test Item"


def test_search_nodes(ontology_client: TestClient) -> None:
    """Test searching nodes."""
    response = ontology_client.get("/api/v1/search?q=apple")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert data["query"] == "apple"
