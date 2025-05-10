# models/usuario.py
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship  # Importar relationship aquí
from database.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    rol = Column(Enum('Administrador', 'Usuario', name='roles'), nullable=False)
    
    # Relaciones
    logs_accesos = relationship("LogAcceso", back_populates="usuario")
    permisos = relationship("PermisoUsuario", back_populates="usuario")
    horarios = relationship("Horario", back_populates="usuario")