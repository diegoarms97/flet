import flet as ft

def cargar_horarios(page: ft.Page, content: ft.Container):
    content.content = ft.Column(
        expand=True,
        spacing=20,
        controls=[
            ft.Text("Restricciones Horarias por Usuario", size=22, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Usuario")),
                    ft.DataColumn(ft.Text("Día")),
                    ft.DataColumn(ft.Text("Hora de Entrada")),
                    ft.DataColumn(ft.Text("Hora de Salida")),
                ],
                rows=[
                    ft.DataRow([
                        ft.DataCell(ft.Text("Carlos Romero")),
                        ft.DataCell(ft.Text("Lunes a Viernes")),
                        ft.DataCell(ft.Text("07:00")),
                        ft.DataCell(ft.Text("19:00")),
                    ]),
                    ft.DataRow([
                        ft.DataCell(ft.Text("María Torres")),
                        ft.DataCell(ft.Text("Fines de Semana")),
                        ft.DataCell(ft.Text("08:00")),
                        ft.DataCell(ft.Text("14:00")),
                    ]),
                ],
            )
        ]
    )
    page.update()
