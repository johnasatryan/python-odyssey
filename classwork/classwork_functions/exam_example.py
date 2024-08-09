# # # # # # # first_question

# # # # # # x = 54

# # # # # # def some(arg = x):
# # # # # #   print(arg)
# # # # # #   print(x)


# # # # # # x = get_user_id()

# # # # # # some()

# # # # # # x = 23

# # # # # # x = "hello"

# # # # # # second question
# # # # # import time

# # # # # def measure_time(origin):
# # # # #   def wrapper(*args, **kwargs):
# # # # #     start = time.time()
# # # # #     result = origin(*args, **kwargs)
# # # # #     # return result
# # # # #     # return origin(*args, **kwargs)
# # # # #     end = time.time() - start
# # # # #     print(f"Function run : {end}")
# # # # #     return result
# # # # #   return wrapper

# # # # # # @measure_time
# # # # # def add(a, b):
# # # # #   time.sleep(4)
# # # # #   return a + b

# # # # # add = measure_time(add)
# # # # # result = add(1, 5)

# # # # # print(result)


# # # # # def out():
# # # # # #   time.sleep(2)
  

# # # # # # out = measure_time(out)

# # # # # # print(out())


# # # # # def decortator(fn):
# # # # #   count = 0
# # # # #   def wrapper(*args, **kwargs):
# # # # #     nonlocal count;
# # # # #     count += 1
# # # # #     return fn(*args, **kwargs)
# # # # #   return wrapper

# # # # # def get_count_of_length(ls: list)->list:
# # # # #   return [len(word) for word in ls]

# # # # #   # for word in ls:
# # # # #   #   res.append(len(word))
  
# # # # #   # return res
# # # # ls = ["hello", "bye", "python", "js", "cpp"]

# # # res = map(lambda word: len(word), ["ss"])


# # # # [5, 3, 6, 2, 3]

# # # # # new_ls = get_count_of_length(ls)

# # # # # print(new_ls)
# # # # # print(list(res))

# # # # # 5-th question 

# # # # # print(5 / 2) true division 
# # # # # print(-5 // 2) # floor division

# # # # import math

# # # # print(math.floor(-5 / 2))

# # # x = 23
# # # ls = [1]
# # # flag = False

# # # # for i in dir(ls):
# # # #   if i == '__iter__':
# # # #     flag =True
# # # #     break

# # # # if flag == True:
# # # #   print("Iterable")
# # # # else: 
# # # #   print("Non iterable")


# # # # print(dir(x))


# # # for item in dir([]):
# # #   if item == "__iter__":
# # #     print("Iterable")
# # #     break
# # # else:
# # #   print("Non iterable")

# # # for item in dir([]):
# # #   if item == "__iter__":
# # #     print("Iterable")
# # #     break
# # #   else:
# # #     for i in range(1):
# # #       if True:
# # #         pass
# # #       else:
# # #         pass
# # # else:
# # #   print("Non iterable")


# # # # print(getattr(x, '__iter__'))

# # # from typing import Iterable, Callable


# # # # print(isinstance(x, Iterable))

# # # # it = iter(ls)

# # # # print(next(res))



# # # # for i in res:
# # # #   ls.append(i)


# # # # print(ls)

# # # def foo(ls):
# # #   ls.append(1)

# # # ls = []


# # # # foo(ls)
# # # # foo(ls)
# # # # foo(ls)
# # # # foo(ls)

# # # # print(ls)
# # # import ctypes

# # # def getrefcount(address):
# # #   return ctypes.c_long.from_address(address).value

# # # def fn2(x):
# # #   print(getrefcount(id(x)))

# # #   x = {'key': 'value'}
# # #   print(getrefcount(id(x)))



# # # x = ["hello", "av", "sadgasgsafasdfsad"]
# # # print(getrefcount(id(x)))

# # # fn2(x)
# # # print("reference count of list", getrefcount(id(x)))


# # # ls = [1, 2, 3]

# # # ls2 = ls
# # # ls2.append(234)
# # # ls = "hello"
# # # print(ls2)

# # def foo(ls: list)->any:
# #   temp = ls[:]

# # word = "hello"
# # ls = [1, 2, 3]
# # # print(word[1:3])
# # # print(word)

# # # print(hex(id(ls)))
# # # ls2 = ls
# # # print(hex(id(ls2)))

# # # print(hex(id(ls[:])))

# # import copy

# # def foo(ls: list)->any:
# #   # temp = copy.copy(ls)
# #   # temp = ls[:]
# #   # temp = ls.copy()
# #   temp = copy.deepcopy(ls)
# #   print("In function", id(temp))
# #   print("In function", id(temp[0]))
# #   temp[0][0] = "hello"

# # ls = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# # foo(ls)

# # print("outside function", id(ls))
# # print("outside function", id(ls[0]))


# from typing import Iterable
# # temp = []
# # # def custom_deep(iterable):

# # #   if iterable is not Iterable:
# # #     return iterable
  
# # #   while True:
# # #     iterator = iter(iterable)
# # #     if iterator is Iterable:
# # #       custom_deep(iterator)

# # custom_deep([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # def shallow_copy(ls):
# #   res = []

# #   for item in ls:
# #     res.append(item)
# #   return res

# # ls = [1, 2, 3]
# # ls2 = shallow_copy(ls)

# # ls2[0] = "hello"

# # print(ls)
# # print(ls2)

# # res = []
# # def custom_deep(iterable):
# #   if type(iterable).__name__ in set(("int", "float", "str", "tuple", "bool")):
# #     # print(f"iterable is {iterable} inside base case")
# #     return iterable
# #   if isinstance(iterable, list):
# #     return [custom_deep(elem) for elem in iterable]
# #   # for iterr in iterable:
# #   #   # print(f"iterr is {iterr} inside for")
# #   #   res.append(custom_deep(iterr))
   



# # simple_list = [[1, 2, 3], [4, 5, 6]]
# # returned_list = custom_deep(simple_list)
# # # print(res)

# # returned_list[0][0] = "hello" 
# # print(returned_list)
# # print(simple_list)


# # copy.deepcopy([(1, 3, 3), [34, 2]])
# import time
# def memoize(fn):
#   cache = {}
#   def wrapper(n):
#     if not n in cache:
#       result = fn(n)
#       cache[n] = result
  
#     return cache[n]
#   return wrapper

# @memoize
# def factorial(n):
#   return 1 if n <= 1 else n * factorial(n - 1)

# import sys

# sys.setrecursionlimit(1000000)

# start = time.time()

# x = factorial()

# print("first call", time.time() - start)


# start = time.time()
# x = factorial()

# print("second call", time.time() - start)



# multiplier_of_3 = make_multiplier(3)
# print(multiplier_of_3(10))  # Expected output: 30

# closure = lambda n : lambda X: n * X

# multiplier_of_3 = closure(3)
# print(multiplier_of_3(4))


# def foo(arg):
#   print(arg + 1)

# def foo(arg1, arg2):
#   print(arg1 + arg2)

# foo(1)
def process_data_1(x):
  return x ** 2

def process_data_2(x, y):
  return x * y

def process_data_3(*, name, age):
  return {name, age}


def process_data(*args, **kwargs):
  if len(args) == 1 and isinstance(args[0], int):
    return process_data_1(args[0])
  elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
    return process_data_2(args[0], args[1])
  elif kwargs:
    return process_data_3(**kwargs)

  else: 
    print("yuhu")



print(process_data(5))
print(process_data(5, 10))
print(process_data(name="Alice", age=30))
print(process_data(1, 2, 3))