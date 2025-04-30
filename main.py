#---------------------------------------------------------------
import flet as ft
from frontend.container.register import register_form
#from frontend.container.login import login_form

#---------------------------------------------------------------
def main(page:ft.Page):
    from frontend.container.login import login_form
    #register = register_form()
    login = login_form(page)
    page.add(login)

    
    
    page.update()


ft.app(target=main)