import mysql.connector

nombre_db = ''

def CREATE_DB(nombre):
    global nombre_db
    nombre_db = nombre
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="")
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+nombre_db)

def CREATE_TABLE(table_db, column_table_db, precio_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "+table_db+" (id INT AUTO_INCREMENT PRIMARY KEY, "+column_table_db+" VARCHAR(255), "+precio_db+" INT(10))")

def INSERT_DB(table_db, column_table_db, message_db, precio_db, valor_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO "+table_db+" ("+column_table_db+", "+precio_db+") VALUES('"+message_db+"', '"+valor_db+"')")
    conexion.commit()
    conexion.close()

def SELECT_DB(table_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM "+table_db)
    result = cursor.fetchall()
    return result
    # for x in result:
    #   print(x[1])

def UPDATE_DB(table_db, producto_db, nombre_prod_db, precio_db, valor_db, code_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("UPDATE "+table_db+" SET "+producto_db+" = '"+nombre_prod_db+"', "+precio_db+" = "+valor_db+" WHERE id = "+code_db)
    conexion.commit()
    conexion.close()

def SELECT_WHERE_DB(table_db, code_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM "+table_db+" WHERE id = "+code_db)
    result = cursor.fetchall()
    return result

def SELECT_WHERE_DB(table_db, code_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM "+table_db+" WHERE id = "+code_db)
    result = cursor.fetchall()
    return result

def SELECT_WHERE_DB(table_db, code_db):
    global nombre_db
    conexion = mysql.connector.connect( host="localhost", user="root", passwd="", database=nombre_db)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM "+table_db+" WHERE id = "+code_db)
    conexion.commit()
    conexion.close()

# DB.CREATE_DB("python_db")
# DB.CREATE_TABLE("users", "user")
# DB.INSERT_DB("users", "user", "nombre")
# DB.SELECT_DB("chat_history", "message")
# DB.SELECT_WHERE_DB("tienda", code)
# DB.UPDATE_DB("tienda", "producto", str(producto), "precio", str(precio), code)
# DB.SELECT_WHERE_DB("tienda", code_db):
