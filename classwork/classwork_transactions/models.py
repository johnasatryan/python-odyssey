from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Float, func

Base = declarative_base()

class Account(Base):
  __tablename__ = 'account'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  balance = Column(Float, nullable=False, default=0.00)
  
  def __repr__(self):
        return f"<Account(id={self.id}, name='{self.name}', balance={self.balance})>"

class Transaction(Base):
  __tablename__ = 'transaction'

  id = Column(Integer, primary_key=True, index=True)
  sender_id = Column(Integer, ForeignKey('account.id'), nullable=False)
  receiver_id = Column(Integer, ForeignKey('account.id'), nullable=False)
  amount = Column(Float, nullable=False)
  timestamp = Column(DateTime(timezone=True), server_default=func.now())

  # relationships 
  sender = relationship("Account", foreign_keys=[sender_id], backref="sent_transactions")
  receiver = relationship("Account", foreign_keys=[receiver_id], backref="received_transactions")
  
  def __repr__(self):
    return f"<Transaction(id={self.id}, sender_id={self.sender_id}, receiver_id={self.receiver_id}, amount={self.amount})>"

  


