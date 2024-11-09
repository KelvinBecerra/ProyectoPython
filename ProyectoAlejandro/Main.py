from Producto import Producto
from Cliente import Cliente

import requests
import json


def gestion_productos(lista_producto):  # funcion encarga de cumplir con el primer puntogestionar productos

    while True:
        print("Estas en Gestion de producto")
        print("Seleccione la opcion correspondiente al numero")
        print("""
            1)Agregar Producto
            2)Buscar producto
            3)Modificar producto
            4)Eliminar producto
            5)Regresar
              """)
        opcion = int(input("--> "))
        if (opcion == 1):
            agregar_producto(lista_producto)
        elif (opcion == 2):
            buscar_producto(lista_producto)
        elif (opcion == 3):
            modificar_producto(lista_producto)
        elif (opcion == 4):
            eliminar_producto(lista_producto)
        elif (opcion == 5):
            return
def eliminar_producto(lista_producto):
     while True:
        print('-'*5,"Estas en 'Eliminar producto'", '-'*5)
        salir = input("Deseas eliminar un producto? si/no: ").lower().replace(" ","")
        producto_eliminar=None
        if (salir == 'si'):
            nombre=input("Ingresa el nombre del producto a eliminar: ").lower().replace(" ","")
            
            for producto in lista_producto:
                if (producto.nombre.lower().replace(" ","")==nombre):
                    producto_eliminar=producto
                    break
            if producto_eliminar:
                lista_producto.remove(producto_eliminar)
                print(f"Producto '{producto.nombre}' eliminado correctamente.")
            else:
                print("Producto no encontrado.")
            
        elif(salir=='no'):
            break
        else:
            print("Ingresar si o no")

def modificar_producto(lista_producto):
    while True:
        print('-'*5,"Estas en 'Modificar producto'", '-'*5)
        salir = input("Deseas modificar un producto? si/no: ").lower()
        if (salir == 'si'):
            nombre=input("Ingrese el nombre del producto a modificar: ").lower().replace(" ","")
            lista_nombres_nombre_buscando=[producto for producto in lista_producto if producto.nombre.lower().replace(" ","")==nombre ]
            if not lista_nombres_nombre_buscando:
                print("sin resultados")
            else:
                print("Que deseas modificar del producto?")
                print("1)Nombre\n2)Descripcion\n3)Precio\n4)Categoria\n5)Cantidad\n6)Carros Compatibles")
                modificacion=input("--> ")
                if(modificacion=="1"):
                    for i in lista_nombres_nombre_buscando:
                        nombre_nuevo=input("Ingresa el nombre nuevo: ").lower()
                        i.nombre=nombre_nuevo
                        print("Modificado: ",i)
                elif (modificacion=='2'):
                    for i in lista_nombres_nombre_buscando:
                        descripcion_nueva=input("Ingrese la nueva descripcion: ")
                        i.descripcion=descripcion_nueva
                        print("Modificado: ",i)
                elif (modificacion=='3'):

                    for i in lista_nombres_nombre_buscando:
                        try:
                            precio_nuevo=int(input("Ingresar el nuevo precio:$"))
                            i.precio=precio_nuevo
                            print("Modificado: ",i)
                        except ValueError:
                            print("Ingresar n valor numerico")
                elif (modificacion=='4'):
                    for i in lista_nombres_nombre_buscando:
                        categoria_nueva=input("Ingresar la nueva categoria: ")
                        i.categoria=categoria_nueva
                        print("Modificado: ",i)
                elif (modificacion=='5'):
                    for i in lista_nombres_nombre_buscando:
                        try:
                            cantidad=int(input("Ingresa la nueva cantidad del producto: "))
                            i.inventario=cantidad
                            print("Modificado: ",i)
                        except ValueError:
                            print("Ingresar un valor numerico")
                elif (modificacion == '6'):
                    for producto in lista_nombres_nombre_buscando:
                        carros_compatibles = []
                        while True:
                            vehiculo = input("Ingrese un modelo de carro compatible (o 'listo' para terminar): ")
                            if vehiculo.lower() == 'listo':
                                break
                            carros_compatibles.append(vehiculo)
                        producto.carros_compa = carros_compatibles
                        print("Modificado: ", producto)
        elif (salir=='no'):#para salir del bucle
            break
        else:
            print("Dato invalido")
