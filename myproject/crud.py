from pip._internal.network import auth
from sqlalchemy.orm import Session
from models import Movie, Character, Vehicle
from schemas import CharacterCreate, Character, MovieCreate, Movie, Vehicle, VehicleCreate
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


