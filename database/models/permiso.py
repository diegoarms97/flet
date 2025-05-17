# models/permiso_usuario.py
from sqlalchemy import Column, Integer, String, ForeignKey
from database.base import Base


class PermisoUsuario(Base):
    __tablename__ = "permisos_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    permiso = Column(String(100), nullable=False)
    
    # Relación
  
    