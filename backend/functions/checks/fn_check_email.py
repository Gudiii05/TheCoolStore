import sqlite3
import re

# Función para validar email
def fn_check_email(email):
    if not email:
        return 0 # Si esta vacía la String, devuelve error
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # Patron de validación de email
    if re.match(pattern, email):
        return 1 # Si es válido entonces devuelve 1
    return 0


con = sqlite3.connect("TheCoolStore_DB.db")
con.create_function("fn_check_email", 1, fn_check_email)

# ---------------------------------------------------------------- #

# Test unitario 

# cur = con.execute("SELECT fn_check_email('correo@example.com')")
# print("Resultado primer test (correo@example.com):", cur.fetchone()[0])  # → 1, exitoso

# cur = con.execute("SELECT fn_check_email('correo.com')")
# print("Resultado segundo test (correo.com):", cur.fetchone()[0])  # → 0, erroneo

# ---------------------------------------------------------------- #

con.close()
