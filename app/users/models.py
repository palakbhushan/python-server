from pydantic import BaseModel, EmailStr

# Base User Schema (Shared by other schemas)
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Schema for Creating a New User
class UserCreate(UserBase):
    password: str  # Password should be hashed in a real application

# Schema for Returning User Data (Response)
class UserResponse(UserBase):
    id: str  # MongoDB ObjectId as string

    class Config:
        from_attributes = True  # Allows easy conversion between Pydantic and MongoDB objects
