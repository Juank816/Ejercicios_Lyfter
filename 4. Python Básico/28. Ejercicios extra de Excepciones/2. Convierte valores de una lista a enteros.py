#Ejercicios extra de Excepciones: Función que suma los valores de una lista 
'''Cree una función convertir_a_entero(lista) que:
Reciba una lista de strings
Intente convertir cada elemento a entero usando int()
Use try-except para atrapar los errores ValueError
Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con 
los demás'''

def give_information():
    my_list = []
    for index in range(0, 4):
        data = input("Ingrese un valor a la lista: ")
        my_list.append(data)
    return my_list


def converter_to_integer(my_list):
    print("Resultado:")
    for index in my_list:
        try:
            number = int(index)
            print(f'" {index}" convertido a {number}')
        except ValueError as ex:
            print(f'No se pudo convertir el elemento: {index}')
            


def main():
    my_list = give_information()
    converter_to_integer(my_list)


if __name__ == "__main__":
    main()