from typing import Optional
from pydantic import BaseModel, Field

class CasoBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    edad: int = Field(..., ge=0, le=120)
    antecedentes: str
    motivo_consulta: str
    signos_sintomas: str
    foto_url: Optional[str] = None

class CasoCreate(CasoBase):
    pass

class CasoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    edad: Optional[int] = Field(None, ge=0, le=120)
    antecedentes: Optional[str] = None
    motivo_consulta: Optional[str] = None
    signos_sintomas: Optional[str] = None
    foto_url: Optional[str] = None

class CasoOut(CasoBase):
    id: int

    class Config:
        from_attributes = True