"""Unit tests for mapping agent."""

from fastapi.testclient import TestClient


def test_health_endpoint(mapping_client: TestClient) -> None:
    """Test health check endpoint."""
    response = mapping_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "mapping-agent"


def test_map_text(mapping_client: TestClient) -> None:
    """Test mapping text to ontology."""
    request_data = {"text": "2 apples"}
    response = mapping_client.post("/api/v1/map", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "2 apples"
    assert "confidence" in data
    assert "alternatives" in data
