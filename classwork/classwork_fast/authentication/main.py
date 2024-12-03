from fastapi import FastAPI, HTTPException, Request, Form, status, Response, Cookie, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from user_db import register_user, authenticate_user
import uvicorn
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
load_dotenv()

PORT = int(os.environ.get('PORT'))
sessions = {}


templates = Jinja2Templates(directory='templates')

app =FastAPI()

@app.get("/", response_class=HTMLResponse) 
async def home(request: Request):
  return templates.TemplateResponse('login.html', {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def regiser(request: Request):
  return templates.TemplateResponse('register.html', {"request": request})

@app.post("/register")
async def register_user_form(username: str = Form(...), password: str = Form(...)):
  if not register_user(username, password):
    raise HTTPException(status_code=400, detail='Username already exist')
  return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)

@app.post("/login")
async def login_user(response: Response, username: str = Form(...), password: str = Form(...)):
  if not authenticate_user(username, password):
    raise HTTPException(status_code=401, detail="Invalid credentials")
  sessions[username] = True
  redirect_response = RedirectResponse(url='/secure', status_code=status.HTTP_303_SEE_OTHER)
  redirect_response.set_cookie(key="username", value=username)

  return redirect_response

def get_current_username(username: str = Cookie(None)):
  if not username:
    raise HTTPException(status_code=401, detail = "Not authenticated")
  return username

@app.get("/secure")
async def secure_page(request: Request, username: str=Depends(get_current_username)):
  if username not in sessions:
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
  return templates.TemplateResponse("secure.html", {"request": request, "username": username})

@app.get("/logout")
def logout_user(response: Response):
  # redirect_response = RedirectResponse(url="/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
  response.delete_cookie('username')



if __name__ == '__main__':
  uvicorn.run('main:app', port=PORT, reload=True)