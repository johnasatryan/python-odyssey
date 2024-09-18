# from abc import ABC, abstractmethod

# # # Abstract Base Class

# # class Shape(ABC):

# #   def __init__(self, x, y):
# #     self.__x = x 
# #     self.__y = y


# #   @abstractmethod
# #   def perimeter(self, radius):
# #     ...





# # def custom_abstractmethod(fn):
# #   fn.__isabstractmethod__ = True
# #   return fn 


# # class Person(ABC):

# #   @custom_abstractmethod
# #   def run(self):
# #     ...


# # class Student(Person):
# #   pass

# # s = Student()



# class Vehicle(ABC):
#   @abstractmethod
#   def speed(self):
#     ...


# class Car(Vehicle):

#   @abstractmethod
#   def drift(self):
#     ...




# Polymorphism

# 1. static
# def foo(x):
#   pass

# def foo(x, y):
#   pass

# 2. Dynamic

# __repr__, __str__

class Person:
  def __init__(self, name: str, age: int):
    self.setName(name)
    self.setAge(age)

  def setName(self, value: str):
    if not isinstance(value, str) or value == "":
      raise ValueError("Name must be string type...")
    self.__name = value

  def setAge(self, value: int):
    if not isinstance(value, int) or value <= 0:
      raise ValueError("Age must be integer...")
    self.__age = value
  
  def __repr__(self):
    return f"Person name({self.__name}), age({self.__age}))"
  
  def __str__(self):
    print("__str__ called...")
    return self.__name



p1 = Person("James", 12)

# print(repr(p1))
# print(p1)


# Math operations, math operators, +, -, *, //, += ...

from numbers import Real

class ValidLengthAndType(TypeError):
  pass


class Vector:
  def __init__(self, *containers):
    for containter in containers:
      if not isinstance(containter, Real):
        raise TypeError("Vector argumnts must be real numbers")
    self.__containers = containers

  def __str__(self):
    return f"Vector{self.__containers}"
  
  def __not_valid_type_and_length(self, other):
    return len(self.__containers) != len(other.__containers) or not isinstance(other, Vector)
  

  def __add__(self, other):
    if self.__not_valid_type_and_length(other):
      raise ValidLengthAndType("Not Valid Type")
    # containers = (x + y for x, y in zip(self.__containers, other.__containers))
    containers = []

    for i in range(len(self.__containers)):
      containers.append(self.__containers[i] + other.__containers[i])

    return Vector(*containers)
  
  def __sub__(self, other):
    if isinstance(other, tuple):
      return Vector(*(x - y for x, y in zip(self.__containers, other)))
    if self.__not_valid_type_and_length(other):
      raise ValidLengthAndType("Not Valid Type")
    containers = (x - y for x, y in zip(self.__containers, other.__containers))
   
    return Vector(*containers)
  
  def __mul__(self, number):
    if isinstance(number, Real):
      # scaliar multiplication
      containers = (x * number for x in self.__containers)
      return Vector(*containers)
    
  def __rmul__(self, number):
    return self * number 
  
  def __iadd__(self, other):
    x = self + other
    self.__containers = x.__containers
    return self
    


v1 = Vector(1, 2)
v2 = Vector(10, 20)

# v1 * 4
# print(v2 * 3)
# print(3 * v2)
# print(v2 - (1, 2))

# print(v1)
# print(v2)

# print(v1 + v2)

v3 = Vector(5, 6)
# print(v2 - v3)
# try:
#   v3 = Vector("hello")

# except TypeError as e:
#   print(e)

print(hex(id(v1)))
v1 += v3


print(v1)
print(hex(id(v1)))

