#------------------------------------------
import flet as ft
from backend.functions.fn_user_exists import user_exists
#from frontend.container.register import register_form
#------------------------------------------

correcto = None
email = ""
passwd = ""
class login_form(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.bgcolor=ft.Colors.WHITE10
        self.width=500
        self.height=500
        self.page = page
        #campos entrada
        self.email = ft.TextField(hint_text="Enter text here", label="Email", width=250)
        self.password = ft.TextField(hint_text="Enter text here", password=True, label="Password", width=250)
        
        self.content = self.campos()
        
    def campos(self):
        boton_login = ft.FilledButton(text="Inicia Sesión", on_click=self.enviar_form)

        # Texto con link a registro
        texto_registro = ft.Text(
            spans=[
                ft.TextSpan("Si no tienes cuenta, "),
                ft.TextSpan(
                    "regístrate aquí",
                    style=ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE),
                    on_click=self.ir_a_registro
                ),
            ],
        )

        return ft.Column(
            [
                ft.Text("Inicia Sesión", size=20, weight="bold"),
                self.email,
                self.password,
                boton_login,
                texto_registro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def enviar_form(self,e):
        email = self.email.value
        passwd = self.password.value

        if not email or not passwd:
            correcto = False
        else:
            correcto = True
        return correcto


#Si hay usuario y contraseña llamo a la función para saber si son correctos.    
    def userExist(self, correcto):
        self.correcto = correcto

        if self.correcto:
            return 1
        else:
            return 0


    def ir_a_registro(self, e):
        from frontend.container.register import register_form
        self.page.controls.clear()
        self.page.add(register_form(self.page))
        self.page.update()
