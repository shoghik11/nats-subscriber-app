
import pytest
import asyncio
from app.data.repository import save_message
from app.data.database import get_db_pool

@pytest.mark.asyncio
async def test_save_message():
    await save_message("Test message")

    pool = await get_db_pool()
    async with pool.acquire() as conn:
        result = await conn.fetchrow("SELECT content FROM messages ORDER BY id DESC LIMIT 1")
        assert result["content"] == "Test message"
