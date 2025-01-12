from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.helpers.utils import decode_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

async def get_current_user_id(token: str = Depends(oauth2_scheme)):
  payload = decode_jwt(token)
  id = payload.get("sub")
  if not id:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
  return id



