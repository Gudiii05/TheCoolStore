#------------------------------------------
from backend.procedures.sp_wdev_user_insert import insertar_usuario
import flet as ft
#------------------------------------------

correcto = None
username = ""
passwd = ""
email = ""
address = ""
class register_form():
    def __init__(self):
        #campos entrada
        self.username = ft.TextField(hint_text="Username")
        self.password = ft.TextField(hint_text="Password", password=True)
        self.email = ft.TextField(hint_text="Email")
        self.address = ft.TextField(hint_text="Address")

        
    def campos(self):
        #boton registro
        boton = ft.ElevatedButton(text="Resgistrarse", on_click=self.enviar_form)

        return ft.Column(
            [
                ft.Text("Registro", size=20, weight="bold"),
                self.username,
                self.password,
                self.email,
                self.address,
                boton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def enviar_form(self):
        username = self.username.value
        passwd = self.password.value
        email = self.email.value
        address = self.address.value

        if not username or not passwd or not email or not address:
            correcto = False
        else:
            correcto = True
        

if __name__ == "__main__":
    if correcto == True:
        insertar_usuario(username, address, passwd, email)

ft.app(target="register_form")


        






