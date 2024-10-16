from typing import List
import random
import time




def bubble_sort(nums: List[int])->None:
  size = len(nums)
  for i in range(size - 1):
    flag = False

    for j in range(size - 1 - i):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        flag = True
    if not flag:
      break



if __name__ == '__main__':
  nums = [random.randint(1, 100) for i in range(10000)]

  start = time.perf_counter()

  bubble_sort(nums)

  end = time.perf_counter()

  print(f"Time for bubble sort: {round(end - start, 6)} seconds")


  start = time.perf_counter()

  bubble_sort(nums)

  end = time.perf_counter()

  print(f"Time for bubble sort: {round(end - start, 6)} seconds")

  # print(f"Sorted array: {nums}")