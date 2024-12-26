from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import AccountResponse, AccountCreate
from database import get_db
from models import Account
from sqlalchemy import select
router = APIRouter(prefix='/accounts', tags=['Accounts'])

@router.post('/', response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def create_account(account: AccountCreate, db: AsyncSession = Depends(get_db)):
  new_account = Account(name=account.name, balance=account.balance)
  db.add(new_account)
  await db.commit()
  await db.refresh(new_account)
  return new_account

@router.get('/{account_id}', response_model=AccountResponse)
async def get_account(account_id: int, db : AsyncSession = Depends(get_db)):
  result = await db.execute(select(Account).where(Account.id == account_id))
  account = result.scalars().first()
  if not account:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")
  return account