#Ejercicios de Iterables y Listas: PROGRAMA QUE ELIMINA TODOS LOS NÚMEROS IMPARES DE UNA LISTA
'''Cree un programa que elimine todos los números impares de una lista.'''
print("---- Elimina todos los números impares de una lista ----")


#Declaración de lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

#Proceso con for 
for index in  range (0, len(my_list)):
    if my_list[index] % 2 == 0:
        new_list.append(my_list[index]) #Se agrega según corrección

print(new_list)


#Nota de correción
# El programa imprime los números pares correctamente, pero la lista original no queda modificada. 
# El objetivo era que la lista resultante contenga solo los pares. Una buena estrategia es crear una lista 
# vacía al inicio y, dentro del ciclo, agregar cada número par con append(). Al final, esa nueva lista tendrá 
# solo los pares y se puede imprimir completa.