from pydantic import BaseModel

class SessionGoal(BaseModel):
    title: str
    description: str = ""

class UserSettings(BaseModel):
    max_tasks: int
    enable_voice_alerts: bool
    enable_notifications: bool
