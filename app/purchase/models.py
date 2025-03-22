from pydantic import BaseModel

# Base Purchase Schema
class PurchaseBase(BaseModel):
    user_id: str  # Reference to User
    item_name: str
    price: float

# Schema for Creating a Purchase
class PurchaseCreate(PurchaseBase):
    pass  # No extra fields needed for creation

# Schema for Returning Purchase Data (Response)
class PurchaseResponse(PurchaseBase):
    id: str  # MongoDB ObjectId as string

    class Config:
        from_attributes = True
