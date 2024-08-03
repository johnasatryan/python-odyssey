# # @decorator

# def decorator(fn):
#   def inner(*args):
#    last_arg = args[len(args) - 1]
#    if last_arg == 0:
#      print("ches karogh 0-i bajanel")
#      return
#    result = fn(*args)
#    return result + 10

#   return inner

# def div(arg1, arg2):
#   return arg1 // arg2


# # def div(arg1, arg2, arg3):
# #   result = arg1 + arg2
# #   return result // arg3


# some_chlp = decorator(div)

# # print(div(134, 0))

# print(some_chlp(8, 2))



# # new_function = decorator(function)

# # new_function()


# # div(5, 0)





# def add(**di):
#   print(f"di: {di}")



# add(arg2=1, arg1= 2, arg3= 2)

# def foo(a, b, c, /):
#   print(a, b, c)


# di = {'a': 97, 'b': 98, 'c': 99}

# foo(**di)
# foo(a = 97, l = 98, c = 99)


def decorator(fn):
  print('chlp+++++')
  def inner(*args, **kwargs):
   print('decorator called...')
   print(f"function name is: {fn.__name__}")
   print(f"function positional arguments are: {args}")
   print(f"function keyword arguments are: {kwargs}")
   print(f"function annotations are: {fn.__annotations__}")
   result = fn(*args, **kwargs)
   return result

  return inner

# @decorator
def add(pos1, pos2, *, arg1: int, arg2: int)->int:
  '''add function to add two positional arguments, \n
     also add two keyword arguments. 
  '''
  return pos1 + pos2 + arg1 + arg2

# print(help(add))

# add(4, 23, arg1 = 1, arg2 = 2)

# print(help(add))


# print(help(print))

# print_ = decorator(print)

# print_("hello world")

# add = decorator(add) ======= @decorator

# add(4, 23, arg1 = 1, arg2 = 2)


# def login_require(fn):
#   print("97 line", fn.__name__)
#   def wrapper(*args, **kwargs):
#     print("login require called...")
#     return fn(*args, **kwargs)
#   return wrapper

# @login_require
# # @decorator
# def foo():
#   pass

# foo()






# def fact(fn):
#   def wrapper(*args, **kwargs):
#     print('hello world')
#     return fn(*args, **kwargs)
#   return wrapper

# @fact
# def factorial(n):
#   if n <= 1:
#     return 1
#   return n * factorial(n - 1)

# print(factorial(5))


# def login_require(fn):
#   import inspect
#   def wrapper(*args, **kwargs):
#     for item in args:
#       if not item:
#         raise ValueError("Some fields are required...")
#     return fn(*args, **kwargs)
#   # wrapper.__name__ = fn.__name__
#   # wrapper.__annotations__ = fn.__annotations__
#   # wrapper.__doc__ = fn.__doc__
#   wrapper.__signature__ = inspect.signature(fn)
#   # wrapper.__code__.co_varnames = fn.__code__.co_varnames


#   return wrapper
from functools import wraps


def login_require(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    for item in args:
      if not item:
        raise ValueError("Some fields are required...")
    return fn(*args, **kwargs)
 


  return wrapper


def ankap():

  @login_require
  def signin(email: str, password: str)->str:
    '''
      This function helps to login to your acount...
    '''
    pass
  print(help(signin))
  signin("example@gmail.com", "123456")


# ankap()

def login_require(fn):
  # print(fn.__name__)
  def wrapper(fn2):
    print(fn2.__name__)
  return wrapper

def bar():
  pass

def foo():
  pass


new_foo = login_require(foo)
new_foo(bar)


