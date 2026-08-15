#Ejercicios de Funciones: RETORNA NUMEROS PRIMOS DE UNA LISTA
'''Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. 
No busque el código, eso no ayudaría.
Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra 
lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.'''

#Funciones
def return_prime_number(number):
    if number < 2:
        return False

    for index in range(2, number):
        if number % index == 0:
            return False

    return True


def add_new_list(my_list):
    new_list = []
    
    for number in my_list:
    
        if return_prime_number(number):
            new_list.append(number)

    return new_list






def main():
    #Declaración de lista
    my_list = [1, 4, 6, 7, 13, 9, 67]
    #Muestra en pantalla
    print(add_new_list(my_list))


if __name__ == "__main__":
    main()