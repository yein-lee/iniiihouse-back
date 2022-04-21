from fastapi import APIRouter, Body
from service.user import UserService
from models.domain.user import User
from models.schemas.user import UserCreate

router = APIRouter()


@router.post("/register", response_model=User)
def register(
        user_in: UserCreate = Body(...),
) -> User:
    return UserService().create_user(user_in)
