# models/permiso_usuario.py
from sqlalchemy import Column, Integer, String, ForeignKey
from database.base import Base
from sqlalchemy.orm import declared_attr, relationship

class PermisoUsuario(Base):
    __tablename__ = "permisos_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'))
    permiso = Column(String(100), nullable=False)
    
    # Relación
    usuario = relationship("Usuario", back_populates="permisos")
    