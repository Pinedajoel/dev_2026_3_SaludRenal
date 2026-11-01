from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class CasoEstudio(Base):
    __tablename__ = "casos_estudio"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion_clinica = Column(String)
    pregunta = Column(String)
    opcion_correcta = Column(String)
    explicacion = Column(String, nullable=True)

class ConsultaPaciente(Base):
    __tablename__ = "consultas_paciente"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(String, index=True)
    sintomas_o_dolor = Column(String)
    nombre_archivo_examen = Column(String, nullable=True)
    orientacion_preliminar = Column(String, nullable=True)
    advertencia_medica = Column(String, default="Aviso médico predeterminado")
    fecha_registro = Column(DateTime, default=datetime.utcnow)