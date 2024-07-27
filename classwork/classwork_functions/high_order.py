
names = ["James", "Bob", "Ann", "Bryan"]
ages = [23, 12, 45]

# [("James", 23), ("Bob", 12)...]

# print(help(zip))

zip_object = zip(names, ages)

# it = iter(zip_object)

# for item in zip_object:
#   print(item)

# __str__ || __repr__ 

# person = {"James" : 12}

# person.keys()

# def custom_zip(*iterables, strict=False):
#   min_length = len(iterables[0])

#   for i in range(1, len(iterables)):
#     if min_length > len(iterables[i]): # (["Bob", "James"], [23, 12])
#       min_length = len(iterables[i])

#   res = []
#   for i in range(min_length):
#     tmp = []

#     for item in iterables:
#       tmp.append(item[i])
#     res.append(tuple(tmp))
#   return res



# def custom_zip(*iterables, strict=False):
#   min_length = min([len(x) for x in iterables])

#   res = [tuple([item[i] for item in iterables]) for i in range(min_length)]
#   return res

def custom_zip(*iterables, strict=False):
  # min_length = min([len(x) for x in iterables])
  iterators = [iter(it) for it in iterables]
  res = []
  while True:
    try:
      res.append(tuple([next(it) for it in iterators]))
      print("exception chka")
    except StopIteration:
      print("stex exception arden qcela")
      break
  return res


# print(custom_zip(names, ages))

def foo(a, b):
  if b < 0:
    raise StopIteration
  
  print("ameninch oka")


try:
  i = 9
  foo(1, -2)


except StopIteration:
  print("nenc areci tsragirs chkangni")

print("hello world")





# it1 = iter(names)
# it2 = iter(ages)

# print(it1)
# print(it2)
