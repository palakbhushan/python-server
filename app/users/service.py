import logging
from app.db import db
from app.users.models import UserCreate
from bson import ObjectId

# MongoDB Collection for Users
collection = db["users"]

# Function to Create a New User
async def create_user2(user: UserCreate):
    print(user,"hsjshjhsjdhjsdhjshdjshdj")
    user_dict = user.dict()  # Convert Pydantic model to dictionary
    result = await collection.insert_one(user_dict)  # Insert into MongoDB
    return {"id": str(result.inserted_id), **user_dict}  # Return with MongoDB ObjectId


async def create_user(user: UserCreate):
    user_dict = user.dict()
    logging.info(f"Inserting user: {user_dict}")  # Debug log

    result = await collection.insert_one(user_dict)
    logging.info(f"Inserted user ID: {result.inserted_id}")  # Debug log

    return {"id": str(result.inserted_id), **user_dict}

# Function to Fetch All Users GET API
async def get_users():
    users = await collection.find().to_list(length=100)  # Get all users, limit 100
    return [{"id": str(user["_id"]), **user} for user in users]  # Convert ObjectId to string

# Function to Fetch a Single User by ID
async def get_user_by_id(user_id: str):
    user = await collection.find_one({"_id": ObjectId(user_id)})  # Find by ObjectId
    if user:
        return {"id": str(user["_id"]), **user}  # Convert ObjectId to string
    return None  # Return None if user not found
