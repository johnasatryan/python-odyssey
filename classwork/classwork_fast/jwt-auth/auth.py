from jose import jwt
from config import Config
import datetime

config = Config()

ALGORITHM='HS256'
EXPIRES_IN = 30


def create_jwt_token(user: dict):
  expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=EXPIRES_IN)
  data = user.copy()
  data['exp'] = expires

  auth_token = jwt.encode(data, config.SECRET_KEY, algorithm=ALGORITHM)
  return auth_token


def verify_jwt_token(token):
  print(token)
  username = jwt.decode(token, config.SECRET_KEY, algorithms=ALGORITHM)
  return username



