from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr


class Gender(str, Enum):
    M = 'male'
    F = 'female'


class UserGrade(str, Enum):
    host = 'host'
    guest = 'guest'


class UserBase(BaseModel):
    username: EmailStr


class UserCreate(UserBase):
    password: str
    gender: Optional[Gender] = None
    grade: UserGrade


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    password: str
    gender: Optional[Gender] = None
    grade: UserGrade

    class Config:
        orm_mode = True
