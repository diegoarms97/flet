# # Importar modelos sin dependencias primero
from .usuario import Usuario  # Primero
from .log_acceso import LogAcceso  # Depende de Usuario
from .horario import Horario
from .permiso import PermisoUsuario

