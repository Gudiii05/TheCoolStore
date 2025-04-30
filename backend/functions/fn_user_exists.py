#-------------------------------------------
#Imports y declaracion variables
import sqlite3
#importar frontend para variable username
users = "" #importar variable usuario
userExist = None

#---------------------------------------------


#conexion a la base de datos fichero
con = sqlite3.connect("TheCoolStore_DB.db")

#permite intreractuar a la BD
cur = con.cursor()

def user_exists(users):
    con = sqlite3.connect("TheCoolStore_DB.db")
    cur = con.cursor()

   # cur.execute("SELECT 1 FROM users WHERE userID = ?", (users)) #comprueba si la var username, esta en la tabla usuarios
  #  result = cur.fetchone()
    con.close()
  #  return result is not None

# Ejemplo de uso
# if user_exists(users):
#     print("Usuario existe.")
#     userExist = True

# else:
#     print("Usuario no existe.")
#     userExist = False

