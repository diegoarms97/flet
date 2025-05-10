import flet as ft

# Estilo de encabezado principal para cada vista
def encabezado(texto: str) -> ft.Text:
    return ft.Text(
        texto,
        size=22,
        weight=ft.FontWeight.BOLD,
        color="#333333",
        text_align=ft.TextAlign.LEFT
    )

# Contenedor estándar para contenido principal
def contenedor_principal(control: ft.Control) -> ft.Container:
    return ft.Container(
        expand=True,
        padding=10,
        bgcolor="white",
        border_radius=8,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.BLACK12, spread_radius=1),
        content=control
    )

# Función para crear tablas con encabezados dinámicos y filas
def crear_tabla(encabezados: list[str], filas: list[ft.DataRow]) -> ft.DataTable:
    columnas = [
        ft.DataColumn(ft.Text(col, weight=ft.FontWeight.BOLD, color="#333333"))
        for col in encabezados
    ]
    return ft.DataTable(columns=columnas, rows=filas)

# Estilo de celda en tabla
def celda_tabla(texto: str) -> ft.DataCell:
    return ft.DataCell(ft.Text(texto, color="#333333"))

# Botón primario reutilizable
def boton_principal(label: str, on_click) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        text=label,
        bgcolor="#007BFF",
        color="white",
        on_click=on_click
    )

# Espaciador vertical
def espaciador(alto: int = 20) -> ft.Container:
    return ft.Container(height=alto)
