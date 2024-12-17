from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends,HTTPException
import asyncpg
from  db import DATABASE_URL, get_db
import models
import uvicorn
import schemas


@asynccontextmanager
async def lifespan(app:FastAPI):
  app.state.pool = await asyncpg.create_pool(DATABASE_URL)
  print("Connection initialized")
  async with app.state.pool.acquire() as conn:
    await conn.execute(models.CREATE_USERS_TABLE_QUERY)
  try:
    yield
  finally:
    if app.state.pool:
      app.state.pool.close()
      print("closed")
    
        


app=FastAPI(lifespan=lifespan)

@app.post("/users", response_model=schemas.UserModel)
async def create_user(user: schemas.UserModel, db = Depends(get_db)):
  existing_user= await db.fetchrow(models.GET_USER_BY_EMAIL, user.email)
  if existing_user:
    raise HTTPException(400, "Email already exists")
  
  password=str(hash(user.password))
  new_user=await db.fetchrow(models.INSERT_USER_QUERY, user.username, password, user.email, user.image_url, user.full_name, user.is_admin)
  return dict(new_user)
  
    
     


if __name__=="__main__":
  uvicorn.run("main:app", port=3001, reload=True )