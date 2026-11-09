from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from app.models.order_status_histories import OrderStatus

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        from_attributes = True

class OrderListItemResponse(BaseModel):
    id: int
    order_code: str
    total_amount: float
    status: OrderStatus
    created_at: datetime

    class Config:
        from_attributes = True

class OrderListResponse(BaseModel):
    total: int
    items: List[OrderListItemResponse]
    has_orders: bool