from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(BaseModel):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
