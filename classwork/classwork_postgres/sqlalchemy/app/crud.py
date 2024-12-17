from db import Session
from schemas import UserModel
from models import UserDB

def create_user(db: Session, user: UserModel):
  password = str(hash(user.password))
  db_user = UserDB(username = user.username, password = password, email = user.email, image_url = user.image_url, full_name = user.full_name, is_admin = user.is_admin)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def get_user_by_email(db: Session, email: str):
  return db.query(UserDB).filter(email == UserDB.email).first()