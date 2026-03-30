from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    email = mapped_column(String(255))

    # NEW FIELD
    age = mapped_column(Integer, nullable=True)