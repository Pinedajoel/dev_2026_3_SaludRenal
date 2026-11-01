from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CRUD casos clinicos")


@app.get("/salud")
def salud():
    return {"estado": "ok"}

