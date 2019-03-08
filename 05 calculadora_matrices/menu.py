import os, time, threading

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
                    print("\n [DETERMINANTE]: " + str(determinante(matrix_1)))
                    break
                if case(2):
                    transpuesta(matrix_1)
                    break
                if case(3):
                    inversa(matrix_1)
                    break
                if case(4):
                    multiplicar(matrix_1)
                    break
                if case(5):
                    elevada(matrix_1)
                    break
                if case(6):
                    matriz_simetrica(matrix_1)
                    break
                if case(7):
                    matriz_identidad(matrix_1)
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

def determinante(matrix_1):

    def lado_a(matrix_1, x, y):
        resultado_temp = 1
        for pos in range(3):
            if x > 2:
                x = 0
            if y > 2:
                y = 0
            resultado_temp = resultado_temp * matrix_1[x][y]
            x = x+1
            y = y+1
        return resultado_temp

    def lado_b(matrix_1, x, y):
        resultado_temp = 1
        determinante = 0
        for pos in range(3):
            if x > 2:
                x = 0
            if y < 0:
                y = 2
            resultado_temp = resultado_temp * matrix_1[x][y]
            x = x+1
            y = y-1
        return resultado_temp

    temp_1 = threading.Thread(target=lado_a, args=(matrix_1, 0, 0))
    temp_2 = threading.Thread(target=lado_a, args=(matrix_1, 0, 1))
    temp_3 = threading.Thread(target=lado_a, args=(matrix_1, 0, 2))
    temp_4 = threading.Thread(target=lado_b, args=(matrix_1, 0, 2))
    temp_5 = threading.Thread(target=lado_b, args=(matrix_1, 0, 0))
    temp_6 = threading.Thread(target=lado_b, args=(matrix_1, 0, 1))

    temp_1.setDaemon = True
    temp_2.setDaemon = True
    temp_3.setDaemon = True
    temp_4.setDaemon = True
    temp_5.setDaemon = True
    temp_6.setDaemon = True

    temp_1.start()
    temp_2.start()
    temp_3.start()
    temp_4.start()
    temp_5.start()
    temp_6.start()

    temp_1.join()
    temp_2.join()
    temp_3.join()
    temp_4.join()
    temp_5.join()
    temp_6.join()

    print(temp_1)
    print(temp_2)
    print(temp_3)
    print(temp_4)
    print(temp_5)
    print(temp_6)

    # temp_7 = temp_1 + temp_2 + temp_3 - temp_4 - temp_5 - temp_6
    # return temp_7

# def transpuesta(matrix_1):
#     pass
# def inversa(matrix_1):
#     pass
# def multiplicar(matrix_1):
#     threads = list()
#
#     num = input("Multiplicar por: ")
#     for x in range(x_size):
#         for y in range(y_size):
#             # matrix = threading.Thread(target=)
#             print('['+str(matrix[x][y]), end=']\t')
#
#
#     threads = list()
#
#     for i in range(3):
#         t = threading.Thread(target=trabajo)
#         threads.append(t)
#         t.start()
#
#     print(threads)
#     print_matrix(x_size, y_size, matrix, letter)
#
# def elevada(matrix_1):
#     pass
# def matriz_simetrica(matrix_1):
#     pass
# def matriz_identidad(matrix_1):
#     pass
# def multiplicar_ab():
#     pass
# def restar_ab():
#     pass
# def dividir_ab():
#     pass


#SWITCH
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))
