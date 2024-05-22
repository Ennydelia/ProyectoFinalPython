# Programación avanzada con Python 
Enedelia Guadalupe Alanis Gómez

## Proyecto final
Descripcion del proyecto
Happy Burger, franquicia de venta de hamburguesas, ha decidido implementar un programa en Python basado en consola para llevar la operación de pedidos de sus restaurantes de franquicia, de igual modo, el programa contará con una interfaz web para consultar pedidos.

Para ello, el programa considera tener un directorio de clientes, un menú de productos y un registro detallado de pedidos.

### Avances del proyecto

 **1. Avance No. 1** 
 Se realiza la definición inicial del proyecto, creando un archivo main.py en el cual se contara con el menú inicial del sistema, dando la bienvenida al portal, y preguntando por la opción que desea realizar, en caso de que se haya seleccionado la opción pedido, pedirá escribir el producto, el precio y la cantidad a solicitar, para posteriormente realizar el calculo y mandar una respuesta de lo solicitado. Este avance se realiza en consola.

 **2. Avance No. 2**
Durante este avance, se fueron creando los archivos para cada una de las opciones del menú (pedidos, clientes y menú), se fueron definiendo las funciones principales de crear, actualizar y eliminar. Para el caso de pedidos, se crearon dos funciones (crear y cancelar). Dichas funciones no contaron con la funcionalidad como tal, simplemente se fueron creando de manera que podamos tenerlas contempladas para la opción del menú. De igual manera en el menú, se definieron las opciones de lo que desea hacer en caso que entre a alguna de las opciones mencionadas, creando una alerta llamada: Usted ha seleccionado  y el nombre de la selección. Todo esto se imprime en consola.

 **3. Avance No. 3**
A partir de aquí se creo una base de datos llamada HappyBurguer, en el cual estarán alojadas las tablas de pedido, menú y cliente. Adicional se creo un nuevo archivo llamado BasesDatos.py en el cual se realiza la creación de las tablas, a su vez se manda a llamar la conexión de la base de datos.
Adicional, se crearon los procesos de las funciones realizadas anteriormente en cada una de las clases anteriores, llamando a la conexión de la BD desde el archivo BasesDatos.py y realizando la estructura correspondiente de cada función.
Para el tema de pedidos, al momento de realizar la función de crear un pedido  solicitara los temas como la cantidad y se realiza la funcionalidad que se hizo en el avance uno. Al final se manda a imprimir el ticket en un archivo .txt y se imprime en consola el resultado del ticket.

 **4. Avance No. 4**
 Para este ultimo avance, se utilizara la herramienta de Flask, donde se mostrara el listado de los pedidos que han sido creados hasta el momento, a su vez, en ese listado se encontrara un link, para ver a detalle los datos del pedido generado.