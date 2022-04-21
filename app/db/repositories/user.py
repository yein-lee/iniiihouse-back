from typing import Optional
from sqlalchemy.orm import Session

from .base import BaseRepo
from models.domain.user import User
from models.schemas.user import UserCreate, UserUpdate


class UserRepo(BaseRepo[User, UserCreate, UserUpdate]):
    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.username == username).first()


user_repo = UserRepo(User)
