#---------------------------------------------------------------
import flet as ft
from frontend.homepage import main
#---------------------------------------------------------------
'''def main(page:ft.Page):
    prueba = homepage()

    page.add(prueba)

    page.update()
'''

ft.app(target=main, assets_dir="content")