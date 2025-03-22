from fastapi import FastAPI
from app.users.router import user_router
from app.purchase.router import purchase_router

# Initialize FastAPI App
app = FastAPI(title="FastAPI MongoDB CRUD", version="1.0")

# Register Routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(purchase_router, prefix="/purchases", tags=["Purchases"])

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI CRUD is running!"}
