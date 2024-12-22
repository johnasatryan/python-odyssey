from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from schemas.product import ProductCreate, ProductResponse
from models.product import Product
from models.db import get_db
from helpers.dependencies import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

# Create a new product
@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),  # Ensure the user is authenticated
):
    # Ensure only admins can create products
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action.",
        )
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        image_url=product.image_url,
        is_active=True,
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


# Get all products
@router.get("/", response_model=List[ProductResponse])
async def get_products(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    query = select(Product).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


# Get a product by ID
@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product


# Update a product
@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),  # Ensure the user is authenticated
):
    # Ensure only admins can update products
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action.",
        )
    
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    
    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.category = product_data.category
    product.image_url = product_data.image_url
    product.is_active = True  # Reactivate if being updated

    await db.commit()
    await db.refresh(product)
    return product


# Delete a product
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),  # Ensure the user is authenticated
):
    # Ensure only admins can delete products
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action.",
        )
    
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    
    await db.delete(product)
    await db.commit()
    return {"detail": "Product deleted successfully"}
