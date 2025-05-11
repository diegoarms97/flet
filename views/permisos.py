import flet as ft

def cargar_permisos(page: ft.Page, content: ft.Container):
    # Tabla de permisos por rol
    tabla_permisos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Usuario", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Rol", color="black", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Áreas Permitidas", color="black", weight=ft.FontWeight.BOLD)),
        ],
        rows=[
            ft.DataRow([
                ft.DataCell(ft.Text("Carlos Romero", color="black")),
                ft.DataCell(ft.Text("Administrador", color="black")),
                ft.DataCell(ft.Text("Todas las áreas", color="black")),
            ]),
            ft.DataRow([
                ft.DataCell(ft.Text("María Torres", color="black")),
                ft.DataCell(ft.Text("Personal Técnico", color="black")),
                ft.DataCell(ft.Text("Sala de Servidores", color="black")),
            ]),
        ],
    )

    # Diseño de la vista
    content.content = ft.Column(
        expand=True,
        spacing=10,
        controls=[
            ft.Row(
                [ft.Text("Permisos de Acceso por Rol", size=20, weight=ft.FontWeight.BOLD, color="#333333")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Container(
                expand=True,
                padding=10,
                width=990,
                bgcolor="white",
                content=tabla_permisos
            )
        ]
    )

    page.update()
