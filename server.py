# Avance 4 - Consulta de Ticktes a traves de Flask
# Se realizara dos templates, uno donde muestre el listado de pedidos y el segundo se mostrara el pedido seleccionado

from flask import Flask, render_template
import sqlite3 
from sqlite3 import OperationalError

app = Flask(__name__, template_folder="templates")


# Creacion de la/las Rutas
@app.route('/')
def consultarTickets():
    # return "Se realiza la consulta de tickets"
    encabezado_pagina = "Happy Burguer"
    titulo_pagina = "Lista de pedidos"
    # Se genera la conexion con la base de datos
    try:
        # Conexion a la Base de datos
        conexion = sqlite3.connect('HappyBurguerBD.db') 
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pedido")     
        pedidos = cursor.fetchall()
        if len(pedidos) > 0:
            return render_template("index.html", 
                        encabezado_pagina = encabezado_pagina, 
                        titulo_pagina = titulo_pagina,
                        pedidos = pedidos)
        else:
           return render_template('Error.html')
    except (sqlite3.Error, OperationalError) as error:
        return "Error al mostrar los pedidos: {}".format(error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()  


@app.route('/pedidos/pedido/<id>')  
def consultarTicket(id):
    # return "Se realiza la consulta de tickets"
    encabezado_pagina = "Happy Burguer"
    # Se genera la conexion con la base de datos
    try:
        # Conexion a la Base de datos
        conexion = sqlite3.connect('HappyBurguerBD.db') 
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pedido WHERE pedido = ?", (id,))    
        pedido, cliente, producto, precio = cursor.fetchone()
        if pedido:
            titulo_pagina = "Pedido No." + str(id) + " a nombre de " + cliente
            return render_template("datosPedido.html", 
                        encabezado_pagina = encabezado_pagina, 
                        titulo_pagina = titulo_pagina,
                        pedido = pedido,
                        cliente = cliente,
                        producto = producto, 
                        precio = precio)
        else:
           return render_template('Error.html')
    except (sqlite3.Error, OperationalError) as error:
        return "Error al mostrar los pedidos: {}".format(error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()  
