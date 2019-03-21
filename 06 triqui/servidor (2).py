from socket import *
from threading import *
import mysql.connector

clientes = {}
direcciones = {}

def configuracion():
    global servidor, turno_jugador
    turno_jugador = '0'

    servidor = socket()
    servidor.bind(("", 9999))
    servidor.listen(10)
    print("Esperando conexiones...")
    aceptar_hilo = Thread(target=aceptar_conexiones)
    aceptar_hilo.start()
    aceptar_hilo.join()

def aceptar_conexiones():
    while True:
        cliente_local, direccion_cliente = servidor.accept()
        print("%s:%s conectado. "% direccion_cliente)
        cliente_local.send(bytes("Bienvenido, ingresa tu nombre y presiona Enter", "utf-8"))
        direcciones[cliente_local] = direccion_cliente
        Thread(target=encargarse_cliente,args=(cliente_local,)).start()

def encargarse_cliente(cliente):
    pass
    # nombre = cliente.recv(1024).decode("utf-8")
    # bienvenido = "Bienvenido %s! si quieres salir, escribe {salir}." %nombre
    # cliente.send(bytes(bienvenido, "utf-8"))
    # mensaje = "%s se ha unido al chat." % nombre
    # broadcast(bytes(mensaje, "utf-8"))
    # clientes[cliente] = nombre
    # while True:
    #     mensaje = cliente.recv(1024)
    #     if mensaje != bytes("{salir}", "utf-8"):
    #         guardar_mensaje(nombre, mensaje)
    #         broadcast(mensaje, nombre+": ")
    #     else:
    #         del clientes[cliente]
    #         broadcast(bytes("%s ha salido del chat." % nombre, "utf-8"))
    #         break



def cambio_turno():
    if turno_jugador == 0:
        v_turno.set("jugador 2")
        turno_jugador = 1
    elif turno_jugador == 1:
        v_turno.set("jugador 1")
        turno_jugador = 0

def broadcast(mensaje, prefix=""):
    for sock in clientes:
        sock.send(bytes(prefix, "utf-8")+mensaje)

def guardar_mensaje(nombre,mensaje):
    conexion = mysql.connector.connect(user="root", password="", host="localhost", database="chat")
    cursor = conexion.cursor()
    sql = "INSERT INTO comunicaciones(usuario, mensaje)VALUES(%s,%s)"
    parametros = (str(nombre), str(mensaje))
    cursor.execute(sql,parametros)
    conexion.commit()
    conexion.close

if __name__ == "__main__":
    configuracion()
