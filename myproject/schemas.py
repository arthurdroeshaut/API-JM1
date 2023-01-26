from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class CoffeeBase(BaseModel):
    name: str
    description: str
    CoffeeBeans: str
    date: str


class CoffeeCreate(CoffeeBase):
    pass


class Coffee(CoffeeBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class TeaBase(BaseModel):
    name: str
    description: str
    water_level: int


class TeaCreate(TeaBase):
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


class CoffeeBeans(CoffeeBeans):
    id: int
    coffee_id: int

    class Config:
        orm_mode = True

