from utiles.conectar import crear_conexion

def agregar_producto_cesta(producto, precio):

    try:

        conex = crear_conexion()            
        cursor = conex.cursor()
        
        insert_query = "INSERT INTO cesta (nombre_producto, precio) VALUES (%s, %s)"
        data = (producto, float(precio)) 
        cursor.execute(insert_query, data)
        
        conex.commit()
        cursor.close()
        conex.close()

        return "Se ha añadido el producto."
    
    except Exception as e:

        return f"Ha ocurrido un error al añadir el producto. {e}"
    
def borrar_cesta():
    try:

        conex = crear_conexion()            
        cursor = conex.cursor()
        
        insert_query = "delete from cesta;"
        cursor.execute(insert_query)
        
        conex.commit()
        cursor.close()
        conex.close()

        return "Se ha limpiado la cesta."
    
    except:

        return "Ha ocurrido un error al eliminar la cesta."
    
def crear_factura(nombre_cliente, bono, descuento):
    try:
        conex = crear_conexion()            
        cursor = conex.cursor()

        insert_sumprecio = "SELECT SUM(precio) FROM cesta;"
        cursor.execute(insert_sumprecio)
        
        total_sin_descuento = cursor.fetchone()[0]
        print(total_sin_descuento)
        print(type(total_sin_descuento))

        if total_sin_descuento is None:
            total_sin_descuento = 0.00
        else:
            total_sin_descuento = float(total_sin_descuento)

        descuento = float(descuento)

        descuento_aplicado = total_sin_descuento * descuento / 100 
        total_final = total_sin_descuento - descuento_aplicado

        insert_query = "INSERT INTO factura (nombre_cliente, bono, descuento, total_sin_descuento, total_final) VALUES (%s, %s, %s, %s, %s)"
        data = (nombre_cliente, bono, descuento, total_sin_descuento, total_final)
        cursor.execute(insert_query, data)
        
        conex.commit()
        cursor.close()
        conex.close()

        return "Se ha creado tu factura."
    
    except Exception as e:
        return "Ha ocurrido un error al crear una factura."