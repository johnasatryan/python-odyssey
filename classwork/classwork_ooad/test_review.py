# # # from abc import ABC, abstractmethod

# # # # class Vehicle(ABC):

# # # #   @abstractmethod
# # # #   def startEngine(self):
# # # #     ...


# # # # class Car(Vehicle):
# # # #   def __init__(self):
# # # #     self.color = "Red"
# # # #   def startEngine(self):
# # # #     print('Car engine starts...')


# # # # class ElectricCar(Vehicle):

# # # #   def __init__(self):
# # # #     self.autopilot = "Autopilot"


# # # # class Tesla(Car, ElectricCar):
# # # #   def __init__(self):
# # # #     # pass
# # # #     super().__init__()

# # # #     super(Car, self).__init__()
# # # #     super(Car).__init__()

# # # # s = Tesla()
# # # # print(s.__dict__)


# # # # class Bird(ABC):
# # # #   @abstractmethod
# # # #   def fly(self):
# # # #     print("Every bird fly")

# # # # 1. karogh em ardyoq object stexcel? -- voch
# # # # 2. inchi hamar tam body abstractmethodin? -- hima asem

# # # class Vehicle(ABC):
# # #   @abstractmethod
# # #   def maxSpeed(self):
# # #     return "180km/h"
  

# # # class SedanCar(Vehicle):
# # #   def maxSpeed(self):
# # #     return super().maxSpeed()

# # # class SUVCar(Vehicle):
# # #   def maxSpeed(self):
# # #     return super().maxSpeed()
  

# # # class SportCar(Vehicle):
# # #   def maxSpeed(self):
# # #     return "240km/h"
  

# # # class ElectricCar(Vehicle):
# # #   def maxSpeed(self):
# # #     return super().maxSpeed()



  
# # # car = SedanCar()
# # # suv = SUVCar()
# # # print(car.maxSpeed())
# # # print(suv.maxSpeed())


# # class Mlass:
# #   def __new__(cls):
# #     print("__new__")
# #     return super().__new__(cls)
    

# #   def __init__(self):
# #     print("__init__")


# # p = Mlass()
# # print(p)

# # Descriptor

# class Person:
#   def __init__(self, name, age):
#     self.setName(name)
#     self.setAge(age)

#   def setName(self, value):
#     if value == "":
#       raise ValueError
#     self.__name = value

#   def setAge(self, value):
#     if value < 0:
#       raise ValueError
#     self.__age = value

#   def getName(self):
#     return self.__name
  
#   def getAge(self):
#     return self.__age
  

# p = Person("James", 40)
# p.getAge()

# p.age = ""


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def setName(self, value):
#     if value == "":
#       raise ValueError
#     self.__name = value

#   def setAge(self, value):
#     if value < 0:
#       raise ValueError
#     self.__age = value

#   def getName(self):
#     return self.__name
  
#   def getAge(self):
#     return self.__age
  
#   age = property(getAge, setAge)
#   name = property(getName, setName)
  

# p = Person("James", 40)
# # p.getAge()

# # p.age = ""

# print(Person.__dict__)
# # print(p.__dict__)

# print(p.name)
# p.name = "Bob"
# print(p.name)
# # print(p.__dict__)
# p.name = ""


class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  @property
  def name(self):
    return self.__name
  
  @property
  def age(self):
    return self.__age
  
  @name.setter
  def name(self, value):
    if value == "":
      raise ValueError
    self.__name = value

p = Person("James", 40)

print(p.__dict__)
# print(Person.__dict__)

print(p.name)