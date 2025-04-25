#-------------------------------------------
#Imports y declaracion variables
import sqlite3
#importar frontend para variable username
username = "" #importar variable usuario
userExist = None

#---------------------------------------------


#conexion a la base de datos fichero
con = sqlite3.connect("store.db")

#permite intreractuar a la BD
cur = con.cursor()

def user_exists(username):
    con = sqlite3.connect("store.db")
    cur = con.cursor()

    cur.execute("SELECT 1 FROM usuarios WHERE userID = ?", (username)) #comprueba si la var username, esta en la tabla usuarios
    result = cur.fetchone()
    con.close()
    return result is not None

'''
# Ejemplo de uso
if user_exists(username):
    print("Usuario existe.")
    userExist = True

else:
    print("Usuario no existe.")
    userExist = False
'''
