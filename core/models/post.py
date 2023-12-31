from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base
from core.models.user import User
class Post(Base):
    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default=""
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(User.id),
    )
