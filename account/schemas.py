from typing import Optional, List
from pydantic import BaseModel, EmailStr


class AccountSchema(BaseModel):
    id: Optional[int] = None
    username: str
    name: str
    activate: bool
    admin: bool

    class Config:
        orm_mode = True


class AccountCreateSchema(AccountSchema):
    password: str


class AccountUpdateSchema(AccountSchema):
    id: Optional[int] = None
    username: Optional[str]
    password: Optional[str]
    name: Optional[str]
    activate: Optional[bool]
    admin: Optional[bool]