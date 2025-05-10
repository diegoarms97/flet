import flet as ft
from routes import router

def crear_sidebar(content: ft.Container, page: ft.Page, estado_activo: bool):
    
    def change_view(e):
        from routes import router
        selected_module = e.control.data
        view_function = router.views.get(selected_module)
        
        if view_function:
            if selected_module == "Inicio":
                view_function(page, content, estado_activo)
            else:
                view_function(page, content)
        else:
            content.content = ft.Text(
                f"Vista no implementada: {selected_module}", 
                size=20, color="#333333", weight=ft.FontWeight.BOLD
            )
        page.update()

    modules = [
        {"title": "Inicio", "icon": ft.Icons.HOME, "color": "#1976D2"},
        {"title": "Logs", "icon": ft.Icons.LIST_ALT, "color": "#388E3C"},
        {"title": "Lista de Usuarios", "icon": ft.Icons.PEOPLE, "color": "#F57C00"},
        {"title": "Permisos de Usuarios", "icon": ft.Icons.VERIFIED_USER, "color": "#7B1FA2"},
        {"title": "Horarios", "icon": ft.Icons.ACCESS_TIME, "color": "#FF5722"},
        {"title": "Gestión de Dispositivos", "icon": ft.Icons.DEVICE_HUB, "color": "#D32F2F"},
        {"title": "Ajustes", "icon": ft.Icons.SETTINGS, "color": "#616161"},
    ]

    sidebar_items = [
        ft.ListTile(
            leading=ft.Icon(module["icon"], color=module["color"]),
            title=ft.Text(module["title"], color="#333333", size=16, weight=ft.FontWeight.BOLD),
            on_click=change_view,
            data=module["title"]
        ) for module in modules
    ]

    return ft.Container(
        width=250,
        bgcolor="#FFFFFF",
        padding=10,
        content=ft.Column(
            controls=[
                *sidebar_items,
                ft.Divider(thickness=1),
                ft.Container(
                    content=ft.Image(
                        src="components/img/logo_institucion.jpeg",
                        
                        fit=ft.ImageFit.CONTAIN
                    ),
                    alignment=ft.alignment.center,
                    padding=0
                )
            ],
            expand=True,
            spacing=8,
            scroll=ft.ScrollMode.AUTO
        )
    )
