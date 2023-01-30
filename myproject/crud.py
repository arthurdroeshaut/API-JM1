from sqlalchemy.orm import Session
import models
import schemas 
import auth
from datetime import datetime


# de create user voor hashing alsook om de users op te vragen via email.


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, email: str, groep: str, password: str):
    hashed_password = auth.get_password_hash(password)
    db_user = models.User(email=email, hashed_password=hashed_password, groep=groep)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# alle andere get cruds


def get_coffee_machine(db: Session, id: int):
    return db.query(models.CoffeeMachine).filter(models.CoffeeMachine.id == id).first()


def get_coffee(db: Session, id: int):
    return db.query(models.Coffee).filter(models.Coffee.id == id).first()


def get_coffee_beans(db: Session, id: int):
    return db.query(models.CoffeeBeans).filter(models.CoffeeBeans.id == id).first()


def get_tea(db: Session, id: int):
    return db.query(models.Tea).filter(models.Tea.id == id).first()


def get_coffee_machines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CoffeeMachine).offset(skip).limit(limit).all()


def get_coffees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coffee).offset(skip).limit(limit).all()


def get_coffee_beans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CoffeeBeans).offset(skip).limit(limit).all()


def get_teas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tea).offset(skip).limit(limit).all()


# alle create cruds


def create_coffee_machine(db: Session, coffee_machine: schemas.CoffeeMachineCreate):
    coffee_machine_db = models.CoffeeMachine(name=coffee_machine.name, description=coffee_machine.description, level_of_water=coffee_machine.level_of_water, level_of_coffeebeans=coffee_machine.level_of_coffeebeans, level_of_milk=coffee_machine.level_of_milk)
    db.add(coffee_machine_db)
    db.commit()
    db.refresh(coffee_machine_db)
    return coffee_machine_db


def create_coffee(db: Session, coffee: schemas.CoffeeCreate):
    coffee_db = models.Coffee(name=coffee.name, description=coffee.description)
    db.add(coffee_db)
    db.commit()
    db.refresh(coffee_db)
    return coffee_db


def create_coffee_beans(db: Session, coffee_beans: schemas.CoffeeBeansCreate):
    coffee_beans_db = models.CoffeeBeans(name=coffee_beans.name)
    db.add(coffee_beans_db)
    db.commit()
    db.refresh(coffee_beans_db)
    return coffee_beans_db


def create_tea(db: Session, tea: schemas.TeaCreate):
    tea_db = models.Tea(name=tea.name)
    db.add(tea_db)
    db.commit()
    db.refresh(tea_db)
    return tea_db


def update_coffee_machine(db: Session, id: int, coffe_machine: schemas.CoffeeMachineUpdate):
    coffe_machine_db = db.query(models.CoffeeMachine).filter(models.CoffeeMachine.id == id).first()
    coffe_machine_db.update(coffe_machine.dict(exclude_unset=True))
    db.commit()
    db.refresh(coffe_machine_db)
    return coffe_machine_db


def update_coffee(db: Session, id: int, coffee: schemas.CoffeeUpdate):
    coffee_db = db.query(models.Coffee).filter(models.Coffee.id == id).first()
    coffee_db.update(coffee.dict(exclude_unset=True))
    db.commit()
    db.refresh(coffee_db)
    return coffee_db


def update_coffee_beans(db: Session, id: int, coffee_beans: schemas.CoffeeBeansUpdate):
    coffee_beans_db = db.query(models.CoffeeBeans).filter(models.CoffeeBeans.id == id).first()
    coffee_beans_db.update(coffee_beans.dict(exclude_unset=True))
    db.commit()
    db.refresh(coffee_beans_db)
    return coffee_beans_db


def update_tea(db: Session, id: int, tea: schemas.TeaUpdate):
    tea_db = db.query(models.Tea).filter(models.Tea.id == id).first()
    tea_db.update(tea.dict(exclude_unset=True))
    db.commit()
    db.refresh(tea_db)
    return tea_db


# alle delete cruds


def delete_coffee_machine(db: Session, id: int):
    db.query(models.CoffeeMachine).filter(models.CoffeeMachine.id == id).delete()
    db.commit()


def delete_coffee(db: Session, id: int):
    db.query(models.Coffee).filter(models.Coffee.id == id).delete()
    db.commit()


def delete_coffee_beans(db: Session, id: int):
    db.query(models.CoffeeBeans).filter(models.CoffeeBeans.id == id).delete()
    db.commit()


def delete_tea(db: Session, id: int):
    db.query(models.Tea).filter(models.Tea.id == id).delete()
    db.commit()


# alle cruds met orders


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Orders).offset(skip).limit(limit).all()

def get_order_by_date(db: Session, date: str):
    return db.query(models.Orders).filter(models.Orders.date == date).all()

def get_order_by_id(db: Session, id: int):
    return db.query(models.Orders).filter(models.Orders.id == id).all()


def get_orders_by_date_by_user_id(db: Session, user_id: int): 
    return db.query(models.Orders).filter(models.Orders.id == user_id).order_by(models.Orders.date).all()

def get_user_orders(db: Session, user_id: int):
    return db.query(models.Orders).filter(models.Orders.id == user_id).order_by(models.Orders.date.asc()).all()


def get_order(db: Session, id: int):
    return db.query(models.Orders).filter(models.Orders.id == id).first()


def create_orders(db: Session, orders: schemas.OrdersCreate):
    now=datetime.now()
    orders_db = models.Orders(quantity=orders.quantity, date=now , price=orders.price)
    db.add(orders_db)
    db.commit()
    db.refresh(orders_db)
    return orders_db


def create_orders_coffee(db: Session, orders_coffee: schemas.OrdersCoffeeCreate):
    orders_coffee_db = models.Orders.coffee(**orders_coffee.dict())
    db.add(orders_coffee_db)
    db.commit()
    db.refresh(orders_coffee_db)
    return orders_coffee_db


def update_orders(db: Session, id: int, orders: schemas.OrdersUpdate):
    orders_db = db.query(models.Orders).filter(models.Orders.id == id).first()
    orders_db.update(orders.dict(exclude_unset=True))
    db.commit()
    db.refresh(orders_db)
    return orders_db


def update_orders_coffee(db: Session, id: int, orders_coffee: schemas.OrdersCoffeeUpdate):
    orders_coffee_db = db.query(models.Orders.coffee).filter(models.Orders.coffee_id == id).first()
    orders_coffee_db.update(orders_coffee.dict(exclude_unset=True))
    db.commit()
    db.refresh(orders_coffee_db)
    return orders_coffee_db


def update_orders_tea(db: Session, id: int, orders_tea: schemas.OrdersTeaUpdate):
    orders_tea_db = db.query(models.Orders.tea).filter(models.Orders.tea_id == id).first()
    orders_tea_db.update(orders_tea.dict(exclude_unset=True))
    db.commit()
    db.refresh(orders_tea_db)
    return orders_tea_db


def delete_order(db: Session, id: int):
    db.query(models.Orders).filter(models.Orders.id == id).delete()
    db.commit()
    

