import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database import Base
from dependencies import get_db
import pytest_asyncio
from httpx import AsyncClient, ASGITransport


# In-memory test database
engine_test = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_test
)

Base.metadata.create_all(bind=engine_test)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as ac:
        yield ac

@pytest.mark.asyncio
async def test_app_starts(client):
    response = await client.get("/")
    assert response.status_code in (200, 404)
