from pydantic import BaseModel


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
    datum: str


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
    water_niveau: int


class TheeCreate(TheeBase):
    pass


class Thee(TheeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class KoffieMachineBase(BaseModel):
    naam: str
    beschrijving: str
    koffiebonen_niveau: int
    melk_niveau: int
    water_niveau: int


class KoffieMachineCreate(KoffieMachineBase):
    pass


class KoffieMachine(KoffieMachineBase):
    id: int
    thee_id: int

    class Config:
        orm_mode = True


class KoffiebonenBase(BaseModel):
    __tablename__ ="Koffiebonen"

    id = int
    naam = str
    beschrijving = str


class KoffiebonenCreate(KoffiebonenBase):
    pass


class Koffiebonen(KoffiebonenBase):
    id: int
    Koffie_id: int

    class Config:
        orm_mode = True

