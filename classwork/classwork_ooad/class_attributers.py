# class Person:
#   age = 0
#   def __init__(self):
#     self.name = ""

#   def foo(self):
#     pass





# person1 = Person()

# print(person1.age)

# print(dir(Person))
# # print(dir(person1))
# print(person1.__dict__)
# print(Person.__dict__)


# person1.foo()
# person1.age


# class Car:
#   color = "BLACK"

#   def __init__(self, model: str):
#     self.__model = model
  

# audi = Car("Audi")
# print(audi.color)
# # audi.color = "RED"

# # print(audi.color)
# print(audi.__dict__)
# bmw = Car("BMW")

# print(bmw.color)


# class Mlass:
#   count = 0
#   def __init__(self):
#     Mlass.count += 1



# ob = Mlass()
# ob2 = Mlass()
# ob3 = Mlass()

# ob4 = Mlass()
# ob5 = Mlass()
# ob6 = Mlass()
# ob7 = Mlass()
# print(Mlass.count)
# print(ob3.count)
# print(ob2.count)




# print(ob.__dict__)
# # ob.count += 1
# print(ob.__dict__)


class A:
  count = 0

  def __init__(self):
    # A.foo()
    print("__init__")

  def foo():
    A.count += 1

# ob = A()
# ob2 = A()
# ob3 = A()
# ob4 = A()
# print(ob.count)
# print(A.__dict__)
# print(dir(A))

# A.foo()

# print(type(ob))

# A.__init__()
# x = type(ob).__init__()

# print(ob)
# print(x)

# class Person:

#   @classmethod
#   def foo(chlp):
#     print(chlp)
#     print("this is class method")
  
#   def bar():
#     print("is this class method too???")

# ob = Person()
# ob.bar() # error
# Person.bar() 

# Person.foo()
# ob.foo()

def classmethod(fn):
  def wrapper(cls, *args, **kwargs):
    if type(cls) != type:
      return fn(type(cls), *args, **kwargs)

    return fn(cls, *args, **kwargs)
  return wrapper

class Base:
  x = "hello X"

  def __init__(self):
    self.x = 555

  @classmethod
  def method(cls):
    print(cls)

ob = Base()
# Base.method()
ob.method()
# print(ob)

# 
# print(type(list))
# print(type(Base))


# print(type(type))

# print(type(object))

print(Base.mro())
print(list.mro())
print(type.mro(type))
print(object.mro())