
# def gen():
#   yield 2
#   print('inside generator')



# var = gen()

# # print(var)
# # print(type(var))

# print(next(var))
# print(next(var))

def gen():
  for i in range(100000):
    print('before yield...')
    yield i + 1 # STop

    print(f"after {i} yield...")


# gen_obj = gen()

# for i in gen_obj:
#   if i == 500:
#     print("Found the user")
#     break
# else:
#   print("not found")


# gen_obj = (x for x in range(6))
# print(gen_obj)

# 1. can I use return with yield?

# def gen():
#   for i in range(10):
#     yield i + 1 # STop

#   print('hello')
#   return None

# x = gen()    

# print(list(x))


# def gen():
#   yield 4
#   return 5


# x = gen()

# print(x)
# print(next(x))
# print(next(x))

# def gen():
#   return 5
#   yield 4


# x = gen()

# print(x)
# print(next(x))


# def another(arg):
#   if arg > 0:
#     return 10
#   else:
#     yield 20



# print(list(another(30)))


def some_gen():
  x = yield 15
  print('after generator')
  print(x)


# gen = some_gen()

# gen.send('hello world')
# next(gen)
# # gen.send("hello world")
# #
# next(gen)


def factorial(n):
  i = 0
  while(i < 14):
    some = yield i * (i - 1)
    if(some):
      i += some



# gen = factorial(14)
# print(next(gen))
# gen.send(5)
# print(next(gen))
# gen.send(6)


# def foo():
#   i = 10
#   j = 20
#   yield i, j


# gen = foo()

# print(next(gen))

def bar():
  yield None


def foo():
  yield bar()


gen = foo()

# print(next(next(gen)))


# class custom_map:
#   def __init__(self, fn, *iterables):
#     pass

#   def __call__(self, fn, *iterable):
#     for i in range(5):
#       yield i
    


# map = custom_map(lambda : 5, [], ())

# print(map(lambda : 5, [], ()))




# def foo():
#   for i in range(3):
#     yield i

# gen = foo()

# print(next(gen))
# gen.close()
# next(gen)

# print(help(filter))

def filter(function, iterable):
  if function is None:
    for i in iterable:
      if bool(i):
        yield i
    return
    
  for i in iterable:
    print(function)
    if function(i):
      yield i


filtered = filter(None, [x for x in range(6)])

# print(next(filtered))
# print(next(filtered))
# print(next(filtered))
# print(next(filtered))
# print(next(filtered))
# print(next(filtered))

# Exceptions

from typing import Iterable
def foo(iterable: Iterable, index: int)->int:
  if  type(iterable) != list and type(iterable) != tuple and type(iterable) != str:
    raise TypeError("Hargelis hajord angam zguysh exir")

  return iterable[index]

try:

  foo([5], 2)
except ValueError as e:
  print(e)
except TypeError as e:
  print(e)
except Exception as e:
  print(e)

print("hello world")
