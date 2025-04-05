from datetime import datetime
from database_setting import ModelBase
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import DateTime, func

class UserModel(ModelBase):
    __tablename__ = "coffee_users"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(unique= True)
    email: Mapped[str] = mapped_column(unique=True)
    phone_number: Mapped[str]
    hased_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default= False)
    role: Mapped[str] 
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
