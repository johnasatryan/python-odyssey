from fastapi import FastAPI, status, Response
import json

users = []

app = FastAPI()



@app.get('/')
def read_get():
  """Home dnpoint to confirm that server is running"""
  return {"message": "Welcome to our..."}

@app.get('/users')
def get_usres():
  return users

@app.post('/users', status_code=201)
def create_user(user: dict, response : Response):
  for _user in users:
    if user['email'] in _user.values():
      
      return Response(json.dumps({"message": "User already exist"}), status_code=400)
  users.append(user)
  return users