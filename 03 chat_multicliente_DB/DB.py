import mysql.connector

nombre_db = ''

def CREATE_DB(nombre):
    global nombre_db
    nombre_db = nombre
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="")
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+nombre_db)

def CREATE_TABLE(table_db, column_table_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "+table_db+" (id INT AUTO_INCREMENT PRIMARY KEY, "+column_table_db+" VARCHAR(255))")

def INSERT_DB(table_db, column_table_db, message_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO "+table_db+" ("+column_table_db+") VALUES('"+message_db+"')")
    conexion.commit()
    conexion.close()

def SELECT_DB(table_db, column_table_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM "+table_db)
    result = cursor.fetchall()
    return result
