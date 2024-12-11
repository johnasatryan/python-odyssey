from helpers import read_json, write_json
from database.__init__ import USERS_FILE

def get_all_users():
  return read_json(USERS_FILE)

def get_user_by_username(username: str):
  users = get_all_users()
  return users.get(username, None)

def add_new_user(user):
  users = get_all_users()
  if user.username in users:
    return False
  new_id = len(users) + 1
  new_user = user.dict()
  new_user["_id"] = new_id
  users[user.username] = new_user
  write_json(USERS_FILE, users)
  return True


