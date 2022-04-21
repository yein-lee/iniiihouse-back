from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime

from db.session import Base


class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    memo = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    accepted = Column(Boolean)
    create_user = Column(Integer, ForeignKey('user.id'))
