# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
  
# #   def __eq__(self, other):
# #     return self.name == other.name and self.age == other.age

# # p1 = Person("James", 40)
# # p2 = Person("James", 41)
    
# # print(f"Persons are equal {p1 == p2}")



# from numbers import Real

# class ValidLengthAndType(TypeError):
#   pass



# class Vector:
#   def __init__(self, *containers):
#     for containter in containers:
#       if not isinstance(containter, Real):
#         raise TypeError("Vector argumnts must be real numbers")
#     self.__containers = containers

#   def __str__(self):
#     return f"Vector{self.__containers}"
  
#   def __not_valid_type_and_length(self, other):
#     return len(self.__containers) != len(other.__containers) or not isinstance(other, Vector)
  

#   def __add__(self, other):
#     if self.__not_valid_type_and_length(other):
#       raise ValidLengthAndType("Not Valid Type")
#     # containers = (x + y for x, y in zip(self.__containers, other.__containers))
#     containers = []

#     for i in range(len(self.__containers)):
#       containers.append(self.__containers[i] + other.__containers[i])

#     return Vector(*containers)
  
#   def __sub__(self, other):
#     if isinstance(other, tuple):
#       return Vector(*(x - y for x, y in zip(self.__containers, other)))
#     if self.__not_valid_type_and_length(other):
#       raise ValidLengthAndType("Not Valid Type")
#     containers = (x - y for x, y in zip(self.__containers, other.__containers))
   
#     return Vector(*containers)
  
#   def __mul__(self, number):
#     if isinstance(number, Real):
#       # scaliar multiplication
#       containers = (x * number for x in self.__containers)
#       return Vector(*containers)
    
#   def __rmul__(self, number):
#     return self * number 
  
#   def __iadd__(self, other):
#     x = self + other
#     self.__containers = x.__containers
#     return self
  
#   def __eq__(self, other):
#     if ValidLengthAndType(self, other):
#       for i in range(len(self.__containers)):
#         if self.__containers[i] != other.__containers[i]:
#           return False
#       return True
#     # return id(self) == id(other)


    

# v1 = Vector(1, 2)
# v2 = Vector(1, 2)
# v3 = v1

# # print(v1 == v3)

# # print(v1 == v2)
# # ls1 = [1, 2]
# # ls2 =[1, 2]

# # print(ls1 == ls2)


# class Person:
#   def __init__(self, name: str, age: int):
#     self.setName(name)
#     self.setAge(age)

#   def setName(self, name: str):
#     if name == "":
#       raise ValueError
#     self.__name = name
  
#   def setAge(self, age: int):
#     if age < 0:
#       raise ValueError
#     self.__age = age
  
#   def __str__(self):
#     return f"Person name({self.__name}), age({self.__age})"

#   def __lt__(self, other: "Person"):
#     print("hello")
#     return self.__name < other.__name and self.__age < other.__age
  
#   def __gt__(self, other):
#     pass
  
#   def __le__(self, other):
#     pass

#   def __ge__(self, other):
#     pass

  



# from typing import List

# names = ["James", "Ann", "Abo", "Bob", "Kate", "Lebron"]
# import random

# persons: List[Person] = [Person(names[index], random.randint(1, 70)) for index in range(6)]
# person1 = Person("James", 10)
# person2 = Person("James", 10)

# # print(persons[0])
# # print(persons[1])
# # # print(persons[0] < persons[0])
# # print(persons[0] > persons[0])
# # # print(person1 > person2)

# print(bool(person1))


# class Person:
#   # pass
#   def __bool__(self):
#     print("Hello bool!")
#     return False

#   def __len__(self):
#     print("hello world")
#     return 0

# p1 = Person()

# print(bool(p1))
# # print(p1)


class Person:
  def __hash__(self):
    print("hello")
    return 10
  
  def __eq__(self, other):
    print("hello equal")
    return isinstance(other, Person)
  
  def __str__(self):
    return "Plomb"
  def __repr__(self):
    print("repr")
    return "sss"

p1 = Person()
p2 = Person()


di = { p1: "this is Person", p2: "this is another Person"}

print(di)


p1 or p2