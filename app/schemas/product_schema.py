from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    restaurant_id: UUID
    category_id: Optional[UUID] = None

    name: str
    description: Optional[str] = None

    price: float

    image_url: Optional[str] = None
    ai_keywords: Optional[str] = None

    preparation_time: Optional[int] = None

    available: bool = True
    featured: bool = False


class ProductCreate(ProductBase):
    """Schema for creating a product."""
    pass


class ProductUpdate(BaseModel):
    category_id: Optional[UUID] = None

    name: Optional[str] = None
    description: Optional[str] = None

    price: Optional[float] = None

    image_url: Optional[str] = None
    ai_keywords: Optional[str] = None

    preparation_time: Optional[int] = None

    available: Optional[bool] = None
    featured: Optional[bool] = None


class ProductResponse(ProductBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
