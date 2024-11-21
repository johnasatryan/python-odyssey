from fastapi import FastAPI
import json
import uvicorn


app = FastAPI()


file_path = 'project.json'
# with open(file_path, 'w') as fs:
#   json.dump([], fs)



@app.get('/users')
def get_users():
  try:
    with open('project.json') as fs:
      users = json.load(fs.read())
      return users

  except FileNotFoundError:
   return []


# @app.get('/users/{user_id}')
# def get_user(user_id: int):
#   result = next(u for u in users if u['id'] == user_id)
#   return result

@app.post('/users')
def create_user(user: dict):
  try:
      fs = open(file_path, 'r')

      users = json.load(fs)
      users.append(user)
      fs.close()

      fs = open(file_path, 'w')

      json.dump(users, fs, indent=2)
  except FileNotFoundError:
   return []
  

if __name__ == '__main__':
  uvicorn.run('main:app', port=8080, reload=True)