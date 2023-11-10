
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:badsha@cluster0.yl2xxge.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["xpay_db"]
collection = db["user_image"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)