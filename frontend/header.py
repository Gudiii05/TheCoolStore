import flet as ft

def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
        width=500
        height=500

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.SHIELD), #Modificar por foto de la tienda
        leading_width=70,
        title=ft.Text("The Cool Store"),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[

            ft.Button(text="<-"),
            ft.Button(text="Carrito"),
            ft.CircleAvatar(
                foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=ft.Text("FF"),
            ),


        ],
    )
    page.add(ft.Text("Contenido APP"))
ft.app(main)