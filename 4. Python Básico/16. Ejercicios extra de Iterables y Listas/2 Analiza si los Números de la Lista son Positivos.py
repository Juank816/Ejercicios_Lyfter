#Ejercicios extra de Iterables y Listas: PROGRAMA VALIDA SI TODOS LOS NÚMEROS DE UNA LISTA SON POSITIVOS
'''Cree un programa que verifique si todos los elementos de una lista son positivos'''

print("---- Analiza si los Números de la Lista son Positivos  ----")

#Declaración de Lista
my_list = [3, 6, 0, -2, 4]

#Declaración de Variables
negative_number_counter = int
negative_number_counter = 0



#Recorre la lista y suma al contador
for index in range(0, len(my_list)):
    print(my_list[index])
    if my_list[index] <= 0:
        negative_number_counter += 1

#Evalúa si los si por lo menos hay un número menor o igual a 0
if negative_number_counter > 0:
    print("Hay al menos un número negativo o cero")
else:
    print("Todos los números son positivos")