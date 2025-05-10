from database.models.usuario import Usuario
from database.models.log_acceso import LogAcceso
from database.session import db

def obtener_usuarios_con_ultimo_log():
    session = db.get_session()
    usuarios = session.query(Usuario).all()
    resultado = []
    for u in usuarios:
        ultimo_log = (
            session.query(LogAcceso)
            .filter_by(usuario_id=u.id)
            .order_by(LogAcceso.fecha_hora.desc())
            .first()
        )
        resultado.append({
            "nombre": u.nombre,
            "rol": u.rol,
            "ultima_actividad": ultimo_log.fecha_hora if ultimo_log else "Sin actividad",
            "resultado": ultimo_log.resultado if ultimo_log else "N/A"
        })
    return resultado
