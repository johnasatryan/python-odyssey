# 1. Abstract class
# 2. Interface class

import abc

class Animal(abc.ABC):
  @abc.abstractmethod
  def eat(self):
    ...
  
  def sleep(self):
    pass

class Dog(Animal):
  def eat(self):
    print("Dog eats bons")

dog = Dog()
dog.eat()

# print(isinstance(dog, Animal))

def run():
  pass


if __name__ == "__main__":
  run()