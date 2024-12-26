from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import  sessionmaker
from config import settings
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

from models import Base

engine = create_async_engine(settings.database_url, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)




async def get_db():
    async with async_session() as session:
      yield session
  
async def create_database_if_not_exists():
    try:
      DEFAULT_URL = "postgresql+asyncpg://odyssey:password@localhost/postgres"
      TARGET_DB = "banking_system"

      engine = create_async_engine(DEFAULT_URL, echo=False, isolation_level='AUTOCOMMIT')  
      async with engine.connect() as conn:
        result = await conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname= '{TARGET_DB}'"))

        if not result.scalar():
          print(f'Database {TARGET_DB} does not exist. Creating it...')
          await conn.execute(text(f'CREATE DATABASE "{TARGET_DB}"'))
          print(f"Database {TARGET_DB} created successfully.")
        else:
           print(f"Database {TARGET_DB} already exists.")
        
      
    except SQLAlchemyError as e:
      print(f"Error while creating database: {e}")
    finally:
      await engine.dispose()        


   