from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.database_psql import Base_Psql


class Users(Base_Psql):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    password = Column(String)