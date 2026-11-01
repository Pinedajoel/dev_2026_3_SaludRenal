from typing import Optional
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Caso(Base):
    __tablename__="casos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    edad: Mapped[int]
    antecedentes: Mapped[str] = mapped_column(Text)
    motivo_consulta: Mapped[str] = mapped_column(Text)
    signos_sintomas: Mapped[str] = mapped_column(Text)
    foto_url: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
