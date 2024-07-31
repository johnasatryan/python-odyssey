# # def outer():
# #   x = 'python'

# #   print(hex(id(x)))
# #   def inner():
# #     print('{0} awesome'.format(x))
# #   print(inner.__closure__)

# # fn = outer()
# # # 


# # def power(n):
# #   print('hello world')
# #   def inner(x):
# #     print(hex(id(n)))
# #     return x ** n
# #   return inner

# # square = power(2)
# # print(hex(id(2)))
# # print(square.__closure__)
# # free variables

# import ctypes

# def getRefCount(address):
#   return ctypes.c_long.from_address(int(address)).value


# def outer(ls):
#   def inner():
#     print(ls)
#     print(getRefCount(id(ls)))
  

#   print(inner.__closure__)

#   # return inner
# ls = [1, 2, 3]
# print(hex(id(ls)))
# x = outer(ls)

# # del ls
# # x()
# # print(x.__code__.co_freevars)

# def fn():
#   pass

# fn.age = 23
# print(fn.__dict__)

# def outer():
#   count = 0

#   def inner():
#     nonlocal count;
#     print("address of count in inner before changing: ", hex(id(count)))

#     count += 1
#     print("address of count in inner after changing: ", hex(id(count)))
#     return count
  
#   print("address of count in outer: ", hex(id(count)))
#   return inner


# fn = outer()

# print(fn.__closure__)
# fn()
# print(fn.__closure__)
# xn = outer()

# xn()
# print(xn.__closure__)


def outer():
  count = 0

#   def inner1():
#     nonlocal count;
#     count += 1
#     return count
  
#   def inner2():
#     nonlocal count;
#     count += 1
#     return count
#   print(inner1.__closure__)
#   print(inner2.__closure__)
#   return (inner1, inner2)

# # f1, f2 = outer()
# f1, f2 = outer()


# outer()

# # print(f1())
# # print(f2())
# print("before f1 & f2 call")
# f1()
# f2()
# print(f1.__closure__)
# print(f2.__closure__)

# print("after f1 & f2 call")


# def f1():
#   a = 13
#   b = 23

#   def f2():
#     a and b
#   print(f2.__closure__)
#   print(f1.__closure__)

# f1()
a = 23
def foo(a, b, c):
  a = 23
  def bar():
    print(a)
  
  bar()

print(help(foo.__code__))
x= foo
print(x.__name__)
