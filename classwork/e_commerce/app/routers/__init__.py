from routers.auth import router as auth_router
from routers.orders import router as orders_router
from routers.products import router as products_router
from routers.users import router as users_router



__all__ = [
  "auth_router",
  "orders_router",
  "products_router",
  "users_router"
]