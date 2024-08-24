# def some():
#   def foo():
#     print("hello world")
#   return foo

# s = some()
# s()

# def level_definition(level: str)->callable:
#   color_level = {
#     "ERROR": "\033[91m",
#     "WARNING": "\033[93m",
#     "INFO": "\033[94m",
#     "DEFAULT": "\033[0m"
#   }

#   def log(message: str)->None:
#     color = color_level.get(level, color_level["DEFAULT"])
#     print(f"{color}{level}:{message}")
#   return log

# info_function = level_definition("INFO")
# error_function = level_definition("ERROR")

# info_function("This is information message")

# error_function("This is error message")

# import time


# start = time.time()

# def foo():
#   time.sleep(5)



# foo()

# end = time.time()

# print(end - start)

# import time

# # current_time = time.localtime()

# # print(time.strftime("%Y-%m/%d %H:%M:%S", current_time))

# def outer(start):
#   def timer():
#     return time.time() - start
#   return timer

# some = outer(time.time())

# time.sleep(3)

# print(some())

# def add(x: int, y: int)->int:
#   return x + y

# def sub(x: int, y: int)->int:
#   return x - y

# def mul(x: int, y: int)->int:
#   return x * y

# def div(x: int, y: int)->int:
#   if y == 0:
#     raise ZeroDivisionError("Hey bro you can't divide by zero")
#   return x // y

# calculator = {'+': add, '-': sub, '*': mul, '/': div}

# op = input("Enter operation: ")

# x = int(input("Enter value of x: "))
# y = int(input("Enter value of y: "))

# print(f"result is: {calculator.get(op)(x, y)}")


# calculator = []

# calculator.extend((add, sub, mul, div))

# print(calculator[0](1, 3))
# print(calculator[1](1, 3))
# print(calculator[2](1, 3))
# print(calculator[3](1, 3))

# def base(n):
#   def mul(x):
#     return x * n
#   return mul

# # print(base(5)(3))

# def foo():
#   def f1():
#     def f2():
#       def f3():
#         return 4
#       return f3
#     return f2
#   return f1


# print(foo()()()())


# calculator = []

# calculator.append(lambda x, y:  x + y)
# calculator.append(lambda x, y:  x - y)
# calculator.append(lambda x, y:  x * y)
# calculator.append(lambda x, y:  "Novu" if y == 0 else x // y)

# print(calculator[0](1, 2))

# def foo(n):
#   res = []
#   for i in range(1, n):
#     print(f"i is: {i}")
#     a = lambda x : i + x
#     print(f"clouser of {i - 1} lambda: {a.__closure__}")
#     res.append(a)
#     for j in res:
#       print(f"closures in res: {j.__closure__}")
#   return res

# lam = foo(4)


# print(lam[0](4))
# print(lam[1](4))
# print(lam[2](4))

# print(lam[0].__closure__)
# print(lam[1].__closure__)
# print(lam[2].__closure__)
# print(hex(id(3)))

# def outer():
#   count = 0

#   def inner1():
#     nonlocal count;
#     count += 1
#     return count

#   def inner2():
#     nonlocal count;
#     count += 1
#     return count
#   return inner1, inner2

# functions = outer()
# print(functions[0]())
# print(functions[1]())


# glob = "hello world"
# def foo(name=glob):
#   print(name)


# glob = 23

# foo()


# def foo(n):
#   res = []
#   for i in range(1, n):
#     def moo(inchuzes):
#       return lambda x : inchuzes * x
#     res.append(moo(i))

   
#   return res

# lam = foo(4)


# print(lam[0](4))


# print(lam[0].__closure__)
# print(lam[1].__closure__)
# print(lam[2].__closure__)



# inch = lambda : lambda : lambda : "hello world"

# def f1():
#   def f2():
#     def f3():
#       return "hello world"
#     return f3
#   return f2

# x = f1()
# y = x()
# z = y()
# print(z)
# print(y)
# print(x)

# print(inch()()())



# def decorator(fn):
#   def wrapper(*args):
#     print(args)
#     print(fn.__name__)
#     return fn(*args)
#   return wrapper


# def foo(x, y):
#   print(x + y)


# foo(1, 3)
# foo = decorator(foo)
# foo(1, 3)

# def chlp(x):
#   return x + 132


# chlp = decorator(chlp)

# chlp(3)


def bar(ls = []):
  ls.append(("C++", "Java"))
  print(ls)
  return ls

bar()
ls = bar(['Python'])
bar()

