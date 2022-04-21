from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from pydantic import ValidationError
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from core.security import ALGORITHM, pwd_context
from core.config import settings
from db.repositories.user import user_repo
from models.domain.user import User as DomainUser
from models.schemas.token import Token, TokenData


class AuthService:
    @classmethod
    def authenticate(cls, username: str, password: str) -> Optional[DomainUser]:
        db_user = user_repo.get_user_by_username(username=username)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect name or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if not cls.verify_password(password, db_user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Password Invalid",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return db_user

    @classmethod
    def create_access_token(
            cls, form_data: OAuth2PasswordRequestForm
    ) -> Token:
        db_user = cls.authenticate(username=form_data.username, password=form_data.password)
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.utcnow() + access_token_expires
        to_encode = {"exp": expire, "sub": db_user.username}
        access_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
        token = Token(access_token=access_token, token_type="bearer")
        return token

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return pwd_context.hash(password)

    @classmethod
    def get_username_from_token(cls, token: str) -> str:
        try:
            decoded_jwt = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
            token_data = TokenData(**decoded_jwt)
            username = token_data.sub
            return username
        except JWTError as decode_error:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not Decode JWT token",
            ) from decode_error
        except ValidationError as validation_error:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            ) from validation_error
