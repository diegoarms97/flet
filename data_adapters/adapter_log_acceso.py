# adapter_log_acceso.py
from queue import Queue

logs_buffer = Queue()

def recibir_log_desde_biometrico(log_data):
    logs_buffer.put(log_data)
    

def obtener_logs_desde_fuente():
    datos = []
    while not logs_buffer.empty():
        datos.append(logs_buffer.get())
    
    return datos
