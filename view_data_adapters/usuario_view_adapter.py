from services.usuario_query_service import obtener_usuarios_con_ultimo_log

def obtener_datos_usuarios_para_vista():
    return obtener_usuarios_con_ultimo_log()
