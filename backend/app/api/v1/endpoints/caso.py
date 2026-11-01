from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.caso import (
    CasoEstudioCreate,
    CasoEstudioOut,
    ConsultaPacienteCreate,
    ConsultaPacienteOut,
)
from app.crud import caso as crud_caso

router = APIRouter()

@router.post("/estudio/", response_model=CasoEstudioOut, status_code=status.HTTP_201_CREATED)
def crear_caso_estudio(caso: CasoEstudioCreate, db: Session = Depends(get_db)):
    return crud_caso.create_caso_estudio(db=db, caso=caso)

@router.get("/estudio/", response_model=List[CasoEstudioOut])
def listar_casos_estudio(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_caso.get_casos_estudio(db=db, skip=skip, limit=limit)

@router.post("/consulta/", response_model=ConsultaPacienteOut, status_code=status.HTTP_201_CREATED)
def crear_consulta_paciente(consulta: ConsultaPacienteCreate, db: Session = Depends(get_db)):
    return crud_caso.create_consulta_paciente(db=db, consulta=consulta)

@router.get("/consulta/", response_model=List[ConsultaPacienteOut])
def listar_consultas_paciente(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_caso.get_consultas_paciente(db=db, skip=skip, limit=limit)