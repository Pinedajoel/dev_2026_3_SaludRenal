from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.caso import (
    CasoEstudioCreate,
    CasoEstudioUpdate,
    CasoEstudioOut,
    ConsultaPacienteCreate,
    ConsultaPacienteUpdate,
    ConsultaPacienteOut,
)
from app.crud import caso as crud_caso

router = APIRouter()


@router.post(
    "/estudio/",
    response_model=CasoEstudioOut,
    status_code=status.HTTP_201_CREATED,
)
def crear_caso_estudio(caso: CasoEstudioCreate, db: Session = Depends(get_db)):
    return crud_caso.create_caso_estudio(db=db, caso=caso)


@router.get("/estudio/", response_model=List[CasoEstudioOut])
def listar_casos_estudio(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud_caso.get_casos_estudio(db=db, skip=skip, limit=limit)


@router.get("/estudio/{caso_id}", response_model=CasoEstudioOut)
def obtener_caso_estudio(caso_id: int, db: Session = Depends(get_db)):
    db_caso = crud_caso.get_caso_estudio(db=db, caso_id=caso_id)
    if not db_caso:
        raise HTTPException(
            status_code=404, detail="Caso de estudio no encontrado"
        )
    return db_caso


@router.put("/estudio/{caso_id}", response_model=CasoEstudioOut)
def actualizar_caso_estudio(
    caso_id: int, caso: CasoEstudioUpdate, db: Session = Depends(get_db)
):
    db_caso = crud_caso.update_caso_estudio(
        db=db, caso_id=caso_id, caso_in=caso
    )
    if not db_caso:
        raise HTTPException(
            status_code=404,
            detail="Caso de estudio no encontrado para actualizar",
        )
    return db_caso


@router.delete("/estudio/{caso_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_caso_estudio(caso_id: int, db: Session = Depends(get_db)):
    db_caso = crud_caso.delete_caso_estudio(db=db, caso_id=caso_id)
    if not db_caso:
        raise HTTPException(
            status_code=404,
            detail="Caso de estudio no encontrado para eliminar",
        )
    return None


@router.post(
    "/consulta/",
    response_model=ConsultaPacienteOut,
    status_code=status.HTTP_201_CREATED,
)
def crear_consulta_paciente(
    consulta: ConsultaPacienteCreate, db: Session = Depends(get_db)
):
    return crud_caso.create_consulta_paciente(db=db, consulta=consulta)


@router.get("/consulta/", response_model=List[ConsultaPacienteOut])
def listar_consultas_paciente(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud_caso.get_consultas_paciente(db=db, skip=skip, limit=limit)


@router.get("/consulta/{consulta_id}", response_model=ConsultaPacienteOut)
def obtener_consulta_paciente(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud_caso.get_consulta_paciente(
        db=db, consulta_id=consulta_id
    )
    if not db_consulta:
        raise HTTPException(
            status_code=404, detail="Consulta de paciente no encontrada"
        )
    return db_consulta


@router.put("/consulta/{consulta_id}", response_model=ConsultaPacienteOut)
def actualizar_consulta_paciente(
    consulta_id: int,
    consulta: ConsultaPacienteUpdate,
    db: Session = Depends(get_db),
):
    db_consulta = crud_caso.update_consulta_paciente(
        db=db, consulta_id=consulta_id, consulta_in=consulta
    )
    if not db_consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta de paciente no encontrada para actualizar",
        )
    return db_consulta


@router.delete("/consulta/{consulta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_consulta_paciente(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud_caso.delete_consulta_paciente(
        db=db, consulta_id=consulta_id
    )
    if not db_consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta de paciente no encontrada para eliminar",
        )
    return None