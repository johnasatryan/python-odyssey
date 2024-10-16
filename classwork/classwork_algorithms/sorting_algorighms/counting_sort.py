from typing import List
import random
import time




def counting_sort(nums: List[int])->None:
  max_value = max(nums)

  count = [0] * (max_value + 1)

  for i in range(len(nums)):
    count[nums[i]] += 1

  # cumulative count

  print(count)

  for i in range(1, len(count)):
    count[i] += count[i - 1]

  output = [0] * len(nums)

  for i in range(len(nums) - 1, -1):
    output[count[nums[i] - 1]] = count[i]
    count[i] -= 1

  return output
 



if __name__ == '__main__':
  nums = [random.randint(1, 100) for i in range(10)]

  start = time.perf_counter()

  print(counting_sort(nums))

  end = time.perf_counter()

  print(nums)
  print(f"Time for insertion sort: {round(end - start, 6)} seconds")
  # print(nums)

