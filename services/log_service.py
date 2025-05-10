# services/log_service.py
from datetime import datetime
from database.session import db
from database.models.log_acceso import LogAcceso

def registrar_log(usuario_id: int, resultado: str = 'Permitido'):
    session=db.get_session()
    log = LogAcceso(
        usuario_id=usuario_id,
        fecha_hora=datetime.now(),
        resultado=resultado
    )
    session.add(log)
    session.commit()
