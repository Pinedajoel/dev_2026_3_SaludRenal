from sqlalchemy.orm import Session
from app.models.caso import CasoEstudio, ConsultaPaciente
from app.schemas.caso import (
    CasoEstudioCreate,
    CasoEstudioUpdate,
    ConsultaPacienteCreate,
    ConsultaPacienteUpdate,
)


def get_caso_estudio(db: Session, caso_id: int):
    return db.query(CasoEstudio).filter(CasoEstudio.id == caso_id).first()


def get_casos_estudio(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CasoEstudio).offset(skip).limit(limit).all()


def create_caso_estudio(db: Session, caso: CasoEstudioCreate):
    db_caso = CasoEstudio(**caso.dict())
    db.add(db_caso)
    db.commit()
    db.refresh(db_caso)
    return db_caso


def update_caso_estudio(
    db: Session, caso_id: int, caso_in: CasoEstudioUpdate
):
    db_caso = db.query(CasoEstudio).filter(CasoEstudio.id == caso_id).first()
    if not db_caso:
        return None
    update_data = caso_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_caso, key, value)
    db.commit()
    db.refresh(db_caso)
    return db_caso


def delete_caso_estudio(db: Session, caso_id: int):
    db_caso = db.query(CasoEstudio).filter(CasoEstudio.id == caso_id).first()
    if db_caso:
        db.delete(db_caso)
        db.commit()
    return db_caso


def get_consulta_paciente(db: Session, consulta_id: int):
    return (
        db.query(ConsultaPaciente)
        .filter(ConsultaPaciente.id == consulta_id)
        .first()
    )


def get_consultas_paciente(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ConsultaPaciente).offset(skip).limit(limit).all()


def create_consulta_paciente(db: Session, consulta: ConsultaPacienteCreate):
    db_consulta = ConsultaPaciente(**consulta.dict())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta


def update_consulta_paciente(
    db: Session, consulta_id: int, consulta_in: ConsultaPacienteUpdate
):
    db_consulta = (
        db.query(ConsultaPaciente)
        .filter(ConsultaPaciente.id == consulta_id)
        .first()
    )
    if not db_consulta:
        return None
    update_data = consulta_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_consulta, key, value)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta


def delete_consulta_paciente(db: Session, consulta_id: int):
    db_consulta = (
        db.query(ConsultaPaciente)
        .filter(ConsultaPaciente.id == consulta_id)
        .first()
    )
    if db_consulta:
        db.delete(db_consulta)
        db.commit()
    return db_consulta


def get_caso(db: Session, caso_id: int):
    return get_caso_estudio(db, caso_id)


def get_casos(db: Session, skip: int = 0, limit: int = 100):
    return get_casos_estudio(db, skip, limit)


def create_caso(db: Session, caso: CasoEstudioCreate):
    return create_caso_estudio(db, caso)


def update_caso(db: Session, caso_id: int, caso_in):
    return update_caso_estudio(db, caso_id, caso_in)


def delete_caso(db: Session, caso_id: int):
    return delete_caso_estudio(db, caso_id)