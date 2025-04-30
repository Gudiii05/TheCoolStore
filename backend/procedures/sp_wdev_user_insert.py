#--------------------------------
#Declaracion variables y imports
import sqlite3
#importar todo del frontend
username = ""
passwd = ""
address = ""


#--------------------------------

def wdev_user_insert(username, name, surname, passwd):
    try:
        con = sqlite3.connect("TheCoolStore_DB.db")
        cur = con.cursor()

        # Ejecutar el insert
        cur.execute("""
            INSERT INTO users (userID, name, surname, password, phone, email, admin)
            VALUES (?, ?, ?, ?, Null, ?, 0)
        """, (username, name, surname, passwd, username))

        # Confirmar cambios
        con.commit()

        # Si se insertó correctamente, retornar True
        return True

    except sqlite3.Error as e:
        print("Error al insertar usuario:", e)
        return False

    finally:
        con.close()

# --------------------------------------------------------
# Ejemplos de uso 

print(wdev_user_insert("pruebaInsert@gmail.com", "prueba", "subprueba", "Hola123_$")) # -> Return True

print(wdev_user_insert("prueba", "subprueba", "Hola123_$"))

# --------------------------------------------------------