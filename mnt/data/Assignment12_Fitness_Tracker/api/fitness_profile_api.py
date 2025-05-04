from fastapi import APIRouter
from services.fitness_profile_service import FitnessProfileService

router = APIRouter()
service = FitnessProfileService()

@router.get("/profiles")
def get_all_profiles():
    return service.get_all_profiles()

@router.get("/profiles/{age}")
def get_profile(age: int):
    return service.get_profile(age)

@router.post("/profiles")
def add_profile(age: int, weight: float, height: float, activity_level: str):
    return service.add_profile(age, weight, height, activity_level)

@router.delete("/profiles/{age}")
def delete_profile(age: int):
    service.delete_profile(age)
    return {"detail": "Profile deleted"}

