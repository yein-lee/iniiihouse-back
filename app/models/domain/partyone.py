from sqlalchemy import Column, ForeignKey, Integer

from db.session import Base


class PartyOne(Base):
    __tablename__ = "party_users_map"

    id = Column(Integer, primary_key=True, index=True)
    party_id = Column(Integer, ForeignKey('parties.id'))
    user_id = Column(Integer, ForeignKey('users.id'))