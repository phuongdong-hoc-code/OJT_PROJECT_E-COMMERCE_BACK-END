from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.db import get_db
from app.models.order_status_histories import OrderStatus
from app.schemas.order_status_histories import OrderListResponse
from app.crud.order_status_histories import OrderService
# from app.dependencies import get_current_active_user

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", response_model=OrderListResponse)
def get_my_orders(
    status: Optional[OrderStatus] = Query(None, description="Lọc theo trạng thái đơn hàng"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    # current_user = Depends(get_current_active_user)
):
    result = OrderService.get_customer_orders(
        db=db, 
        # user_id=current_user.id, 
        status=status, 
        skip=skip, 
        limit=limit
    )
    return result