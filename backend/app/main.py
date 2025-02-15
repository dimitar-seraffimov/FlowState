from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

from routers import session

app = FastAPI()

# creates the static path
static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../", "static")

# mounts the static files directory to the app
app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(session.router)

templates = Jinja2Templates(directory="templates")

# serve index.html
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

