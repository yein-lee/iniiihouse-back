from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTime

from db.session import Base
from models.schemas.user import UserGrade


class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    memo = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    accepted = Column(Boolean)
