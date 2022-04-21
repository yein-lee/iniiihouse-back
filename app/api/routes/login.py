from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.schemas.token import Token
from service.auth import AuthService

router = APIRouter()


@router.post("/token", response_model=Token)
def login_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
):
    return AuthService().create_access_token(form_data)
