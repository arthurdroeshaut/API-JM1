from sqlalchemy.orm import Session
from models import Koffie, User, Thee, KoffieMachine
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


# alle andere cruds

def get_koffie(db: Session, koffie_id: int):
    return db.query(Koffie).filter(koffie_id == koffie_id).first()


def get_thee(db: Session, thee_id: int):
    return db.query(Thee).filter(thee_id == thee_id).first()


def get_total_amount_of_koffie(db: Session, koffie_id: int):
    return db.query(Koffie).filter(koffie_id == koffie_id).count()


def get_total_amount_of_koffiebonen(db: Session, koffiebonen: str):
    return db.query(Koffie.koffiebonen).filter(Koffie.koffiebonen == koffiebonen).count()


def get_total_amount_of_water_left(db: Session, water: str):
    return db.query(Thee.water).filter(Thee.water == water).count()


def get_coffees_drank_by_user(db: Session, koffie, user):
    return db.query(User.id).filter(user.id == koffie.user_id).filter()


def get_sorts_of_coffee_beans_drank_by_user(db: Session, koffie, user):
    return db.query(User.id).filter(user.id == koffie.koffiebonen).filter()


def get_total_amount_of_thee_drank_by_user(db: Session, thee, user):
    return db.query(User.id).filter(user.id == thee.naam).filter()


def get_total_amount_of_coffee_drank_by_user(db: Session, koffie, user):
    return db.query(User.id).filter(user.id == koffie.naam).count()


def get_level_of_milk(db: Session, melk_niveau):
    return db.query(KoffieMachine.id).filter(KoffieMachine.id == KoffieMachine.melk_niveau).count()

def get_level_inside_koffeemachine(db: Session, )

# 2 cruds om een koffie en thee aan te maken.


def create_koffie(db: Session, koffie: schemas.KoffieCreate):
    db_koffie = koffie
    db.add(db_koffie)
    db.commit()
    db.refresh(db_koffie)
    return db_koffie


def create_thee(db: Session, thee: schemas.TheeCreate):
    db_thee = thee
    db.add(db_thee)
    db.commit()
    db.refresh(db_thee)
    return db_thee
