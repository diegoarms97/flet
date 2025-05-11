import flet as ft
import csv
from fpdf import FPDF


def exportar_a_csv(logs):
    with open("logs_exportados.csv", mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Fecha", "Hora", "Evento"])
        for log in logs:
            writer.writerow([
                log["fecha"],
                log["hora"],
                log["evento"]
            ])


def exportar_a_pdf(logs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Logs Exportados", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(50, 10, "Fecha", 1)
    pdf.cell(40, 10, "Hora", 1)
    pdf.cell(90, 10, "Evento", 1)
    pdf.ln()

    for log in logs:
        pdf.cell(50, 10, log["fecha"], 1)
        pdf.cell(40, 10, log["hora"], 1)
        pdf.cell(90, 10, log["evento"], 1)
        pdf.ln()

    pdf.output("logs_exportados.pdf")


def cargar_logs(page: ft.Page, content: ft.Container):
    # Ejemplo de logs (esto se puede reemplazar por tu función que obtiene los logs de la base de datos)
    logs = [
        {"fecha": "2025-03-20", "hora": "10:15", "evento": "Usuario autenticado"},
        {"fecha": "2025-03-20", "hora": "10:30", "evento": "Acceso denegado"},
        {"fecha": "2025-03-21", "hora": "09:00", "evento": "Usuario autenticado"},
    ]
    
    filas = []
    for log in logs:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(log["fecha"], color="#333333")),
                    ft.DataCell(ft.Text(log["hora"], color="#333333")),
                    ft.DataCell(ft.Text(log["evento"], color="#333333")),
                ]
            )
        )

    tabla_logs = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Fecha", weight=ft.FontWeight.BOLD, color="#333333")),
            ft.DataColumn(ft.Text("Hora", weight=ft.FontWeight.BOLD, color="#333333")),
            ft.DataColumn(ft.Text("Evento", weight=ft.FontWeight.BOLD, color="#333333")),
        ],
        rows=filas
    )

    # Crear diálogo de exportación
    def exportar_pdf(e):
        exportar_a_pdf(logs)
        exportar_dialogo.open = False
        page.snack_bar = ft.SnackBar(content=ft.Text("PDF exportado correctamente"))
        page.snack_bar.open = True
        page.update()

    def exportar_csv(e):
        exportar_a_csv(logs)
        exportar_dialogo.open = False
        page.snack_bar = ft.SnackBar(content=ft.Text("CSV exportado correctamente"))
        page.snack_bar.open = True
        page.update()

    def cerrar_dialogo():
        exportar_dialogo.open = False
        page.update()

    exportar_dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Exportar logs", text_align=ft.TextAlign.CENTER),
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
    content.content = ft.Column(
        controls=[
            ft.Row(
            [ft.Text("Registro de Logs", size=20, weight=ft.FontWeight.BOLD, color="#333333")],
            alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row([boton_exportar], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(
                expand=True,
                padding=10,
                width=990,
                bgcolor="white",
                content=tabla_logs
            )
        ],
        expand=True,
        spacing=10,
    )

    page.update()
