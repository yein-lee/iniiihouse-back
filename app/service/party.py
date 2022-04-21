from api.errors import NotFoundException
from db.repositories.party import PartyRepo
from models.schemas.party import PartyCreate, PartyUpdate
from models.domain.party import Party as DomainParty


class PartyService:
    @classmethod
    def get_party_service(cls, id_in: int) -> DomainParty:
        domain_party = PartyRepo(DomainParty).get(id_in)
        if not domain_party:
            raise NotFoundException(detail="Party")
        return domain_party

    @classmethod
    def throw_party_service(cls, obj_in: PartyCreate) -> DomainParty:
        domain_party = PartyRepo(DomainParty).get(obj_in.id)
        if not domain_party:
            raise NotFoundException(detail="Party")
        obj_in.accept = True
        return PartyRepo(DomainParty).create(obj_in)

    @classmethod
    def request_party_service(cls, obj_in: PartyCreate) -> DomainParty:
        domain_party = PartyRepo(DomainParty).get(obj_in.id)
        if not domain_party:
            raise NotFoundException(detail="Party")
        obj_in.accept = None
        return PartyRepo(DomainParty).create(obj_in)

    @classmethod
    def accept_party_service(cls, id_in: int) -> DomainParty:
        domain_party = PartyRepo(DomainParty).get(id_in)
        if not domain_party:
            raise NotFoundException(detail="Party")
        update_obj = PartyUpdate(id=id_in, accepted=True)
        return PartyRepo(DomainParty).update(domain_obj=domain_party, obj_in=update_obj)

    @classmethod
    def reject_party_service(cls, id_in: int) -> DomainParty:
        domain_party = PartyRepo(DomainParty).get(id_in)
        if not domain_party:
            raise NotFoundException(detail="Party")
        update_obj = PartyUpdate(id=id_in, accepted=False)
        return PartyRepo(DomainParty).update(domain_obj=domain_party, obj_in=update_obj)

    @classmethod
    def delete_party_service(cls, id_in: int) -> DomainParty:
        domain_party = PartyRepo(DomainParty).get(id_in)
        if not domain_party:
            raise NotFoundException(detail="Party")
        return PartyRepo(DomainParty).delete(id_in)

    @classmethod
    def update_party_service(cls, party_in: PartyUpdate):
        domain_party = PartyRepo(DomainParty).get(party_in.id)
        if not domain_party:
            raise NotFoundException(detail="Party")
        return PartyRepo(DomainParty).update(domain_obj=domain_party, obj_in=party_in)
