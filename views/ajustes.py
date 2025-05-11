import flet as ft

def cargar_ajustes(page: ft.Page, content: ft.Container):
    # Controles de configuración
    configuraciones = ft.Column([
        ft.Row([ft.Switch(value=True), ft.Text("Notificaciones de Accesos no autorizados", color="black")]),
        ft.Row([ft.Switch(value=True), ft.Text("Bloqueo de acceso fuera de horario", color="black")]),
        ft.Row([ft.Switch(value=True), ft.Text("Modo mantenimiento (desactiva lectores)", color="black")]),
    ])

    # Diseño de la vista
    content.content = ft.Column(
        expand=True,
        spacing=10,
        controls=[
            ft.Row(
                [ft.Text("Configuraciones Generales del Sistema", size=20, weight=ft.FontWeight.BOLD, color="#333333")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        padding=10,
                        width=400,
                        bgcolor="white",
                        content=ft.Column(
                            expand=True,
                            spacing=15,
                            controls=[
                                ft.TextField(label="Cambiar Nombre de Administrador", hint_text="Ej: Nombre Nuevo"),
                                ft.TextField(label="Cambiar Contraseña", hint_text="Ej: Contraseña Nueva"),
                                ft.Text("ID Dispositivo: BIO-001", weight=ft.FontWeight.BOLD, color="black"),
                                configuraciones,
                                ft.ElevatedButton("Guardar Cambios", on_click=lambda _: print("Cambios guardados")),
                            ]
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        ]
    )

    page.update()
