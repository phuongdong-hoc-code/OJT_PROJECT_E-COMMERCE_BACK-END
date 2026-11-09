from sqlalchemy.orm import Session
from typing import Optional
from app.models.order_status_histories import Order, OrderStatus

class OrderService:
    @staticmethod
    def get_customer_orders(
        db: Session, 
        user_id: int, 
        status: Optional[OrderStatus] = None, 
        skip: int = 0, 
        limit: int = 10
    ):
        query = db.query(Order).filter(Order.user_id == user_id)
        
        if status:
            query = query.filter(Order.status == status)
            
        total = query.count()
        orders = query.order_by(Order.created_at.desc()).offset(skip).limit(limit).all()
        
        return {
            "total": total,
            "items": orders,
            "has_orders": total > 0
        }