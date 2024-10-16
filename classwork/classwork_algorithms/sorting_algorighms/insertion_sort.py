from typing import List
import random
import time




def insertion_sort(nums: List[int])->None:
  for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
      nums[j + 1] = nums[j]
      j -= 1
    key, nums[j + 1] = nums[j + 1], key





if __name__ == '__main__':
  nums = [random.randint(1, 100) for i in range(10000)]

  start = time.perf_counter()

  insertion_sort(nums)

  end = time.perf_counter()

  print(f"Time for insertion sort: {round(end - start, 6)} seconds")


  start = time.perf_counter()

  insertion_sort(nums)

  end = time.perf_counter()

  print(f"Time for insertion sort: {round(end - start, 6)} seconds")

