from fastapi import FastAPI, HTTPException, Request, Form, status, Response, Cookie, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from users_db import register_user, authenticate_user
import uvicorn
from fastapi.security import OAuth2PasswordBearer
from model import User
from auth import create_jwt_token, verify_jwt_token
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from config import Config

config = Config()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




templates = Jinja2Templates(directory='templates')

app =FastAPI()

@app.get("/", response_class=HTMLResponse) 
async def home(request: Request):
  return templates.TemplateResponse('login.html', {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def regiser(request: Request):
  return templates.TemplateResponse('register.html', {"request": request})

@app.post("/register")
async def register_user_form(user: User):
  if not register_user(user):
    raise HTTPException(status_code=400, detail='Username already exist')
  return {"message": "Registered successfully", "path": "/"}

@app.post("/login")
async def login_user(user: User):
  if not authenticate_user(user):
    raise HTTPException(status_code=401, detail="Invalid credentials")
  
  auth_token = create_jwt_token({"sub": user.username})
  return {"auth_token": auth_token}



@app.get("/secure")
async def secure_page(request: Request, token: str=Depends(oauth2_scheme)):
  print(token)
  username = verify_jwt_token(token)
  print(username)
  return templates.TemplateResponse("secure.html", {"request": request, "username": username})

@app.get("/logout")
def logout_user(response: Response):
  # redirect_response = RedirectResponse(url="/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
  response.delete_cookie('username')



if __name__ == '__main__':
  uvicorn.run('main:app', port=config.PORT, reload=True)