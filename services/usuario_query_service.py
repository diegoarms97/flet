from database.models.usuario import Usuario
from database.models.log_acceso import LogAcceso
from database.session import db
#obtener usuarios de la bd
def obtener_usuarios():
    session = db.get_session()
    usuarios = session.query(Usuario).all()
    resultado = []
    for usuario in usuarios:
        resultado.append({
            "id": usuario.id,
            "usuario_id": usuario.usuario_id,
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "fecha_registro": usuario.fecha_registro
        })
    return resultado