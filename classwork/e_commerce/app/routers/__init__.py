from .auth import router as auth_router
from .orders import router as orders_router
from .products import router as products_router
from .users import router as users_router


__all__ = [
  "auth_router",
  "orders_router",
  "products_router",
  "users_router"
]