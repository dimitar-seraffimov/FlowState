from fastapi import FastAPI
from playsound import playsound
import os

app = FastAPI()

@app.post("/play-sound/")
async def play_sound(file_path: str):
    if os.path.exists(file_path):
        playsound(file_path)
        return {"status": "success", "message": "Sound played successfully"}
    else:
        return {"status": "error", "message": "File not found"}
