"""Unit tests for shared schemas."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from shared.schemas.base import (
    ErrorResponse,
    HealthResponse,
    MappingRequest,
    MappingResponse,
    OntologyNode,
)


def test_health_response() -> None:
    """Test HealthResponse schema."""
    health = HealthResponse(status="healthy", service="test-service")
    assert health.status == "healthy"
    assert health.service == "test-service"
    assert isinstance(health.timestamp, datetime)


def test_error_response() -> None:
    """Test ErrorResponse schema."""
    error = ErrorResponse(error="Test error", detail="Detailed information")
    assert error.error == "Test error"
    assert error.detail == "Detailed information"
    assert isinstance(error.timestamp, datetime)


def test_ontology_node() -> None:
    """Test OntologyNode schema."""
    node = OntologyNode(
        id="node_001",
        label="Test Node",
        category="food_item",
        attributes={"key": "value"},
    )
    assert node.id == "node_001"
    assert node.label == "Test Node"
    assert node.category == "food_item"
    assert node.attributes == {"key": "value"}
    assert node.embedding is None


def test_ontology_node_with_embedding() -> None:
    """Test OntologyNode with embedding."""
    node = OntologyNode(
        id="node_002",
        label="Test Node",
        category="unit_of_measure",
        embedding=[0.1, 0.2, 0.3],
    )
    assert node.embedding == [0.1, 0.2, 0.3]


def test_mapping_request() -> None:
    """Test MappingRequest schema."""
    request = MappingRequest(text="apple", context={"location": "US"})
    assert request.text == "apple"
    assert request.context == {"location": "US"}


def test_mapping_response() -> None:
    """Test MappingResponse schema."""
    response = MappingResponse(
        text="apple",
        mapped_node_id="food_001",
        confidence=0.95,
        alternatives=[{"id": "food_002", "confidence": 0.75}],
    )
    assert response.text == "apple"
    assert response.mapped_node_id == "food_001"
    assert response.confidence == 0.95


def test_mapping_response_confidence_validation() -> None:
    """Test confidence score validation."""
    with pytest.raises(ValidationError):
        MappingResponse(text="apple", confidence=1.5)  # Invalid: > 1.0

    with pytest.raises(ValidationError):
        MappingResponse(text="apple", confidence=-0.5)  # Invalid: < 0.0
