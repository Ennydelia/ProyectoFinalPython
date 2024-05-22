# Avance 3 - Creacion de la base de datos 

import sqlite3

# Conexion de la base de datos
conexion = sqlite3.connect('HappyBurguerBD.db')
cursor = conexion.cursor()

# Creacion de las tablas de la base de datos 
# Tabla clientes
conexion.execute('''CREATE TABLE clientes (
                clave TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                correo_electronico TEXT NOT NULL,
                telefono TEXT NOT NULL);''')
# Tabla menu
conexion.execute('''CREATE TABLE menu (
                clave TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL);''')
# Tabla pedidos
conexion.execute('''CREATE TABLE pedido (
                pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                producto TEXT NOT NULL,
                precio REAL);''')