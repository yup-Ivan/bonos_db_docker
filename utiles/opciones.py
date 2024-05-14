def opcion_1():
    print("""
    a) Introducir nombre del artículo (texto) y su precio (número decimal).
    b) Introducción del código del bono (número entero de exactamente 8 dígitos) y su descuento (número entero entre 0 y 100)
    c) Finalizar compra.
    """)

    opciones = ["a", "b", "c"]

    while True:
        opcion = input('Introduce una opción: ')
        if opcion in opciones:
            return opcion
        else:
            print('Has introducido una opción invalida.')

def opcion_2():
    print("""
    a) Introducir nombre del artículo (texto) y su precio (número decimal).
    c) Finalizar compra.
    """)

    opciones = ["a", "c"]

    while True:
        opcion = input('Introduce una opción: ')
        if opcion in opciones:
            return opcion
        else:
            print('Has introducido una opción invalida.')

def bono_valido():
    while True:
        bono = input("Introduce el codigo del bono: ")
        descuento = int(input("Introduce el descuento (1 - 100): "))
        if len(bono) == 8:
            if descuento > 0 and descuento <= 100:
                return bono, descuento
            else:
                print("El descuento debe ser de 0 - 100")
        else:
            print("El bono es invalido (debe ser de 8 caracteres).")