import socket

class Servidor():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        global nombre
        nombre = conexion.recv(1024)
        conexion.send("{{nombre aceptado}}".encode())

        while True:
            mensaje = conexion.recv(1024)
            print("["+nombre.decode()+"]: "+mensaje.decode())
            conexion.send("{{recibido}}".encode())
            if(mensaje.decode()== 'cerrar'):
                break
        print("close")
        conexion.close()
        self.mi_socket.close()

servidor = Servidor()
