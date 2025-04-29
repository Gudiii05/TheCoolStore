import re

# Función para validar email
def fn_check_email(email):
    if not email:
        return False # Si esta vacía la String, devuelve error
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # Patron de validación de email
    if re.match(pattern, email):
        return True # Si es válido entonces devuelve 1
    return False




# ---------------------------------------------------------------- #

# Test unitario 


print("Resultado primer test (correo@example.com):", fn_check_email("correo@example.com"))  # → True, exitoso

print("Resultado segundo test (correo.com):", fn_check_email("correo.com"))  # → False, erroneo

# ---------------------------------------------------------------- #


