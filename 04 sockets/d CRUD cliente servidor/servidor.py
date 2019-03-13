import socket
import DB

DB.CREATE_DB("python_tienda_db")
DB.CREATE_TABLE("tienda", "producto", "precio")
# DB.INSERT_DB("tienda", "producto", "tomato", "precio", "1500")

class Servidor():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        while True:
            while True:
                conexion.send("\n1.[VER PRODUCTOS]    \n2.[AGREGAR PRODUCTOS] \n3.[EDITAR PRODUCTOS]  \n4.[ELIMINAR PRODUCTOS]    \n\n0.[SALIR]\n".encode())
                try:
                    mensaje = conexion.recv(1024)
                    if int(mensaje) > 4:
                        mensaje = "error"
                    mensaje = int(mensaje)
                except ValueError:
                    conexion.send("\n\n<<Opción Invalida>>\n\n".encode())

            print("[]: "+mensaje.decode())
            if(mensaje.decode() == '0'):
                break

            if(mensaje == '1'):
                print("opcion 1")
                # products = DB.SELECT_DB("tienda")
                # for product in products:
                #   print(product)

            if(mensaje == '2'):
                print("opcion 2")

            if(mensaje == '3'):
                print("opcion 3")

            if(mensaje == '4'):
                print("opcion 4")
            # conexion.send("{{recibido}}".encode())
        print("close")
        conexion.close()
        self.mi_socket.close()

servidor = Servidor()
