from dotenv import load_dotenv
import os 
import asyncpg
import asyncio


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_connection_pool():
  return await asyncpg.create_pool(DATABASE_URL)

async def get_db():
  pool = await get_connection_pool()
  async with pool.acquire() as conn:
    try:
      yield conn
    finally:
      pass
    


