# services/init_services.py

# Aquí importarías también otros servicios
from services.log_service import guardar_logs_accesos
from services.event_listener import levantar_listening
import threading
from services.log_service import guardar_logs_accesos
import time

def sincronizar_logs_periodicamente():
    while True:
        guardar_logs_accesos()
        time.sleep(2)  # Ajusta el intervalo según lo que necesites


def sincronizar_todo():
    levantar_listening()
    threading.Thread(target=sincronizar_logs_periodicamente, daemon=True).start()
    print("[init_service] Servicio de sincronización de logs iniciado.")
    
    # sincronizar_logs()  <- si en un futuro hay más datos de logs independientes
    # sincronizar_horarios() ...
