from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.database_psql import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()), index=True)
   
    first_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    password = Column(String)
    
    # Define the relationship to the Image table
    images = relationship("Image", back_populates="user")

class Image(Base):
    __tablename__ = "images"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()), index=True)
    user_id = Column(String, ForeignKey("users.id"))
    image_url = Column(String)
    
    # Define the relationship back to the User table
    user = relationship("User", back_populates="images")