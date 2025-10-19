FROM python:3.11-slim

ARG AGENT_NAME=ontology

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY agents/ ./agents/
COPY shared/ ./shared/
COPY data/ ./data/

# Expose port (default, can be overridden)
EXPOSE 8000

# Default command (will be overridden by docker-compose)
CMD ["uvicorn", "agents.${AGENT_NAME}.main:app", "--host", "0.0.0.0", "--port", "8000"]
