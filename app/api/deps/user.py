from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from service.auth import AuthService
from db.repositories.user import user_repo
from models.domain.user import User as DomainUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(
        token: str = Depends(oauth2_scheme)
) -> DomainUser:
    username = AuthService().get_username_from_token(token)
    db_user = user_repo.get_user_by_username(username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
