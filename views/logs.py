import flet as ft

def cargar_logs(page: ft.Page, content: ft.Container):
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
                        # ...
                    ],
                ),
            )
        ],
    )
    page.update()