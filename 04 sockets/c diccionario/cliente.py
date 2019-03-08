import socket, string, sys, os, time
clear = lambda: os.system('cls')

class Cliente():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('127.0.0.1',9090))

        print("[DICIONARIO BINARIO]")
        time.sleep(1)
        clear()

        while True:
            mensaje = input("[]: ")
            self.mi_socket.send(mensaje.encode())
            if(mensaje == 'cerrar'):
                break
            recibido=self.mi_socket.recv(1024)
            print(recibido.decode())

        print("adios")
        self.mi_socket.close()

cliente = Cliente()
