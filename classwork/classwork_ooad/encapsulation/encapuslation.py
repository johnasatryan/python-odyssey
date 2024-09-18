# # Abstraction 
# # Encapsulation

# # class Car:
# #   def __init__(self, model: str, year: int):
# #     self.model = model
# #     self.year = year
  
# #   def output_car(self):
# #     print(f"Car model is {self.model} and year is {self.year}")

# # toyota = Car("Toyota", 2020)


# # toyota.output_car()

# # toyota.model = ""
# # toyota.year = -1990

# # toyota.output_car()


# # def foo(arg1, arg2, arg3):
# #   pass

# # foo(1, 2)



# class Car:
#   def __init__(self, model: str, year: int):
#     # __ -> private
#     self.__model = model 
#     self.__year = year
#     self.x = 23

#     # _ -> protected
#     self._color = "black"
  
#   def output_car(self):
#     print(dir(self))
#     print(f"Car model is {self.__model} and year is {self.__year} x is {self.x}")

# toyota = Car("Toyota", 2020)


# # toyota.output_car()

# # toyota.__model = 23

# # toyota._color = "white"
# # # toyota.x = 64
# # toyota.output_car()

# # toyota.__dict__.update({"newProp" : 55})
# # print(toyota.__dict__)

# # audi = Car("Audi", 2021)
# # print(audi.__dict__)

# # print(dir(toyota))
# # toyota._Car__model = "Chlp"
# # print(toyota._Car__model)


# # class Mlass:
# #   def constructor(self, name):
# #     self.__name = name


# # ob = Mlass()

# # # ob.constructor("Mlass")
# # ob.__name = "name"
# # print(dir(ob))


# # ls = [1, 2, 3]

# # ls.x = 23


# class Car:
#   def __init__(self, model: str, year: int):
#     # __ -> private
#     self.__model = model 
#     self.__year = year

#   def getModel(self):
#     return self.__model # -> self._Car__model

#   def setModel(self, model):
#     if model == "":
#       raise ValueError("Model can't be empty")
    
#     if type(model) != str:
#       raise TypeError("Type must be string...")

#     self.__model = model

#     # _ -> protected
#     # self._color = "black"
  
#   def output_car(self):
#     print(dir(self))
#     print(f"Car model is {self.__model} and year is {self.__year}")


# toyota = Car("Toyota", 2020)

# toyota.__model = "Zap"
# toyota.__dict__.pop('_Car__model')

# # toyota.setModel("Audi")
# toyota.getModel()



# # try:

# #   toyota.setModel("")
# # except :
# #   print("error unem")


# # print(toyota.__model)

# print(toyota.getModel())



class Mlass:
  def __init__(self):
    self.a = 1
    self.b = 2
    self.c = 3


ob = Mlass()


temp = {}
for key in ob.__dict__.keys():
 temp.update({"_" + type(ob).__name__ + "__"+ str(key) : ob.__dict__.get(key)})



ob.__dict__ = temp

# print(ob.__dict__)


# class Mlass:
#   def __init__(self):
#     self.__a = 1
#     self.__b = 2
#     self.__c = 3


# ob = Mlass()

# print(ob.__dict__)


class Car:
  def __init__(self, model: str, year: int):
    # __ -> private
    self.setModel(model) 
    self.__year = year

  def getModel(self):
    return self.__model # -> self._Car__model

  def setModel(self, model):
    if model == "":
      raise ValueError("Model can't be empty")
    
    if type(model) != str:
      raise TypeError("Type must be string...")

    self.__model = model

    # _ -> protected
    # self._color = "black"
  
  def output_car(self):
    print(f"Car model is {self.__model} and year is {self.__year}")

  def __helper(self):
    import random

    return random.randint(1, 100)
  





toyota = Car("Audi", 2020)

# toyota.output_car()

print(dir(toyota))