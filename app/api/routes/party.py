from fastapi import APIRouter, Depends, Body

from api.deps.user import get_current_user
from service.party import PartyService
from models.domain.party import Party
from models.schemas.party import PartyCreate
from models.schemas.user import User


router = APIRouter()


@router.post("/", response_model=Party)
def create_party(
        current_user: User = Depends(get_current_user),
        party_in: PartyCreate = Body(...)
) -> Party:
    return PartyService.throw_party(party_in)
