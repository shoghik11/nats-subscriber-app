
from app.data.database import get_db_pool

async def save_message(content: str):
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            "INSERT INTO messages (content) VALUES ($1)", content
        )
