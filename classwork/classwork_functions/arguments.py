# pass by value
import sys

def foo(a):
  print(hex(id(a)))
  a = 25
  print(hex(id(a)))

  
a = [10, 1]
# print(hex(id(a)))
# foo(a)
# print(hex(id(25)))
# print(a)


# pass by reference

def bar(a):
  print(hex(id(a)))

  a.append(15)
  

# a = [10, 1]
# print(hex(id(a)))
# bar(a)
# print(hex(id(a)))

# print(a)

# def bar(a):
#   print("a[0] before inplace changing", hex(id(a[0])))

#   a[0] = 15
#   print("a[0] after inplace changing", hex(id(a[0])))

  

# a = 5
# print("a's address before function call", hex(id(a)))
# print("a[0] before inplace changing", hex(id(a[0])))
# bar(a)
# print("a[0] after inplace changing", hex(id(a[0])))

# print("a's address after function call", hex(id(a)))

# Arbitary arguments *args

def max_2_args(a, b):
  return a if a > b else b

def max_3_args(a, b, c):
  if(a > b and a > c):
    return a
  elif(b > a and b > c):
    return b
  return c

def max(*args):
  if len(args) == 2:
    # x = args[0]
    # y = args[1]
    return max_2_args(*args)
  elif len(args) == 3:
    # x = args[0]
    # y = args[1]
    # z = args[2]
    return max_3_args(*args)
  else:
    print("there is no such function")

# print(max(1, 22))
# print(max(1, 12, 3))
# print(max(1))
# print(help(print))

ls = (1, 2)

# print(max_2_args(*ls))

# print(max(1, 22))
# print(max(1, 12, 3))
# print(max(1))
# print(help(print))

# def func(*names, b):
#   print(names)
#   print(b)


# b = 4
# func(1, 2, 3, b  = 2, 23)

def foo(a, b, c):
  print(a)
  print(b)
  print(c)


def custom_print(*value, sep='+', end='8888'):
  print(*value, sep = sep, end = end)

# custom_print(1, 2, 3, 4, sep='+', end='____')
# custom_print([1, 2, 3], "hello")
# print(help(print))


def func(*, name, age):
  print("name is: ", name)
  print("age is: ", age)


# func(1, 2, 3, 4, name="Bob", age=12)

