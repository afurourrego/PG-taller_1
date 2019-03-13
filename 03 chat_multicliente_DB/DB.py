import mysql.connector

nombre_db = ''
table_db = ''
column_table_db = 'message'

def CREATE_DB(nombre):
    global nombre_db
    nombre_db = nombre
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="")
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+nombre_db)

def CREATE_TABLE(table):
    global table_db, column_table_db
    table_db = table
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "+table_db+" (id INT AUTO_INCREMENT PRIMARY KEY, "+column_table_db+" VARCHAR(255))")

def INSERT_DB(message_db):
    global nombre_db, table_db, column_table_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO "+table_db+" ("+column_table_db+") VALUES('"+message_db+"')")
    conexion.commit()
    conexion.close()

def SELECT_DB():
    global nombre_db, table_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM "+table_db)
    result = cursor.fetchall()
    return result
    # for x in result:
    #   print(x[1])

# DB.CREATE_DB("python_db")
# DB.CREATE_TABLE("chat_history")
# DB.INSERT_DB("hola k ase")
# DB.SELECT_DB()









# import mysql.connector
#
# class Database(object):
#
#     def __init__(self):
#         self.nombre_db = ''
#         self.table_db = ''
#         self.column_table_db = 'message'
#
#     def CREATE_DB(self, nombre_db):
#         self.nombre_db = nombre_db
#         conexion = mysql.connector.connect( host="localhost", user="root", passwd="")
#         cursor = conexion.cursor()
#         cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.nombre_db)
#
#     def CREATE_TABLE(self, table_db):
#         self.table_db = table_db
#         conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=self.nombre_db)
#         cursor = conexion.cursor()
#         cursor.execute("CREATE TABLE IF NOT EXISTS "+self.table_db+" (id INT AUTO_INCREMENT PRIMARY KEY, "+self.column_table_db+" VARCHAR(255))")
#
#     def INSERT_DB(self, message_db):
#         conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=self.nombre_db)
#         cursor = conexion.cursor()
#         cursor.execute("INSERT INTO "+self.table_db+" ("+self.column_table_db+") VALUES('"+message_db+"')")
#         conexion.commit()
#         conexion.close()
#
#     def SELECT_DB(self):
#         conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=self.nombre_db)
#         cursor = conexion.cursor()
#         cursor.execute("SELECT * FROM "+self.table_db)
#         result = cursor.fetchall()
#         return result
#         # for x in result:
#         #   print(x[1])
#
# database_python = Database()
#
# # database_python.CREATE_DB("python_db")
# # database_python.CREATE_TABLE("chat_history")
# # database_python.INSERT_DB("hola k ase")
# # database_python.SELECT_DB()
