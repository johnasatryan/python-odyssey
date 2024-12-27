from fastapi import APIRouter, Depends, HTTPException, status
from schemas.order import OrderCreate, OrderResponse
from helpers.dependencies import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from models.order import Order, OrderItem
from sqlalchemy.future import select
from models.product import Product
from database.db import get_db
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])


# Create a new order
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Ensure the total price is calculated and products exist
    total_price = 0
    for item in order_data.items:
        product = await db.get(Product, item.product_id)
        if not product: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {item.product_id} not found.",
            )
        if not product.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with ID {item.product_id} is not active.",
            )
        total_price += product.price * item.quantity

    # Create the order
    new_order = Order(
        user_id=current_user.id,
        total_price=total_price,
        status=order_data.status,
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    # Create the order items
    for item in order_data.items:
        product = await db.get(Product, item.product_id)
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price,
        )
        db.add(order_item)

    await db.commit()
    return new_order


# Get all orders for the current user
@router.get("/", response_model=List[OrderResponse])
async def get_orders(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    query = select(Order).where(Order.user_id == current_user.id).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


# Get a specific order by ID
@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    order = await db.get(Order, order_id)
    if not order or order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found.",
        )
    return order


# Update order status (Admin-only)
@router.put("/{order_id}/status", response_model=OrderResponse)
async def update_order_status(
    order_id: int,
    status: str,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Ensure only admins can update order statuses
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action.",
        )

    order = await db.get(Order, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found.",
        )

    if status not in ["PENDING", "ARRIVING", "DELIVERED"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid status. Allowed values: PENDING, ARRIVING, DELIVERED.",
        )

    order.status = status
    await db.commit()
    await db.refresh(order)
    return order


# Delete an order (Admin-only)
@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Ensure only admins can delete orders
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action.",
        )

    order = await db.get(Order, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found.",
        )

    await db.delete(order)
    await db.commit()
    return {"detail": "Order deleted successfully"}
