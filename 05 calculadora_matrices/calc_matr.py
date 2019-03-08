import os, time

clear = lambda: os.system('cls')

def titulo_ingrese_valor():
    clear()
    print("[INGRESE LOS VALORES DE LA MATRIZ]\n")

def titulo():
    clear()
    print("[CALCULADORA DE MATRICES]")
    print("Seleccione el tamaño de su matriz \n")

while True:
    try:
        titulo()
        x_size = input("X: ")
        y_size = input("Y: ")
        x_size = int(x_size)
        y_size = int(y_size)
        break
    except ValueError:
        clear()
        print("\n\n¡Alguno no es un numero!\n")
        time.sleep(.500)

print("\nMatriz de " + str(x_size) + "x" + str(y_size))

time.sleep(1)
titulo_ingrese_valor()

x = 0
y = 0
matriz = [[0 for y in range(y_size)] for x in range(x_size)]

for x in range(x_size):
    for y in range(y_size):
        while True:
            try:
                titulo_ingrese_valor()

                matriz[x][y] = input("M-"+str(x+1)+","+str(y+1)+": ")
                matriz[x][y] = int(matriz[x][y])
                break
            except ValueError:
                clear()
                print("\n\n¡No es un numero!\n")
                time.sleep(.500)

time.sleep(1)
clear()
print("\n\n[SU MATRIZ]\n")

for x in range(x_size):
    for y in range(y_size):
        print('['+str(matriz[x][y]), end=']\t')
    print()
