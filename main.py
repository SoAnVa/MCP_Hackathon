from fastapi import FastAPI
from pydantic import BaseModel
from db import init_db
from agent import agent

# Init DB au démarrage
init_db()

app = FastAPI()

class Query(BaseModel):
    prompt: str

@app.post("/mcp")
async def ask_mcp(query: Query):
    result = agent.run(query.prompt)
    return {"result": result}
