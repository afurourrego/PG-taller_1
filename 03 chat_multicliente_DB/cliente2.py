import socket, threading, sys, os, time
import DB

class Cliente():
    def __init__(self, host="localhost", puerto=9999):
        clear = lambda: os.system('cls')

        self.sock = socket.socket()
        self.sock.connect((host, puerto))

        mensaje_servidor = threading.Thread(target=self.mensaje_server)
        mensaje_servidor.setDaemon(True)
        mensaje_servidor.start()

        global nombre
        nombre = input("[INGRESE SU NOMBRE]: ")
        print("{{recibido}}")
        clear()
        time.sleep(.500)

        DB.CREATE_DB("python_db")
        DB.CREATE_TABLE("chat_history")
        result = DB.SELECT_DB()
        for x in result:
          print(x[1])



        while True:
            mensaje = input()
            if mensaje !='salir':
                self.enviar_mensaje("["+nombre+"]: "+mensaje)
            else:
                self.sock.close()
                sys.exit()

    def mensaje_server(self):
        while True:
            try:
                datos = self.sock.recv(1024)
                if datos:
                    print(datos.decode())
            except:
                pass

    def enviar_mensaje(self, mensaje):
        self.sock.send(mensaje.encode())

cliente = Cliente()

#
#
# import socket
# import threading
# import sys
#
# class Cliente():
#     def __init__(self, host="localhost", puerto=9999):
#         self.sock = socket.socket()
#         self.sock.connect((host, puerto))
#
#         mensaje_servidor = threading.Thread(target=self.mensaje_server)
#         mensaje_servidor.setDaemon(True)
#         mensaje_servidor.start()
#
#         while True:
#             mensaje = input(">>")
#             if mensaje !='salir':
#                 self.enviar_mensaje(mensaje)
#             else:
#                 self.sock.close()
#                 sys.exit()
#
#     def mensaje_server(self):
#         while True:
#             try:
#                 datos = self.sock.recv(1024)
#                 if datos:
#                     print(datos.decode())
#             except:
#                 pass
#
#     def enviar_mensaje(self, mensaje):
#         self.sock.send(mensaje.encode())
#
# cliente = Cliente()
