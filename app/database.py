import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

load_dotenv()

# MongoDB Configuration
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")

# Initialize async MongoDB client with Stable API for version consistency
client = AsyncIOMotorClient(mongo_uri, server_api=ServerApi('1'))

# Database and collections references 
db = client[db_name]
items_collection = db[collection_name]