from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.models.stock_log import StockLogType


class StockLogCreate(BaseModel):
    product_id: int = Field(gt=0)
    movement_type: StockLogType
    quantity: int = Field(examples=[-3, 5])
    stock_after: int = Field(ge=0)
    order_code: str | None = Field(default=None, max_length=50)
    note: str | None = None
    performed_by: str = Field(min_length=1, max_length=100)

    @field_validator("quantity")
    @classmethod
    def quantity_must_not_be_zero(cls, quantity: int) -> int:
        if quantity == 0:
            raise ValueError("quantity must not be zero")
        return quantity


class StockLogOut(StockLogCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
