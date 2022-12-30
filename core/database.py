from typing import Generator
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession
)
from sqlalchemy.ext.declarative import declarative_base
from core.configs import database as dbconf


engine: AsyncEngine = create_async_engine(dbconf.DB_URL)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

DBBaseModel = declarative_base()

async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
