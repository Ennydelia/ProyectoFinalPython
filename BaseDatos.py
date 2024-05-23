""" Avance 3 - Creacion de la base de datos /Llamado de conexion de la base de datos """

import sqlite3
import os


"""
    Aqui se realizara la creacion y conexion de la base de datos, 
    creando las tablas de clientes, menu y pedidos
"""

class BaseDatos:
    def crearBaseDatos(self):
        try:
            conn = sqlite3.connect('HappyBurguerBD.db') 
        except Exception as e:
            print('Error al crear la Base de datos: {}'.format(e))

    """ Verificar que existe la BD """
    def verificarBaseDatosExiste(self):
        if os.path.isfile('HappyBurguerBD.db'):
            return True
        else:
            return False
    """ Creacion de las tablas de la base de datos  """
    def crearTablaProductos(self):
        conexion = self.abrirConexion()

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

        conexion.close()
    
    """ Abrir la conexion de la BD 
    Esta conexion se estara llamando en cada modulo del sistema """
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect('HappyBurguerBD.db') 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))