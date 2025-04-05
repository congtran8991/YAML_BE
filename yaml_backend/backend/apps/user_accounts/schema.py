from pydantic import BaseModel, Field
from typing import Optional

class RegisterAccountSchema(BaseModel):
    name: str 
    email: str = Field(..., min_length=6)
    password: str = Field(..., min_length=6)
    phone_number: Optional[str]

class UpdateAccountSchema(BaseModel):
    name: str 
    email: str = Field(..., min_length=6)
    password: str = Field(..., min_length=6)
    phone_number: Optional[str]
