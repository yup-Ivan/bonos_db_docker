from utiles.opciones import (
    opcion_1, 
    opcion_2,
    bono_valido,
    )
from utiles.models import Funcionalidades

MAX_BONO = 50
bono = "N/A"
descuento = "0"
comprando = True

nombre = input('Introduce tu nombre de usuario: ')

while comprando:

    gestor = Funcionalidades()

    gestor.crear_tablas()

    if bono != "N/A":
        opcion = opcion_2()
    else:
        opcion = opcion_1()

    match opcion:

        case "a":
            
            producto = input('Introduce el nombre del producto: ')
            precio = input('Introduce el precio: ')
            resultado = gestor.actualizar_cesta(producto, precio)
            print(resultado)

        case "b":

            bono, descuento = bono_valido()

        case "c":

            resultado = gestor.crear_factura(nombre, bono, descuento)
            print(resultado)
            resultado = gestor.borrar_cesta()
            print(resultado)

            comprando = False
            print(f"\nGracias por tu compra {nombre.upper()}.\n")