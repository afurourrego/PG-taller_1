import socket, string, sys, os, time

clear = lambda: os.system('cls')

def principal():
    mi_socket = socket.socket()
    mi_socket.connect(('127.0.0.1',9090))

    print("    [JUEGO AHORCADO]")
    time.sleep(1)
    print("\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n")

    while True:
        mensaje = input("[]: ")
        mi_socket.send(mensaje.encode())
        if(mensaje == 'cerrar'):
            break
        clear()
        print("    [JUEGO AHORCADO]")
        recibido=mi_socket.recv(1024)
        print(recibido.decode())

    print("adios")
    mi_socket.close()


if (__name__ == '__main__'):
    principal()
