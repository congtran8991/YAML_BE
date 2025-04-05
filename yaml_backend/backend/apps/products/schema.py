from pydantic import BaseModel

class ProductSchemaTest(BaseModel):
    title: str
    description: str
    status: str
