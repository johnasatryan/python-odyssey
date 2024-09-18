import abc

class Account(abc.ABC):
  def __init__(self, account_number:int, balance: float, account_type: str):
    self.__account_number = account_number
    self.__balance = balance
    self.__account_type = account_type

  @abc.abstractmethod
  def deposit(self, amount: float)->None:
    ...

    