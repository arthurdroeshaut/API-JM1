from pydantic import BaseModel
from models import User as UserBase, Koffie as KoffieBase, Thee as TheeBase


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class KoffieBase(BaseModel):
    naam: str
    beschrijving: str
    koffiebonen: str


class KoffieCreate(KoffieBase):
    pass


class Koffie(KoffieBase):
    id: int
    owner_id: int 

    class Config:
        orm_mode = True


class TheeBase(BaseModel):
    naam: str
    beschrijving: str 


class TheeCreate(TheeBase):
    pass


class Thee(TheeBase):
    id: int
    owner_id: int 

    class Config:
        orm_mode = True