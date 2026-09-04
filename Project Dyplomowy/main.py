from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import create_tables
from routers import router

app = FastAPI(
    title="Project Dyplomowy API",
    description="Basic API skeleton for the diploma project",
    version="0.1.0",
)

create_tables()

app.include_router(router)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())



