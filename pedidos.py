# Avance 2 - Modulos y Clases / Avance 3 - Creacion de funciones
import sqlite3
from clientes import Cliente
from menu import Producto
from BaseDatos import BaseDatos

# Creacion de la clase Pedido
class Pedido:
        # Inicializar la BaseDatoe
    def __init__(self):
        self.BaseDatos = BaseDatos()

    # Realizamos un listado de pedidos (Para comprobar conexion SQL)
    def mostrarPedidos(self):
        try:
            # Conexion a la Base de datos
            conexion = self.BaseDatos.abrirConexion() 
            cursor = conexion.cursor()
            # Obtiene el listado de pedidos si es que existen pedidos
            cursor.execute("SELECT * FROM pedido")     
            pedidos = cursor.fetchall()
            if len(pedidos) > 0:
                print("Listado de Pedidos Actuales: ")
                for pedido,cliente,producto,precio in pedidos:
                    print("""
                          pedido: {}, cliente: {}, producto {}, precio: {}
                    """
                          .format(pedido,cliente,producto,precio))
            else:
                print("No se cuenta con pedidos actualmente")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los pedidos", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    # Realizamos la creacion de un nuevo pedido
    def agregarPedido(self):
        menu = Producto()
        cliente = Cliente()
        try:
            # Conexion a la base de datos
            conexion = self.BaseDatos.abrirConexion() 
            cursor = conexion.cursor()
            # Realiza la muestra de los Clientes
            cliente.mostrarClientes()                 
            # Se realiza la busqueda del cliente en base a la clave ingresada
            claveCliente = ''
            datos_incorrectos = True
            while datos_incorrectos:
                try:
                    claveCliente = input("Cliente que realiza el pedido: ")
                    datos_incorrectos = False
                except Exception as e:
                    print('Error al capturar el id del cliente: {}'.format(e))
                    print('Intente de nuevo ingresar el id \n')
                    datos_incorrectos = True
            # Guarda el nombre del cliente
            eCliente = cursor.execute("SELECT nombre FROM clientes WHERE clave = ?", (claveCliente,))    
            cliente_nombre = eCliente.fetchone()[0]
            if cliente_nombre :
                # Se realiza la busqueda de los productos hasta el momento
                menu.mostrarProductos()
                claveProducto = ''
                datos_incorrectos = True
                while datos_incorrectos:
                    try:
                        claveProducto = input("Cual es el producto que requiere: ")
                        datos_incorrectos = False
                    except Exception as e:
                        print('Error al capturar el id del cliente: {}'.format(e))
                        print('Intente de nuevo ingresar el id \n')
                        datos_incorrectos = True
                
                # Guarda el nombre y precio del producto
                cursor.execute("SELECT nombre, precio FROM menu WHERE clave = ?", (claveProducto,))
                producto_nombre, precio_unitario = cursor.fetchone()
                if producto_nombre :
                    # Se realiza la solicitud de la cantidad ha pedir para hacer el calculo
                    unidades = int(input("Ingrese la cantidad de unidades a solicitar: "))
                    costo_total = precio_unitario * unidades

                    producto_nombre = str(unidades) + ' ' + producto_nombre
                    # Se realiza el guardado y se imprime la informacion
                    valores = (cliente_nombre, producto_nombre, costo_total)
                    sql = ''' INSERT INTO pedido(cliente,producto,precio)
                            VALUES(?,?,?) '''
                            
                    cursor.execute(sql,valores)
                    conexion.commit()
                    print("Datos guardados correctamente")  
                    print("----------------------------------")
                    print("El costo total de", producto_nombre , "es: $",costo_total, "")
                    print("----------------------------------")
                    print("Se imprime el ticket de compra")
                    # Se imprime en ticket
                    archivo = open('Ticket de Pedido.txt', 'w')

                    archivo.write(cliente_nombre + " ha realizado el pedido de\n"+ 
                                  producto_nombre + "\n" + 
                                  "dando un total de: $" + str(costo_total))
                    archivo.close()
                else:
                    print('No se localizo el producto')              
            else:
                print("No existe el cliente")
        except sqlite3.Error as error:
            print('Error al querer agregar un pedido: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    # Se realiza la cancelacion de un pedido (Se elimina)
    def cancelarPedido(self):
        try:
            # Conexion a la Base de datos
            conexion = self.BaseDatos.abrirConexion() 
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM pedido")     
            pedidos = cursor.fetchall()
            if len(pedidos) > 0:
                # Muestra el listado de Pedidos                
                self.mostrarPedidos()
                print("------------------------------------")
                # Busca un pedido por clave
                idPedido = ''
                datos_incorrectos = True
                while datos_incorrectos:
                    try:
                        idPedido = input("Cual es el pedido a eliminar?")
                        datos_incorrectos = False
                    except Exception as e:
                        print('Error al capturar el id del pedido: {}'.format(e))
                        print('Intente de nuevo ingresar el id \n')
                        datos_incorrectos = True
                
                ePedido = cursor.execute("SELECT * FROM pedido WHERE pedido = ?", (idPedido,))    
                pedido = ePedido.fetchone()
                if pedido :
                    # Realiza el Delete del pedido
                    sql = ''' DELETE FROM pedido WHERE pedido = ? '''
                    cursor.execute(sql,(idPedido,))
                    conexion.commit()
                    print("Pedido cancelado")                   
                else:
                    print("No existe el pedido con esa clave")                   
            else:  
                print("No hay pedidos para cancelar")
                print("------------------------------------")
                
        except sqlite3.Error as error:
            print('Error al intentar cancelar el pedido: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()