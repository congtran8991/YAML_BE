from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from apps.products.schema import ProductSchemaTest
from apps.products.models import ProductModel
from database_connection import get_db_session
from apps.products.ultils import ProductUtils

router = APIRouter()

@router.get("/products/test")
async def product_test():
    return {"Hello Product Test"}

@router.post("/products/add")
async def product_test_add(request_data: ProductSchemaTest):
    print("DDDEEEBUUG")
    print(request_data)
    return {"Hello Product Add Test"}

@router.get("/products/get_data_test")
async def product_test_data(db_session: Annotated[AsyncSession, Depends(get_db_session)]):
    """
        This URL is used for testing only
    """
    
    # Create data for Product table
    # product_id = await ProductUtils.create_product(db_session)

    # Get data of Product table
    product_data = await ProductUtils.get_product_data(db_session)

    return {f"Hello Product Test : product_id ={product_data}"}