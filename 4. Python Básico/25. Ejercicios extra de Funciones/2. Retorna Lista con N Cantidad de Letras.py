#Ejercicios extra de Funciones: RETORNA LISTA CON N CANTIDAD DE LETRAS
'''Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las 
palabras que tengan más de n letras
Ejemplo:
Entrada:

Copiar
["cielo","sol","maravilloso","día"]

"Ingrese el numero de letras minimas en la palabra: "4
Salida:
["cielo","maravilloso"]'''

def receive_information():
    number = int(input("Ingrese un número "))
    
    my_list = []
    
    for index in range(0, number):
        word = input("Ingrese un texto ")
        my_list.append(word)

    return return_list(my_list, number)


def return_list(my_list, number):
    new_list = []
    word = 0
    
    for index in range(0, len(my_list)):
        word = len(my_list[index])
        if word > number:
            new_list.append(my_list[index])
    return new_list


def main():
    print("---- Programa que filtra palabras por cantidad de letras ----")
    #Muestra en pantalla
    print(receive_information())


if __name__ == "__main__":
    main()