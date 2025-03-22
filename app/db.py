import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB credentials from .env
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "dev_fastapi_crud")

# Initialize MongoDB client and database
client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
