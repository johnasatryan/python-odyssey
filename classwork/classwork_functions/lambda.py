# անուն ֆունցկիաներ, որոնք կիրառության տեսանկյունից, հնարավոր է դարձնում սահմանել ֆունկցիա այնտեղ, որտեղ def-ը անզոր է

# a = -5

# if a > 0:
#   def foo():
#     return 16
# else:
#   def bar():
#     return "hello"
  
# print(bar())


# def foo(x, y): return x + y


mp_it = map(lambda x, y:x + y, [1, 2, 3], [4, 5, 6])

# print(list(mp_it))

# lambda arguments if exist : այստեղ գոյություն ունի թակնված return, հետո expression

# ft_it = filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5])

# foo = lambda x: x %2 != 0
# print(foo(2))

def foo(x):
  return x + x

def bar(fn):
  return fn()

new_foo = lambda : foo(bar(lambda : "hello"))

print(new_foo())
# case 1: error
# case 2: "hello world", None chisht
# case 3: "hello world"
# case 4: None
# x = lambda: '''return''' 5
# print(x())

# new_foo = lambda : print("hello world")
# new_foo = lambda: return None
