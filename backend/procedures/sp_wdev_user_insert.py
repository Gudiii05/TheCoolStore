#--------------------------------
#Declaracion variables y imports
import sqlite3
#importar todo del frontend
username = ""
passwd = ""
address = ""
email = ""


#--------------------------------

def insertar_usuario(username, address, passwd, email):
    try:
        con = sqlite3.connect("store.db")
        cur = con.cursor()
        print("Hola insertar")
        # Ejecutar el insert
        cur.execute("""
            INSERT INTO usuarios (userID, name, address, password, email)
            VALUES (?, ?, ?, ? , ?)
        """, (email, username, address, passwd, email))

        # Confirmar cambios
        con.commit()

        # Si se insertó correctamente retornar 0
        return 0

        # Si no se inserto correctamente retornar -1
    except sqlite3.Error as e:
        print("Error al insertar usuario:", e)
        return -1

    finally:
        con.close()