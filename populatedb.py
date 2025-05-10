from database.session import db
from database.models import Usuario
from datetime import datetime

def insertar_usuarios_prueba():
    session = db.get_session()
    try:
        # Verificar si ya existen usuarios
        if not session.query(Usuario).first():
            # Crear usuarios de prueba
            usuarios = [
                Usuario(
                    nombre="Admin Principal",
                    rol="Administrador",
                    ultima_actividad=datetime.now()
                ),
                Usuario(
                    nombre="Usuario Demo",
                    rol="Operador",
                    ultima_actividad=datetime.now()
                )
            ]
            
            session.add_all(usuarios)
            session.commit()
            print("✅ Usuarios de prueba insertados correctamente")
        else:
            print("ℹ️  Ya existen usuarios en la base de datos")
    except Exception as e:
        session.rollback()
        print("❌ Error insertando usuarios:", str(e))
    finally:
        session.close()