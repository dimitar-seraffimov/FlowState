from pydantic import BaseModel
from typing import List


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
