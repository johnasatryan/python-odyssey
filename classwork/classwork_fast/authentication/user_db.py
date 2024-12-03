import json
from passlib.context import CryptContext


pwd_context = CryptContext(schemes='sha256_crypt')

def _initialize_user_file(users: dict):
  try:
    with open('users.json', 'w') as file:
      json.dump(users, file, indent=2)
  except json.JSONDecodeError:
    pass
   
  
def _read_users_db() -> dict:
  try:
    with open('users.json') as file:
      return json.load(file)
  except FileNotFoundError:
    return {}


def hash_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
  return pwd_context.verify(plain_password, hashed_password)


def register_user(username: str, password: str):
  db = _read_users_db()
  if username in db:
    return False
  db[username] = {"username": username, "password": hash_password(password)}
  _initialize_user_file(db)
  return True

def authenticate_user(username: str, password: str) -> bool:
  db = _read_users_db()
  user = db.get(username)
  if not user:
    return False
  
  return verify_password(password, user["password"])