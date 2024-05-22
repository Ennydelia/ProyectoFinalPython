# Avance 2 - Modulos y Clases / Avance 3 Creacion de funciones
import sqlite3

# Creacion de la clase Producto
class Producto:
    # Conexion de SQL
    def abrirConexion(self):
        conexion = None
        try:
            conexion = sqlite3.connect('HappyBurguerBD.db') 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))
    

    # Realizamos un listado de Productos (Para comprobar conexion SQL)
    def mostrarProductos(self):
        try:
            # Conexion con la base de datos
            conexion = sqlite3.connect('HappyBurguerBD.db') 
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM menu")     
            productos = cursor.fetchall()
            if len(productos) > 0:
                print("Listado de Productos: ")
                for clave,nombre,precio in productos:
                    print("""
                          clave: {}, nombre: {}, precio {}
                    """
                          .format(clave,nombre,precio))
            else:
                print("No contamos con productos")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los productos", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
        
    # Agregar un nuevo producto
    def agregarProducto(self):
        try:
            # Conexion a la Base de datos
            conexion = sqlite3.connect('HappyBurguerBD.db') 
            cursor = conexion.cursor()
            datos_incorrectos = True
            while datos_incorrectos:
                try:
                    # Solicita los datos a ingresar
                    clave = input("Ingresa la clave para el producto: \n")
                    nombre = input("Nombre del producto: \n")
                    precio = float(input("Precio: \n"))
                    datos_incorrectos = False
                except Exception as e:
                    print('Error al capturar un dato: {}'.format(e))
                    print('Intente de nuevo ingresar los datos \n')
                    datos_incorrectos = True
            # Realiza el insert de los datos solicitados
            valores = (clave, nombre, precio)
            sql = ''' INSERT INTO menu(clave,nombre,precio)
                    VALUES(?,?,?) '''                    
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")            
        except sqlite3.Error as error:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                print("------------------------------------")
                # Muestra un listado actualizado de productos
                self.mostrarProductos()

    # Actualizar informacion de un producto
    def modificarProducto(self):
        try:
            # Conexion a la base de datos
            conexion = sqlite3.connect('HappyBurguerBD.db') 
            cursor = conexion.cursor()
            # Realiza una consulta de productos para ver que existan
            cursor.execute("SELECT * FROM menu")     
            productos = cursor.fetchall()
            if len(productos) > 0:
                # Muestra el listado de productos
                self.mostrarProductos()
                print("----------------------------------")
                # Busca el producto por clave
                claveProducto = ''
                datos_incorrectos = True
                while datos_incorrectos:
                    try:
                        claveProducto = input("Cual es la clave del producto a modificar?")
                        datos_incorrectos = False
                    except Exception as e:
                        print('Error al capturar el id del producto: {}'.format(e))
                        print('Intente de nuevo ingresar el id \n')
                        datos_incorrectos = True
                eProducto = cursor.execute("SELECT * FROM menu WHERE clave = ?", (claveProducto,))    
                producto = eProducto.fetchone()
                if producto :
                    # Se solicita los datos del cliente a modificar
                    datos_incorrectos = True
                    while datos_incorrectos:
                        try:
                            nombre = input("Nombre del producto: \n")
                            precio = float(input("Precio: \n"))
                            datos_incorrectos = False
                        except Exception as e:
                            print('Error al capturar un dato: {}'.format(e))
                            print('Intente de nuevo ingresar los datos \n')
                            datos_incorrectos = True
                    # Se realiza el update del cliente a modificar
                    sql = ''' UPDATE menu SET nombre = ?, precio = ? WHERE clave = ? '''
                    datosProducto = (nombre,precio,claveProducto)
                    cursor.execute(sql,datosProducto)
                    conexion.commit()
                    print("Producto modificado correctamente")                   
                else:
                    print("No existe el Producto")                   
            else:  
                print("No hay productos para modificar")
                print("------------------------------------")
            
        except sqlite3.Error as error:
            print('Error al intentar modificar el producto: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()


    # Eliminar un producto
    def eliminarProducto(self):
        try:
            # Conexion con la base de datos
            conexion = sqlite3.connect('HappyBurguerBD.db') 
            cursor = conexion.cursor()
            # Verifica que existan productos a Eliminar
            cursor.execute("SELECT * FROM menu")     
            productos = cursor.fetchall()
            if len(productos) > 0:
                # Muestra el listado de clientes                
                self.mostrarProductos()
                print("------------------------------------")
                # Busca un cliente por clave
                claveProducto = ''
                datos_incorrectos = True
                while datos_incorrectos:
                    try:
                        claveProducto = input("Cual es la clave del producto a eliminar?")
                        datos_incorrectos = False
                    except Exception as e:
                        print('Error al capturar el id del producto: {}'.format(e))
                        print('Intente de nuevo ingresar el id \n')
                        datos_incorrectos = True
                eProducto = cursor.execute("SELECT * FROM menu WHERE clave = ?", (claveProducto,))    
                producto = eProducto.fetchone()
                if producto :
                    # Realiza el Delete del cliente
                    sql = ''' DELETE FROM menu WHERE clave = ? '''
                    cursor.execute(sql,(claveProducto,))
                    conexion.commit()
                    print("Producto eliminado")                   
                else:
                    print("No existe el producto con esa clave")                   
            else:  
                print("No hay productos para eliminar")
                print("------------------------------------")
        except sqlite3.Error as error:
            print('Error al intentar eliminar el producto: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()