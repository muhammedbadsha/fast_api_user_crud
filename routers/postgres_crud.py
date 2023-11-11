from sqlalchemy.orm import Session
from models.models import User
from database.database_psql import SessionLocalPsql
from schemas.userField import UserCreate
import uuid
from fastapi import Depends
from routers.index import get_postgres_db
def create_postgres_user(db:Session, User:UserCreate):
    db_user = User(first_name=User.first_name, email=User.email,phone_number=User.phone_number,passsword=User.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_postgres_email(email: str,db:Session=Depends(get_postgres_db)):
    return db.query(User).filter(User.email == email).first()

def get_postgres_phone_number(phone_number:str, db:Session = Depends(get_postgres_db)):
    return db.query(User).filter(User.phone_number == phone_number).first()

def get_postgres_user_by_id(user_id:uuid.UUID, db:Session = Depends(get_postgres_db)):
    return db.query(User).filter(User.id == user_id).first()
