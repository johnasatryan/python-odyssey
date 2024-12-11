from fastapi import FastAPI, Request, HTTPException
from router import users_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time

app = FastAPI(title='simple app', description='Creating a test version of dependency', version='1.0.0')

app.include_router(users_router)


# @app.middleware('http')
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     print("middleware start execution")
#     response = await call_next(request)
#     print("middleware continue working ")
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


@app.middleware('http')
async def authentication(request: Request, call_next):
  token = request.headers['authorization']
  if token:
    response = await call_next(request)
    return response
  raise HTTPException(status_code=400, detail='hajoxutyun')


@app.get('/')
async def root():
  print("root called")
  return {"message": "Welcome to our website"}


if __name__ == '__main__':
  uvicorn.run('main:app', host='0.0.0.0', port=3001, reload=True)