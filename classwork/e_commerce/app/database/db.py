from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from config import settings

DATABASE_URL = settings.database_url + settings.target_db
engine = create_async_engine(DATABASE_URL, echo=False, isolation_level="AUTOCOMMIT")
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
  async with async_session() as session:
    yield session

  
async def create_db():
  try:
    target_db_url = settings.database_url + settings.default_db
    target_engine = create_async_engine(target_db_url, echo=False, isolation_level="AUTOCOMMIT")
    async with target_engine.connect() as conn:
      result = await conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname= '{settings.target_db}'"))
      if not result.scalar():
        print(f'Database {settings.target_db} does not exist. Creating it...')
        await conn.execute(text(f'CREATE DATABASE "{settings.target_db}"'))
        print(f"Database {settings.target_db} created successfully.")
  except Exception as e:
    print(f"Error during database creation: {e}")
    await engine.dispose()


async def create_tables():
  try:
    async with engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)
  except Exception as e:
    print(f"Error during tables creation: {e}")
    await engine.dispose()