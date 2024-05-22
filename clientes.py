# Avance 2 - Modulos y Clases / Avance 3 - Creacion de funciones
import sqlite3
from BaseDatos import BaseDatos

# Creacion de la clase cliente
class Cliente:

    # Inicializar la BaseDatos
    def __init__(self):
        self.BaseDatos = BaseDatos()

    # Realizamos un listado de clientes (Para comprobar conexion SQL)
    def mostrarClientes(self):
        try:
            # Conexion a la Base de datos
            conexion = self.BaseDatos.abrirConexion() 
            cursor = conexion.cursor()
            # Se verifica que la tabla clientes cuente con informacion
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                # Imprime el listado de clientes
                print("Listado de Clientes Actuales: ")
                for clave,nombre,direccion,correo_electronico,telefono in clientes:
                    print("""
                          clave: {}, nombre Cliente: {}, direccion {}, correo_electronico: {}, telefono: {}
                    """
                          .format(clave, nombre, direccion, correo_electronico, telefono))
            else:
                print("No contamos con clientes actualmente")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los clientes", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
        
    # Agregar un nuevo cliente
    def agregarcliente(self):
        try:
            # Conexion a la Base de datos
            conexion = self.BaseDatos.abrirConexion() 
            cursor = conexion.cursor()
            datos_incorrectos = True
            while datos_incorrectos:
                try:
                    # Solicita los datos a ingresar
                    clave = input("Ingresa la clave del cliente: \n")
                    nombre = input("Ingresa el nombre: \n")
                    direccion = input("Direccion de cliente: \n")
                    correo_electronico = input("Correo electronico: \n")
                    telefono = int(input("Telefono: \n"))
                    datos_incorrectos = False
                except Exception as e:
                    print('Error al capturar un dato: {}'.format(e))
                    print('Intente de nuevo ingresar los datos \n')
                    datos_incorrectos = True
            # Se realiza el insert de la informacion
            valores = (clave, nombre, direccion, correo_electronico, telefono)
            sql = ''' INSERT INTO clientes(clave,nombre,direccion,correo_electronico,telefono)
                    VALUES(?,?,?,?,?) '''                    
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
                self.mostrarClientes()

    # Actualizar un cliente
    def modificarCliente(self):
        try:
            # Conexion a la Base de datos
            conexion = self.BaseDatos.abrirConexion() 
            cursor = conexion.cursor()
            # Realiza una consulta de clientes para ver que existan
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                # Muestra el listado de clientes
                self.mostrarClientes()
                print("----------------------------------")
                # Busca el cliente por clave
                claveCliente = ''
                datos_incorrectos = True
                while datos_incorrectos:
                    try:
                        claveCliente = input("Cual es la clave del cliente a modificar?")
                        datos_incorrectos = False
                    except Exception as e:
                        print('Error al capturar el id del cliente: {}'.format(e))
                        print('Intente de nuevo ingresar el id \n')
                        datos_incorrectos = True
                eCliente = cursor.execute("SELECT * FROM clientes WHERE clave = ?", (claveCliente,))    
                cliente = eCliente.fetchone()
                if cliente :
                    # Se solicita los datos del cliente a modificar
                    datos_incorrectos = True
                    while datos_incorrectos:
                        try:
                            nombre = input("Ingresa el nombre: \n")
                            direccion = input("Direccion de cliente: \n")
                            correo_electronico = input("Correo electronico: \n")
                            telefono = int(input("Telefono: \n"))
                            datos_incorrectos = False
                        except Exception as e:
                            print('Error al capturar un dato: {}'.format(e))
                            print('Intente de nuevo ingresar los datos \n')
                            datos_incorrectos = True
                    # Se realiza el update del cliente a modificar
                    sql = ''' UPDATE clientes SET nombre = ?, direccion = ?, correo_electronico = ?, telefono = ? WHERE clave = ? '''
                    datosCliente = (nombre,direccion,correo_electronico,telefono,claveCliente)
                    cursor.execute(sql,datosCliente)
                    conexion.commit()
                    print("Cliente modificado correctamente")                   
                else:
                    print("No existe el cliente")                   
            else:  
                print("No hay clientes para modificar")
                print("------------------------------------")
            
        except sqlite3.Error as error:
            print('Error al intentar modificar el cliente: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    # Eliminar un cliente
    def eliminarCliente(self):
        try:
            # Conexion a la Base de datos
            conexion = self.BaseDatos.abrirConexion() 
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                # Muestra el listado de clientes                
                self.mostrarClientes()
                print("------------------------------------")
                # Busca un cliente por clave
                claveCliente = ''
                datos_incorrectos = True
                while datos_incorrectos:
                    try:
                        claveCliente = input("Cual es la clave del cliente a eliminar?")
                        datos_incorrectos = False
                    except Exception as e:
                        print('Error al capturar el id del cliente: {}'.format(e))
                        print('Intente de nuevo ingresar el id \n')
                        datos_incorrectos = True                
                eCliente = cursor.execute("SELECT * FROM clientes WHERE clave = ?", (claveCliente,))    
                cliente = eCliente.fetchone()
                if cliente :
                    # Realiza el Delete del cliente
                    sql = ''' DELETE FROM clientes WHERE clave = ? '''
                    cursor.execute(sql,(claveCliente,))
                    conexion.commit()
                    print("Cliente eliminado")                   
                else:
                    print("No existe el cliente con esa clave")                   
            else:  
                print("No hay clientes para eliminar")
                print("------------------------------------")
                
        except sqlite3.Error as error:
            print('Error al intentar eliminar el cliente: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()