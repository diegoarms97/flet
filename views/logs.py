import flet as ft
import csv
from fpdf import FPDF
from view_data_adapters.log_view_adapter import get_logs_view_data

def exportar_a_csv(logs):
    with open("logs_exportados.csv", mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Usuario ID", "Fecha", "Evento"])
        for log in logs:
            writer.writerow([
                log["usuario_id"],
                log["fecha_hora"],
                log["tipo_evento"]
            ])

def exportar_a_pdf(logs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Logs Exportados", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(10, 10, "Usuario_id", 1)
    pdf.cell(50, 10, "Fecha", 1)
    pdf.cell(30, 10, "Tipo evento", 1)
    pdf.cell(30, 10, "Resultado", 1)
    pdf.ln()

    for log in logs:
        pdf.cell(10, 10, str(log["usuario_id"]), 1)
        pdf.cell(50, 10, str(log["fecha_hora"]), 1)
        pdf.cell(30, 10, str(log["tipo_evento"]), 1)
        pdf.cell(30, 10, str(log["resultado"]), 1)
        pdf.ln()

    pdf.output("logs_exportados.pdf")

def cargar_logs(page: ft.Page, content: ft.Container):
    logs = get_logs_view_data()

    # Inicializar snackbar
    snack_bar = ft.SnackBar(content=ft.Text(""))
    page.overlay.append(snack_bar)
    # Crear tabla de logs
    filas = []
    for log in logs:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(log["usuario_id"], color="#333333")),
                    ft.DataCell(ft.Text(log["fecha_hora"], color="#333333")),
                    ft.DataCell(ft.Text(log["tipo_evento"], color="#333333")),
                    ft.DataCell(ft.Text(log["resultado"], color="#333333")),
                ]
            )
        )

    tabla_logs = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("usuario", weight=ft.FontWeight.BOLD, color="#333333")),
            ft.DataColumn(ft.Text("fecha", weight=ft.FontWeight.BOLD, color="#333333")),
            ft.DataColumn(ft.Text("tipo_evento", weight=ft.FontWeight.BOLD, color="#333333")),
            ft.DataColumn(ft.Text("resultado", weight=ft.FontWeight.BOLD, color="#333333")),
        ],
        rows=filas
    )

    # Crear diálogo de exportación
    def exportar_pdf(e):
        exportar_a_pdf(logs)
        exportar_dialogo.open = False
        snack_bar.content.value = "PDF exportado correctamente"
        snack_bar.open = True
        page.update()

    def exportar_csv(e):
        exportar_a_csv(logs)
        exportar_dialogo.open = False
        snack_bar.content.value = "CSV exportado correctamente"
        snack_bar.open = True
        page.update()
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

    page.overlay.append(exportar_dialogo)

    def mostrar_dialogo_exportar(e):
        page.dialog = exportar_dialogo
        exportar_dialogo.open = True
        page.update()

    boton_exportar = ft.ElevatedButton(
        "Exportar", icon=ft.icons.DOWNLOAD, on_click=mostrar_dialogo_exportar
    )

    # Construcción del layout
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
