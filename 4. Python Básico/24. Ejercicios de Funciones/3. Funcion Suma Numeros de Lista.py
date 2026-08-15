#Ejercicios de Funciones: RETORNA LA SUMA DE UNA LISTA
'''Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
[4, 6, 2, 29] → 41'''  

#FUNCIONES
def sum_list(list_a):
    #Variables de función
    sum1 = 0
    for index in range (0,len(list_a)):
        sum1 = sum1 + list_a[index]
    return sum1


def main():
    numbers = [4, 6, 2, 29]
    print(sum_list(numbers))


if __name__ == "__main__":
    main()
