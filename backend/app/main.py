from fastapi import FastAPI, Request
from routers import session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

from routers import session

app = FastAPI()

# creates the static path
static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../", "static")
templates = Jinja2Templates(directory="templates")


# mounts the static files directory to the app
app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(session.router)


# serve index.html
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/session-setup", response_class=HTMLResponse)
async def read_session_setup(request: Request):
    return templates.TemplateResponse("session-setup.html", {"request": request})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

