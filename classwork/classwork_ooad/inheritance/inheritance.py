# # # class A:
# # #   pass

# # # # print(A.mro())

# # # class Person:
# # #   def __init__(self, name:str = "", age = 0):
# # #     self.__name = name
# # #     self.__age = age
  
# # #   def getAge(self):
# # #     return self.__age
  
# # #   def getName(self):
# # #     return self.__name
  
# # #   def setAge(self, age):
# # #     self.__age = age


# # # class Student(Person):
# # #   pass


# # # class Teacher(Person):
# # #   pass


# # # # print(Student.mro())

# # # class Lesson:
# # #   def __init__(self, name):
# # #     self.__lesson_name = name

# # #   def start_lesson(self, teacher: Teacher, students: list[Student]):
# # #     print(f" Lesson: {self.__lesson_name},  {teacher.getName()} is talking about OOAD...")
# # #     print(f"There are {len(students)} students")

  
# # # python_odyssey = Lesson("Python Odyssey")

# # # teacher = Teacher("Bob", 30)

# # # students = [Student() for x in range(10)]



# # # python_odyssey.start_lesson(teacher, students)

# # # -------------------------------------------------------
# # class Person:
# #   def __init__(self, name:str, age:int):
# #     self.__name = name
# #     self.__age = age
  
# #   def getAge(self):
# #     return self.__age
  
# #   def getName(self):
# #     return self.__name
  
# #   def setAge(self, age):
# #     self.__age = age


# # class Student(Person):
# #   def __init__(self, name, age, avg_score):
# #     # print(help(super))
# #     # Person.__init__(self, name, age)
# #     super().__init__(name, age)
# #     self.__avg_score = avg_score
  
# #   def getAvgScore(self):
# #     return self.__avg_score


# #   # def getName(self):
# #   #   return self.__name


# # class Teacher(Person):
# #   pass



# # # student = Student("Bob", 22, 98)

# # # print(student.getName())
# # # print(student.__dict__)
# # # print(student.getName())


# # # Person.__init__(student, "Bob", 23)


# # class A:
# #   count = 0

# #   def foo(self):
# #     print("Hello world")
# #   def __init__(self):
# #     self.x = 24


# # a = A()

# # # print(a.__dict__)
# # # print(A.__dict__)

# # class B(A):
# #   pass
  

# # b = B()

# # b.foo()

# # # print(b.__dict__)
# # # print(B.mro())

# # # print(B.__dict__)
# # # print(dir(B))

# # # class A:
# # #   def foo(self):
# # #     print("A::foo")


# # # class B(A):
# # #   def bar(self, fn):
# # #     def chlp(self, fn2):
# # #       super.foo()



# # class Musician:
# #   def play(self):
# #     print("Musician plays...")


# # class Guitarist(Musician):
# #   def play(self):
# #     print("Guitarist plays...")

# # class Pianist(Musician):
# #   def play(self):
# #     print("Pianist plays...")


# # def party(musicians: list[Musician]):
# #   for musician in musicians:
# #     musician.play()

# # # def party(guitaris: list[Guitarist], pianist: [Pianist]):
# # #   guitaris.play()
# # #   pianist.play()


# # guitarists = [Guitarist() for i in range(5)]
# # pianists = [Pianist() for i in range(3)]

# # class Hunter:
# #   def play(self):
# #     print("Non musician")
  


# # # party([*guitarists, *pianists])


# from typing import Iterable, Mapping, Sequence, Container, Sized

# class container:
#   def __contains__(self, element):
#     ...

# class sized:
#   def __len__(self):
#     ...

# ls = []
# di = {}
# tp = tuple()
# # print(dir(ls))

# # class chlp_list():
# #   def __len__(self):
# #     return 14
  

# # # print(dir(chlp_list))
# # a = chlp_list()

# # print(chlp_list.mro())
# # print(isinstance(a, Sized))

# class animast_list:
#   def __init__(self):
#     self.mem = [1, 2, 3]
#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     return 
  

# ob = animast_list()
# # print(iter(ob))

# print(isinstance(ob, Iterable))
# print()
# from typing import Sized
# class Mlass:
#   def __foo__(self):
#     ...


# class MyClass:
#   def __foo__(self):
#     print("hello foo")


# ob = MyClass()

# print(isinstance(ob, Mlass))

# print(help(Sized))


# class Mlass:
#   def __len__(self, a):
#     return 14
  

# ob = Mlass()

# print(len(ob))

class Pilot:
  def __init__(self, name, age_of_experience):
    self.name = name
    self.age_of_experience = age_of_experience

  def output(self):
    print(f"Pilot name is {pilot.name}")
    


class Plane:
  def boarding(self, pilot):
    self.pilot = pilot


boeing = Plane()

pilot = Pilot("James", 20)

boeing.boarding(pilot)

del boeing

pilot.output()