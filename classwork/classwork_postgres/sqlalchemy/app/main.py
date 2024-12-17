from fastapi import FastAPI, Depends,HTTPException
from models import Base
from db import engine
from schemas import UserModel
from db import Session, get_db
import uvicorn
import crud


app = FastAPI()

@app.on_event("startup")
def startup():
  try:
    Base.metadata.create_all(bind=engine)
    print("tables are created")
  except Exception as e:
    print(e)

@app.post('/users', response_model=UserModel)
def create_user(user: UserModel, db: Session = Depends(get_db)):
  existing_user = crud.get_user_by_email(db, user.email)
  if existing_user:
    raise HTTPException(status_code=400, detail="email already exists")
  # existing_user = crud.create_user(db, user)
  return crud.create_user(db, user)


if __name__ == "__main__":
  uvicorn.run("main:app", port=3001, reload=True)