# # from threading import Thread
# # import time

# # def counting_ints(numbers):
# #   for num in numbers:
# #     print(f"num is: {num}")
# #     time.sleep(0.5)



# # def counting_letters(letters):
# #   for letter in letters:
# #     print(f"letter is: {letter}")
# #     time.sleep(0.5)




# # if __name__ == '__main__':
# #   numbers = [1, 2, 3, 4, 5]

# #   letters = ['A', 'B', 'C', 'D', 'E']


# #   thread1 = Thread(target=counting_ints, args=(numbers, ))
# #   thread2 = Thread(target=counting_letters, args=(letters, ))

# #   thread1.start()
# #   thread2.start()
  


# #   thread1.join()
# #   thread2.join()

# #   print("Finishing execution of programm...")


# import time
# import random


# def calculate_square(numbers: list) -> None:
#   for num in numbers:
#     print(f"Square of num: {num ** 2}")
#     time.sleep(0.5)


# import multiprocessing
# import threading


# if __name__ == '__main__':
#   start = time.perf_counter()
  
#   numbers = [random.randint(1, 100) for x in range(25)]

#   process1 = threading.Thread(target=calculate_square, args=(numbers[:13],))
#   process2 = threading.Thread(target=calculate_square, args=(numbers[12:],))


#   process1.start()
#   process2.start()

#   process1.join()
#   process2.join()
#   # calculate_square(numbers)

#   print(f"Execution of programm: {time.perf_counter() - start:.3f}")




import asyncio

async def fetch_from_url(url:str)->str:
  print(f'Starting to fetch data from url...{url}')
  print('Data fetched...')
  return f'{url}-data'



async def main():
  urls = ['https://example.com/source1', 'https://example.com/source2', 'https://example.com/source3']

  tasks = [ await fetch_from_url(url) for url in urls]


  print("hello world")
  # results = await asyncio.gather(*tasks)

  for result in tasks:
    print(result)




asyncio.run(main())

