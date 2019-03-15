from tkinter import *

class Triqui():
    def __init__(self):
        global ventana
        ventana = Tk()
        ventana.title("[JUEGO TRIQUI]")
        ventana.geometry("700x360")
        global turnoPJ
        turnoPJ = 0

        self.create_buttons()

        label_turno = Label(ventana, text="[TURNO]", font=('Arial 18 bold'), fg='grey').place(x=460, y= 10)
        label_turno_jugador = Label(ventana, text=" ", font=('Arial 18 bold'), fg='grey').place(x=450, y= 50)
        
        v = StringVar()
        Label(master, textvariable=v).pack()

        v.set("New Text!")
        v.set("New Text!")

        ventana.mainloop()



    def marcar(self, button_click):
        # self.turno()
        if button_click["text"] == " " and turnoPJ == 0:
            button_click["text"] = "O"
            self.cambio_turno()
        elif button_click["text"] == " " and turnoPJ == 1:
            button_click["text"] = "X"
            self.cambio_turno()
        print("holi"+button_click["text"])

    def cambio_turno(self):
        global turnoPJ
        if turnoPJ == 0:
            turnoPJ = 1
        elif turnoPJ == 1:
            turnoPJ = 0

    def turno(self):
        global turnoPJ
        if turnoPJ == 0:
            label_turno_jugador["text"] = "Jugador O"
        elif turnoPJ == 1:
            label_turno_jugador["text"] = "Jugador X"

    def create_buttons(self):
        # for x in range(3):
        #     for y in range(3):
        #         buttons[button] = Button(ventana, text=button, font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(buttons, button))
        #         buttons[button].grid(row = x, column = y, sticky = S+N+E+W)
        #         button = button + 1
        button_1 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_1))
        button_1.grid(row = 0, column = 0, sticky = S+N+E+W)
        button_2 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_2))
        button_2.grid(row = 0, column = 1, sticky = S+N+E+W)
        button_3 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_3))
        button_3.grid(row = 0, column = 2, sticky = S+N+E+W)
        button_4 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_4))
        button_4.grid(row = 1, column = 0, sticky = S+N+E+W)
        button_5 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_5))
        button_5.grid(row = 1, column = 1, sticky = S+N+E+W)
        button_6 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_6))
        button_6.grid(row = 1, column = 2, sticky = S+N+E+W)
        button_7 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_7))
        button_7.grid(row = 2, column = 0, sticky = S+N+E+W)
        button_8 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_8))
        button_8.grid(row = 2, column = 1, sticky = S+N+E+W)
        button_9 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(button_9))
        button_9.grid(row = 2, column = 2, sticky = S+N+E+W)

triqui = Triqui()
