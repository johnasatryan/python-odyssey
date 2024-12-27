from fastapi import APIRouter, Depends, HTTPException, status
from helpers.utils import pwd_context, create_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database.db import get_db


router = APIRouter(prefix="/auth", tags=["Authentication"])

async def authenticate_user(email: str, password: str, db: AsyncSession):
    query = await db.execute(text('SELECT * FROM users WHERE email = :email'), {"email": email})
    user = query.fetchone()
    if user and pwd_context.verify(password, user.password):
        return user
    return None

@router.post("/login")
async def login(loginUser: dict, db: AsyncSession = Depends(get_db)):
    """
    Authenticate user and return a JWT token if valid.
    """
    email, password = loginUser.values()
    user = await authenticate_user(email, password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
