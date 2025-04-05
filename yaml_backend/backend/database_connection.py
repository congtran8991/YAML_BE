import os
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
SQLALCHEMY_DATABASE_URL= "postgresql+asyncpg://admin:admin@yaml_sql_db/yaml_db"

def get_engine():
    return create_async_engine(
        SQLALCHEMY_DATABASE_URL, echo=True
    )


# sessionmaker for async sessions
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=get_engine(),
    class_=AsyncSession,
)


async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session
        # async with session.begin():  # Transaction tự động commit hoặc rollback
        #     yield session  # Trả session cho request sử dụng
