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
    coffee = relationship('Coffee', back_populates='user')
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    order = relationship('Orders', back_populates='user')
    order_id = Column(Integer, ForeignKey('orders.id'))


class CoffeeMachine(Base):
    __tablename__ = 'coffee_machine'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    level_of_water = Column(Float)
    level_of_coffeebeans = Column(Float)
    level_of_milk = Column(Float)
    coffee = relationship('Coffee', back_populates='coffeemachine')
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    tea = relationship('Tea', back_populates='coffeemachine')
    tea_id = Column(Integer, ForeignKey('tea.id'))


class Coffee(Base):
    __tablename__ = 'coffee'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    milk_id = Column(Integer, ForeignKey('coffee_machine.id'))
    milk = relationship('CoffeeMachine', back_populates='coffee')
    water_id = Column(Integer, ForeignKey('coffee_machine.id'))
    water = relationship('CoffeeMachine', back_populates='coffee')
    CoffeeBeans = relationship("CoffeeBeans", secondary="coffee_coffee_beans", back_populates="coffee")
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Orders', back_populates='coffee')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='coffee')


class CoffeeBeans(Base):
    __tablename__ = 'coffee_beans'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    coffee = relationship("Coffee", secondary="coffee_coffee_beans", back_populates="coffee_beans")


class CoffeeCoffeeBeans(Base):
    __tablename__ = 'coffee_coffee_beans'

    id = Column(Integer, primary_key=True)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    coffee_beans_id = Column(Integer, ForeignKey('coffee_beans.id'))


class Tea(Base):
    __tablename__ = 'tea'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    water_id = Column(Integer, ForeignKey('coffee_machine.id'))
    water = relationship('CoffeeMachine', back_populates='tea')
    coffeemachine_id = Column(Integer, ForeignKey('coffee_machine.id'))
    coffeemachine = relationship('CoffeeMachine', back_populates='tea')
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Orders', back_populates='tea')


class Orders(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    quantity = Column(Integer)
    price = Column(Float)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    tea_id = Column(Integer, ForeignKey('tea.id'))
    tea_name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    

class CoffeeMachineCreate(CoffeeMachine):
    pass


class CoffeeCreate(Coffee):
    pass


class CoffeeBeansCreate(CoffeeBeans):
    pass


class TeaCreate(Tea):
    pass


class OrderCreate(Orders):
    pass


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class OrderCreate(Orders):
    pass