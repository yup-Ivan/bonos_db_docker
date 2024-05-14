import mysql.connector
from mysql.connector import Error

def crear_conexion():

    config = {
        'host': 'db',
        'port': '3306',
        'user': 'bonoman',
        'password': 'ivan',
        'database': 'bonos'
    }

    try:
        conex = mysql.connector.connect(**config)
        if conex.is_connected():
            print("Estas conectado.")
            return conex
    except mysql.connector.Error as error:
        print(f'Error: {error}')
        return False
    
def crear_tablas():
    conex = crear_conexion()            
    cursor = conex.cursor()
    datos_injectar = [
        """
        CREATE TABLE IF NOT EXISTS bonos.cesta (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_producto VARCHAR(255),
            precio FLOAT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS bonos.factura (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_cliente VARCHAR(255),
            bono VARCHAR(8),
            descuento INT CHECK (descuento BETWEEN 0 AND 100),
            total_sin_descuento FLOAT,
            total_final FLOAT
        )
        """
    ]
    try:
        for query in datos_injectar:
            cursor.execute(query)
        conex.commit()
        print("He creado las tablas.")
    except Error as e:
        print(f"Error al crear las tablas: {e}")
    finally:
        cursor.close()
        conex.close()