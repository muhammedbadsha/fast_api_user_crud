from database.database_mongo import db_motor as mongo_conn
from database.database_psql import engine_psql, SessionLocalPsql, Base
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, File, UploadFile, HTTPException
from secrets import token_hex
from models.models import User, Image
from schemas.userField import UserCreate, ImageModel
from passlib.context import CryptContext
import secrets
import os
from fastapi.responses import JSONResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError

IMAGE_DIR = "images/"
router = APIRouter()
Base.metadata.create_all(bind=engine_psql)


def get_postgres_db():
    psql_db = SessionLocalPsql()
    try:
        yield psql_db
        psql_db.commit()
    finally:
        psql_db.close()


# def get_mongo_db():
#     try:
#         yield db_mongo
#     finally:
#         db_mongo.client.close()


# router.mount('/static/', StaticFiles(directory="static", name="static"))
@router.get("/")
async def intial_value(db: Session = Depends(get_postgres_db)):
    users = db.query(User).all()
    return users

@router.get("/detail_view/{id}")
async def DetailView(id:str,db_postgres: Session = Depends(get_postgres_db),):
    user = db_postgres.query(User).filter(User.id == id).first()
    file = os.listdir(IMAGE_DIR)
    image_path = mongo_conn.images.find_one(user_id = id)
    ext_path = image_path.image_url
    path = f"{IMAGE_DIR}{file[ext_path]}"

    response= {
        "user" :user,
        "image":FileResponse(path)
    }
    return response

@router.post("/add_user/", status_code=status.HTTP_201_CREATED)
async def add_user(
    user: UserCreate,
    db_postgres: Session = Depends(get_postgres_db),
    file: UploadFile = File(...),
):
    try:
        #chacking email existing or not 

        if db_postgres.query(User).filter(User.email == user.email).first() is not None:
                raise ValueError(
                    {"message": "User already exists in this email try another one"}
                )
        #checking phone number is existing or not
        if (
            db_postgres.query(User).filter(User.phone_number == user.phone_number).first()
            is not None
        ):
            raise ValueError(
                {"message": "User already exists in this phone number try another one"}
            )
        #user fields
        psw_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hased_password = psw_cxt.hash(user.password)
        new_user = User(
            first_name=user.first_name,
            email=user.email,
            phone_number=user.phone_number,
            password=hased_password,
        )
        db_postgres.add(new_user)
        db_postgres.commit()
        db_postgres.refresh(new_user)
        print(new_user.id)
        new_user_id = new_user.id 
        file_ext = file.filename.split(".").pop()
        file_name = token_hex(10)
        file_path = f"{file_name}.{file_ext}"
        with open(f"{IMAGE_DIR}{file_path}", "wb") as f:
            content = await file.read()
            f.write(content)
        user_image = mongo_conn.images.insert_one(
            {"user_id": new_user_id, "image_url": file_path}
                )

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            )
    except ValidationError as e:
        print("Validation error details:", e.errors())
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Validation error. Check the payload for any formatting issues.",
        )
    except HTTPException as e:
        print(e.detail) 
        raise e 
    

  
  
