import enum
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class StockLogType(str, enum.Enum):
    IMPORT = "NHẬP"
    SALE = "BÁN"
    ORDER_CANCEL = "HUỶ ĐƠN"
    ADJUSTMENT = "ĐIỀU CHỈNH"


class StockLog(Base):
    __tablename__ = "stock_logs"
    __table_args__ = (
        CheckConstraint("quantity <> 0", name="ck_stock_logs_quantity_nonzero"),
        CheckConstraint("stock_after >= 0", name="ck_stock_logs_stock_after_nonnegative"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("items.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    movement_type: Mapped[StockLogType] = mapped_column(
        Enum(
            StockLogType,
            values_callable=lambda enum_type: [member.value for member in enum_type],
            name="stock_log_type",
        ),
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    stock_after: Mapped[int] = mapped_column(Integer, nullable=False)
    order_code: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
    performed_by: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    product = relationship("Item")
