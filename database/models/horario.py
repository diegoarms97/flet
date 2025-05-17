from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from database.base import Base

class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True)
    
    hora_inicio = Column(DateTime)

    # Relación con Usuario usando string
    