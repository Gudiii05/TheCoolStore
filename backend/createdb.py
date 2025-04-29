import sqlite3

# -----------Tablas----------- #

tablas = [
    {
        # Usuarios
        "nombre": "users",
        "sql": '''CREATE TABLE IF NOT EXISTS users 
                    (userID TEXT NOT null primary key,
                    name TEXT NOT null,
                    surname TEXT NOT null,
                    password TEXT NOT null,
                    phone TEXT null,
                    email TEXT NOT null,
                    admin INTEGER default 0 not null
                    );'''
    },
    {
        # Descuentos
        "nombre": "discounts",
        "sql": '''CREATE TABLE IF NOT EXISTS discounts 
                    (codeID TEXT NOT null primary key,
                    discount_amount REAL NOT null
                    );'''
    },
    {
        # Categorias
        "nombre": "categories",
        "sql": '''CREATE TABLE IF NOT EXISTS categories 
                    (categoryID INTEGER NOT null primary key,
                    name TEXT NOT null
                    );'''
    },
    {
        # Productos
        "nombre": "products",
        "sql": '''CREATE TABLE IF NOT EXISTS products 
                    (productID INT NOT null primary key,
                    categoryID INTEGER NOT null,
                    name TEXT NOT null,
                    price REAL NOT null,
                    description TEXT null,
                    stock INT NOT null,
                    FOREIGN KEY(categoryID) REFERENCES categories(categoryID)
                    );'''
    },
    {
        # Proveedores
        "nombre": "suppliers",
        "sql": '''CREATE TABLE IF NOT EXISTS suppliers 
                    (supplierID INTEGER NOT null primary key,
                    productID INTEGER NOT null,
                    name TEXT NOT null,
                    phone TEXT NOT null,
                    FOREIGN KEY(productID) REFERENCES products(productID)
                    );'''
    },
    {
        # Pedidos
        "nombre": "orders",
        "sql": '''CREATE TABLE IF NOT EXISTS orders 
                    (orderID INTEGER NOT null PRIMARY KEY,
                    userID TEXT NOT null,
                    productID INTEGER NOT null,
                    detailID INTEGER not null,
                    address TEXT not null,
                    quantity INTEGER not null,
                    unit_price REAL not null,
                    comments TEXT null,
                    FOREIGN KEY(userID) REFERENCES users(userID),
                    FOREIGN KEY(productID) REFERENCES products(productID)
                    );'''
    }
]

#conexion a la base de datos fichero
con = sqlite3.connect("TheCoolStore_DB.db")

#permite intreractuar a la BD
cur = con.cursor()


for tabla in tablas:
    cur.execute(tabla["sql"])
    print(f"Tabla '{tabla['nombre']}' creada o ya existente.")

con.commit()
con.close()