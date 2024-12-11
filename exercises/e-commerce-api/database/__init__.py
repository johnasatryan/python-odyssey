import os
import json

DATABASE_DIR="database/json_files"
USERS_FILE=os.path.join(DATABASE_DIR, "users.json")
PRODUCTS_FILE=os.path.join(DATABASE_DIR, "products.json")
ORDERS_FILE=os.path.join(DATABASE_DIR, "orders.json")

USERS_DATA={}
PRODUCTS_DATA=[]
ORDERS_DATA=[]

def ensure_file_exists(file_path:str, data):
  if not os.path.exists(file_path):
    with open(file_path, "w") as file:
      json.dump(data, file, indent=2)

def initialize_database():
  os.makedirs(DATABASE_DIR, exist_ok=True)
  ensure_file_exists(USERS_FILE, USERS_DATA)
  ensure_file_exists(PRODUCTS_FILE, PRODUCTS_DATA)
  ensure_file_exists(ORDERS_FILE, ORDERS_DATA)
  print("database initialized")