# # # # # # first_question

# # # # # x = 54

# # # # # def some(arg = x):
# # # # #   print(arg)
# # # # #   print(x)


# # # # # x = get_user_id()

# # # # # some()

# # # # # x = 23

# # # # # x = "hello"

# # # # # second question
# # # # import time

# # # # def measure_time(origin):
# # # #   def wrapper(*args, **kwargs):
# # # #     start = time.time()
# # # #     result = origin(*args, **kwargs)
# # # #     # return result
# # # #     # return origin(*args, **kwargs)
# # # #     end = time.time() - start
# # # #     print(f"Function run : {end}")
# # # #     return result
# # # #   return wrapper

# # # # # @measure_time
# # # # def add(a, b):
# # # #   time.sleep(4)
# # # #   return a + b

# # # # add = measure_time(add)
# # # # result = add(1, 5)

# # # # print(result)


# # # # def out():
# # # #   time.sleep(2)
  

# # # # out = measure_time(out)

# # # # print(out())


# # # def decortator(fn):
# # #   count = 0
# # #   def wrapper(*args, **kwargs):
# # #     nonlocal count;
# # #     count += 1
# # #     return fn(*args, **kwargs)
# # #   return wrapper

# # # def get_count_of_length(ls: list)->list:
# # #   return [len(word) for word in ls]

# # #   # for word in ls:
# # #   #   res.append(len(word))
  
# # #   # return res
# # ls = ["hello", "bye", "python", "js", "cpp"]

# res = map(lambda word: len(word), ["ss"])


# # [5, 3, 6, 2, 3]

# # # new_ls = get_count_of_length(ls)

# # # print(new_ls)
# # # print(list(res))

# # # 5-th question 

# # # print(5 / 2) true division 
# # # print(-5 // 2) # floor division

# # import math

# # print(math.floor(-5 / 2))

# x = 23
# ls = [1]
# flag = False

# # for i in dir(ls):
# #   if i == '__iter__':
# #     flag =True
# #     break

# # if flag == True:
# #   print("Iterable")
# # else: 
# #   print("Non iterable")


# # print(dir(x))


# for item in dir([]):
#   if item == "__iter__":
#     print("Iterable")
#     break
# else:
#   print("Non iterable")

# for item in dir([]):
#   if item == "__iter__":
#     print("Iterable")
#     break
#   else:
#     for i in range(1):
#       if True:
#         pass
#       else:
#         pass
# else:
#   print("Non iterable")


# # print(getattr(x, '__iter__'))

# from typing import Iterable, Callable


# # print(isinstance(x, Iterable))

# # it = iter(ls)

# # print(next(res))



# # for i in res:
# #   ls.append(i)


# # print(ls)

# def foo(ls):
#   ls.append(1)

# ls = []


# # foo(ls)
# # foo(ls)
# # foo(ls)
# # foo(ls)

# # print(ls)
# import ctypes

# def getrefcount(address):
#   return ctypes.c_long.from_address(address).value

# def fn2(x):
#   print(getrefcount(id(x)))

#   x = {'key': 'value'}
#   print(getrefcount(id(x)))



# x = ["hello", "av", "sadgasgsafasdfsad"]
# print(getrefcount(id(x)))

# fn2(x)
# print("reference count of list", getrefcount(id(x)))


ls = [1, 2, 3]

ls2 = ls
ls2.append(234)
ls = "hello"
print(ls2)
