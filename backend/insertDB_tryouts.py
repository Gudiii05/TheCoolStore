import sqlite3 as sql

conn = sql.connect('TheCoolStore_DB.db')
cursor = conn.cursor()

# Insertar datos de prueba
cursor.executescript("""
-- Users
INSERT INTO users (userID, name, surname, password, phone, email, admin) VALUES
('ahmed.khalil@example.com', 'Ahmed', 'Khalil', 'hash1234', '600111222', 'ahmed.khalil@example.com', 0),
('sofia.romero@example.com', 'Sofía', 'Romero', 'romero2024', '699888777', 'sofia.romero@example.com', 1);

-- Discounts
INSERT INTO discounts (codeID, discount_amount) VALUES
('CACHI10', 10.0),
('SMOKE15', 15.0);

-- Categories
INSERT INTO categories (categoryID, name) VALUES
(1, 'Cachimbas'),
(2, 'Cazoletas'),
(3, 'Tabaco');

-- Products
INSERT INTO products (productID, categoryID, name, price, description, stock) VALUES
(201, 1, 'Cachimba Khalil Mamoon', 150.00, 'Cachimba egipcia tradicional de acero inoxidable', 10),
(202, 2, 'Cazoleta Oblako', 25.00, 'Cazoleta de cerámica tipo phunnel', 30),
(203, 3, 'Tabaco Al Fakher Menta', 7.50, 'Tabaco de menta para cachimba (50g)', 100);

-- Suppliers
INSERT INTO suppliers (supplierID, productID, name, phone) VALUES
(1, 201, 'Importaciones Khalil', '910001122'),
(2, 202, 'Distribuciones Oblako', '910223344'),
(3, 203, 'Tabacos del Sur', '910334455');

-- Orders
INSERT INTO orders (orderID, userID, productID, detailID, address, quantity, unit_price, comments) VALUES
(1, 'ahmed.khalil@example.com', 201, 6001, 'Calle Fumar 23, Valencia', 1, 150.00, 'Regalo, envolver si es posible'),
(2, 'ahmed.khalil@example.com', 202, 6001, 'Calle Fumar 23, Valencia', 1, 25.00, NULL),
(3, 'sofia.romero@example.com', 203, 6002, 'Av. del Humo 78, Barcelona', 3, 7.50, 'Entrega urgente');
""")

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()