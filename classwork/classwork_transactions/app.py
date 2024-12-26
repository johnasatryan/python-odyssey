from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_database_if_not_exists
import uvicorn
from models import Base
from database import engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import  sessionmaker
from account_router import router as account_router
from transaction_router import router as transaction_router


async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@asynccontextmanager
async def lifespan(app:FastAPI):
  try:
    await create_database_if_not_exists()
    async with engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)
    yield
  except Exception as e:
    print(f"Unexpected error during lifespan setup: {e}")
  finally:
    print("Database connection closed")
   

app = FastAPI(title='Banking System', description='Simple CRUD with transactions', version='1.0.0', lifespan=lifespan)

app.include_router(account_router)
app.include_router(transaction_router)

if __name__ == '__main__':
  from config import settings
  uvicorn.run('app:app', port=settings.port, reload=True)