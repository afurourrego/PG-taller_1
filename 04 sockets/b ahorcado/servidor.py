import socket

# global palabra, palabra_oculta, temp_var, num_error, game_over
palabra = ""
palabra_oculta = ""
palabra_oculta_temp = ""
temp_var = ""
num_error = 0
game_over = False
win = False

error = {
    0 : "\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
    1 : "\t ______\n\t |    |\n\t O    |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
    2 : "\t ______\n\t |    |\n\t O    |\n\t |    |\n\t      |\n\t      |\n\t______|_\n\n",
    3 : "\t ______\n\t |    |\n\t O    |\n\t/|    |\n\t      |\n\t      |\n\t______|_\n\n",
    4 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/     |\n\t      |\n\t______|_\n\n",
    5 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/ \   |\n\t      |\n\t______|_\n\n",
    6 : "\t [END]"
}

def principal():
    mi_socket = socket.socket()
    mi_socket.bind(("",9090))
    mi_socket.listen(1)
    conexion, direccion = mi_socket.accept()

    asignar_palabra()

    while True:
        mensaje = conexion.recv(1024)
        print("[]: "+mensaje.decode())

        # mensaje = print_ahorcado(mensaje.decode())
        if_game_over()
        if game_over == False:
            buscar_letra(mensaje.decode())
            conexion.send(print_ahorcado().encode()+print_palabra_oculta().encode())
        if win == True:
            conexion.send("\n     [GANASTE]".encode())
        if game_over == True and win == False:
            conexion.send("\n      [GAME OVER]".encode())

    print("close")
    conexion.close()
    mi_socket.close()




def print_ahorcado():
    return error[num_error]

def asignar_palabra():
    global palabra, palabra_oculta

    palabra = "programacion"
    for letra in range(len(palabra)):
        palabra_oculta = palabra_oculta + "_"

def print_palabra_oculta():
    global palabra_oculta_temp
    if num_error <= 5:
        palabra_oculta_temp = ""

        for letra in range(len(palabra)):
            palabra_oculta_temp = palabra_oculta_temp + palabra_oculta[letra] + " "

        return palabra_oculta_temp

def buscar_letra(letra):
    global temp_var, palabra_oculta, num_error, game_over, win

    if num_error <= 5:
        temp_var = ""
        for pos in range(len(palabra)):
            if palabra[pos] == str(letra):
                temp_var = temp_var + str(letra)
            else:
                temp_var = temp_var + palabra_oculta[pos]
        if palabra_oculta == temp_var and num_error < 6:
            num_error = num_error + 1
        palabra_oculta = temp_var

def if_game_over():
    global num_error, game_over, win
    if num_error >= 5:
        game_over = True
    if palabra == palabra_oculta:
        win = True


if __name__ == '__main__':
    principal()