def buscar_producto(lista_producto):
    while True:
        print('-'*5, "Estas en 'Buscar producto'", '-'*5)
        salir = input("Deseas buscar un producto? si/no: ").lower()
        if (salir == 'si'):
            print("Selecciona la opcion de busqueda con el numero respectivo")
            print(f"""
            1)Categoria
            2)Precio
            3)Nombre
            4)Disponibilidad
            """)
            opcion = int(input("--> "))
            if (opcion == 1):
               #se crea una lista apartir de las categorias de los productos sin repetirlas
               categorias_unicas={producto.categoria for producto in lista_producto}
               print(f"Categorias disponibles:{categorias_unicas}")

               categorias=list(categorias_unicas)
               #se enumeran lascategorias para que el usuario las elija con respecto al numerpo
               for indice,categoria in enumerate(categorias,1):
                   print(f"{indice}) {categoria}")
                
                #se resta 1 a la entrada del usuario porque en la lista los indices comienzan desde el 0
               opcionUser=int(input("Seleccione el numero correspondiente a la categoria: "))-1
               categoria_seleccionada=categorias[opcionUser]
               #se crea una lista de los productos con sus detalles mientras sean iguales a la categoria elegida
               producto_elegido=[producto for producto in lista_producto if producto.categoria==categoria_seleccionada]
               print(f"Lista de productos de la categoria {categoria_seleccionada}")
               for i in producto_elegido:
                   print(i,"\n")
               
            elif (opcion==2):#por precio
                minimo=int(input("Ingresa el precio minimo que deseas buscar: "))
                maximo=int(input("Ingresa el precio maximo que deseas buscar: "))
                lista_precio=[producto for producto in lista_producto if minimo<producto.precio<maximo ]
                print("Estos son los productos que estan en el rango seleccionado: ")
                for i in lista_precio:
                    print(i,"\n")

            elif(opcion==3):#por nombre
                nombre=input("Ingrese el nombre del producto: ").lower().replace(" ","")
                lista_nombres_nombre_buscando=[producto for producto in lista_producto if producto.nombre.lower().replace(" ","")==nombre ]
                if not lista_nombres_nombre_buscando:
                    print("sin resultados")
                else:
                    print("Lista de productos con el nombre ",nombre)
                    for i in lista_nombres_nombre_buscando:
                        print(i,"\n")

                
            elif (opcion==4):#por disponibilidad
                cantidad_min=int(input("Ingresar la cantidad minima de los productos: "))
                cantidad_max=int(input("Ingresar la cantidad maxima de los productos: "))
                lista_productos_disponibilidad=[producto for producto in lista_producto if cantidad_min<producto.inventario<cantidad_max]
                for i in lista_productos_disponibilidad:

                    print(i,"\n")
            else:
                print("selecciona un numero correspondiente a las opciones")
        elif (salir=='no'):
            break
        else:
            print("Seleccionar una respuesta entre si/no")

           
