from passlib.hash import pbkdf2_sha256
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth
import models
import crud
import schemas
from schemas import KoffieCreate, Koffie, TheeCreate, Thee, UserCreate, User
from database import SessionLocal, engine
import os


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# api routes voor aanmaken accounts en tokens op te vragen.


# token route
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect Username or Password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    # Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_user(db, skip=skip, limit=limit)
    return users

# apis voor alle rest, koffies, thee, gebruikers,...
# beginnende met de post endpoints.


@app.post("/Users/CreateCoffee")
def create_coffee(koffie: KoffieCreate, db: Session = Depends(get_db)):
    db_koffie = models.Koffie(**koffie.dict())
    db.add(db_koffie)
    db.commit()
    db.refresh(db_koffie)
    return db_koffie


@app.post("/Thee/CreateThee")
def create_thee(thee: TheeCreate, db: Session = Depends(get_db)):
    db_thee = models.Thee(**thee.dict())
    db.add(db_thee)
    db.commit()
    db.refresh(db_thee)
    return db_thee


# nu komen alle get endpoints...

#@app.get("/Thee")
#def get_thee(thee: Thee, db: Session = Depends(get_db)):


#@app.get("/koffie")
#def get_koffie(koffie: Koffie, db: Session = Depends(get_db)):


#@app.get("/koffieMachine/niveaus")
#def get_koffiemachineniveau(koffiemachine: melk_niveau, koffiebonen_niveau, melk_niveau, db: Session(get_db)):


