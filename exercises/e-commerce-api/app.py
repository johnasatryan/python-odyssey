from fastapi import FastAPI
from routers import users_router, products_router, orders_router
from database import initialize_database
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# Create the FastAPI application
app = FastAPI(
    title="E-Commerce API",
    description="A FastAPI-powered backend for managing users, products, and orders.",
    version="1.0.0"
)

# Middleware for CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialize_database()

app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)

@app.get("/")
def read_root():
    """
    Root endpoint providing API information.
    """
    return {"message": "Welcome to the E-Commerce API!", "version": "1.0.0"}


if __name__ == "__main__":
    uvicorn.run('app:app', port=3001)