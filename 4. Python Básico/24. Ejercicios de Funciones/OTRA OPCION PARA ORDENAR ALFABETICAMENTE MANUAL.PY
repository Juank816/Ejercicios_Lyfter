# Ejercicios de Funciones: RETORNA UN STRING ORDENADO MANUALMENTE

def ordenate_string(my_string):

    # 1. Convertimos el string en una lista
    my_list = my_string.split("-")

    # 2. Ordenamos manualmente la lista
    for index1 in range(0, len(my_list)):
        for index2 in range(index1 + 1, len(my_list)):

            if my_list[index1] > my_list[index2]:

                temporary = my_list[index1]

                my_list[index1] = my_list[index2]

                my_list[index2] = temporary

    # 3. Convertimos la lista nuevamente en string
    result = "-".join(my_list)

    return result


def main():

    my_string = "python-variable-funcion-computadora-monitor"

    print(ordenate_string(my_string))


if __name__ == "__main__":
    main()