import flet as ft
import csv
from fpdf import FPDF
from view_data_adapters.usuario_view_adapter import obtener_datos_usuarios_para_vista


def exportar_a_csv(usuarios):
    with open("usuarios_exportados.csv", mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo, delimiter=',')  # Aseguramos que usamos coma como delimitador
        writer.writerow(["Nombre", "Rol", "Última Actividad", "Resultado"])  # Encabezados

        for usuario in usuarios:
            writer.writerow([  # Escribir los datos separados por comas
                usuario["nombre"],
                usuario["rol"],
                usuario["ultima_actividad"],
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
        pdf.cell(60, 10, str(usuario["ultima_actividad"]), 1)
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
                    ft.DataCell(ft.Text(usuario["nombre"], color="black")),
                    ft.DataCell(ft.Text(usuario["rol"], color="black")),
                    ft.DataCell(ft.Text(str(usuario["ultima_actividad"]), color="black")),
                    ft.DataCell(ft.Text(usuario["resultado"], color="black")),
                ]
            )
        )

    tabla_usuarios = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre", color="black")),
            ft.DataColumn(ft.Text("Rol", color="black")),
            ft.DataColumn(ft.Text("Última Actividad", color="black")),
            ft.DataColumn(ft.Text("Resultado", color="black"))
        ],
        rows=filas
    )

    # Crear diálogo de exportación
    def exportar_pdf(e):
        exportar_a_pdf(usuarios)
        exportar_dialogo.open = False
        page.snack_bar = ft.SnackBar(content=ft.Text("PDF exportado correctamente"))
        page.snack_bar.open = True
        page.update()

    def exportar_csv(e):
        exportar_a_csv(usuarios)
        exportar_dialogo.open = False
        page.snack_bar = ft.SnackBar(content=ft.Text("CSV exportado correctamente"))
        page.snack_bar.open = True
        page.update()

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

    # ⬅️ Esta línea es FUNDAMENTAL para que el diálogo funcione
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
