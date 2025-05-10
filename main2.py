import flet as ft

# Función principal con configuración de la ventana
def main(page: ft.Page):
    page.title = "Sistema de Control Biométrico"
    page.bgcolor = "#F4F4F4"
    page.padding = 0
    page.window.height = 720
    page.window.width = 1280
    page.window.resizable = False

    estado_activo = True  # Estado inicial del sistema
    content = ft.Container(expand=True)  # Contenedor principal de los módulos

    # Función para cambiar la vista del módulo seleccionado
    def change_view(e):
        selected_module = e.control.data
        if selected_module == "Inicio":
            cargar_inicio()
        elif selected_module == "Logs":
            cargar_logs()
        else:
            content.content = ft.Text(f"Contenido de {selected_module}", size=20, color="#333333", weight=ft.FontWeight.BOLD)
        page.update()

    # Cargar contenido de "Inicio"
    def cargar_inicio():
        content.content = ft.Column(
            expand=True,
            spacing=20,
            controls=[
                # Indicador de estado
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Estado del Sistema:", size=18, weight=ft.FontWeight.BOLD, color="#333333"),
                        ft.Container(width=15, height=15, bgcolor="green" if estado_activo else "red", border_radius=7.5),
                        ft.Text("Activo" if estado_activo else "Inactivo", size=18, color="#333333"),
                    ],
                ),
                # Botón de reconectar
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.ElevatedButton("Reconectar", on_click=lambda _: print("Intentando reconectar...")),
                ),
                # Tabla de logs dentro de un contenedor expandible
                ft.Container(
                    expand=True,
                    padding=10,
                    bgcolor="white",
                    border_radius=5,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("Hora", weight=ft.FontWeight.BOLD, color="#333333")),
                                    ft.DataColumn(ft.Text("Evento", weight=ft.FontWeight.BOLD, color="#333333")),
                                ],
                                rows=[
                                    ft.DataRow([
                                        ft.DataCell(ft.Text("12:01", color="#333333")),
                                        ft.DataCell(ft.Text("Dispositivo conectado", color="#333333")),
                                    ]),
                                    ft.DataRow([
                                        ft.DataCell(ft.Text("12:05", color="#333333")),
                                        ft.DataCell(ft.Text("Usuario autenticado", color="#333333")),
                                    ]),
                                    ft.DataRow([
                                        ft.DataCell(ft.Text("12:10", color="#333333")),
                                        ft.DataCell(ft.Text("Intento fallido de acceso", color="#333333")),
                                    ]),
                                    ft.DataRow([
                                        ft.DataCell(ft.Text("12:15", color="#333333")),
                                        ft.DataCell(ft.Text("Base de datos actualizada", color="#333333")),
                                    ]),
                                    ft.DataRow([
                                        ft.DataCell(ft.Text("12:20", color="#333333")),
                                        ft.DataCell(ft.Text("Sistema reiniciado", color="#333333")),
                                    ]),
                                ],
                            )
                        ],
                    ),
                ),
            ],
        )
        page.update()

    # Cargar contenido de "Logs" con herramientas de filtrado
    def cargar_logs():
        content.content = ft.Column(
            expand=True,
            spacing=10,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.TextField(label="Filtrar por fecha"),
                        ft.TextField(label="Filtrar por evento"),
                        ft.ElevatedButton("Aplicar filtros", on_click=lambda _: print("Filtrando..."))
                    ],
                ),
                ft.Container(
                    expand=True,
                    padding=20,
                    bgcolor="white",
                    border_radius=5,
                    content=ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Fecha", weight=ft.FontWeight.BOLD, color="#333333")),
                            ft.DataColumn(ft.Text("Hora", weight=ft.FontWeight.BOLD, color="#333333")),
                            ft.DataColumn(ft.Text("Evento", weight=ft.FontWeight.BOLD, color="#333333")),
                        ],
                        rows=[
                            ft.DataRow([
                                ft.DataCell(ft.Text("2025-03-20", color="#333333")),
                                ft.DataCell(ft.Text("10:15", color="#333333")),
                                ft.DataCell(ft.Text("Usuario autenticado", color="#333333")),
                            ]),
                            ft.DataRow([
                                ft.DataCell(ft.Text("2025-03-20", color="#333333")),
                                ft.DataCell(ft.Text("11:30", color="#333333")),
                                ft.DataCell(ft.Text("Intento de acceso denegado", color="#333333")),
                            ]),
                            ft.DataRow([
                                ft.DataCell(ft.Text("2025-03-20", color="#333333")),
                                ft.DataCell(ft.Text("12:45", color="#333333")),
                                ft.DataCell(ft.Text("Dispositivo desconectado", color="#333333")),
                            ]),
                        ],
                    ),
                )
            ],
        )
        page.update()

    # Lista de módulos con sus respectivos iconos y colores
    modules = [
        {"title": "Inicio", "icon": ft.Icons.HOME, "color": "#1976D2"},
        {"title": "Logs", "icon": ft.Icons.LIST_ALT, "color": "#388E3C"},
        {"title": "Lista de Usuarios", "icon": ft.Icons.PEOPLE, "color": "#F57C00"},
        {"title": "Permisos de Usuarios", "icon": ft.Icons.VERIFIED_USER, "color": "#7B1FA2"},
        {"title": "Horarios", "icon": ft.Icons.ACCESS_TIME, "color": "#FF5722"},
        {"title": "Gestión de Dispositivos", "icon": ft.Icons.DEVICE_HUB, "color": "#D32F2F"},
        {"title": "Ajustes", "icon": ft.Icons.SETTINGS, "color": "#616161"},
    ]

    sidebar_items = [
        ft.ListTile(
            leading=ft.Icon(module["icon"], color=module["color"]),
            title=ft.Text(module["title"], color="#333333", size=16, weight=ft.FontWeight.BOLD),
            on_click=change_view,
            data=module["title"]
        ) for module in modules
    ]

    page.add(ft.Row([ft.Container(width=250, content=ft.Column(sidebar_items)), content], expand=True))
    cargar_inicio()

# Ejecución de la aplicación
ft.app(target=main)
