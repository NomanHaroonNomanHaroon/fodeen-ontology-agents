"""Mapping Agent - Maps unstructured text to canonical ontology nodes."""

from datetime import datetime

from fastapi import FastAPI

from shared.schemas.base import HealthResponse, MappingRequest, MappingResponse

app = FastAPI(
    title="Mapping Agent",
    description="Maps unstructured text to canonical ontology nodes",
    version="0.1.0",
)


@app.get("/", response_model=HealthResponse)
async def root() -> HealthResponse:
    """Root endpoint returning service health."""
    return HealthResponse(
        status="healthy",
        service="mapping-agent",
        timestamp=datetime.utcnow(),
    )


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        service="mapping-agent",
        timestamp=datetime.utcnow(),
    )


@app.post("/api/v1/map", response_model=MappingResponse)
async def map_text(request: MappingRequest) -> MappingResponse:
    """
    Map unstructured text to ontology nodes.

    Args:
        request: Mapping request with text and optional context

    Returns:
        Mapped node with confidence score and alternatives
    """
    # Stub implementation - will use embeddings and similarity search
    return MappingResponse(
        text=request.text,
        mapped_node_id=None,
        confidence=0.0,
        alternatives=[],
    )
