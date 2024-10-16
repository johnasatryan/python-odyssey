from typing import List
import random
import time

from insertion_sort import insertion_sort


def selection_sort(nums: List[any])->None:
  for i in range(len(nums)):
    minIndex = i
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[minIndex]:
        minIndex = j

    nums[i], nums[minIndex] = nums[minIndex], nums[i]




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @property
  def age(self):
    return self.__age
  
  @property
  def name(self):
    return self.__name
  
  @age.setter
  def age(self, value):
    if value < 0:
      raise ValueError
    self.__age = value

  @name.setter
  def name(self, value):
    if value == "":
      raise ValueError
    self.__name = value

  def __lt__(self, other):
    return self.__age < other.__age
  
  def __repr__(self):
    return f"{self.__name}: {self.__age}"
  



if __name__ == '__main__':

  # nums = [random.randint(1, 100) for i in range(10000)]

  # start = time.perf_counter()

  # selection_sort(nums)

  # end = time.perf_counter()

  # print(f"Time for insertion sort: {round(end - start, 6)} seconds")

  # start = time.perf_counter()

  # selection_sort(nums)

  # end = time.perf_counter()

  # print(f"Time for insertion sort: {round(end - start, 6)} seconds")
  # print(nums)

  names = ["Bob", "James", "Ann", "Tylor", "Valod"]
  persons = [Person(names[0], 30), Person(names[1], 22), Person(names[2], 22), Person(names[4], 18), Person(names[3], 10)]



  print(persons)

  selection_sort(persons)
  print(persons)

  print()
  persons = [Person(names[0], 30), Person(names[1], 22), Person(names[2], 22), Person(names[4], 18), Person(names[3], 10)]

  print(persons)

  insertion_sort(persons)
  print(persons)

