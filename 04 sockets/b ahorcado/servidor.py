import socket


class Servidor():

    def __init__(self):
        # global palabra, palabra_oculta, temp_var, num_error, game_over
        self.palabra = ""
        self.palabra_oculta = ""
        self.palabra_oculta_temp = ""
        self.temp_var = ""
        self.num_error = 0
        self.game_over = False
        self.win = False

        self.error = {
        0 : "\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
        1 : "\t ______\n\t |    |\n\t O    |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
        2 : "\t ______\n\t |    |\n\t O    |\n\t |    |\n\t      |\n\t      |\n\t______|_\n\n",
        3 : "\t ______\n\t |    |\n\t O    |\n\t/|    |\n\t      |\n\t      |\n\t______|_\n\n",
        4 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/     |\n\t      |\n\t______|_\n\n",
        5 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/ \   |\n\t      |\n\t______|_\n\n",
        6 : "\t [END]"
        }

        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        self.asignar_palabra()

        while True:
            mensaje = conexion.recv(1024)
            print("[]: "+mensaje.decode())

            # mensaje = print_ahorcado(mensaje.decode())
            self.if_game_over()
            if self.game_over == False:
                self.buscar_letra(mensaje.decode())
                conexion.send(self.print_ahorcado().encode()+self.print_palabra_oculta().encode())
            if self.win == True:
                conexion.send("\n     [GANASTE]".encode())
            if self.game_over == True and self.win == False:
                conexion.send("\n      [GAME OVER]".encode())

        print("close")

    def print_ahorcado(self):
        return self.error[self.num_error]

    def asignar_palabra(self):
        # global palabra, palabra_oculta

        self.palabra = "programacion"
        for letra in range(len(self.palabra)):
            self.palabra_oculta = self.palabra_oculta + "_"

    def print_palabra_oculta(self):
        # global palabra_oculta_temp
        if self.num_error <= 5:
            self.palabra_oculta_temp = ""

            for letra in range(len(self.palabra)):
                self.palabra_oculta_temp = self.palabra_oculta_temp + self.palabra_oculta[letra] + " "

            return self.palabra_oculta_temp

    def buscar_letra(self, letra):
        # global temp_var, palabra_oculta, num_error, game_over, win

        if self.num_error <= 5:
            self.temp_var = ""
            for pos in range(len(self.palabra)):
                if self.palabra[pos] == str(letra):
                    self.temp_var = self.temp_var + str(letra)
                else:
                    self.temp_var = self.temp_var + self.palabra_oculta[pos]
            if self.palabra_oculta == self.temp_var and self.num_error < 6:
                self.num_error = self.num_error + 1
            self.palabra_oculta = self.temp_var

    def if_game_over(self):
        # global num_error, game_over, win
        if self.num_error >= 5:
            self.game_over = True
        if self.palabra == self.palabra_oculta:
            self.win = True

servidor = Servidor()
