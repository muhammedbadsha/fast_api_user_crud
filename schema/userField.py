from pydantic import BaseModel,EmailStr,constr,HttpUrl
import uuid


class UsersModel(BaseModel):
    id : uuid.uuid4()
    first_name : str
    email : EmailStr
    phone_number : constr(regex=r'^\+?[1-9]\d{1,14}$')
    password : constr(min_length=6, max_length=50)


class ImageModel(BaseModel):
    image_url : HttpUrl
    alternative_text : str

