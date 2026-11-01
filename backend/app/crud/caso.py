from sqlalchemy.orm import Session
from app.models.caso import CasoEstudio, ConsultaPaciente
from app.schemas.caso import CasoEstudioCreate, ConsultaPacienteCreate

# --- Alias genéricos de compatibilidad (para evitar que falle el __init__.py) ---
def get_caso(db: Session, caso_id: int):
    return db.query(CasoEstudio).filter(CasoEstudio.id == caso_id).first()

def get_casos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CasoEstudio).offset(skip).limit(limit).all()

def create_caso(db: Session, caso: CasoEstudioCreate):
    return create_caso_estudio(db=db, caso=caso)

def update_caso(db: Session, caso_id: int, caso_in):
    db_caso = db.query(CasoEstudio).filter(CasoEstudio.id == caso_id).first()
    if not db_caso:
        return None
    update_data = caso_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_caso, key, value)
    db.commit()
    db.refresh(db_caso)
    return db_caso

def delete_caso(db: Session, caso_id: int):
    db_caso = db.query(CasoEstudio).filter(CasoEstudio.id == caso_id).first()
    if db_caso:
        db.delete(db_caso)
        db.commit()
    return db_caso

# --- Funciones específicas de Casos de Estudio ---
def create_caso_estudio(db: Session, caso: CasoEstudioCreate):
    db_caso = CasoEstudio(**caso.dict())
    db.add(db_caso)
    db.commit()
    db.refresh(db_caso)
    return db_caso

def get_casos_estudio(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CasoEstudio).offset(skip).limit(limit).all()

# --- Funciones específicas de Consultas de Pacientes ---
def create_consulta_paciente(db: Session, consulta: ConsultaPacienteCreate):
    db_consulta = ConsultaPaciente(**consulta.dict())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

def get_consultas_paciente(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ConsultaPaciente).offset(skip).limit(limit).all()