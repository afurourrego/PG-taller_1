
error = {
    0 : "\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
    1 : "\t ______\n\t |    |\n\t O    |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
    2 : "\t ______\n\t |    |\n\t O    |\n\t |    |\n\t      |\n\t      |\n\t______|_\n\n",
    3 : "\t ______\n\t |    |\n\t O    |\n\t/|    |\n\t      |\n\t      |\n\t______|_\n\n",
    4 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/     |\n\t      |\n\t______|_\n\n",
    5 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/ \   |\n\t      |\n\t______|_\n\n"
}

def print_ahorcado():
    return error[num_error]

def asignar_palabra():
    global palabra, palabra_oculta, game_over, num_error, temp_var
    game_over = False
    palabra_oculta = []

    num_error = 0
    temp_var = ""

    palabra = "programacion"
    print(len(palabra))

    for pos in range(len(palabra) - 1):
        palabra_oculta[pos] = "_"
    print(palabra_oculta)

def print_palabra_oculta():
    # return palabra_oculta
    pass

# def buscar_letra(letra):
#     print(palabra)
#     for pos in range(len(palabra)):
#
#         if palabra[pos] == str(letra):
#             temp_var = temp_var + str(letra)
#         else:
#             temp_var = temp_var + palabra_oculta[pos]
#
#     print(temp_var)

def if_game_over():
    if palabra == palabra_oculta or num_error == 5:
        game_over = True
    return game_over
