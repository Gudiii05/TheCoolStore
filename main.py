#---------------------------------------------------------------
import flet as ft
from frontend.container.login import login_form
#---------------------------------------------------------------
def main(page:ft.Page):
    prueba = login_form()

    page.add(prueba)

    page.update()


ft.app(target=main)