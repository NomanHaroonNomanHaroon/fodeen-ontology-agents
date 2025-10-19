"""Base schemas used across all agents."""

from datetime import datetime

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = Field(..., description="Service status")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    service: str = Field(..., description="Service name")
    version: str = Field(default="0.1.0", description="Service version")


class ErrorResponse(BaseModel):
    """Standard error response."""

    error: str = Field(..., description="Error message")
    detail: str | None = Field(None, description="Detailed error information")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class OntologyNode(BaseModel):
    """Represents a node in the ontology graph."""

    id: str = Field(..., description="Unique identifier for the node")
    label: str = Field(..., description="Human-readable label")
    category: str = Field(..., description="Ontology category (e.g., food, unit, property)")
    attributes: dict = Field(default_factory=dict, description="Additional attributes")
    embedding: list[float] | None = Field(None, description="Vector embedding")


class MappingRequest(BaseModel):
    """Request to map unstructured text to ontology."""

    text: str = Field(..., description="Input text to map")
    context: dict | None = Field(None, description="Additional context for mapping")


class MappingResponse(BaseModel):
    """Response from mapping service."""

    text: str = Field(..., description="Original input text")
    mapped_node_id: str | None = Field(None, description="ID of matched ontology node")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    alternatives: list[dict] = Field(default_factory=list, description="Alternative matches")
