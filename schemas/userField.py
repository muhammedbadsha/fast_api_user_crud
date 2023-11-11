from pydantic import BaseModel,EmailStr,constr


# Pydantic model for user creation
class UserCreate(BaseModel):
    first_name: str
    email: EmailStr
    phone_number: str
    password: constr(min_length=8, max_length=50)



class ImageModel(BaseModel):
    user_id: int
    image_url : str

    