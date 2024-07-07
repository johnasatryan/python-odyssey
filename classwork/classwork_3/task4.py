# Ստեղծել ծրագիր, որը կներառի օգտատերերի տվյալների ներմուծումը, 
# պահպանումը բառարանում և ցուցակում, ապա ցույց կտա օգտատերերին 
# ըստ ներմուծված անվան(“Not found”, եթե այդպիսի օգտատեր գոյություն չունի)։ 
# Յուրաքանչյուր օգտատեր պետք է ունենա հետևյալ դաշտերը՝ 
# ID, անուն, ազգանուն, Էլ. փոստ, գաղտնաբառ և հեռախոսահամար:
import random

count = ""

# count = input("Please input count of persons: ")

# if count.isdigit():
#   count = int(count)
# else:
#   print("Error")
#   exit(1)


persons = []
person = {"name": None, "surname": None, "email": None, "phone_number": None, "password": None}



# for i in range(count):
#   for key in person.keys():
#     person[key] = input(f"Enter valid {key} for {i + 1} person: ")

#   persons.append(person.copy())

# print(persons)
# person = {"name": "Bob", "surname": "Smith", "age": 15}````


persons = [{'name': 'James', 'surname': 'Smith', 'email': 'james@example.com', 'phone_number': '12345', 'password': '1234'}, 
           {'name': 'Bob', 'surname': 'Smith', 'email': 'bob@example.com', 'phone_number': '12345', 'password': '3245'}]

for person in persons:
  person["id"] = random.randint(1, 5435234)

name = input("Please enter a name: ")


x = {'name': 'James', 'surname': 'Smith', 'email': 'james@example.com', 'phone_number': '12345', 'password': '1234'}
persons = {
  "James" : {
    "phone_number": None,
    "email": None
  },
  "Bob": {
    "phone_number": None,

  }
}

persons[name]

name = id("James") + "salt" 
