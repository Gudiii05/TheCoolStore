import re
import sqlite3

# Funcion para validar la password
def fn_check_pwd(password):
    if not password or len(password) < 8: #Verifica la longitud de la pwd sea almenos de 8 carácteres
        return 0
    if not re.search(r"[a-z]", password): #Verifica que haya 1 minúscula almenos
        return 0
    if not re.search(r"[A-Z]", password): #Verifica que haya 1 mayúscula almenos
        return 0
    if not re.search(r"\d", password): #Verifica que haya 1 numero almenos
        return 0
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\\-=/]", password): #Verifica que haya 1 carácter especial almenos
        return 0
    return 1  # Es segura

try:
    con = sqlite3.connect("TheCoolStore_DB.db")
    print("Conexión exitosa.")
except Exception as e:
    print("Error de conexión:", e)

con.create_function("fn_check_pwd", 1, fn_check_pwd)

# ---------------------------------------------------------------- #

# Test unitario

# cur = con.execute("select fn_check_pwd('Hola123_')") # → 1, exitoso
# print("Resultado primer test (Hola123_): ",cur.fetchone()[0])

# cur = con.execute("select fn_check_pwd('Hola1')") # → 0, erroneo
# print("Resultado segundo test (Hola1): ",cur.fetchone()[0])



# ---------------------------------------------------------------- #

con.close()