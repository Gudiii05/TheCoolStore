#-------------------------------------------
#Imports 
import sqlite3


#---------------------------------------------

def fn_password_match(user, passwd):
    con = sqlite3.connect("TheCoolStore_DB.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE userID = ?", (user,)) #comprueba si la var username, esta en la tabla usuarios
    result = cur.fetchone()
    con.close()
    if result[3] == passwd:
        return True
    else:
        return False

# --------------------------------------------
# Ejemplos de uso
print(fn_password_match("ahmed.khalil@example.com", "hash1234"))  # Return True

print(fn_password_match("ahmed.khalil@example.com", "")) # Return False

# --------------------------------------------