from Producto import Producto
from Clientes import Clientes
from Venta import Venta
import requests
import json


def gestion_productos(lista_producto):  # funcion encarga de cumplir con el primer puntogestionar productos

    while True:
        print("Estas en 'Gestion de producto'")
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


            nuevoProducto = Producto(nuevoId, nombre, descripcion, precio, categoria, inventario, carros_compa)
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
def generar_factura(lista_ventas):
    pass
def registrar_ventas(lista_ventas,lista_cliente,lista_producto):
    while True:
        print("Estas en 'Registrar ventas' ")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            cliente_cedula=int(input("Ingresa la cedula del cliente: "))
            cliente=None
            # Verificar si el cliente existe
            for i in lista_cliente:
                if i.cedula == cliente_cedula:  # Si el cliente existe
                    cliente = i
                    break
            
            if cliente is None:  # Si no se encuentra el cliente
                print("El cliente no existe. ¿Deseas agregarlo? si/no: ")
                opcion = input("--> ").lower()
                if opcion == 'si':
                    registrar_cliente(lista_cliente)
                else:
                    print("No se puede continuar sin un cliente. Intente nuevamente.")
                    continue  # Vuelve a pedir la cédula si no se quiere agregar el cliente
            for i in lista_cliente:
                if i.cedula == cliente_cedula: #para asignarle el cliente en cliente
                    cliente = i
                    break
            
            producto_comprado=[]
            cantidades=[]
            while True:
                for idx, producto in enumerate(lista_producto, start=1):
                    print(f"{idx}. ID: {producto.ids} - Nombre: {producto.nombre}")
                seleccion=int(input("Ingresa el numero del producto correspondiente: "))
                if 1 <= seleccion <= len(lista_producto):
                    producto_seleccionado = lista_producto[seleccion - 1]  # se usa seleccion - 1 para obtener el indice correcto
                    print(f"Has seleccionado el producto: {producto_seleccionado.nombre}")
                    cant_producto=int(input("Ingresa la cantidad del producto comprado: "))

                    producto_comprado.append(producto_seleccionado)
                    cantidades.append(cant_producto)

                else:
                    print("Selección inválida. Intente nuevamente.")


            
                salir=input("Deseas seguir agregando?si/no: ").lower()
                if (salir=='no'):
                    break
          #metodos de pago  
            metodo_pago=input("Ingresa el metodo de pago dolares/bolivares: ").lower().replace(" ","")
            metodo_envio=input("Ingrese el metodo del envio: ").lower().replace(" ","")

            nueva_venta=Venta(cliente,metodo_pago,metodo_envio,producto_comprado,cantidades)
            lista_ventas.append(nueva_venta)# lo agrego a la lista de ventas
            print(" ")
            print("Venta Registrada con exito!")
            print(" ")
            nueva_venta.mostrar_desglose()
            print(" ")
        elif(salir=='si'):
            break
def buscar_ventas(lista_ventas):
    pass
def gestion_ventas(lista_ventas,lista_cliente,lista_producto):#funcion encargada de cumplir con el segundo punto del proyecto
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
           registrar_ventas(lista_ventas,lista_cliente,lista_producto)
        elif(opcion==2):
           generar_factura(lista_ventas)
        elif(opcion==3):
            buscar_ventas(lista_ventas)
        else:
            print("Dato invalido")

def registrar_cliente(lista_compradores):
    nombre_cli=input("Ingresar nombre: ")
    try:
        ids=int(input("Ingresar Cédula o RIF: "))
        telf_contacto=""
    except ValueError:
        print("Dato invalido")
    natural_juridico=input("Escribir V (persona natural) J(persona juridica): ").upper().replace(" ", "")
    
    nombre_contacto=""

    email_contacto=""
    
    if natural_juridico=='J':
        nombre_contacto=input("Ingresar nombre del contacto: ")
        telf_contacto=int(input("Ingresar telefono del contacto: "))
        email_contacto=input("Ingresar email del contacto sin agregar '@gmail.com': ")+'@gmail.com'

    email=input("Ingresar correo electronico sin agregar '@gmail.com': ")+'@gmail.com'
    direccion=input("Ingresar direccion: ")
    telefono=int(input("Ingresar telefono: "))
    clientico=Clientes(nombre_cli,ids,email,direccion,telefono,natural_juridico,nombre_contacto,telf_contacto,email_contacto)
    lista_compradores.append(clientico)
    print(" ")
    print("Cliente agregado: ",clientico.nombre,clientico.cedula)

