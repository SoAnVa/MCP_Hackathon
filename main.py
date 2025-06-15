from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from db import init_db
from agent import agent  # suppose que tu peux logguer ici

# Initialize DB on startup
init_db()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Query(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/mcp")
async def ask_mcp(query: Query):
    result = agent.run(query.prompt)
    return {"result": result}
