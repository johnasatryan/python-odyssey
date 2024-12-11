from .users import router as users_router
from .products import router as products_router
from .orders import router as orders_router

__all__ = ["users_router", "products_router", "orders_router"]
