#--------------------------------
#Declaracion variables y imports
import sqlite3
#importar todo del frontend
username = ""
passwd = ""
address = ""


#--------------------------------

def insertar_usuario(username, address, passwd):
    try:
        con = sqlite3.connect("store.db")
        cur = con.cursor()

        # Ejecutar el insert
        cur.execute("""
            INSERT INTO users (userID, address, password)
            VALUES (?, ?, ?)
        """, (username, address, passwd))

        # Confirmar cambios
        con.commit()

        # Si se insertó correctamente, retornar 0
        return 0

    except sqlite3.Error as e:
        print("Error al insertar usuario:", e)
        return -1

    finally:
        con.close()