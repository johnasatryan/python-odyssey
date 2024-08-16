# # 3

# def custom_filter(fn, iterable):
#   res = []

#   if fn is None:
#     for item in iterable:
#       if item == True:
#         res.append(item)
#   else:
#     for item in iterable:
#       if fn(item):
#         res.append(item)
#   return res


# # print(custom_filter(lambda x: x % 2 == 0  , [1, 2, 3, 4, 5, 6]))
# # print(list(filter(lambda x: False, [1, 2, 3, 4, 5, 6])))

# def memorize(fn):
#   cache = {}
#   def wrapper(*args, **kwargs):
    
#     key = str(args) 
#     key = key + str(kwargs)
#     if cache.get(key):
#       return cache.get(key)
#     result = fn(*args, **kwargs)
#     cache[key] = result
#     return result
#   wrapper.cache = cache
  
#   return wrapper

# @memorize
# def fibonacci(n):
#   if n == 1 or n == 2: return 1

#   return fibonacci(n - 1) + fibonacci(n - 2)


# # print(fibonacci(8))
# # print(fibonacci(10))
# # print(fibonacci(8))

# # print(fibonacci.cache)

# @memorize
# def foo(*, name, age):
#   return name, age


# foo(name="james", age=12)
# foo(name="bob", age=12)
# foo(name="james", age=12)

# print(foo.cache)



# # cache = {}

# # cache[(1, 2)] = "hello"
# # kwargs = {6: "hello", 2: "bye"}

# # cache[tuple(kwargs)] = "hello world"
# # print(cache)


def factorial(n: int):
  if isinstance(n, int):
    if n <= 1:
      return 1
    return n * factorial(n - 1)
  
# def factorial(n: int):
#   if type(n).__name__ == "int":
#     if n <= 1:
#       return 1
#     return n * factorial(n - 1)
#   else: 
#     print("hello")
  
# factorial(5.5)

ls = [1, 2, 3]
ls2 = ls.copy()

ls = [[1, 2, 3]]
ls2 = ls.copy()

# ls2[0][0] = "hello"
# print(ls)

import time

def timing(fn):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = fn(*args, **kwargs)
    print(time.time() - start)
    return result
  return wrapper
@timing
def foo():
  time.sleep(2)


# foo()


# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# print(colors[2::2])
# print(colors[-2::-2])
# print(colors[-2:])


# def isPowerOfTwo(n: int) -> bool:
#   count = 0
#   while(n != 0):
#     if n % 2 != 0:
#       count += 1
#     n //= 2
#   return True if count == 1 else False

# def isPowerOfTwo(n: int) -> bool:
#   count = 0
#   while(n != 0):
#     if n & 1 == 1:
#       count += 1
#     n >>= 1
#   return True if count == 1 else False


def isPowerOfTwo(n: int) -> bool:
  count = 0
  while(n != 0):
    if n % 2 != 0:
      count += 1
    n //= 2
  return True if count == 1 else False

# 1
# 10
# 100
# 1000
# 10000
# 1010
# 110

# 4 == 100 - 1
# 11
# 8 = 1000 -1
# 111
# 16 = 10000 - 1
# 1111

def isPowerOfTwo(n: int) -> bool:
  if ((n - 1) & n) == 0 and n != 0:
    return True
  return False

# print(isPowerOfTwo(5))
# print(isPowerOfTwo(4))
# print(isPowerOfTwo(64))
# print(isPowerOfTwo(0))


main_dict = {}
def insert_item(item):
   if item in main_dict:
       main_dict[item] += 1
   else:
       main_dict[item] = 1

insert_item('Key1') 
# main_dict = {'Key1': 1}
insert_item('Key2')
# main_dict = {'Key1': 1, 'Key2': 1}
insert_item('Key2')
# main_dict = {'Key1': 1, 'Key2': 2}
insert_item('Key3')
# main_dict = {'Key1': 1, 'Key2': 2, 'Key3':1}

insert_item('Key1')
# main_dict = {'Key1': 2, 'Key2': 2, 'Key3':1}


# print (len(main_dict))

def decorator(fn):
  def wrapper(*args, **kwargs):
    result = fn(*args, **kwargs)
    print(f'{fn.__name__}({args}, {kwargs})->{result}')
    return result
  return wrapper

@decorator
def display(i, j):
    x, y = i, j
    return x * y
# display(4, 6)   
# prints out display((4, 6), {}) -> 24

def base(n):
  def pow(x):
    return x ** n
  return pow

square = base(2)  

# print(square(5))

# print(square.__closure__)



def outer(N):
  ls = []
  for i in range(N):
    print(i)
    def inner(x):
      return x * i  
    # inner.__closure__(cell -> 0x100)
    # inner.__closure__(cell -> 0x200)
    # inner.__closure__(cell -> 0x300)
    # inner.__closure__(cell -> 3)
    # inner.__closure__(cell -> 0x500)
    ls.append(inner)



  return ls

# result = outer(5)
# for foo in result:
#   print(foo(3))

import math

# print(math.trunc(-5 / 2))
# print(math.floor(-5 / 2))


def foo():
    college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    return list(enumerate(college_years, 2019))


# print(foo())


def custom_enumerate(iterable, start = 0):
  res = []
  
  for i in iterable:
    res.append((start, i))
    start += 1
  return res

# print(custom_enumerate(['Freshman', 'Sophomore', 'Junior', 'Senior'], 2019))


ls = [bool(None), bool('muchacha'), 0, int(), bool()]

# [False, True, 0, 0, False]

# [0, 1, 0, 0, 0]
# [0, 0, 0, 0, 1]
# [False, 0, 0, False, True]

ls.sort()

# print(ls)


def foo(bar=None):
    if bar is None:
        bar = []
    bar.append(1)
    return bar

# print(foo()) # [1]
# print(foo()) # [1]
# print(foo([1, 2, 3, 4])) # [1, 2, 3, 4, 1]


# Example usage of the closure
make_multiplier = lambda X: lambda n: X * n
multiplier_of_3 = make_multiplier(3)
print(multiplier_of_3(10))  # Expected output: 30