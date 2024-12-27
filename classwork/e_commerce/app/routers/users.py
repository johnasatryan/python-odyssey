from fastapi import APIRouter, Depends, HTTPException, status
from helpers.dependencies import get_current_user
from schemas.user import UserCreate, UserResponse
from helpers.validation import validate_password
from sqlalchemy.ext.asyncio import AsyncSession
from helpers.utils import pwd_context
from sqlalchemy.future import select
from database.db import get_db
from models.user import User
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    validate_password(user.password)
    existing_user_query = select(User).where(User.email == user.email)
    existing_user_result = await db.execute(existing_user_query)
    if existing_user_result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        full_name=user.full_name,
        image_url=user.image_url,
        is_admin=user.is_admin,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    query = select(User).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int, user_data: UserCreate, db: AsyncSession = Depends(get_db)
):
    existing_user = await db.get(User, user_id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    existing_user.username = user_data.username
    existing_user.email = user_data.email
    existing_user.password = pwd_context.hash(user_data.password)
    existing_user.full_name = user_data.full_name
    existing_user.image_url = user_data.image_url
    existing_user.is_admin = user_data.is_admin

    await db.commit()
    await db.refresh(existing_user)
    return existing_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    await db.delete(user)
    await db.commit()
    return {"detail": "User deleted successfully"}

@router.get("/me", response_model=UserResponse)
async def get_current_authenticated_user(current_user: User = Depends(get_current_user)):
    return current_user
