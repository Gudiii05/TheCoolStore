import re


# Funcion para validar la password
def fn_check_pwd(password):
    check = True
    if not password or len(password) < 8: #Verifica la longitud de la pwd sea almenos de 8 carácteres
        check = False 
    if not re.search(r"[a-z]", password): #Verifica que haya 1 minúscula almenos
        check = False 
    if not re.search(r"[A-Z]", password): #Verifica que haya 1 mayúscula almenos
        check = False 
    if not re.search(r"\d", password): #Verifica que haya 1 numero almenos
        check = False 
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\\-=/]", password): #Verifica que haya 1 carácter especial almenos
        check = False 
    return check  # Es segura



# ---------------------------------------------------------------- #

# Test unitario


print("Resultado primer test (Hola123_): ", fn_check_pwd("Hola123_")) # -> True, exitoso

print("Resultado segundo test (Hola1): ", fn_check_pwd("Hola1")) # -> False, fracaso


# ---------------------------------------------------------------- #

