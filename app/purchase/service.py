from app.db import db
from app.purchase.models import PurchaseCreate
from app.users.service import get_user_by_id
from bson import ObjectId

# MongoDB Collection for Purchases
collection = db["purchases"]

# Function to Create a New Purchase
async def create_purchase(purchase: PurchaseCreate):
    user = await get_user_by_id(purchase.user_id)  # Ensure user exists
    if not user:
        return None  # Return None if user doesn't exist

    purchase_dict = purchase.dict()  # Convert Pydantic model to dictionary
    result = await collection.insert_one(purchase_dict)  # Insert into MongoDB
    return {"id": str(result.inserted_id), **purchase_dict}  # Return with MongoDB ObjectId

# Function to Fetch Purchases by User ID
async def get_purchases_by_user(user_id: str):
    purchases = await collection.find({"user_id": user_id}).to_list(length=100)
    return [{"id": str(p["_id"]), **p} for p in purchases]