def modificar_cliente(lista_clientes):
    while True:
        print("Estas en 'Gestion de Clientes'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            print("Lista de clientes")
            for i, cliente in enumerate(lista_clientes):
                print(f"{i+1}){cliente.nombre} ID:{cliente.cedula}")

            try:
                eleccion=int(input("Seleccione el cliente correspondiente al numero: "))
                cliente_modificar=lista_clientes[eleccion-1]
            except ValueError:
                print("Seleccion invalida")
                return
            print(f"\nCliente seleccionado: {cliente_modificar}")
            print("¿Qué información deseas modificar?")
            print("1. Nombre")
            print("2. Correo electrónico")
            print("3. Dirección")
            print("4. Teléfono")
            if cliente_modificar.tipo == 'J':  # Si es un cliente jurídico
                print("5. Nombre de contacto")
                print("6. Teléfono de contacto")
                print("7. Correo de contacto")
    
            modificacion = input("Elige una opción: ")
            if (modificacion == '1'):
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                cliente_modificar.nombre = nuevo_nombre
            elif (modificacion == '2'):
                nuevo_email = input("Ingrese el nuevo correo electrónico: ")
                cliente_modificar.correo = nuevo_email
            elif (modificacion == '3'):
                nueva_direccion = input("Ingrese la nueva dirección: ")
                cliente_modificar.direccion_envio = nueva_direccion
            elif (modificacion == '4'):
                try:
                    nuevo_telefono = int(input("Ingrese el nuevo teléfono: "))
                except ValueError:
                    print("Dato invalido")
                cliente_modificar.telefono = nuevo_telefono
            elif (modificacion == '5') and (cliente_modificar.tipo == 'J'):
                nuevo_nombre_contacto = input("Ingrese el nuevo nombre de contacto: ")
                cliente_modificar.nombre_contacto = nuevo_nombre_contacto
            elif (modificacion == '6') and (cliente_modificar.tipo == 'J'):
                try:
                    nuevo_telefono_contacto = int(input("Ingrese el nuevo teléfono de contacto: "))
                except ValueError:
                    print("Dato invalido")
                cliente_modificar.telf_contacto = nuevo_telefono_contacto

            elif (modificacion == '7') and (cliente_modificar.tipo == 'J'):
                nuevo_email_contacto = input("Ingrese el nuevo correo electrónico de contacto: ")
                cliente_modificar.correo_contacto = nuevo_email_contacto
            else:
                print("Opción inválida.")
                return

            print(f"\nCliente modificado: {cliente_modificar}")   
        elif(salir=='si'):
            break
        else:
            print("dato invalido")


def eliminar_cliente(lista_clientes):
    while True:

        print("Estas en 'Eliminar cliente'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            cedula=int(input("Ingresa la cedula del cliente a eliminar: "))
            cliente_eliminar=None
            for i in lista_clientes:
                if i.cedula==cedula:
                    cliente_eliminar=i
            if cliente_eliminar:
                lista_clientes.remove(cliente_eliminar)
                print(f"Cliente con la cedula {cedula} fue eliminado")
            else:
                print("Cliente no encontrado")
        elif(salir=='si'):
            break
        else:
            print("Dato invalido")
def buscar_cliente(lista_cliente):
    while True:

        print("Estas en 'Buscar cliente'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            print("Selecciona el numero correspondiente: ")
            print("""
                  1)Cedula/rif
                  2)Email""")
            opcion=int(input("--> "))
            cliente_buscado=None

            if(opcion==1):
                cedula_buscar=int(input("Ingresa la cedula del cliente a buscar: "))
                for i in lista_cliente:
                    if i.cedula==cedula_buscar:
                        cliente_buscado=i
                        print(cliente_buscado)
                if not cliente_buscado:
                    print("No encontrado")
            elif (opcion==2):
                correo_buscar=input("Ingrese el correo a buscar sin agregar '@gmail.com': ")+'@gmail.com' 
                for i in lista_cliente:
                    if i.correo==correo_buscar:
                        cliente_buscado=i 
                        print(cliente_buscado) 
                if not cliente_buscado:
                    print("No encontrado")    
            elif(opcion!=1 or opcion!=2):
                print("Dato invalido")
        elif (salir=='si'):
            break
        elif(salir!='si' or salir!='no'):
            print("dato invalido")

    
def gestion_clientes(lista_clientes):#funcion encargada de cumplir con el tercer punto del proyecto
    while True:
        print("Estas en 'Gestion de Clientes'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            print("Estas en 'Agregar cliente'")
            print("Seleccione la opcion correspondiente al numero")
            print("""
                  1)Registrar cliente
                  2)Modificar Informacion de un cliente
                  3)Eliminar clientes
                  4)Buscar Clientes
                  """)
            opcion=int(input("--> "))
            if(opcion==1):
                registrar_cliente(lista_clientes)
            elif (opcion==2):
                modificar_cliente(lista_clientes)
            elif (opcion==3):
                eliminar_cliente(lista_clientes)
            elif (opcion==4):
                buscar_cliente(lista_clientes)
        elif(salir=='si'):
            break
        else:
            print("Dato invalido")
def registrar_pago(lista_ventas):
    pass
def buscar_pago(lista_ventas):
    pass

           
def registrar_envios(lista_ventas):
    pass
def buscar_envios(lista_ventas):
    pass
def gestion_envios(lista_ventas,lista_clientes):# funcion encargada de cumplir con el cuaarto punto
    while True:
        print("Estas en 'Gestion de Envios'")
        print("Seleccionar una opcion correspondiente a su numero")
        print("""
            1)Registrar los envíos
            2)Buscar envíos
            
            """)
        opcion=int(input("--> "))
        if (opcion==1):
           registrar_envios(lista_ventas)
        elif(opcion==2):
            buscar_envios(lista_ventas)
        else:
            print("Dato invalido")
def gestion_pagos(lista_ventas):# funcion encargada de cumplir con el cuaarto punto
    while True:
        print("Estas en 'Gestion de Pagos'")
        print("Seleccionar una opcion correspondiente a su numero")
        print("""
            1)Registrar pago
            2)Buscar pago
            
            """)
        opcion=int(input("--> "))
        if (opcion==1):
           registrar_pago(lista_ventas)
        elif(opcion==2):
            buscar_pago(lista_ventas)
        else:
            print("Dato invalido")



def estadisticas():#funcion encargada de cumplir con el sexto punto del
    pass

def main():  # funcion encargada de la gestion de menu del programa
    lista_producto = consumoAPI()
    lista_clientes=cargar_clientes()    
    lista_ventas=cargar_ventas()
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
                gestion_ventas(lista_ventas,lista_clientes,lista_producto)
            elif(respuesta==3):
                gestion_clientes(lista_clientes)
            elif (respuesta==4):
                pass
            elif (respuesta==5):
                pass
            elif(respuesta==6):
                pass
                
            elif (respuesta == 7):
                guardar_producto_txt(lista_producto)
                guardar_clientes_txt(lista_clientes)
                print("Adios :)")
                break

        except ValueError:
            print("Ingrese un numero valido")

def cargar_ventas():
    try:
        with open('venta.txt','r',encoding='UTF-8') as archivo:
            venta_data=json.load(archivo)
            lista_ventas=[Venta(**venta_data) for venta_data in venta_data]
            return lista_ventas
    except FileNotFoundError:
        print("No se encontró el archivo de clientes. Se iniciará con una lista vacía.")
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo de clientes. Se iniciará con una lista vacía.")
        return []
def cargar_clientes():
    try:
        with open('clientes.txt', 'r', encoding='UTF-8') as archivo:
            clientes_data = json.load(archivo)
            # Convertir cada diccionario en una instancia de la clase Clientes
            lista_clientes = [Clientes(**cliente_data) for cliente_data in clientes_data]
            return lista_clientes
    except FileNotFoundError:
        print("No se encontró el archivo de clientes. Se iniciará con una lista vacía.")
        return []  # Devuelve una lista vacía si el archivo no existe
    except json.JSONDecodeError:
        print("Error al leer el archivo de clientes. Se iniciará con una lista vacía.")
        return []  # Devuelve una lista vacía si hay un error en el formato JSON


def guardar_clientes_txt(lista_clientes):
    with open('clientes.txt','w',encoding='UTF-8')as archivo:
        clientes_guardar=[cliente.__dict__ for cliente in lista_clientes]
        json.dump(clientes_guardar,archivo,indent=4,ensure_ascii=False)

#__dict__ metodo magico que devuelve un diccionario con los atributos del objeto

def guardar_producto_txt(lista_producto):
    with open('estado.txt', 'w', encoding='UTF-8') as archivo:
        # Convertir cada objeto Producto a diccionario y guardarlo
        productos_guardar = [producto.__dict__ for producto in lista_producto]
        json.dump(productos_guardar, archivo, indent=4, ensure_ascii=False)


main()
