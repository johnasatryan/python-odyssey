import json
from passlib.context import CryptContext
from model import User
from config import Config

config = Config()
pwd_context = CryptContext(schemes='sha256_crypt')


def initialize_users_db():
  try:
    with open(config.FILE_PATH, mode='x') as file:
      json.dump({}, file)
  except FileExistsError:
    pass

def write_users_db(users):
  with open(config.FILE_PATH, mode='w') as file:
    json.dump(users, file, indent=2)


def read_users_db():
  try:
    with open(config.FILE_PATH) as file:
      return json.load(file)
  except json.JSONDecodeError:
    return {}
  
def register_user(user: User) -> bool:
  users = read_users_db()
  print(user)
  if user.username in users:
    return False
  
  hashed_password = pwd_context.hash(user.password)
  users[user.username] = {"username": user.username, "password": hashed_password}

  write_users_db(users)
  return True


def authenticate_user(user: User) -> bool:
    users = read_users_db()
    current_user = users.get(user.username)
    if not user:
        return False
    return pwd_context.verify(user.password, current_user["password"])


