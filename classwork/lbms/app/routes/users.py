from fastapi import APIRouter, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.helpers.config import settings
from app.models.users import UserBase, UserIn, UserOut
from app.helpers.utils import hash_password, create_jwt, verify_password


router = APIRouter(prefix='/users', tags=['users'])
db_client = AsyncIOMotorClient(settings.MONGO_URI)
db = db_client.library

@router.post('/signup')
async def signup(user: UserBase):
  existing_user = db.users.findOne({"email": user.email})
  if existing_user:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')
  hashed_password = hash_password(user.password)
  await db.users.insert_one(UserBase(username=user.username, email=user.email, password=hashed_password).model_dump())
  return {"message": "User registered successfully"}

@router.post('/signin')
async def signin(user: UserIn):
  db_user = await db.users.find_one({"email": user.email})
  if not db_user or not verify_password(user.password, db["password"]):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
  token = create_jwt(user)
  return {"access_token": token, "token_type": "bearer"}

@router.put('/{id}')
async def update_user(user_id: str, user: UserBase):
  if not ObjectId.is_valid(user_id):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID")
  
  if user.password:
    user.password = hash_password(user.password)
  update_data = user.model_dump(exclude_unset=True)

  result = await db.users.update_one({"_id": ObjectId(user_id), "$set": update_data})

  if result.modified_count == 0:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No changes made to the user")
  return {"message": " User updated successfully"}
