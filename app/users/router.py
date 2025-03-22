from fastapi import APIRouter, HTTPException
from app.users.service import create_user, get_users, get_user_by_id
from app.users.models import UserCreate, UserResponse

# Initialize Router for Users
user_router = APIRouter()

# API Route: Create a New User
@user_router.post("/", response_model=UserResponse)
async def create_new_user(user: UserCreate):
    print(user,"hsjshjhsjdhjsdhjshdjshdj")
    return await create_user(user)

# API Route: Get All Users
@user_router.get("/", response_model=list[UserResponse])
async def list_users():
    return await get_users()

# API Route: Get User by ID
@user_router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
