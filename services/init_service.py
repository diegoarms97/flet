# services/init_services.py
from services.usuario_service import sincronizar_usuarios
# Aquí importarías también otros servicios

def sincronizar_todo():
    sincronizar_usuarios()
    # sincronizar_logs()  <- si en un futuro hay más datos de logs independientes
    # sincronizar_horarios() ...
