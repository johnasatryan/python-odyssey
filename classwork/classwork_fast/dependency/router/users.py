from fastapi import FastAPI, Depends, status, HTTPException, Request, Query
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix ='/users', tags = ['Users'])

users = {}


def username_validation(username):
  if not username:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Username must be filled")
  if username in users:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "User already exist")
  return True


# @router.get('/')
# def get_users():
#   return users


# @router.post('/')
# def create_user(request: Request, user: dict):
#   print(request['headers'])
#   if username_validation(user.get('username')):
#     users[user.get('username')] = user
  
#   return JSONResponse({"message" : "User created successfully"}, status_code=status.HTTP_201_CREATED)

def validate_user(username: str, password: str) -> dict:

  if not username:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Username must be filled")
  user = {username : password}
  return user


@router.get('/')
def create_user(request: Request, user: dict = Depends(validate_user)):
  return users


@router.post('/')
def create_user(user: dict):
  print(user)
  return users