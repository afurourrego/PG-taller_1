import mysql.connector

class Database(object):

    def __init__(self):
        self.nombre_db = ''
        self.table_db = ''
        self.column_table_db = 'message'

    def CREATE_DB(self, nombre_db):
        self.nombre_db = nombre_db
        conexion = mysql.connector.connect( host="localhost", user="root", passwd="")
        cursor = conexion.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.nombre_db)

    def CREATE_TABLE(self, table_db):
        self.table_db = table_db
        conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=self.nombre_db)
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.table_db+" (id INT AUTO_INCREMENT PRIMARY KEY, "+self.column_table_db+" VARCHAR(255))")

    def INSERT_DB(self, message_db):
        conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=self.nombre_db)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO "+self.table_db+" ("+self.column_table_db+") VALUES('"+message_db+"')")
        conexion.commit()
        conexion.close()

database_python = Database()

database_python.CREATE_DB("python_db")
database_python.CREATE_TABLE("chat_history")
database_python.INSERT_DB("hola k ase")
