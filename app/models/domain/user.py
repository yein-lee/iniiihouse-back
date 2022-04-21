from sqlalchemy import Column, Integer, String, Enum

from db.session import Base
from models.schemas.user import UserGrade


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    gender = Column(String)
    grade = Column(Enum(UserGrade))
