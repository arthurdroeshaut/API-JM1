from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from pydantic import BaseModel
from database import Base
from datetime import datetime



class CoffeeMachine(Base):
    __tablename__ = 'coffee_machine'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    level_of_water = Column(Float)
    level_of_coffeebeans = Column(Float)
    level_of_milk = Column(Float)




class Coffee(Base):
    __tablename__ = 'coffee'

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    description = Column(String)


class CoffeeBeans(Base):
    __tablename__ = 'coffee_beans'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
  

class Tea(Base):
    __tablename__ = 'tea'

    id = Column(Integer, primary_key=True)
    name = Column(String)
 

class Orders(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    coffee_beans_id = Column(Integer, ForeignKey('coffee_beans.id'))
    tea_id = Column(Integer, ForeignKey('tea.id'))
    date = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

    user = relationship("User", foreign_keys=[user_id])
    coffee = relationship("Coffee", foreign_keys=[coffee_id])
    coffee_beans = relationship("CoffeeBeans", foreign_keys=[coffee_beans_id])
    tea = relationship("Tea", foreign_keys=[tea_id])

    
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    orders_id = Column(Integer, ForeignKey('orders.id'))
    
    orders = relationship("Orders", foreign_keys=[orders_id])


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