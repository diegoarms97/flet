import flet as ft
from components.sidebar import crear_sidebar

from database.session import db
from routes import router
import sys
from pathlib import Path
from services.init_service import sincronizar_todo
# Obtiene la ruta absoluta del directorio raíz
ROOT_DIR = Path(__file__).parent.absolute()

# Agrega el directorio raíz al PYTHONPATH
sys.path.insert(0, str(ROOT_DIR))
# URL de la base de datos
DATABASE_URL = "sqlite:///biometric.db"  # O PostgreSQL, etc.

# Instanciar y preparar la base de datos



def main(page: ft.Page):
    db.init_db()
    print("tablas creadas")# Crea todas las tablas
    sincronizar_todo()    
    # 2. Ejemplo de uso directo
    
    page.title = "Sistema de Control Biométrico"
    page.bgcolor = "#F4F4F4"
    page.padding = 0
    page.window.height = 720
    page.window.width = 1280
    page.window.resizable = False

    estado_activo = 0
    content = ft.Container(expand=True)

    sidebar = crear_sidebar(content, page, estado_activo)
    page.add(ft.Row([sidebar, content], expand=True))

    

ft.app(target=main,assets_dir="img")
