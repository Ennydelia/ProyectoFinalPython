""" Proyecto Final Python 
    Enedelia Guadalupe Alanis Gómez

    Descripcion del proyecto
    Happy Burger, franquicia de venta de hamburguesas, ha decidido implementar un programa en Python basado en 
    consola para llevar la operación de pedidos de sus restaurantes de franquicia, de igual modo, el programa contará 
    con una interfaz web para consultar pedidos. 
    Para ello, el programa considera tener un directorio de clientes, un menú de productos y un registro 
    detallado de pedidos
"""

# Importacion de los modulos y clases
from clientes import Cliente
from pedidos import Pedido
from menu import Producto

""" Avance 1 - Condicionales del menu """
class HappyBurger:
    def __init__(self):
        self.iniciarAplicacion()

    def iniciarAplicacion(self):        
        def pedidos():
            menu = Pedido ()
            print("------------------------------------")
            """ En esta seccion, se busca el que el usuario pueda agregar o cancelar un pedido 
            ademas tambien podra ver en la consola un listado de pedidos generados """
            print("Seccion de Pedidos, que desea hacer: ")
            while True:
                print("Seleccione una opción:")
                print(""" 
                1. Crear un nuevo pedido
                2. Cancelar pedido
                3. Mostrar los pedidos
                4. Regresar al menu principal
                """)

                opcionPedido = input("Selecciona una opcion: ")
                if opcionPedido == "1":
                    """ Se crea un nuevo pedido """
                    print('Agregar nuevo pedido')
                    print("------------------------------------")
                    """ Realiza el proceso para realizar un pedido """
                    menu.agregarPedido()
                elif opcionPedido == "2":
                    print('Cancelar Pedido')
                    print("------------------------------------")           
                    """ Se realiza la funcion donde muestra los pedidos y pide cancelar 1 """
                    menu.cancelarPedido()
                elif opcionPedido == "3":
                    print('Mostrar Pedidos')
                    print("------------------------------------")           
                    """ Se realiza la funcion donde muestra los pedidos"""
                    menu.mostrarPedidos()
                elif opcionPedido == "4":
                    print('Volver al menu principal')
                    print("------------------------------------")
                    return              
                else:
                    print("Opcion no encontrada en el menu")
        """ Calcular el costo de un solo producto, solicitanto: nombre, precios y unidades """
        """ Se comenta funcion ya que se paso al modulo del producto
            print("------------------------------------")
            print("Favor de ingresar el pedido")
            nombreprod = input("Ingrese el nombre del producto: ")
            precioprod = float(input("Ingrese el precio del producto: "))
            unidades = int(input("Ingrese la cantidad de unidades a solicitar: "))
            costo_total = precioprod * unidades
            print("El costo total de", unidades, nombreprod , "es: $",costo_total, "")
            print("------------------------------------")
            return"""
        
        """ Opcion del menu de producto """
        def menu():
            producto = Producto()
            print("------------------------------------")
            """ En este modulo se busca que el usuario pueda realizar la Alta/Baja/Modificacion 
            de los productos que estan en el menu, adicional que pueda ver los productos existentes"""
            print("Bienvenido al menu, que desea hacer: ")
            while True:
                print("Seleccione una opción:")
                print(""" 
                1. Agregar producto
                2. Actualizar producto
                3. Eliminar producto
                4. Mostrar el Menu
                5. Volver al menu
                """)

                opcionProductos = input("Selecciona una opcion: ")
                if opcionProductos == "1":
                    """ Agregar un producto """
                    print('Ha seleccionado agregar un producto')
                    print("------------------------------------")
                    producto.agregarProducto()
                    """ Actualizar un producto """
                elif opcionProductos == "2":
                    print('Ha seleccionado actualizar un producto')
                    print("------------------------------------")
                    producto.modificarProducto()
                elif opcionProductos == "3":
                    """ Eliminar un producto """
                    print('Ha seleccionado eliminar un producto')
                    print("------------------------------------")
                    producto.eliminarProducto()
                elif opcionProductos == "4":
                    """ Mostrar los productos """
                    print('Mostrar productos')
                    print("------------------------------------")
                    producto.mostrarProductos()
                elif opcionProductos == "5":
                    print('Volver al menu principal')
                    print("------------------------------------")
                    return              
                else:
                    print("Opcion no encontrada en el menu")

        """ Menu para clientes """
        def clientes():
            cliente = Cliente()
            print("------------------------------------")
            """ Se realiza la funcion para el agregar/actualizar/eliminar clientes """
            print("Bienvenido al listado de clientes, que desea hacer:")
            while True:                
                print("Seleccione una opción:")
                print(""" 
                1. Agregar cliente
                2. Actualizar cliente
                3. Eliminar cliente
                4. Mostrar clientes
                5. Volver al menu
                """)
                opcionClientes = input("Selecciona una opcion: ")
                if opcionClientes == "1":
                    """ Agregar un cliente """
                    print('Ha seleccionado agregar un cliente')
                    print("------------------------------------")
                    cliente.agregarcliente()        
                    print("------------------------------------")           
                    """  Actualizar un cliente """
                elif opcionClientes == "2":
                    print('Ha seleccionado actualizar un cliente')
                    print("------------------------------------")
                    """ Se inicializa la opcion para actualizar un cliente """
                    cliente.modificarCliente()
                    print("------------------------------------")
                elif opcionClientes == "3":
                    """ Eliminar un cliente """
                    print('Ha seleccionado eliminar un cliente')
                    print("------------------------------------")
                    """ Se inicializa la opcion para eliminar un cliente """
                    cliente.eliminarCliente()
                    print("------------------------------------")
                elif opcionClientes == "4":
                    """ Muestra el listado de clientes """
                    print('Listado de clientes')
                    print("------------------------------------")
                    cliente.mostrarClientes()
                    print("------------------------------------")                    
                elif opcionClientes == "5":
                    print('Volver al menu principal')
                    print("------------------------------------")
                    return              
                else:
                    print("Opcion no encontrada en el menu")

        print("------------------------------------")
        print("Bienvenido a Happy Burguer")
        salir_programa = False
        while not salir_programa:
            print("Donde desea entrar")
            print(""" 
                a.- Pedidos
                b.- Clientes
                c.- Menú
                d.- Salir del programa
                """)
            opcion = input("Indicar una opcion ")
            if opcion == "a":
                # Se selecciona un menu de opciones de Pedidos
                print("Bienvenido a la seccion de Pedidos")
                pedidos()
            elif opcion == "b":
                # Se selecciona un menu de opciones de Clientes
                print("Bienvenido a la seccion de Clientes")
                clientes()
            elif opcion == "c":
                # Se selecciona un menu de opciones de Menu
                print("Este es el Menu de Happy Burguer")
                menu()
            elif opcion == "d":
                print("Gracias por pasar a Happy Burguer, hasta pronto")
                salir_programa = True
                
sistema_inventario = HappyBurger()