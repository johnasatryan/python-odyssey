from database import async_session
from sqlalchemy import select
from models import Account

async def perform_tansactoin():
  async with async_session() as session:
    result = session.execute(select(Account).where(Account.id == 1))
    account = result.scalars().first()

    account.balance += 100

    session.add(account)

    await session.commit()

