from pydantic import BaseModel


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
    CoffeeBeans: str


class CoffeeCreate(CoffeeBase):
    pass


class CoffeeUpdate(CoffeeBase):
    pass


class Coffee(CoffeeBase):
    id: int
    user_id: int
    water_id: int
    milk_id: int
    coffeebeans_id: int
    order_id: int

    class Config:
        orm_mode = True


class TeaBase(BaseModel):
    name: str
    description: str
    water_level: int


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


class CoffeeBeans(BaseModel):
    name = str
    description = str


class CoffeeBeansCreate(CoffeeBeans):
    pass


class CoffeeBeansUpdate(CoffeeBeans):
    pass


class CoffeeBeans(CoffeeBeans):
    id: int
    coffee_id: int

    class Config:
        orm_mode = True


class Orders(BaseModel):
    date: str
    quantity: int
    price: float
    
    
class OrderCreate(Orders):
    pass


class Orders(Orders):
    id: int
    user_id: int
    product_id: int
    coffee_id: int
    tea_id: int

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