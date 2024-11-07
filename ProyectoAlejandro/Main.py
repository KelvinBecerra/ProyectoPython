from Producto import Producto
import requests
import json


def gestion_productos():

    while True:
        """funcion encargada de mostrar las opciones del primer modulo"""
        print("Estas en Gestion de producto")
        print("Seleccione la opcion correspondiente al numero")
        print("""
            1)Agregar Producto
            2)Buscar producto
            3)Modificar producto
            4)Eliminar producto
            5)Regresar""")
        opcion = int(input("--> "))
        if (opcion == 1):
            agregar_producto()
        elif (opcion == 2):
            print("mostrar opcion 2")
        elif (opcion == 3):
            print("mostrar opcion 2")
        elif (opcion == 4):
            print("mostrar opcion 2")
        elif (opcion == 5):
            return


def agregar_producto():

    while True:

        print("ya estas en agregar producto")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'si'):
            break
#funcion encargada de consumir la api, gestionarla con un formato tipo json

def consumoAPI():
    url="https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"
    try:
        obtencion=requests.get(url,timeout=10)
        obtencion.raise_for_status()
        datos=obtencion.json()
        #permite abrir el archivo txt y guardar una escritura del tipo json
        #en el archivo 'estado.txt' como archivo
        #teniendo una indentacion de 4 espacios
        #se especifica utf8 porque es el que cubre la mayoria de los estandares de caracteres
        with open('estado.txt',"w",encoding="UTF-8") as archivo:
            json.dump(datos,archivo,indent=4)
            
    except requests.exceptions.Timeout:
        print("Tiempo de espera terminado")
    except requests.exceptions.RequestException as e:
        print("Error de tipo: ",e)

 

def main():
    consumoAPI()
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
                gestion_productos()
            elif (respuesta == 7):
                print("Adios :)")
                break

        except ValueError:
            print("Ingrese un numero valido")


main()
