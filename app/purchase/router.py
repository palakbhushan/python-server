from fastapi import APIRouter, HTTPException
from app.purchase.service import create_purchase, get_purchases_by_user
from app.purchase.models import PurchaseCreate, PurchaseResponse

# Initialize Router for Purchases
purchase_router = APIRouter()

# API Route: Create a New Purchase
@purchase_router.post("/", response_model=PurchaseResponse)
async def create_new_purchase(purchase: PurchaseCreate):
    purchase_data = await create_purchase(purchase)
    if not purchase_data:
        raise HTTPException(status_code=404, detail="User not found")
    return purchase_data

# API Route: Get Purchases by User ID
@purchase_router.get("/user/{user_id}", response_model=list[PurchaseResponse])
async def list_purchases_by_user(user_id: str):
    return await get_purchases_by_user(user_id)
