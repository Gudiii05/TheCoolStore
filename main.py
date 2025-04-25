#---------------------------------------------------------------
import flet as ft
from frontend.container.register import register_form
#---------------------------------------------------------------
def main(page:ft.Page):
    prueba = register_form()

    page.add(prueba)

    page.update()


ft.app(target=main)