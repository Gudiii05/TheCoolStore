#------------------------------------------
import flet as ft
from backend.functions.fn_user_exists import user_exists
#------------------------------------------

correcto = None
username = ""
passwd = ""
class login_form(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor=ft.Colors.AMBER
        self.width=500
        self.height=500

        #campos entrada
        self.username = ft.TextField(hint_text="Username")
        self.password = ft.TextField(hint_text="Password", password=True)
        
        self.content = self.campos()
        
    def campos(self):
        #boton login
        boton = ft.ElevatedButton(text="Inicia Sesión", on_click=self.enviar_form)

        return ft.Column(
            [
                ft.Text("Inicia Sesión", size=20, weight="bold"),
                self.username,
                self.password,
                boton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def enviar_form(self,e):
        username = self.username.value
        passwd = self.password.value

        if not username or not passwd:
            correcto = False
        else:
            correcto = True
        #Si hay usuario y contraseña llamo a la función para saber si son correctos.
        if correcto == True:
            userExist = user_exists(username, passwd)
            if userExist == True:
                print ("Correcto---------------------------------")
            else:
                print ("Aviso error de Usuario o Contraseña Erroneos.")



