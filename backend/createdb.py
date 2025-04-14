import sqlite3

#conexion a la base de datos fichero
con = sqlite3.connect("store.db")

#permite intreractuar a la BD
cur = con.cursor()
