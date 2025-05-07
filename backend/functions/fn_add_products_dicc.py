def fn_add_products_dicc(dicc, new_product):
    for item in dicc:
        print(item)
        if item["productID"] == new_product["productID"]:
            item["quantity"] += 1
            return
    # Si no se encontró, lo añadimos como nuevo
    dicc.append({**new_product, "quantity": 1})

# Ejemplo de uso
# ------------------------------------------ #
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

fn_add_products_dicc(dicc,
                            {
        "productID":202,
        "quantity":2,
        "comments":"Con cuidao"
    })
print(dicc)

# ------------------------------------------ #