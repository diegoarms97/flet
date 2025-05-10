from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))  # Nombre de tabla
    hora_inicio = Column(DateTime)

    # Relación con Usuario usando string
    usuario = relationship("Usuario", back_populates="horarios")  # ← Correcto