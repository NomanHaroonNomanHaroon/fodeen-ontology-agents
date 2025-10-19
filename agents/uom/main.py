"""UoM Agent - Handles unit of measure conversions and normalization."""

from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, Field

from shared.schemas.base import HealthResponse

app = FastAPI(
    title="UoM Agent",
    description="Handles unit of measure conversions and normalization",
    version="0.1.0",
)


class ConversionRequest(BaseModel):
    """Request for unit conversion."""

    value: float = Field(..., description="Value to convert")
    from_unit: str = Field(..., description="Source unit")
    to_unit: str = Field(..., description="Target unit")


class ConversionResponse(BaseModel):
    """Response from unit conversion."""

    original_value: float
    original_unit: str
    converted_value: float
    converted_unit: str


@app.get("/", response_model=HealthResponse)
async def root() -> HealthResponse:
    """Root endpoint returning service health."""
    return HealthResponse(
        status="healthy",
        service="uom-agent",
        timestamp=datetime.utcnow(),
    )


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        service="uom-agent",
        timestamp=datetime.utcnow(),
    )


@app.post("/api/v1/convert", response_model=ConversionResponse)
async def convert_unit(request: ConversionRequest) -> ConversionResponse:
    """
    Convert a value from one unit to another.

    Args:
        request: Conversion request with value and units

    Returns:
        Converted value
    """
    # Stub implementation - will use ontology unit definitions
    return ConversionResponse(
        original_value=request.value,
        original_unit=request.from_unit,
        converted_value=request.value,
        converted_unit=request.to_unit,
    )


@app.get("/api/v1/units")
async def list_units(dimension: str | None = None) -> dict:
    """
    List available units of measure.

    Args:
        dimension: Filter by dimension (mass, volume, length, count)

    Returns:
        List of available units
    """
    # Stub implementation
    return {"units": []}
