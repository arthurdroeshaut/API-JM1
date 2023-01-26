from pip._internal.network import auth
from sqlalchemy.orm import Session
from models import Koffie, User, Thee, KoffieCreate, TheeCreate, UserCreate
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


def get_coffee_beans_drank_by_user(db: Session, koffie, user):
    return db.query(User.id).filter(user.id == koffie.koffiebonen).filter()


def get_thee_drank_by_user(db: Session, thee, user):
    return db.query(User.id).filter(user.id == thee.naam).filter()



def