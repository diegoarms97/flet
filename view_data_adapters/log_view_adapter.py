from services.log_query_service import obtener_logs_acceso

#retorna los datos para la vista de logs
# view_data_adapters/log_view_adapter.py        

def get_logs_view_data():
    
    # Aquí puedes adaptar los datos si es necesario antes de retornarlos a la vista
    return obtener_logs_acceso()
