# # def foo():
# #   print('chlp->foo')


# # def bar():
# #   print('bar->foo')


# # import run

# # run.chlp2.some()

# import run

# print("name of modules", __name__)


def factorial(n: int)->int:
  return 1 if n <= 1 else n * factorial(n - 1)


def random():
  return factorial(5)


