# models/usuario.py
from sqlalchemy import Column, String, DateTime, Integer
from database.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(String, unique=True, nullable=False)  # ID del biométrico
    nombre = Column(String)
    correo = Column(String)
    fecha_registro = Column(DateTime)
    