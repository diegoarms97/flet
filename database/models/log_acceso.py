from sqlalchemy import Column, Integer, DateTime, String, Enum
from database.base import Base

class LogAcceso(Base):
    __tablename__ = "logs_accesos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, nullable=True)
    fecha_hora_biometrico = Column(DateTime(timezone=True), nullable=True)
    fecha_hora_sistema = Column(DateTime(timezone=True), nullable=False)
    tipo_evento = Column(String(50), nullable=False)
    resultado = Column(Enum('Permitido', 'Denegado', name='resultados_acceso'), nullable=False)
