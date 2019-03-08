import os, time

clear = lambda: os.system('cls')

def title():
    clear()
    print("[CALCULADORA DE MATRICES] \n")

def menu():
    global size, matrix_1, matrix_2
    size = 3

    while True:
        title()
        print("1.[UNA MATRIZ]")
        print("2.[DOS MATRIZ]")
        try:
            option = input("\nElige tu opción: ")
            option = int(option)
            while switch(option):
                if case(1):
                    matrix_1 = create_matrix()

                    title()
                    print("[UNA MATRIZ]\n")
                    print_matrix(matrix_1,"[A]")

                    one_matrix(matrix_1)
                    break
                if case(2):
                    matrix_1 = create_matrix()

                    clear()
                    print("[SEGUNDA MATRIZ]")
                    time.sleep(.500)
                    matrix_2 = create_matrix()

                    title()
                    print("[DOS MATRICES]\n")
                    print_matrix(matrix_1,"[A]")
                    print_matrix(matrix_2,"[B]")
                    two_matrix(matrix_1, matrix_2)
                    break
            break
        except ValueError:
            clear()
            print("\n\n¡Opción invalida!")
            time.sleep(.500)

def create_matrix():
    time.sleep(.500)
    matrix = [[0 for y in range(size)] for x in range(size)]

    for x in range(size):
        for y in range(size):
            while True:
                try:
                    clear()
                    print("[INGRESE LOS VALORES DE LA MATRIZ]\n")
                    matrix[x][y] = input("M-"+str(x+1)+","+str(y+1)+": ")
                    matrix[x][y] = int(matrix[x][y])
                    break
                except ValueError:
                    clear()
                    print("\n\n¡No es un numero!\n")
                    time.sleep(.500)
    return matrix

def print_matrix(matrix, letter):
    time.sleep(.500)
    print("[MATRIZ]"+letter+"\n")

    for x in range(size):
        for y in range(size):
            print('['+str(matrix[x][y]), end=']\t')
        print()
    print()

def one_matrix(matrix_1):
    while True:
        print("1.[DETERMINANTE]")
        print("2.[TRANSPUESTA]")
        print("3.[INVERSA]")
        print("4.[MULTIPLICAR POR NUMERO]")
        print("5.[ELEVADA A UNA POTENCIA]")
        print("6.[MATRIZ SIMETRICA]")
        print("7.[MATRIZ IDENTIDAD]")
        try:
            option = input("\nElige tu opción: ")
            option = int(option)
            while switch(option):
                if case(1):
                    determinante()
                    break
                if case(2):
                    transpuesta()
                    break
                if case(3):
                    inversa()
                    break
                if case(4):
                    multiplicar()
                    break
                if case(5):
                    elevada()
                    break
                if case(6):
                    matriz_simetrica()
                    break
                if case(7):
                    matriz_identidad()
                    break
            break
        except ValueError:
            clear()
            print("\n\n¡Opción invalida!")
            time.sleep(.500)

def two_matrix(matrix_1, matrix_2):
    while True:
        print("1.[A x B]")
        print("2.[A - B]")
        print("3.[A / B]")
        try:
            option = input("\nElige tu opción: ")
            option = int(option)
            while switch(option):
                if case(1):
                    multiplicar_ab()
                    break
                if case(2):
                    restar_ab()
                    break
                if case(3):
                    dividir_ab()
                    break
            break
        except ValueError:
            clear()
            print("\n\n¡Opción invalida!")
            time.sleep(.500)

def determinante():

    pass
def transpuesta():
    pass
def inversa():
    pass
def multiplicar(m):
    threads = list()

    num = input("Multiplicar por: ")
    for x in range(x_size):
        for y in range(y_size):
            # matrix = threading.Thread(target=)
            print('['+str(matrix[x][y]), end=']\t')


    threads = list()

    for i in range(3):
        t = threading.Thread(target=trabajo)
        threads.append(t)
        t.start()

    print(threads)
    print_matrix(x_size, y_size, matrix, letter)

def elevada():
    pass
def matriz_simetrica():
    pass
def matriz_identidad():
    pass
def multiplicar_ab():
    pass
def restar_ab():
    pass
def dividir_ab():
    pass


#SWITCH
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))
