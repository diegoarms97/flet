import flet as ft
import csv
from fpdf import FPDF
from view_data_adapters.usuario_view_adapter import obtener_datos_usuarios_para_vista
from services.utilities.parse_fecha import parsear_fecha

def exportar_a_csv(usuarios):
    with open("usuarios_exportados.csv", mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo, delimiter=',')
        writer.writerow(["Nombre", "Rol", "Última Actividad", "Resultado"])

        for usuario in usuarios:
            writer.writerow([
                usuario["nombre"],
                usuario["rol"],
                parsear_fecha(usuario["ultima_actividad"]) if usuario["ultima_actividad"] else "",
                usuario["resultado"]
            ])

def exportar_a_pdf(usuarios):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Usuarios Exportados", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(50, 10, "Nombre", 1)
    pdf.cell(40, 10, "Rol", 1)
    pdf.cell(60, 10, "Última Actividad", 1)
    pdf.cell(40, 10, "Resultado", 1)
    pdf.ln()

    for usuario in usuarios:
        pdf.cell(50, 10, usuario["nombre"], 1)
        pdf.cell(40, 10, usuario["rol"], 1)
        pdf.cell(60, 10, str(parsear_fecha(usuario["ultima_actividad"])) if usuario["ultima_actividad"] else "", 1)
        pdf.cell(40, 10, usuario["resultado"], 1)
        pdf.ln()

    pdf.output("usuarios_exportados.pdf")

def cargar_usuarios(page: ft.Page, content: ft.Container):
    usuarios = obtener_datos_usuarios_para_vista()
    filas = []

    for usuario in usuarios:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(usuario["id"], color="black")),
                    ft.DataCell(ft.Text(usuario["nombre"], color="black")),
                    ft.DataCell(ft.Text(str(usuario["correo"]), color="black")),
                    ft.DataCell(ft.Text(str(parsear_fecha(usuario["fecha_registro"])), color="black")),
                    ft.DataCell(ft.Text(usuario["usuario_id"], color="black")),
                ]
            )
        )

    tabla_usuarios = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("id", color="black")),
            ft.DataColumn(ft.Text("nombre", color="black")),
            ft.DataColumn(ft.Text("correo", color="black")),
            ft.DataColumn(ft.Text("fecha registro", color="black")),
            ft.DataColumn(ft.Text("id biométrico", color="black")),
        ],
        rows=filas
    )

    # Snackbar global
    snack = ft.SnackBar(content=ft.Text(""))
    page.snack_bar = snack

    def mostrar_snackbar(mensaje):
        snack.content.value = mensaje
        snack.open = True
        page.update()

    # Exportar acciones
    def exportar_pdf(e):
        exportar_a_pdf(usuarios)
        exportar_dialogo.open = False
        mostrar_snackbar("PDF exportado correctamente")

    def exportar_csv(e):
        exportar_a_csv(usuarios)
        exportar_dialogo.open = False
        mostrar_snackbar("CSV exportado correctamente")

    def cerrar_dialogo():
        exportar_dialogo.open = False
        page.update()

    exportar_dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Exportar datos", text_align=ft.TextAlign.CENTER),
        content=ft.Column(
            controls=[
                ft.ElevatedButton("Exportar como PDF", on_click=exportar_pdf),
                ft.ElevatedButton("Exportar como CSV", on_click=exportar_csv),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
            spacing=10,
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialogo())
        ],
        on_dismiss=lambda e: print("Exportación cancelada"),
    )

    page.overlay.append(exportar_dialogo)

    def mostrar_dialogo_exportar(e):
        print("Botón exportar presionado")
        page.dialog = exportar_dialogo
        exportar_dialogo.open = True
        page.update()

    boton_exportar = ft.ElevatedButton(
        "Exportar", icon=ft.icons.DOWNLOAD, on_click=mostrar_dialogo_exportar
    )

    # Diseño de la vista
    content.content = ft.Column([
        ft.Row(
            [ft.Text("Lista de Usuarios", size=20, weight=ft.FontWeight.BOLD, color="#333333")],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([boton_exportar], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(
            expand=True,
            padding=10,
            width=990,
            bgcolor="white",
            content=tabla_usuarios
        )
    ])

    page.update()
