from helpers import read_json, write_json
from database.__init__ import PRODUCTS_FILE

def get_all_products():
  return read_json(PRODUCTS_FILE)

def get_prod_by_id(id: int):
  products = get_all_products()
  return next((prod for prod in products if prod['_id'] == id))

def add_product(prod):
  products = get_all_products()
  new_id = len(products) + 1
  new_prod = {"_id":new_id, **prod.dict()}
  products.append(new_prod)
  return new_id


