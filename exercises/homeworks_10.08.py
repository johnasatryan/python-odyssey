# # # # def counter_statistics(file_path: str):
# # # #   fs = open(file_path, 'r')

# # # #   content = fs.read()
# # # #   fs.close()

# # # #   lines_count = content.count('\n') + 1

# # # #   words_count = len(content.split())

# # # #   characters_count = len(''.join(content.split()))

# # # #   fs = open('statistics.txt', 'w')

# # # #   fs.write(f"Lines: {lines_count}\nWords: {words_count}\nCharacters: {characters_count}")

# # # #   fs.close()

# # # # counter_statistics('file.txt')


# # # def counter_statistics(file_path: str):
# # #   fs = open(file_path, 'r')

# # #   lines = fs.readlines()
# # #   lines_count = len(lines)
# # #   # words_count = [len(item.split()) for item in lines]  
# # #   words_count = 0
# # #   characters_count = 0

# # #   for item in lines:
# # #     splited = item.split()
# # #     words_count += len(splited)
# # #     # print("splited:", splited)
# # #     for word in splited:
# # #       characters_count += len(word)
# # #   fs = open('statistics.txt', 'w')

# # #   fs.write(f"Lines: {lines_count}\nWords: {words_count}\nCharacters: {characters_count}")

# # #   fs.close()

# # # counter_statistics('file.txt')

# # import json

# # # Karevor funkcianer
# # # 1. load & loads
# # # 2. dump & dumps



# # def process_json_file(file_path, output_path, attribute, value):
# #   fs = open(file_path)
# #   data = json.load(fs)
# #   fs.close()

# #   filtered_data = []
# #   for item in data:
# #     if item[attribute] == value:
# #       filtered_data.append(item)
  
# #   fs = open(output_path, 'w')
# #   # json.dump(filtered_data, fs, indent=2)
# #   data = json.dumps(filtered_data, indent=2)
# #   # fs.write(str(filtered_data)) No No No
# #   fs.write(data)

# #   # data_string = fs.read()
# #   # data = json.loads(data_string)






# # ls = process_json_file('input.json', 'outputt.json', 'age', 30)


# def validate(fn):
#   def wrapper(*args, **kwargs):

#     for arg in args:
#       if not isinstance(arg, int) or arg < 0:
#         return "Arguments must be positive integers"
#     for kwarg in kwargs.values():
#       if not isinstance(kwarg, int) or kwarg < 0:
#          return  "Arguments must be positive integers"
       
#     return fn(*args, **kwargs)
  
#   return wrapper
  
# @validate
# def add(a:int, b:int)->int:
#   return a + b

# # print(add(1, 5))
# # print(add(1, 5.5))
# # print(add(-1, -5.5))


# @validate
# def add(a:int, b:int, *, c)->int:
#   return a + b + c


# print(add(1, b = 22, c = 3.5))

# import time 


# def retry(delay):
#   def limit_funtion(limit):
#     def decorator(fn):
#       def wrapper(*args, **kwargs):
        
#         for i in range(limit):
#           try:
#             return fn(*args, **kwargs)
#           except Exception as e:
#             print(f"Function can't be executed {i + 1} time, trying execute after {delay}")
#             time.sleep(delay)
#         raise ValueError("Function can't  be executed anymore")
#       return wrapper
#     return decorator
#   return limit_funtion

# arg = int(input("Enter retry limit: "))

# @retry(1)
# def read_file(file_path):
#   fs = open(file_path)
#   return fs.read()


# try:
#   read_file('fil.txt')
# except ValueError as e:
#   print(e)


def isPrime(n: int)->bool:

  if n <= 1:
    return False
  if n == 2:
    return True
  
  limit = int(n ** 0.5) + 1
  for i in range(3, limit, 2):
    if n % i == 0:
      return False
  return True
n = 25
i = 5

def foo(n):
  if n <= 1:
    return False
  if n == 2 or n == 3:
    return True
  
  if n % 2 == 0 or n % 3 == 0:
    return False
  
  i = 5

  while( i * i <= n):
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True
    

print(foo(647))
