from socket import *
from threading import *
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

def configuracion():
    global cliente_socket
    cliente_socket = socket()
    cliente_socket.connect(('localhost',9999))
    # recibir_hilo = Thread(target=recibir)
    # recibir_hilo.start()

    global ventana, turnoPJ, gameover, v_turno
    ventana = Tk()
    ventana.title("[JUEGO TRIQUI]")
    ventana.geometry("700x360")
    turnoPJ = 0
    gameover = 0
    v_turno = StringVar()


    create_buttons()
    create_interfaz()
    v_turno.set("jugador 1")

    mainloop()


# def interfaz():
    # global mi_mensaje, ventana, mensaje_lista
    # ventana = Tk()
    # ventana.title("Messenger")
    # frame = Frame(ventana)
    # mi_mensaje = StringVar()
    # mi_mensaje.set("")
    # scroll = Scrollbar(frame)
    # mensaje_lista = Listbox(frame, height=30, width=100, yscrollcommand=scroll.set)
    # scroll.pack(side=RIGHT, fill=Y)
    # mensaje_lista.pack(side=LEFT, fill=BOTH)
    # mensaje_lista.pack()
    # frame.pack()
    # campo_entrada = Entry(ventana,textvariable=mi_mensaje)
    # campo_entrada.bind("<Return>",enviar)
    # campo_entrada.pack()
    # boton_envio = Button(ventana,text="Enviar",command=enviar)
    # boton_envio.pack()
    # ventana.protocol("WM_DELETE_WINDOW", cerrando)


# def recibir():
#     while True:
#         try:
#             mensaje = cliente_socket.recv(1024).decode("utf-8")
#             mensaje_lista.insert(END,mensaje)
#             mensaje_lista.see(END)
#         except OSError:
#             break
#
# def enviar(event=None):
#     mensaje = mi_mensaje.get()
#     mi_mensaje.set("")
#     cliente_socket.send(bytes(mensaje, "utf-8"))
#     if mensaje == '{salir}':
#         cliente_socket.close()
#         ventana.quit()
#
# def cerrando(event=None):
#     mi_mensaje.set("{salir}")
#     enviar()


#triqui=========================================================================

def marcar(button_click):
    global gameover
    if gameover == 0:
        if button_click["text"] == " " and turnoPJ == 0:
            button_click["text"] = "O"
        elif button_click["text"] == " " and turnoPJ == 1:
            button_click["text"] = "X"

        if turnoPJ == 0:
            gameover_func("jugador 1")
        else:
            gameover_func("jugador 2")

        cambio_turno()

# def cambio_turno():
#     global turnoPJ
#     if turnoPJ == 0:
#         v_turno.set("jugador 2")
#         turnoPJ = 1
#     elif turnoPJ == 1:
#         v_turno.set("jugador 1")
#         turnoPJ = 0

def create_buttons():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9
    button_1 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_1))
    button_1.grid(row = 0, column = 0, sticky = S+N+E+W)
    button_2 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_2))
    button_2.grid(row = 0, column = 1, sticky = S+N+E+W)
    button_3 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_3))
    button_3.grid(row = 0, column = 2, sticky = S+N+E+W)
    button_4 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_4))
    button_4.grid(row = 1, column = 0, sticky = S+N+E+W)
    button_5 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_5))
    button_5.grid(row = 1, column = 1, sticky = S+N+E+W)
    button_6 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_6))
    button_6.grid(row = 1, column = 2, sticky = S+N+E+W)
    button_7 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_7))
    button_7.grid(row = 2, column = 0, sticky = S+N+E+W)
    button_8 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_8))
    button_8.grid(row = 2, column = 1, sticky = S+N+E+W)
    button_9 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(button_9))
    button_9.grid(row = 2, column = 2, sticky = S+N+E+W)

def create_interfaz():

    label_turno = Label(ventana, text="[TURNO]", font=('Arial 18 bold'), fg='grey').place(x=460, y= 40)
    label_turno_jugador = Label(ventana, textvariable=v_turno, font=('Arial 18 bold'), fg='grey').place(x=450, y= 80)

    label_victorias = Label(ventana, text="[VICTORIAS]", font=('Arial 18 bold'), fg='grey').place(x=430, y= 170)

    label_victorias_jugador_1 = Label(ventana, text="[jugador 1]", font=('Arial 18 bold'), fg='grey').place(x=440, y= 210)
    label_victorias_jugador_2 = Label(ventana, text="[jugador 2]", font=('Arial 18 bold'), fg='grey').place(x=440, y= 250)

def gameover_func(Jugador):
    global gameover
    if button_1["text"] != " " and button_1["text"] == button_2["text"] and button_1["text"] == button_3["text"]:
        gameover = 1
    if button_4["text"] != " " and button_4["text"] == button_5["text"] and button_4["text"] == button_6["text"]:
        gameover = 1
    if button_7["text"] != " " and button_7["text"] == button_8["text"] and button_7["text"] == button_9["text"]:
        gameover = 1

    if button_1["text"] != " " and button_1["text"] == button_4["text"] and button_1["text"] == button_7["text"]:
        gameover = 1
    if button_2["text"] != " " and button_2["text"] == button_5["text"] and button_2["text"] == button_8["text"]:
        gameover = 1
    if button_3["text"] != " " and button_3["text"] == button_6["text"] and button_3["text"] == button_9["text"]:
        gameover = 1

    if button_1["text"] != " " and button_1["text"] == button_5["text"] and button_1["text"] == button_9["text"]:
        gameover = 1
    if button_3["text"] != " " and button_3["text"] == button_5["text"] and button_3["text"] == button_7["text"]:
        gameover = 1
    if gameover == 1:
        winner_pop(Jugador)
        print("win")

def winner_pop(nombre_ganador):
    global login_error_screen
    mensaje_alert = StringVar()
    mensaje_alert.set("Ganador "+nombre_ganador)
    winner_pop = Toplevel(ventana)

    width = 200
    height = 100
    screen_width = winner_pop.winfo_screenwidth()
    screen_height = winner_pop.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    winner_pop.geometry("%dx%d+%d+%d" % (width, height, x, y))
    winner_pop.resizable(0, 0)

    winner_pop.title("GANADOR")
    Label(winner_pop, height="1").pack()
    Label(winner_pop, textvariable=mensaje_alert).pack()
    Button(winner_pop, text="OK", command=winner_pop.destroy).pack()

if __name__ == "__main__":
    configuracion()
