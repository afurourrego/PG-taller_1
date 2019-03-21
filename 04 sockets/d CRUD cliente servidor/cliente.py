import socket, string, sys, os, time
clear = lambda: os.system('cls')

class Cliente():

    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('127.0.0.1',9090))

        # clear()

        while True:
            recibido = self.mi_socket.recv(1024)
            print(recibido.decode())
            mensaje = input("[]: ")

            self.mi_socket.send(mensaje.encode())

            if(mensaje == '0'):
                break


        print("\n\n<<Presione 'ENTER' para salir>>\n\n")
        self.mi_socket.close()


cliente = Cliente()
