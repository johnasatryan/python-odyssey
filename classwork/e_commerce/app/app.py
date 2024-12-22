from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from routers import auth_router, users_router, products_router, orders_router
from models import db, OrderItem, Product, Order, User
from config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        # Create all tables
        await conn.run_sync(User.metadata.create_all)
        await conn.run_sync(Product.metadata.create_all)
        await conn.run_sync(Order.metadata.create_all)
        await conn.run_sync(OrderItem.metadata.create_all)
    yield  # Application runs here
    await db.engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=settings.app_port, reload=True)
