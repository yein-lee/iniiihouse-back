from fastapi import APIRouter, Depends, Body, Path

from api.errors import PermissionException
from api.deps.user import get_current_user
from service.party import PartyService
from service.user import UserService
from models.domain.party import Party
from models.schemas.party import PartyCreate, PartyUpdate
from models.schemas.user import User


router = APIRouter()


@router.post("/", response_model=Party)
def create_party(
        current_user: User = Depends(get_current_user),
        party_in: PartyCreate = Body(...)
) -> Party:
    if UserService().is_host(current_user.grade):
        return PartyService().throw_party_service(party_in)
    else:
        return PartyService.request_party_service(party_in)


@router.put("/accept/{party_id}", response_model=Party)
def accept_party(
        current_user: User = Depends(get_current_user),
        party_id: int = Path(...)
):
    if UserService().is_host(current_user.grade):
        return PartyService().accept_party_service(party_id)
    raise PermissionException()


@router.delete("/reject/{party_id}", response_model=Party)
def reject_party(
        current_user: User = Depends(get_current_user),
        party_id: int = Path(...)
):
    if UserService().is_host(current_user.grade):
        return PartyService().delete_party_service(party_id)
    raise PermissionException()


@router.delete("/{party_id}", response_model=Party)
def delete_party(
        current_user: User = Depends(get_current_user),
        party_id: int = Path(...)
):
    if UserService().is_host(current_user.grade):
        return PartyService().delete_party_service(party_id)

    domain_party = PartyService().get_party_service(party_id)
    if domain_party.create_user != current_user:
        PermissionException()
    return PartyService().delete_party_service(party_id)


@router.update("/", response_model=Party)
def update_party(
        current_user: User = Depends(get_current_user),
        party_in: PartyUpdate = Body(...)
):
    if UserService().is_host(current_user.grade):
        return PartyService().update_party_service(party_in)

    domain_party = PartyService().get_party_service(party_in.id)
    if domain_party.create_user.id != current_user.id:
        PermissionException()
    return PartyService().delete_party_service(party_in)
