"""Database utilities and connection management."""

import os
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


def get_database_url() -> str:
    """Get database URL from environment."""
    database_url = os.getenv(
        "DATABASE_URL", "postgresql://fodeen:fodeen_dev@localhost:5432/fodeen_agents"
    )
    # Convert psycopg2 URL to asyncpg if needed
    if database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://")
    return database_url


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Get database session for dependency injection."""
    database_url = get_database_url()
    engine = create_async_engine(database_url, echo=False)
    async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        yield session
