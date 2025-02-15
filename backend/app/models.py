from pydantic import BaseModel
from typing import List


class SessionGoal(BaseModel):
    title: str
    description: str = ""

class UserSettings(BaseModel):
    max_tasks: int
    enable_voice_alerts: bool
    enable_notifications: bool


class Tab(BaseModel):
    index: str
    window_id: str
    title: str
    url: str
    active: str
    status: str


class Task(BaseModel):
    tabs: List[Tab]
    intention: str
    task_summary: str


class ActiveTabs(BaseModel):
    tabs: List[Tab]


class ActiveTasks(BaseModel):
    active_tasks: List[Task]
