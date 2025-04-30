#------------------------------------------
from backend.procedures.sp_wdev_user_insert import insertar_usuario
from frontend.container.login import login_form
import flet as ft
#------------------------------------------

correcto = None
username = ""
passwd = ""
email = ""
address = ""
class register_form(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.bgcolor=ft.Colors.WHITE10
        self.width=500
        self.height=500
        self.page = page
        #campos entrada
        self.name = ft.TextField(hint_text="Enter text here", label="Name", width=250)
        self.surname = ft.TextField(hint_text="Enter text here", label="Surname", width=250)
        self.password = ft.TextField(hint_text="Enter text here", password=True, label="Password", width=250)
        self.email = ft.TextField(hint_text="Enter text here", label="Email",width=250)
        
        self.content = self.campos()
        
    def campos(self):
        #boton registro
        boton = ft.FilledButton(text="Resgistrarse", on_click=self.enviar_form)

        texto_login = ft.Text(
            spans=[
                ft.TextSpan("Volver al "),
                ft.TextSpan(
                    "login",
                    style=ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE),
                    on_click=self.ir_a_login
                ),
            ],
        )

        return ft.Column(
            [
                ft.Text("Registro", size=20, weight="bold"),
                self.name,
                self.surname,
                self.password,
                self.email,
                boton,
                texto_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def enviar_form(self,e):
        username = self.username.value
        passwd = self.password.value
        email = self.email.value
        address = self.address.value

        if not username or not passwd or not email or not address:
            correcto = False
        else:
            correcto = True
        
        if correcto == True:
            insertar_usuario(username, address, passwd, email)

    def ir_a_login(self, e):
        self.page.controls.clear()
        self.page.add(login_form(self.page))
        self.page.update()


