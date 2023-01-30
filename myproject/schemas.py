from pydantic import BaseModel
import datetime
from datetime import datetime




class UserBase(BaseModel):
    email: str
#    groep: str

class UserCreate(UserBase):
    password: str




class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    orders_id: int = None


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
    order_id : int

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
    order_id : int

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
    order_id : int

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
    order_id : int

    class Config:
        orm_mode = True


class Orders(BaseModel):
    Type_drank: str
    soort_koffie: str
    soort_thee: str
    type_bonen: str
    
    
class OrdersCreate(Orders):
    pass


class Order(Orders):
    id: int
    user_id: int
    CoffeeBeans_id: int
    CoffeeMachine_id: int
    Coffee_id: int
    Tea_id: int
    

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