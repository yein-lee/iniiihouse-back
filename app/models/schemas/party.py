from datetime import datetime
from pydantic import BaseModel


class PartyBase(BaseModel):
    id: int


class PartyCreate(PartyBase):
    title: str
    memo: str
    start_at: datetime
    end_at: datetime
    accept: bool


class PartyUpdate(PartyBase):
    title: str
    memo: str
    start_at: datetime
    end_at: datetime
    accept: bool


class Party(PartyBase):
    title: str
    memo: str
    start_at: datetime
    end_at: datetime
    accept: bool

    class Config:
        orm_mode = True