def agregar_producto(lista_producto):#funcion encargada de agregar productos a lista de productos

    while True:

        print("Estas en 'Agregar producto'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            nombre = input("Ingresa el nombre del producto: ")
            descripcion = input("Ingresa una descripcion del producto: ")
            precio = int(input("Ingresa el precio en numeros del producto: $"))
            categoria = input("Categoria ej: aceite,filtro,empacadura etc: ")
            inventario = int(input("Ingresa las cantidades: "))

            modelo = ""
            carros_compa = []
            while True:
                respuesta = input(
                    "Deseas agregar algun modelo al cual aplica el repuesto? si/no: ").lower()
                if (respuesta == 'si'):
                    modelo = input("Ingresa los modelos a los cuales aplica: ")
                    carros_compa.append(modelo)
                elif (respuesta == "no"):
                    break
                else:
                    print("Por favor, ingresa 'si' o 'no': ")

                if (modelo == ''):
                    modelo = "N/A"

           
            maxId=0
            for producto in lista_producto:
                
                if (producto.ids)>maxId:
                    maxId=producto.ids
            nuevoId=maxId+1


            nuevoProducto = Producto(
                nuevoId, nombre, descripcion, precio, categoria, inventario, carros_compa)
            lista_producto.append(nuevoProducto)
            print(f"Producto agregado: {nuevoProducto}")
        elif( salir=='si'):
            break
        else:
            print("Ingresa 'si' o 'no'")
           


def consumoAPI():  # funcion encargada de consumir la api, gestionarla a un objeto
    lista_producto = []
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"
    try:
        obtencion = requests.get(url, timeout=10)
        obtencion.raise_for_status()
        datos = obtencion.json()
        for item in datos:
            producto = Producto(
                ids=item['id'],
                nombre=item['name'],
                descripcion=item['description'],
                precio=item['price'],
                categoria=item['category'],
                inventario=item['inventory'],
                carros_compa=item['compatible_vehicles']
            )
            lista_producto.append(producto)
        return lista_producto

    except requests.exceptions.RequestException as e:
        print("Error de tipo: ", e)
        return []

def gestion_ventas():#funcion encargada de cumplir con el segundo punto del proyecto
   while True:
       print("Estas en 'Gestion de Ventas'")
       print("Seleccionar una opcion correspondiente a su numero")
       print("""
             1)Registrar Venta
             2)Generar factura
             3)Buscar ventas
             """)
       opcion=int(input("--> "))
       if (opcion==1):
           pass
           
def registrar_cliente():
    nombre=input("Ingresar nombre/apellido/razon social: ")

    natural_juridico=input("Escribir V (persona natural) J(persona juridica): ").lower().replace(" ","")
    nombre_contacto=""
    telf_contacto=""
    email_contacto=""
    if natural_juridico=='j':
        nombre_contacto=input("Ingresar nombre del contacto: ")
        telf_contacto=int(input("Ingresar telefono del contacto: "))
        email_contacto=input("Ingresar email del contacto: ")

    email=input("Ingresar correo electronico: ")
    direccion=input("Ingresar direccion: ")
    telefono=int(input("Ingresar telefono: "))
    clientico=Cliente
def registrarVenta():
    while True:

        print("Estas en 'Registrar venta'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            cedula=int(input("Cliente que realizo la venta"))
            producto_comprado=input("Ingrese el nombre del producto comprado: ").lower()
            cant_produc=int(input("Ingresar la cantidad del producto: "))
            metodo_pago=input("Metodo de pago? PagoMovil/efectivo/punto: " ).lower()
            metodo_envio=input("Ingrese el metodo del envio: ").lower()

        elif(salir=='si'):
            break
        else:
            print("Dato invalido")

def gestion_clientes():#funcion encargada de cumplir con el tercer punto del proyecto
    pass 

def gestion_pagos():# funcion encargada de cumplir con el cuaarto punto
    pass

def gestion_envios():#funcion encargada de cumplir con el quinto punto del programa
    pass

def estadisticas():#funcion encargada de cumplir con el sexto punto del
    pass
def main():  # funcion encargada de la gestion de menu del programa
    lista_producto = consumoAPI()

    while True:
        print("-"*10, "Bienvenido a la tienda de productos", "-"*10)
        print("Selecciona una de las opciones con el numero correspondiente:")
        print("""
                1)Gestion de proyectos
                2)Gestion de ventas
                3)Gestion de clientes
                4)Gestion de pagos
                5)Gestion de envios
                6)Estadisticas
                7)Salir""")
        try:
            respuesta = int(input("--> "))

            if (respuesta == 1):
                gestion_productos(lista_producto)
            elif (respuesta==2):
                gestion_ventas()
            elif (respuesta == 7):
                guardar_txt(lista_producto)
                print("Adios :)")
                break

        except ValueError:
            print("Ingrese un numero valido")


def guardar_txt(lista_producto):
    with open('estado.txt', 'w', encoding='UTF-8') as archivo:
        # Convertir cada objeto Producto a diccionario y guardarlo
        productos_guardar = [producto.__dict__ for producto in lista_producto]
        json.dump(productos_guardar, archivo, indent=4, ensure_ascii=False)


main()
