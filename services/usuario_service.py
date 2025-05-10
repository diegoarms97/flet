from database.models.usuario import Usuario
from database.models.log_acceso import LogAcceso
from database.session import db
from data_adapters.adapter_usuario import obtener_usuarios_desde_fuente
from datetime import datetime

def sincronizar_usuarios():
    session = db.get_session()
    datos = obtener_usuarios_desde_fuente()
    for u in datos:
        usuario = session.query(Usuario).filter_by(correo=u["correo"]).first()
        if not usuario:
            usuario = Usuario(**u)
            session.add(usuario)
            session.commit()
            session.refresh(usuario)

        log = LogAcceso(
            usuario_id=usuario.id,
            fecha_hora=datetime.now(),
            resultado="Permitido"
        )
        session.add(log)
        session.commit()
