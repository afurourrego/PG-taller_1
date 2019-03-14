import socket
import DB

DB.CREATE_DB("python_tienda_db")
DB.CREATE_TABLE("tienda", "producto", "precio")

class Servidor():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()
        # global mensaje

        while True:
            while True:
                conexion.send("\n1.[VER PRODUCTOS]    \n2.[AGREGAR PRODUCTOS] \n3.[EDITAR PRODUCTOS]  \n4.[ELIMINAR PRODUCTOS]    \n\n0.[SALIR]\n".encode())
                try:
                    mensaje = conexion.recv(1024)
                    if int(mensaje) > 4:
                        mensaje = "error"
                    mensaje = int(mensaje)
                    break
                except ValueError:
                    conexion.send("\n\n<<Opción Invalida>>\n\n".encode())

            print("[]: "+str(mensaje))
            if(mensaje == 0):
                break

            if(mensaje == 1):
                products = DB.SELECT_DB("tienda")
                conexion.send("\n<<Cargando presione ENTER>>\n".encode())
                for product in products:
                    conexion.send(("\n  [CODE]: "+str(product[0])).encode())
                    conexion.send(("\n  [PRODUCTO]: "+str(product[1])).encode())
                    conexion.send(("\n  [PRECIO]: $"+str(product[2])).encode())
                    conexion.send("\n-------------------------------".encode())

            if(mensaje == 2):
                conexion.send("[NOMBRE DEL PRODUCTO]: ".encode())
                producto = conexion.recv(1024).decode()
                conexion.send("[PRECIO DEL PRODUCTO]: ".encode())
                precio = conexion.recv(1024).decode()
                DB.INSERT_DB("tienda", "producto", str(producto), "precio", str(precio))

            if(mensaje == 3):
                conexion.send("[INGRESE EL CODIGO DEL PRODUCTO QUE DESEA EDITAR]".encode())
                code = conexion.recv(1024).decode()
                product = DB.SELECT_WHERE_DB("tienda", code)
                print(product)
                if product == []:
                    print("nulo")
                    conexion.send("[NO EXISTE ESTE PRODUCTO]".encode())
                else:
                    print("lleno")
                    conexion.send("[NOMBRE DEL PRODUCTO]: ".encode())
                    producto = conexion.recv(1024).decode()
                    conexion.send("[PRECIO DEL PRODUCTO]: ".encode())
                    precio = conexion.recv(1024).decode()

                    if producto == ' ':
                        print(product)
                        producto =str(product[0][1])
                    if precio == ' ':
                        precio = str(product[0][2])

                    DB.UPDATE_DB("tienda", "producto", str(producto), "precio", str(precio), code)

            if(mensaje == 4):
                conexion.send("[INGRESE EL CODIGO DEL PRODUCTO QUE DESEA ELIMINAR]".encode())
                code = conexion.recv(1024).decode()
                DB.SELECT_WHERE_DB("tienda", code)

        print("\n\n<<Presione 'ENTER' para salir>>\n\n")
        conexion.close()
        self.mi_socket.close()

servidor = Servidor()
