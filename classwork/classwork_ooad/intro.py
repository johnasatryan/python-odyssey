# # # class Mlass:
# # #   pass


# # # print(Mlass)

# # # ob = Mlass
# # # ob2 = Mlass()

# # # # print(isinstance(ob2, object))

# # # print(dir(ob2))


# # # class Person(object):
# # #   def init(self):
# # #     print("custom init")


# # # ob = Person()


# # # class Person(object):
# # #   def __init__(self, value):
    
# # #     print("init called...", value)

# # #   def foo():
# # #     pass

  
# # # class Person(object):
# # #   def init(self):
# # #     print("custom init")


# # # ob = Person()

# # # ob = Person()

# # # ob.foo()



# # # class Person:
# # #   def __init__(self, age):
# # #     self.age = age

# # #   def getAge(self):
# # #     return self.age
  
# # #   def setAge(self, value):
# # #     if value < 0:
# # #       raise ValueError("...")
# # #     self.age = value


# # # person1 = Person(55)

# # # print(person1.getAge())
# # # person1.setAge(11)

# # # print(person1.getAge())

# # # person1.setAge(-5)



# # class Mlass:

# #   def foo(chlp):
# #     print("inside foo method", id(chlp))



# # ob = Mlass()

# # print("outside class", id(ob))

# # ob.foo()

# # # ob.foo == foo(&ob)

# # ob2 = Mlass()

# # ob2.foo()

# # print(id(ob2))


# class A:
#   def __init__(self):
#     print("hello init")
#     return None
  


# ob = A()

class Mlass:
  def getAge(self, value):
    return value
  

ob = Mlass()

print(ob.getAge())