from db.repositories.party import PartyRepo
from models.schemas.party import PartyCreate
from models.domain.party import Party as DomainParty


class PartyService:
    @classmethod
    def throw_party(cls, obj_in: PartyCreate) -> DomainParty:
        obj_in.accept = True
        return PartyRepo(DomainParty).create(obj_in)

    @classmethod
    def request_party(cls, obj_in: PartyCreate) -> DomainParty:
        obj_in.accept = False
        return PartyRepo(DomainParty).create(obj_in)

    @classmethod
    def accept_party(cls, id_in: int) -> DomainParty:
        return PartyRepo(DomainParty).accept(id_in)
