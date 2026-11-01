from typing import List, Optional
from pydantic import BaseModel


class CasoEstudioCreate(BaseModel):
    pass


class CasoEstudioUpdate(BaseModel):
    pass


class CasoEstudioOut(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ConsultaPacienteCreate(BaseModel):
    pass


class ConsultaPacienteUpdate(BaseModel):
    pass


class ConsultaPacienteOut(BaseModel):
    id: int

    class Config:
        orm_mode = True