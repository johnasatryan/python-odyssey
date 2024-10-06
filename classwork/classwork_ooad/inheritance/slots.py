# # class PersonDict:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age



# # import sys

# # class PersonSlot:

# #   __slots__ = 'name', 'age'

# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# # p = PersonSlot("James", 34)
# # p_dict = PersonDict("James", 34)


# # p.age = 12

# # p_dict = 12
# # print(p.age)


# # print(p.__dict__)
# # print(p.__slots__)
# # print(f"{10000 * sys.getsizeof(p.__slots__) / 1024}kb")
# # print(f"{10000 * sys.getsizeof(p_dict.__dict__) / 1024}kb")


# # print(type(p.__slots__))
# # print(p_dict.__dict__)

# # p.x = 12


# # def make_dict():
# #   p = PersonDict("James", 23)
# #   p.name
# #   del p.name

# # def make_slot():
# #   p = PersonSlot("James", 23)
# #   p.name 
# #   del p.name


# # import timeit

# # print(timeit.timeit(make_dict))
# # print(timeit.timeit(make_slot))


# class Location:
#   __slots__ = 'name', '__langitude', '__latitude'
#   # slots class attribute

#   def  __init__(self, name, langitude, latitude):
#     self.name = name
#     self.__langitude = langitude
#     self.__latitude = latitude

#   @property
#   def langitude(self):
#     return self.__langitude
  
#   @property
#   def latitude(self):
#     return self.__latitude
  
#   # @langitude.setter
#   # def langitude(self, value):
#   #   pass
  

# l = Location("Madrid", 39.001, 41.0001)

# # print(l.__slots__)

# l.name = "Yerevan"

# # l.get_location = lambda x: 23

  
# print(l.__slots__)
# # non-data descriptor
# # data descriptor


# Inheritance

# class Person:
#   def __init__(self, name):
#     self.name = name


# p = Person("James")

# class Student(Person):
#   pass

# s = Student("Jack")

# print(s.__dict__)

class Person:
  __slots__ = '__name',

  def __init__(self, name):
    self.name = name # setter

  def eat(self):
    print(f"{self} eats some frtuits...")

  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, value):
    if value == "":
      raise ValueError("value can't be empty")
    
    self.__name = value

p = Person("James")
# p.age = 12

# print(p.__dict__)

# class Student(Person):
#   __slots__ = ('age')

#   def __init__(self, name, age):
#     super().__init__(name) # delegation 
#     self.age = age


# s = Student("James", 23)
# print(s.__slots__)
# # print(p.__slots__)

# print(s.name)
# print(Student.__mro__)


# st = Student("James", 45)

# print(st.__dict__)



# class Student(Person):
#   __slots__ = tuple()

#   def study(self):
#     print(f"{self} is going to classroom early in the morning...")

  

# s = Student("James")

# # print(s.__dict__)
# # print(s.__slots__)

# print(s.name)

# def foo():
#   pass

# foo.x = 23

# print(foo.x)


ls = [1, 2, 3]

# ls.x = 23

class Custom_List:
  __slots__ = 'arr',



ls = Custom_List()
ls.x = 23