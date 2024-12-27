from routers import auth_router, products_router, users_router, orders_router
from contextlib import asynccontextmanager
from database.db import create_db, create_tables
from fastapi import FastAPI
from config import settings
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)

if __name__ == "__main__":
    uvicorn.run("app:app", port=settings.app_port, reload=True)
