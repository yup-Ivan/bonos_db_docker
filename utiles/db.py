import mysql.connector
from mysql.connector import Error

class BaseDeDatos:

    def __init__(self):
        
        self.conexion = None
        self.config = {
            'host': 'db',
            'port': '3306',
            'user': 'bonoman',
            'password': 'ivan',
            'database': 'bonos'
        }

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            if self.conexion.is_connected():
                return self.conexion
        except mysql.connector.Error as error:
            print(f'Error al conectar: {error}')

    def desconectar(self):
        try:
            if self.conexion.is_connected():
                self.conexion.close()
        except mysql.connector.Error as error:
            print(f'Error al desconectar: {error}')

    def ejecutar(self, linea, data=None):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(linea, data)
            self.conexion.commit()
            cursor.close()
        except mysql.connector.Error as error:
            print(f'Error al ejecutar: {error}')

    def recuperar(self, linea, data=None):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(linea, data)
            resp = cursor.fetchall()
            cursor.close()
            return resp
        except mysql.connector.Error as error:
            print(f'Error al recuperar: {error}')