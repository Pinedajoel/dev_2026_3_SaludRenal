from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CasoEstudioBase(BaseModel):
    titulo: str
    descripcion_clinica: str
    pregunta: str
    opcion_correcta: str
    explicacion: Optional[str] = None

class CasoEstudioCreate(CasoEstudioBase):
    pass

class CasoEstudioOut(CasoEstudioBase):
    id: int

    class Config:
        from_attributes = True

class ConsultaPacienteBase(BaseModel):
    paciente_id: str
    sintomas_o_dolor: str
    nombre_archivo_examen: Optional[str] = None

class ConsultaPacienteCreate(ConsultaPacienteBase):
    pass

class ConsultaPacienteOut(ConsultaPacienteBase):
    id: int
    orientacion_preliminar: Optional[str] = None
    advertencia_medica: str
    fecha_registro: datetime

    class Config:
        from_attributes = True