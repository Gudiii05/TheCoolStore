import flet as ft

def main(page: ft.Page):
    # Fuente personalizada
    page.fonts = {"Orbitron": "fonts/Orbitron-Regular.ttf"}
    page.font_family = "Orbitron"

    page.theme = ft.Theme(
        text_theme= ft.TextTheme(body_medium=ft.TextStyle(color=ft.Colors.RED))
    )



    page.bgcolor = color="#D9D9D9"

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    # Barra superior de navegación
    page.appbar = ft.AppBar(
        leading=ft.Image(
            src="icon.jpg", 
            width=40,
            height=40,
            fit=ft.ImageFit.CONTAIN
        ),
        leading_width=70,
        title=ft.Text("The Cool Store"),
        center_title=True,
        bgcolor="#F2F2F2",
        actions=[
            ft.TextButton(text="<-"),
            ft.TextButton(text="Carrito"),
            ft.CircleAvatar(
                foreground_image_src="profile.png",
                content=ft.Text("FF"),
            ),
        ],
    )
    
    '''
    # Submenú
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="#F2F2F2",
        actions=[
            ft.TextButton(text="Cachimbas"),
            ft.TextButton(text="Cazoletas"),
            ft.TextButton(text="Tabaco"),
        ],
    )
    '''



    # Contenido de la página
    page.add(
        ft.Text("Contenido APP")
    )

ft.app(target=main, assets_dir="content")