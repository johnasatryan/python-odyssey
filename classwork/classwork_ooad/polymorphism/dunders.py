# # # # # class Person:
# # # # #   def __init__(self, name):
# # # # #     self.__name = name

# # # # #   def __call__(self):
# # # # #     print("hello callable object...")



# # # # # p = Person("Muchacha")

# # # # # p()
# # # # # print(callable(p))


# # # # from functools import partial

# # # # def add(a, b, c):
# # # #   return a + b + c

# # # # new_add = partial(add, 4)
# # # # # print(new_add(6, 7))

# # # # class custom_partial:
# # # #   def __init__(self, fn, *args):
# # # #     self.__fn = fn
# # # #     self.__args = args
  
# # # #   def __call__(self, *args):
# # # #     return self.__fn(*self.__args, *args)
  

# # # # new_add = custom_partial(add, 4, 5)
# # # # print(new_add(10))

  
# # # chlp = dict(name= "James", age= 20)

# # # # person["hobby"]
# # # # print(person.get("hobby", 555))

# # # from collections import defaultdict


# # # count = 0
# # # def default_print():
# # #   global count;
# # #   count += 1
# # #   return "N/A"

# # # person = defaultdict(default_print)
# # # person2 = defaultdict(default_print)

# # # # person.update(chlp)
# # # # person2.update(chlp)
# # # # print(person["hobby"])
# # # # print(person2["hobby"])
# # # # # print(person)
# # # # print(count)

# # # class DefaultPrintable:
# # #   def __init__(self):
# # #     self.count = 0

# # #   def __call__(self):
# # #     pass  

# # # d = DefaultPrintable()

# # # person = defaultdict(d)
# # # person["hobby"]

# # class Person:
# #   def __new__(cls, *args, **kwargs):
# #     print("__new__")
# #     instance = super().__new__(cls)
# #     return instance

# #   def __init__(self, name):
# #     print("__init__")


# # # p = Person.__new__(Person)
# # # p.__init__(p)

# # class Singleton:
# #  __instance = None
# #  def __new__(cls, *args, **kwargs):
# #   if Singleton.__instance == None:
# #     print("<<<<<<< when")
# #     Singleton.__instance = super().__new__(cls)
# #   print(">>>>>>> where")

# #   return Singleton.__instance
  

    

# # s = Singleton()
# # s2 = Singleton()
# # s3 = Singleton()


# class Person:
#   def __init__(self):
#     print("instance construction...")

#   def __del__(self):
#     print("instance deconstruction...")


# import ctypes

# def getRefcount(address):
#   return ctypes.c_long.from_address(address).value



# # p = Person()
# # id_person = id(p)

# # # p = 23

# # print(getRefcount(id_person))

# import sqlite3

# class Database:
#   def __init__(self, db_path):
#     print("Creating database...")
#     self.__db = sqlite3.connect(db_path)

#   def exeucte_query(self, query):
#     self.__db.execute(query)


#   def __del__(self):
#     print("Deleting database...")
#     self.__db.close()

# def start_program():

#   d = Database("simple_db")
#   d.exeucte_query("""CREATE TABLE IF NOT EXISTS projects (
#                 id INTEGER PRIMARY KEY, 
#                 name text NOT NULL, 
#                 begin_date TEXT, 
#                 end_date TEXT
#         );""")

#   d.exeucte_query("SELECT * FROM projects")   


# if __name__ == "__main__":
#   start_program()
#   print("another part of our program")


# class A:
#   def foo():
#     print("A::foo")

# class B(A):
#   def foo():
#     print("B::foo")

# class C(A):
#   def foo():
#     print("C::foo")

# class D(B, C):
#   pass

# d = D()
# d.foo()

import abc


class Jinjer(abc.ABC):
  @abc.abstractmethod
  def jinj(self):
    ...



# class Person:
#   def jinj(self):
#     print("Person")

# Jinjer.register(Person)
# p = Person()

# print(isinstance(p, Jinjer))
# print(Person.__mro__)


class Mlass:
  def __repr__(self):
    return "chlp"


m1 = Mlass()
m2 = Mlass()

di = {m1: "bb", m2: "cc"}
