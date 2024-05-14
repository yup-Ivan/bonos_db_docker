from utiles.opciones import (
    opcion_1, 
    opcion_2,
    bono_valido,
    )
from utiles.funciones import (
    agregar_producto_cesta, 
    borrar_cesta, 
    crear_factura,
    )
from utiles.conectar import (
    crear_tablas
)

MAX_BONO = 50
bono = "N/A"
descuento = "0"
comprando = True

nombre = input('Introduce tu nombre de usuario: ')

while comprando:

    crear_tablas()

    if bono != "N/A":
        opcion = opcion_2()
    else:
        opcion = opcion_1()

    match opcion:

        case "a":
            
            producto = input('Introduce el nombre del producto: ')
            precio = input('Introduce el precio: ')
            resultado = agregar_producto_cesta(producto, precio)
            print(resultado)

        case "b":

            bono, descuento = bono_valido()

        case "c":

            resultado = crear_factura(nombre, bono, descuento)
            print(resultado)
            resultado = borrar_cesta()
            print(resultado)

            comprando = False
            print(f"\nGracias por tu compra {nombre.upper()}.\n")