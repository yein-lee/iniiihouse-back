from .base import BaseRepo
from models.domain.party import Party as DomainParty
from models.schemas.party import PartyCreate, PartyUpdate
from db.session import SessionLocal


class PartyRepo(BaseRepo[DomainParty, PartyCreate, PartyUpdate]):
    def accept(self, id_in: int):
        with SessionLocal() as db:
            domain_party = db.query(self.model).filter(self.model.id == id_in).first()
            domain_party.accept = True
            db.commit()
            db.refresh(domain_party)
        return domain_party
