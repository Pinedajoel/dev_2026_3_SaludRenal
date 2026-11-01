from fastapi import FastAPI
from app.api.v1.endpoints.caso import router as caso_router
from app.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="VidaRenal - CRUD Casos Clínicos")


@app.get("/salud")
def salud():
    return {"estado": "ok"}


app.include_router(caso_router, prefix="/api/v1/casos", tags=["Casos Clínicos"])