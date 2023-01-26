from sqlalchemy.orm import Session
from models import Coffee, CoffeeMachine, CoffeeBeans, Tea, User, 
import models
import schemas
import auth


# de create user voor hashing alsook om de users op te vragen via email.


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
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


def get_coffee_beanss(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CoffeeBeans).offset(skip).limit(limit).all()


def get_teas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tea).offset(skip).limit(limit).all()


# alle create cruds


def create_coffee_machine(db: Session, coffe_machine: schemas.CoffeeMachineCreate):
    coffe_machine_db = models.CoffeeMachine(**coffe_machine.dict())
    db.add(coffe_machine_db)
    db.commit()
    db.refresh(coffe_machine_db)
    return coffe_machine_db


def create_coffee(db: Session, coffee: schemas.CoffeeCreate):
    coffee_db = models.Coffee(**coffee.dict())
    db.add(coffee_db)
    db.commit()
    db.refresh(coffee_db)
    return coffee_db


def create_coffee_beans(db: Session, coffee_beans: schemas.CoffeeBeansCreate):
    coffee_beans_db = models.CoffeeBeans(**coffee_beans.dict())
    db.add(coffee_beans_db)
    db.commit()
    db.refresh(coffee_beans_db)
    return coffee_beans_db


def create_tea(db: Session, tea: schemas.TeaCreate):
    tea_db = models.Tea(**tea.dict())
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
