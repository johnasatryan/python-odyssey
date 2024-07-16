
def some_recursion(x):
  if x < 0:
    return 645
  
  z = some_recursion(x - 1)
  print(f"z is return from base case :{z}")
  print(f"x is :{x}")



x = 5
# y = some_recursion(x)

# print(f"y is {y}")

# def acc(x):
#   sum = 0
#   for i in range(1, x + 1):
#     print(f"sum is {sum}")
#     sum += i
#   return sum



def acc(x):
  if x <= 1:
    return x
  return x + acc(x - 1)

# 5! = 5 * 4! -> 5 * 4 * 3 * 2 * 1
# 4! = 4 * 3! -> 4 * 3 * 2 * 1 
# 3! = 3 * 2! -> 3 * 2 * 1
# 2! = 2 * 1! -> 2 * 1
# 1! = 1 

# result = acc(6)
# print(result)

# def factorial(n):
#   result = 1
#   for i in range(1, n + 1):
 

#     result = i * result
#     print(f"result in every step {result}")
#     print(f"i in every step {i}")

def factorial(n):
  if n == 1:
    return 1
  
  return n * factorial(n - 1)
 

factorial(5)