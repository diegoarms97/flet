import flet as ft
from view_data_adapters.usuario_view_adapter import obtener_datos_usuarios_para_vista

def cargar_usuarios(page: ft.Page, content: ft.Container):
    usuarios = obtener_datos_usuarios_para_vista()
    filas = []

    for usuario in usuarios:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(usuario["nombre"])),
                    ft.DataCell(ft.Text(usuario["rol"])),
                    ft.DataCell(ft.Text(str(usuario["ultima_actividad"]))),
                    ft.DataCell(ft.Text(usuario["resultado"]))
                ]
            )
        )

    tabla_usuarios = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Rol")),
            ft.DataColumn(ft.Text("Última Actividad")),
            ft.DataColumn(ft.Text("Resultado"))
        ],
        rows=filas
    )

    content.content = ft.Container(
        expand=True,
        padding=10,
        bgcolor="white",
        content=tabla_usuarios
    )

    page.update()
