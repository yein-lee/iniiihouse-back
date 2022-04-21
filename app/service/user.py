from fastapi import HTTPException

from db.repositories.user import user_repo
from models.domain.user import User as DomainUser
from models.schemas.user import UserGrade, UserCreate


class UserService:
    @classmethod
    def create_user(cls, user_in: UserCreate) -> DomainUser:
        db_user = user_repo.get_user_by_username(username=user_in.username)
        if db_user:
            raise HTTPException(status_code=400, detail="username already registered")
        return user_repo.create(obj_in=user_in)

    @classmethod
    def is_host(cls, grade_in: UserGrade) -> bool:
        if grade_in == UserGrade.host:
            return True
        return False