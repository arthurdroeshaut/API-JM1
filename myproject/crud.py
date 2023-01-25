from pip._internal.network import auth
from sqlalchemy.orm import Session
from models import User
import models 
import schemas
import auth


# de create user voor hashing


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