import os
import json


def read_json(file_path: str):
  if not os.path.exists(file_path):
    return None
  try:
    with open(file_path, "r") as file:
      return json.load(file)
  except json.JSONDecodeError:
    return None
  
def write_json(file_path: str, data: dict | list):
  try:
    with open(file_path, "w") as file:
      json.dump(data, file)
  except json.JSONEncoder:
    return None

