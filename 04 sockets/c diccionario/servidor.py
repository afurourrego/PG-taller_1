import socket, diccionario

class Servidor():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        while True:
            mensaje = conexion.recv(1024)
            print("[]: "+mensaje.decode())

            mensaje = diccionario.traducir(mensaje.decode())

            conexion.send("[BINARIO]: ".encode() + str(mensaje).encode())

        print("close")
        conexion.close()
        self.mi_socket.close()

servidor = Servidor()
