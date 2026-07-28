from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    sku: Optional[str] = None
    description: str
    quantity: int
    unit_price: float
    lead_time_days: Optional[int] = None


class Quote(BaseModel):
    supplier_name: str
    currency: str
    items: list[Item]
    quote_expiry: Optional[str] = None
    shipping_included: bool
    notes: list[str]
    assumptions: list[str]
    needs_review: bool