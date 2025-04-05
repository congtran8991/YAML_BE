
from sqlalchemy.ext.asyncio import AsyncSession
from apps.products.models import ProductModel
from sqlalchemy import text, select

class ProductUtils:

    @staticmethod
    async def create_product(
        db_session: AsyncSession,
        # show_name: str,
        # user: str = None,
        # price: float = None,
    ) -> int:
        product = ProductModel(
            procduct_name="product1",
            price=100,
        )

        async with db_session.begin():
            db_session.add(product)
            await db_session.flush()
            product_id = product.id
            await db_session.commit()
        return product_id
    
    @staticmethod
    async def get_product_data(
        db_session: AsyncSession,
    ) -> dict:
        
        # Way1: Raw query
        # query = text(" select * from product;")
        # result = await db_session.execute(query)
        # rows = result.all()
        # return rows

        # Way2: SQLalchemy support
        query = select(ProductModel)
        result = await db_session.execute(query)
        data = result.scalars().all()
        if data:
            final_data = {"name": data[0].procduct_name, "price": data[0].price}
        else:
            final_data = {}
        return final_data
