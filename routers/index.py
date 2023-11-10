from database.database_mongo import db as db_mongo , collection as mongo_collection
from database.database_psql import engine_psql, SessionLocalPsql

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def intial_value():
    return {'value':"success"}

