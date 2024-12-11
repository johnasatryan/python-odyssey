from helpers import read_json, write_json
from database.__init__ import ORDERS_FILE

def get_all_orders():
  return read_json(ORDERS_FILE)


def order_by_id(order_id):
  all_orders = get_all_orders()
  for order in all_orders:
    if order["_id"] == order_id:
      return order
  return {}


def add_order(order):
  all_orders = get_all_orders()
  new_id = len(all_orders) + 1
  new_order = {"_id": new_id}
  new_order.update(order)
  all_orders.append(new_order)
  write_json(ORDERS_FILE, all_orders)
  return new_id

