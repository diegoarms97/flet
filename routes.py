class AppRouter:
    def __init__(self):
        self._views = None
    
    @property
    def views(self):
        if not self._views:
            # Importaciones diferidas para evitar circulares
            from views.inicio import cargar_inicio
            from views.logs import cargar_logs
            from views.v_usuarios import cargar_usuarios
            from views.permisos import cargar_permisos
            from views.horarios import cargar_horarios
            from views.dispositivos import cargar_dispositivos
            from views.ajustes import cargar_ajustes
            
            self._views = {
                "Inicio": cargar_inicio,
                "Logs": cargar_logs,
                "Lista de Usuarios": cargar_usuarios,
                "Permisos de Usuarios": cargar_permisos,
                "Horarios": cargar_horarios,
                "Gestión de Dispositivos": cargar_dispositivos,
                "Ajustes": cargar_ajustes
            }
        return self._views

router = AppRouter()