import flet as ft

def cargar_dispositivos(page: ft.Page, content: ft.Container):
    # Tabla de dispositivos biométricos
    tabla_dispositivos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID Dispositivo", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Ubicación", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Estado", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Última Lectura", color="black", weight=ft.FontWeight.BOLD)),
        ],
        rows=[
            ft.DataRow([
                ft.DataCell(ft.Text("BIO-001", color="black")),
                ft.DataCell(ft.Text("Entrada Principal", color="black")),
                ft.DataCell(ft.Text("Operativo", color="black")),
                ft.DataCell(ft.Text("2025-04-30 08:41", color="black")),
            ]),
            ft.DataRow([
                ft.DataCell(ft.Text("BIO-002", color="black")),
                ft.DataCell(ft.Text("Área de Producción", color="black")),
                ft.DataCell(ft.Text("Sin conexión", color="black")),
                ft.DataCell(ft.Text("2025-04-29 21:10", color="black")),
            ]),
        ],
    )

    # Diseño de la vista
    content.content = ft.Column(
        expand=True,
        spacing=10,
        controls=[
            ft.Row(
                [ft.Text("Dispositivos Biométricos Registrados", size=20, weight=ft.FontWeight.BOLD, color="#333333")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Container(
                expand=True,
                padding=10,
                width=990,
                bgcolor="white",
                content=tabla_dispositivos
            )
        ]
    )

    page.update()
