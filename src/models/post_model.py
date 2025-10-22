from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base_model import BaseModel
from datetime import datetime
from typing import Optional
from models.user_model import UserModel


class PostModel(BaseModel):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    updated_at: Mapped[Optional[datetime]] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey(""))

