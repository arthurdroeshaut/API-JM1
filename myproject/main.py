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
from schemas import UserUpdate, UserCreate, User, CoffeeMachineCreate, CoffeeMachine, CoffeeBeansCreate, CoffeeBeans, OrdersCreate, Orders, CoffeeMachineUpdate, CoffeeBeansUpdate, CoffeeUpdate, TeaUpdate, TeaCreate, Tea, CoffeeCreate, Coffee
from database import SessionLocal, engine
import os
import sqlite3

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
def create_user (user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, email=user.email, password=user.password, groep=user.groep)
#    if db_user 
#    raise HTTPException(status_code=400, detail="Email already registered")
    return db_user




@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_user(db=db, user_id=token)
    return users


# apis voor alle rest, koffies, thee, gebruikers,...
# beginnende met de post endpoints.


@app.post("/coffee-machine/")
def create_coffee_machine(coffee_machine: schemas.CoffeeMachineCreate, db: Session = Depends(get_db)):
    return crud.create_coffee_machine(db=db, coffee_machine=coffee_machine)


@app.post("/orders/")
def create_orders(orders: schemas.OrdersCreate, db: Session = Depends(get_db)):
    return crud.create_orders(db=db, orders=orders)

@app.post("/coffee/")
def create_coffee(coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
    return crud.create_coffee(db=db, coffee=coffee)


@app.post("/coffee-beans/")
def create_coffee_beans(coffee_beans: schemas.CoffeeBeansCreate, db: Session = Depends(get_db)):
    return crud.create_coffee_beans(db=db, coffee_beans=coffee_beans)


@app.post("/tea/")
def create_teas(tea: schemas.TeaCreate, db: Session = Depends(get_db)):
    return crud.create_tea(db=db, tea=tea)


@app.post("/drank/")
def create_drankjes(drankjes: schemas.DrankjesCreate, db: Session = Depends(get_db)):
    return crud.create_drank(db=db, drankjes=drankjes)

# nu komen alle get endpoints...


@app.get("/coffee-machine/{coffee_machine_id}")
def read_coffee_machine(coffee_machine_id: int, db: Session = Depends(get_db)):
    return crud.get_coffee_machine(db, coffee_machine_id)


@app.get("/coffee/{coffee_id}")
def read_coffee(coffee_id: int, db: Session = Depends(get_db)):
    return crud.get_coffee(db, coffee_id)


@app.get("/coffee-beans/{coffee_beans_id}")
def read_coffee_beans(coffee_beans_id: int, db: Session = Depends(get_db)):
    return crud.get_coffee_beans(db, coffee_beans_id)


@app.get("/tea/{tea_id}")
def read_tea(tea_id: int, db: Session = Depends(get_db)):
    return crud.get_tea(db, tea_id)


@app.get("/coffee-machines/")
def read_coffee_machines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_coffee_machines(db, skip=skip, limit=limit)


@app.get("/coffees/")
def read_coffees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_coffees(db, skip=skip, limit=limit)


@app.get("/coffee-beans/")
def read_coffee_beans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_coffee_beans(db, skip=skip, limit=limit)


@app.get("/teas/")
def read_teas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_teas(db, skip=skip, limit=limit)


@app.get("/order/date/{date}")
def get_order_by_date(date: str, db: Session = Depends(get_db)):
    return crud.get_order_by_date(db, date)


# belangrijkste get endpoints: orders op basis van users hun id, en orders op basis van de datum, in de crud wordt dit al ascended opgezet.


@app.get("/orders/user/{user_id}")
def read_user_orders(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_orders(db, user_id)


# hieronder een get endpoint om een order op te vragen op basis van datum.

@app.get("/orders/date/{date}")
def get_order_by_date(date: str, db: Session = Depends(get_db)):
    return crud.get_order_by_date(db, date)


@app.get("/orders/date")
def get_order_date(date: str, db: Session = Depends(get_db)):
    return crud.get_order_date(db, date)


@app.get("/orders/")
def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)

