import flet as ft

def cargar_horarios(page: ft.Page, content: ft.Container):
    # Tabla de restricciones horarias
    tabla_horarios = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Usuario", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Día", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Hora de Entrada", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Hora de Salida", color="black", weight=ft.FontWeight.BOLD)),
        ],
        rows=[
            ft.DataRow([
                ft.DataCell(ft.Text("Carlos Romero", color="black")),
                ft.DataCell(ft.Text("Lunes a Viernes", color="black")),
                ft.DataCell(ft.Text("07:00", color="black")),
                ft.DataCell(ft.Text("19:00", color="black")),
            ]),
            ft.DataRow([
                ft.DataCell(ft.Text("María Torres", color="black")),
                ft.DataCell(ft.Text("Fines de Semana", color="black")),
                ft.DataCell(ft.Text("08:00", color="black")),
                ft.DataCell(ft.Text("14:00", color="black")),
            ]),
        ],
    )

    # Diseño de la vista
    content.content = ft.Column(
        expand=True,
        spacing=10,
        controls=[
            ft.Row(
                [ft.Text("Restricciones Horarias por Usuario", size=20, weight=ft.FontWeight.BOLD, color="#333333")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Container(
                expand=True,
                padding=10,
                width=990,
                bgcolor="white",
                content=tabla_horarios
            )
        ]
    )

    page.update()
