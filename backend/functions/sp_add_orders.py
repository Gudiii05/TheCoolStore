#-------------------------------------------
#Imports 
import sqlite3


#---------------------------------------------
# dictOfProducts ha de contener {
#       "productID": productID,
#       "quantity": quantity,
#       "comments": comments}



def sp_add_orders(userID, dictOfProducts, address):
    try:
        con = sqlite3.connect("TheCoolStore_DB.db")
        cur = con.cursor()

        # Coger el DetailID
        # ------------------------------------------------- #
        cur.execute("SELECT MAX(detailID) from orders")
        res = cur.fetchone()
        detailID = res[0] if res[0] is not None else 1
        detailID += 1
        # ------------------------------------------------- #

        # Coger el orderID
        # ------------------------------------------------- #
        cur.execute("SELECT MAX(orderID) from orders")
        res = cur.fetchone()
        orderID = res[0] if res[0] is not None else 1
        orderID += 1
        # ------------------------------------------------- #

        for product in dictOfProducts:
            # Cogemos la ID del producto
            productID = product["productID"]

            # Cogemos la cantidad x producto
            quantity = product["quantity"]

            # Cogemos el comentario por producto
            comments = product["comments"]

            cur.execute("SELECT price from products where productID = ?", (productID,))
            res = cur.fetchone()

            unit_price = res[0]
            # Ejecutar el insert
            cur.execute("""
                INSERT INTO orders (orderID, userID, productID, detailID, address, quantity, unit_price, comments)
                VALUES (?,?,?,?,?,?,?,?)
            """, 
                (orderID, 
                 userID, 
                 productID, 
                 detailID, 
                 address, 
                 quantity, 
                 unit_price, 
                 comments))
        
            orderID += 1
            

        # Confirmar cambios
        con.commit()

        # Si se insertó correctamente, retornar True
        return True

    except sqlite3.Error as e:
        print("Error al insertar pedidos:", e)
        return False

    finally:
        con.close()

# Ejemplos de uso 

# ------------------------------------ #
dicc = [
    {
        "productID":201,
        "quantity":2,
        "comments":"Con cuidao"
    },
    {
        "productID":203,
        "quantity":1,
        "comments":"Con cuidao" 
    }
]

print(sp_add_orders("ahmed.khalil@example.com", dicc, "Avenida de Prueba 123"))


# ------------------------------------ #