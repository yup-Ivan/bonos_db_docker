from utiles.db import BaseDeDatos

class Funcionalidades:

    def __init__(self):
        self.db = BaseDeDatos()
        self.db.conectar()

    def __del__(self):
        self.db.desconectar()

    def actualizar_cesta(self, producto, precio):

        linea = "INSERT INTO cesta (nombre_producto, precio) VALUES (%s, %s)"
        data = (producto, float(precio)) 
        self.db.ejecutar(linea, data)
        return "Se ha añadido el producto."
    
    def borrar_cesta(self):
        linea = "delete from cesta;"
        self.db.ejecutar(linea)
        return "Se ha limpiado la cesta."
        
    def crear_factura(self, nombre_cliente, bono, descuento):
        
        linea_1 = "SELECT SUM(precio) FROM cesta;"
        respuesta = self.db.recuperar(linea_1)
        total_sin_descuento = respuesta[0][0]

        if total_sin_descuento is None:
            total_sin_descuento = 0.00
        else:
            total_sin_descuento = float(total_sin_descuento)

        descuento = float(descuento)

        descuento_aplicado = total_sin_descuento * descuento / 100 
        total_final = total_sin_descuento - descuento_aplicado

        insert_query = "INSERT INTO factura (nombre_cliente, bono, descuento, total_sin_descuento, total_final) VALUES (%s, %s, %s, %s, %s)"
        data = (nombre_cliente, bono, descuento, total_sin_descuento, total_final)
        self.db.ejecutar(insert_query, data)

        return "Se ha creado tu factura."
    
    def crear_tablas(self):
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
        for linea in datos_injectar:
            self.db.ejecutar(linea)