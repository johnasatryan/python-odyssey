# class Circle:
#   def __init__(self, radius):
#     self.radius = radius

#   @property
#   def radius(self):
#     print("getter")

#     return self.__radius
  
#   @radius.setter
#   def radius(self, value):
#     print("setter")
#     if value < 0: 
#       raise ValueError("Radius can't be negative")
#     self.__radius = value


# circle = Circle(5)


# descriptor ->  նկարագրող 

# __get__ & __set__ 

# print(help(property))

# class props:
#   def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#     self.__fget = fget
#     self.__fset = fset
#     self.__fdel = fdel
#     self.__doc = doc
  
#   def __get__(self, instance, owner=None):
#     print(f"self is {self}")
#     print(f"instance is {instance}")
#     print(f"owner is {owner}")


# class Circle:
#   def __init__(self, radius):
#     self.__radius = radius

#   def getRadius(self):
#     print("getter called")
#     return self.__radius
#   radius = props(getRadius)

# r = Circle(5)

# print(r.radius)
# r.radius # radius.__get__(radius, r, Circle)
# print(r)
# print(Circle.radius)


# class Mlass:
#   def foo(self):
#     pass


# m = Mlass()

# m.foo()

# print(p.__get__(m))


class props:
  def __init__(self, fget=None, fset=None, fdel=None, doc=None):
    self.__fget = fget
    self.__fset = fset
    self.__fdel = fdel
    self.__doc = doc
  
  def __get__(self, instance, owner=None):
    print(owner)
    if instance is None:
      return self
    if owner == None:
      raise AttributeError("yaaaaaa")
    return self.__fget(instance)
  
  def __repr__(self):
    return f"<{type(self).__name__} object at {hex(id(self))}>"
    


class Circle:
  def __init__(self, radius):
    self.__radius = radius

  def getChlp(self):
    print("getter called")
    return self.__radius
  radius = props(getChlp)

r = Circle(5)

# r.radius
# print("client code: ", id(r))

# print(Circle.radius)

class Circle:
  def __init__(self, radius):
    self.__radius = radius

  def getChlp(self):
    print("getter called")
    return self.__radius
  radius = property(getChlp)


x = Circle(5)

# print(Circle.radius)


# p = property()
# p2 = props()

# # print(p)

# # print(p2)

# class Person:
#   def __init__(self):
#     self.name = props()


# class Person2:
#   def __init__(self):
#     self.name = property()


# p2 = Person2()
# # print(p2.name.__get__(p2.name))

# p1 = Person()


class Person:
  def __init__(self, name):
    self.__name = name

  @props
  def getName(self):
    return self.__name
  

  
#   # name = props(getName)
  



# p = Person("James")

# # p.name
# print(Person.__dict__)
# print(p.__dict__)


class props:
  def __init__(self, fget=None, fset=None, fdel=None, doc=None):
    self.__fget = fget
    self.__fset = fset
    self.__fdel = fdel
    self.__doc = doc
  
  def __get__(self, instance, owner=None):
    if instance is None:
      return self
    if owner == None:
      raise AttributeError("yaaaaaa")
    return self.__fget(instance)
  
  def foo(self, fn):
    self.__fset = fn
    return self

  def __set__(self, instance, value):
    if self.__fset == None:
      raise AttributeError("yaaaaaa")
    self.__fset(instance, value)



    
  
  def __repr__(self):
    return f"<{type(self).__name__} object at {hex(id(self))}>"
  

class Person:
  def __init__(self, name):
    self.name = name

  @props
  def name(self):
    return self.__name
  

  @name.foo
  def name(self, value):
    if value == "":
      raise ValueError("chi kara")
    self.__name = value




  
# print(Person.__dict__)

p = Person("James")
print(p.name)

p.name = "Bob"
print(p.name)

# print(p.__dict__)
# print(p.name)