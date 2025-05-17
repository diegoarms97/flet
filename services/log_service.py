from data_adapters.adapter_log_acceso import obtener_logs_desde_fuente
from database.models.log_acceso import LogAcceso
from database.session import db
from datetime import datetime
from services.utilities.parse_fecha import parsear_fecha_biometrico
from services.usuario_service import asegurar_usuario_existe
from database.models.usuario import Usuario

def guardar_logs_accesos():
    session = db.get_session()
    logs = obtener_logs_desde_fuente()
    #comprobar si el usuario_id coincide con el suario_id de la tabla usuarios
    # si no coincide, registrar el usuario en la tabla usuarios
    
    
    for log in logs:
        nuevo_log = LogAcceso(
            usuario_id=log.get("usuario_id"),  # este viene del biométrico (no está relacionado con la tabla usuarios)
            fecha_hora_biometrico=parsear_fecha_biometrico(log.get("fecha_hora")),
            fecha_hora_sistema=datetime.now(),  # Fecha y hora del sistema
            tipo_evento=log.get("tipo_evento", "Desconocido"),  # Valor por defecto por seguridad
            resultado=log.get("resultado", "Denegado")  # Valor por defecto por seguridad
        )
        
        session.add(nuevo_log)
        usuario_id = log.get("usuario_id")
        resultado = log.get("resultado", "Denegado")

        # Registrar usuario si es nuevo y log exitoso
        if resultado.lower() == "permitido":
            asegurar_usuario_existe(usuario_id)

       

    if logs:
        session.commit()
        print(f"[LogService] {len(logs)} logs guardados.")
    
