#-------------------------------------------
#Imports 
import sqlite3


#---------------------------------------------

def fn_user_exists(user):
    con = sqlite3.connect("TheCoolStore_DB.db")
    cur = con.cursor()

    cur.execute("SELECT 1 FROM users WHERE userID = ?", (user,)) #comprueba si la var username, esta en la tabla usuarios
    result = cur.fetchone()
    con.close()

    return True if result != None else False


# Ejemplo de uso
# print(fn_user_exists("ahmed.khalil@example.com")) # -> Devuelve True

# print(fn_user_exists("")) # -> Devuelve False

