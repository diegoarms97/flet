import flet as ft

def cargar_inicio(page: ft.Page, content: ft.Container, estado_activo: bool):
    content.content = ft.Column(
        expand=True,
        spacing=20,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Estado del Sistema:", size=18, weight=ft.FontWeight.BOLD, color="#333333"),
                    ft.Container(width=15, height=15, bgcolor="green" if estado_activo else "red", border_radius=7.5),
                    ft.Text("Activo" if estado_activo else "Inactivo", size=18, color="#333333"),
                ],
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.ElevatedButton("Reconectar", on_click=""),
            ),
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
                                # ...
                            ],
                        )
                    ],
                ),
            ),
        ],
    )
    page.update()
