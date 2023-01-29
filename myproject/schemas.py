from pydantic import BaseModel
import datetime
from datetime import datetime




class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class CoffeeBase(BaseModel):
    name: str
    description: str
 


class CoffeeCreate(CoffeeBase):
    pass


class CoffeeUpdate(CoffeeBase):
    pass


class Coffee(CoffeeBase):
    id: int

    class Config:
        orm_mode = True


class TeaBase(BaseModel):
    name: str


class TeaCreate(TeaBase):
    pass


class TeaUpdate(TeaBase):
    pass


class Tea(TeaBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class CoffeeMachineBase(BaseModel):
    name: str
    description: str
    level_of_coffeebeans: float
    level_of_water: float
    level_of_milk: float


class CoffeeMachineCreate(CoffeeMachineBase):
    pass


class CoffeeMachineUpdate(CoffeeMachineBase):
    pass


class CoffeeMachine(CoffeeMachineBase):
    id: int
    tea_id: int

    class Config:
        orm_mode = True


class CoffeeBeansBase(BaseModel):
    name: str


class CoffeeBeansCreate(CoffeeBeansBase):
    pass


class CoffeeBeansUpdate(CoffeeBeansBase):
    pass


class CoffeeBeans(CoffeeBeansBase):
    id: int

    class Config:
        orm_mode = True


class Orders(BaseModel):
    quantity: int
    price: float
    
    
class OrdersCreate(Orders):
    pass


class Orders(Orders):
    id: int
    user_id: int
    date : str
    

    class Config:
        orm_mode = True
        
        
class OrdersUpdate(Orders):
    pass

class OrdersCoffeeCreate(Orders):
    pass

class OrdersCoffeeUpdate(Orders):
    pass

class OrdersTeaCreate(Orders):
    pass

class OrdersTeaUpdate(Orders):
    pass