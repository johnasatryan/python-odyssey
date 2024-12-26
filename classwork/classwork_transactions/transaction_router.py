from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import TransactionCreate, TransactionResponse
from database import get_db
from models import Transaction, Account
from sqlalchemy import select

router = APIRouter(prefix='/transactions', tags=['Transactions'])

@router.post('/', response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def perform_transaction(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
  sender = await db.execute(select(Account).where(Account.id == transaction.sender_id))
  sender = sender.scalars().first()

  receiver = await db.execute(select(Account).where(Account.id == transaction.receiver_id))
  receiver = receiver.scalars().first()

  if not sender or not receiver:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sender or Receiver accpunt not found")
  
  receiver.balance += transaction.amount

  if sender.balance < transaction.amount:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient funds...")
  
  sender.balance -= transaction.amount

  new_transaction = Transaction(sender_id = transaction.sender_id, receiver_id = transaction.receiver_id, amount = transaction.amount)

  db.add(new_transaction)
  await db.commit()
  await db.refresh(new_transaction)
  return new_transaction
