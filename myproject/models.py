import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from database import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    date = datetime.datetime


class KoffieMachine(Base):
    __tablename__ = "KoffieMachine"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    beschrijving = Column(String, index=True)
    melk_niveau = Column(Integer, index=True)
    koffiebonen_niveau = Column(Integer, index=True)
    water_niveau = Column(Integer, Index=True)
    thee_id = Column(Integer, ForeignKey("thee.id"))


class Koffie(Base):
    __tablename__ = "Koffie"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    beschrijving = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    koffiebonen_id = Column(Integer, ForeignKey("Koffiebonen.id"))

    owner = relationship("User", back_populates="Koffie")


class Koffiebonen(Base):
    __tablename__ ="Koffiebonen"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    beschrijving = Column(String, index=True)
    Koffie_id = Column(Integer, ForeignKey("koffie.id"))





class Thee(Base):
    __tablename__ = "Thee"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(Integer, index=True)
    beschrijving = Column(String, index=True)
    water_niveau = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    KoffieMachine_id = Column(Integer, ForeignKey("KoffieMachine.id"))

    owner = relationship("User", back_populates="Thee")


class KoffieMachineCreate(KoffieMachine):
    pass


class KoffieCreate(Koffie):
    pass


class TheeCreate(Thee):
    pass


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
