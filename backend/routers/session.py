from fastapi import APIRouter, HTTPException
from app.models import SessionGoal, UserSettings

router = APIRouter()

@router.post("/create-session-goal")
async def create_session_goal(goal: SessionGoal):
    # Logic to create a session goal
    return {"message": "Session goal created successfully"}

@router.post("/update-settings")
async def update_settings(settings: UserSettings):
    # Logic to update user settings
    return {"message": "Settings updated successfully"}
