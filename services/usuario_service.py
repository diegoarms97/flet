from database.models.usuario import Usuario
from database.session import db
from data_adapters.adapter_usuario import obtener_datos_usuario_desde_biometrico
from datetime import datetime

def asegurar_usuario_existe(usuario_id):
    session = db.get_session()
    usuario = session.query(Usuario).filter_by(usuario_id=usuario_id).first()

    if not usuario:
        

        datos = obtener_datos_usuario_desde_biometrico(usuario_id)
        if not datos:
            print(f"[usuario_service] Usuario {usuario_id} no encontrado en biométrico.")
            return None

        nuevo_usuario = Usuario(
            usuario_id=datos["usuario_id"],
            nombre=datos["nombre"],
            correo=datos["correo"],
            fecha_registro=datos["fecha_registro"] 
        )
        session.add(nuevo_usuario)
        session.commit()
        print(f"[usuario_service] Usuario {datos['usuario_id']} registrado.")
        return nuevo_usuario
