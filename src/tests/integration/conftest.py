import asyncio

import pytest
import pytest_asyncio
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from adapters.orm_engines.models import Base
from core.settings import TestSettings


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    asyncio.set_event_loop(loop)
    loop._close = loop.close
    loop.close = lambda: None
    yield loop
    loop._close()


@pytest.fixture(scope="session")
def engine():
    db_url = URL.create(**TestSettings().get_db_creds)
    engine = create_async_engine(db_url, echo=True)
    yield engine
    engine.sync_engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def create(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="session")
async def session(engine, create):
    async with AsyncSession(engine) as async_session:
        yield async_session
