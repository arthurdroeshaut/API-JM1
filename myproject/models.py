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


class Koffie(Base):
    __tablename__ = "Koffie"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    beschrijving = Column(String, index=True)
    koffiebonen = Column(String, index=True)
    #   aantal = ?
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="Koffie")


class Thee(Base):
    __tablename__ = "Thee"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(Integer, index=True)
    beschrijving = Column(String, index=True)
    water = Column(String, index=True)
    #   aantal = ?
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="Thee")


class KoffieCreate(Koffie):
    pass


class TheeCreate(Thee):
    pass


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
