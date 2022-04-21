from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class PartyBase(BaseModel):
    id: int


class PartyCreate(PartyBase):
    title: str
    memo: str
    start_at: datetime
    end_at: datetime
    accepted: Optional[bool] = None


class PartyUpdate(PartyBase):
    title: Optional[str] = None
    memo: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    accepted: Optional[bool] = None


class Party(PartyBase):
    title: str
    memo: str
    start_at: datetime
    end_at: datetime
    accepted: bool

    class Config:
        orm_mode = True
