from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/trigger-action")
async def trigger_action():
    return {"message": "Action triggered due to max concurrent tasks."}

def check_max_concurrent_tasks(current_tasks, max_tasks):
    if current_tasks >= max_tasks:
        # Call the FastAPI endpoint
        response = requests.post("http://localhost:8000/trigger-action")
        if response.status_code == 200:
            print("Action triggered successfully.")
        else:
            print("Failed to trigger action.")
