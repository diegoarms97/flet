# models/log_acceso.py
from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship  # Importar aquí
from database.base import Base

class LogAcceso(Base):
    __tablename__ = "logs_accesos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='SET NULL'))
    fecha_hora = Column(DateTime, nullable=False)
    resultado = Column(Enum('Permitido', 'Denegado', name='resultados_acceso'), nullable=False)
    
    # Relación
    usuario = relationship("Usuario", back_populates="logs_accesos")