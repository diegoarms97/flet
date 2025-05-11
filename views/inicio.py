import flet as ft

def cargar_inicio(page: ft.Page, content: ft.Container, estado_activo: bool):
    content.content = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        padding=20,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Estado del Sistema:", size=20, weight=ft.FontWeight.BOLD, color="#333333"),
                        ft.Container(width=15, height=15, bgcolor="green" if estado_activo else "red", border_radius=7.5),
                        ft.Text("Activo" if estado_activo else "Inactivo", size=20, color="#333333"),
                    ],
                ),
                ft.ElevatedButton("Reconectar", on_click=lambda _: print("Reconectando...")),
                ft.Container(
                    expand=True,
                    width=350,
                    padding=20,
                    bgcolor="white",
                    border_radius=10,
                    content=ft.Column(
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            ft.Text("Registros recientes", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
                            ft.Divider(),
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
                                    # Agrega más registros si lo deseas
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )
    page.update()
