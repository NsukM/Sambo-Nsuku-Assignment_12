from fastapi import APIRouter, HTTPException
from services.user_service import UserService

router = APIRouter()
service = UserService()

@router.get("/users")
def get_all_users():
    return service.get_all_users()

@router.get("/users/{user_id}")
def get_user(user_id: str):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
def create_user(user_id: str, name: str, email: str, password: str, goal: str):
    return service.create_user(user_id, name, email, password, goal)

@router.put("/users/{user_id}")
def update_user(user_id: str, name: str = None, email: str = None, goal: str = None):
    return service.update_user(user_id, name, email, goal)

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    service.delete_user(user_id)
    return {"detail": "User deleted"}

