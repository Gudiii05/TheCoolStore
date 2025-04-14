import sqlite3

#conexion a la base de datos fichero
con = sqlite3.connect("store.db")

#permite intreractuar a la BD
cur = con.cursor()


try: 
    cur.execute('''CREATE TABLE usuarios 
                (userID NVARCHAR(255) not null primary key,
                name NVARCHAR(255) null,
                surname NVARCHAR(255) null,
                password NVARCHAR(255) null,
                phone INT null,
                email NVARCHAR(255) null,
                address NVARCHAR(255) not null
                )
               ''')
    
    cur.execute('''create table productos(
                prendaID INT not null primary key,
                talla nvarchar(4) null,
                precio FLOAT null,
                descripcion nvarchar(255) null
                )
                ''')
    
    cur.execute('''CREATE TABLE proveedores 
                (proveedorID INT not null primary key,
                name NVARCHAR(255) null,
                nif NVARCHAR(255) null,
                prenda NVARCHAR(255) null,
                cantidad INT null,
                precio_unidad FLOAT null,
                phone INT null
                )
               ''')
    
    cur.execute('''CREATE TABLE descuentos
                (codigoID NVARCHAR(255) not null primary key,
                descuento INT null
                )
                ''')

except sqlite3.Error as e:
    print("Base de datos ya existe", e)

try: 
    
    cur.execute('''CREATE TABLE proveedores 
                (proveedorID INT not null primary key,
                name NVARCHAR(255) null,
                nif NVARCHAR(255) null,
                prenda NVARCHAR(255) null,
                cantidad INT null,
                precio_unidad FLOAT null,
                phone INT null
                )
               ''')
    
    cur.execute('''CREATE TABLE descuentos
                (codigoID NVARCHAR(255) not null primary key,
                descuento INT null
                )
                ''')

except sqlite3.Error as e:
    print("Base de datos ya existe", e)