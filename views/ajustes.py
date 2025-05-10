import flet as ft

def cargar_ajustes(page: ft.Page, content: ft.Container):
    content.content = ft.Column(
        expand=True,
        spacing=20,
        controls=[
            ft.Text("Configuraciones Generales del Sistema", size=22, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.TextField(label="Nombre del Sistema", hint_text="Ej: Control Biométrico ZK"),
            ft.Switch(label="Notificaciones de Accesos no autorizados", value=True),
            ft.Switch(label="Bloqueo de acceso fuera de horario", value=True),
            ft.Switch(label="Modo mantenimiento (desactiva lectores)", value=False),
            ft.ElevatedButton("Guardar Cambios", on_click=lambda _: print("Cambios guardados"))
        ]
    )
    page.update()
