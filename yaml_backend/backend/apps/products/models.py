from database_setting import ModelBase
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

class ProductModel(ModelBase):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    procduct_name: Mapped[str]
    price: Mapped[float] = mapped_column(nullable=True)