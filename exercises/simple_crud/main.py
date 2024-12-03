from fastapi import FastAPI, HTTPException
import uvicorn
import dotenv
import os
from utils import read_file_json, write_file_json
from models import User


dotenv.load_dotenv()

PORT = int(os.environ.get('PORT', 8080))
USERS_FILE = os.environ.get('USERS_FILE')
TASKS_FILE = os.environ.get('TASKS_FILE')


app = FastAPI()

@app.on_event('startup')
async def startup_event():
  await write_file_json(USERS_FILE, [])
  await write_file_json(TASKS_FILE, [])


@app.get('/')
def home():
  return 'Our task api'


# Users CRUD

@app.get('/users')
async def get_users():
  return await read_file_json(USERS_FILE)


@app.get('/users/{user_id}')
async def get_user(user_id: int):
  users = await read_file_json(USERS_FILE)

  for user in users:
    if user['id'] == user_id:
      # if user['password'] == 
      pass
  raise HTTPException(status_code=404, detail="User not found")

@app.post('/users')
async def create_user(user: User):
  users = await read_file_json(USERS_FILE)
  user.id = len(users) + 1
  users.append(user.model_dump())
  await write_file_json(USERS_FILE, users)
  return user
  
if __name__ == '__main__':
  uvicorn.run('main:app', port=PORT, reload=True)