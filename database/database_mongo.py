from schemas.userField import ImageModel
from pymongo.mongo_client import MongoClient
from models.models import Image
from decouple import config
uri = 'mongodb://localhost:27017'

# Create a new client and connect to the server
client = MongoClient(uri)
db_motor = client["xpay_db"]


# def create_mongo_userimage(image:ImageModel):
#     user_image = Image(user_id = image.user_id, image_url=image.image_url)
#     result = collection.insert_one(user_image.dict())
#     return result

# def get_mongo_userimage(user_id:str):
#     user_image = list(collection.find({"user_id":user_id}))
#     return [Image(**user_image) for user_image in user_image]



