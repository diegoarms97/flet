import flet as ft

def cargar_dispositivos(page: ft.Page, content: ft.Container):
    content.content = ft.Column(
        expand=True,
        spacing=20,
        controls=[
            ft.Text("Dispositivos Biométricos Registrados", size=22, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID Dispositivo")),
                    ft.DataColumn(ft.Text("Ubicación")),
                    ft.DataColumn(ft.Text("Estado")),
                    ft.DataColumn(ft.Text("Última Lectura")),
                ],
                rows=[
                    ft.DataRow([
                        ft.DataCell(ft.Text("BIO-001")),
                        ft.DataCell(ft.Text("Entrada Principal")),
                        ft.DataCell(ft.Text("Operativo")),
                        ft.DataCell(ft.Text("2025-04-30 08:41")),
                    ]),
                    ft.DataRow([
                        ft.DataCell(ft.Text("BIO-002")),
                        ft.DataCell(ft.Text("Área de Producción")),
                        ft.DataCell(ft.Text("Sin conexión")),
                        ft.DataCell(ft.Text("2025-04-29 21:10")),
                    ]),
                ],
            )
        ]
    )
    page.update()
