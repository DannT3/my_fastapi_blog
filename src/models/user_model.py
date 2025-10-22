from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class UserModel(BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    age: Mapped[int] = mapped_column(nullable=False)
    password: Mapped[int] = mapped_column(hash=True, nullable=False)
