#obtener logs
from database.models.log_acceso import LogAcceso
from database.session import db     
from datetime import datetime

def obtener_logs_acceso():
    session = db.get_session()
    logs = session.query(LogAcceso).all()
    resultado = []
    for log in logs:
        resultado.append({
            "usuario_id": log.usuario_id,
            "fecha_hora": log.fecha_hora_biometrico,
            "tipo_evento": log.tipo_evento,
            "resultado": log.resultado
        })
    return resultado