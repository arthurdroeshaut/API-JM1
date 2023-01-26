from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from pydantic import BaseModel
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    date = datetime.datetime


class CoffeeMachine(Base):
    __tablename__ = 'coffee_machine'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    level_of_water = Column(Float)
    level_of_coffeebeans = Column(Float)
    level_of_milk = Column(Float)
    coffee = relationship('Coffee', back_populates='coffeemachine')
    tea = relationship('Tea', back_populates='coffeemachine')


class Coffee(Base):
    __tablename__ = 'coffee'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    description = Column(String)
    water_id = Column(Integer, ForeignKey('coffee_machine.id'))
    water = relationship('CoffeeMachine', back_populates='coffee')
    coffeebeans = relationship('CoffeeBeans', back_populates='coffee')


class CoffeeBeans(Base):
    __tablename__ = 'coffee_beans'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    coffee = relationship('Coffee', back_populates='coffeebeans')




class Tea(Base):
    __tablename__ = 'tea'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    level_of_water = Column(Float)
    coffeemachine_id = Column(Integer, ForeignKey('coffee_machine.id'))
    coffeemachine = relationship('CoffeeMachine', back_populates='tea')


class CoffeeMachineCreate(CoffeeMachine):
    pass


class CoffeeCreate(Coffee):
    pass


class CoffeeBeansCreate(CoffeeBeans):
    pass

class TeaCreate(Tea):
    pass


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
