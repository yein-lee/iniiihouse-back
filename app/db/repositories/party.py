from .base import BaseRepo
from models.domain.party import Party as DomainParty
from models.schemas.party import PartyCreate, PartyUpdate
from db.session import SessionLocal


class PartyRepo(BaseRepo[DomainParty, PartyCreate, PartyUpdate]):
    ...
