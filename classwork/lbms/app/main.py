from fastapi import FastAPI
from app.routes import users
import uvicorn
from app.helpers.config import settings

app = FastAPI()
app.include_router(users.router)

if __name__ == '__main__':
  uvicorn.run('main:app', port=settings.PORT, reload=True)