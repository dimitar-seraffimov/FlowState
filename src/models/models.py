from pydantic import BaseModel


class Tab(BaseModel):
    index = str
    window_id = str
    title = str
    url = str
    active = str
    status = str


class Task(BaseModel):
    tabs: list[Tab]
    intention: str

