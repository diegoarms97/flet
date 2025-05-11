import flet as ft
from flet import Page

def login_window(page: ft.Page):
    page.title = "Sistema de Control Biométrico"
    page.bgcolor = "#F4F4F4"
    page.padding = 0
    page.window.height = 500
    page.window.width = 400
    page.window.resizable = False

    # Campos de texto definidos como variables para fácil acceso
    usuario_input = ft.TextField(label="Usuario", hint_text="Ingrese su usuario")
    contrasena_input = ft.TextField(label="Contraseña", hint_text="Ingrese su contraseña", password=True)

    def comprobar_credenciales(e,aplicacion):
        usuario = usuario_input.value
        contrasena = contrasena_input.value

        if usuario == "user" and contrasena == "pass":
            return True
        else:
            return False

    # Contenido de la ventana de inicio de sesión
    content = ft.Container(
        expand=True,
        bgcolor="white",
        width=400,
        height=500,
        padding=20,
        content=ft.Column(
            [
                ft.Row(
                [ft.Text("Iniciar Sesión", size=22, weight=ft.FontWeight.BOLD, color="#333333")],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                usuario_input,
                contrasena_input,

                ft.Row(
                
                [ft.ElevatedButton("Ingresar", on_click=comprobar_credenciales)],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
    )

    page.add(content)

# Esta línea va FUERA de la función
ft.app(target=login_window)