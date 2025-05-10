import flet as ft

def cargar_permisos(page: ft.Page, content: ft.Container):
    content.content = ft.Column(
        expand=True,
        spacing=20,
        controls=[
            ft.Text("Permisos de Acceso por Rol", size=22, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Usuario")),
                    ft.DataColumn(ft.Text("Rol")),
                    ft.DataColumn(ft.Text("Áreas Permitidas")),
                ],
                rows=[
                    ft.DataRow([
                        ft.DataCell(ft.Text("Carlos Romero")),
                        ft.DataCell(ft.Text("Administrador")),
                        ft.DataCell(ft.Text("Todas las áreas")),
                    ]),
                    ft.DataRow([
                        ft.DataCell(ft.Text("María Torres")),
                        ft.DataCell(ft.Text("Personal Técnico")),
                        ft.DataCell(ft.Text("Sala de Servidores")),
                    ]),
                ],
            )
        ]
    )
    page.update()
